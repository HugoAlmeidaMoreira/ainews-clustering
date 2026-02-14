#!/usr/bin/env python3
"""
Script to combine all lecture markdown files into a single master markdown file.
"""

import os
from pathlib import Path

# Configuration
KNOWLEDGE_DIR = Path(__file__).parent.resolve()
OUTPUT_FILE = KNOWLEDGE_DIR / "master.md"

# Order of lectures (by folder name)
LECTURE_ORDER = [
    "01 IntroductionML.pdf",
    "02 DescriptiveStatistics.pdf",
    "03a Clustering Part1.pdf",
    "03b Clustering Part2.pdf",
    "04 RepresentationLearning.pdf",
    "05 DimensionalityReduction.pdf",
    "06 OutlierAnalysis.pdf",
    "07a PatternDiscovery.pdf",
    "07b SubspaceClustering v2.pdf",
    "08 AdvancedPM LearningFromComplexData.pdf",
]

# Strings to remove from each lecture
REMOVE_STRINGS = [
    "TÉCNICO+ FORMAÇÃO AVANÇADA",
    "TÉCNICO+ FORMAÇÃO ALGARA",
    "TÉCNICO FORMAÇÃO ALGARA",
    "TÉCNICO FORMAÇÃO AV",
    "TÉCNICO FORMAÇÃO ALGÃO",
    "TÉCNI",
    "CO+ FORMAÇÃO AVANÇADA",
    "CO+",
    "CO FORMAÇÃO ALGARA",
    "CO FORMACÃO ALGARA",
    " CO FORMAÇÃO ALGARA",
    " FORMAÇÃO AVANÇADA",
    "FORMAÇÃO AVANÇADA",
    "FORMAÇÃO ALGARA",
    "FORMACÃO AVANÇADA",
    "DASH: Data Science e Análise Não Supervisionada",
    "Rui Henriques, rmch@tecnico.ulisboa.pt",
    "Instituto Superior Técnico, Universidade de Lisboa",
    "Thank you!",
    "rmch@tecnico.ulisboa.pt",
    "rui henriques",
]


def clean_content(content: str) -> str:
    """Remove noise strings from content."""
    result = content
    for pattern in REMOVE_STRINGS:
        result = result.replace(pattern, "")
    # Remove lines with only numbers (page numbers)
    import re

    result = re.sub(r"^\s*\d+\s*$", "", result, flags=re.MULTILINE)
    # Remove lines that are just whitespace + FORMACÃO
    result = re.sub(r"^\s*CO\s*FORMAC[ÇC]O[^\w]*", "", result, flags=re.MULTILINE)
    result = re.sub(r"^\s*FORMAC[ÇC]O[^\w]*", "", result, flags=re.MULTILINE)
    # Remove image references ![img-N.jpeg](img-N.jpeg)
    result = re.sub(r"!\[img-\d+\.jpeg\]\(img-\d+\.jpeg\)", "", result)
    # Remove multiple blank lines
    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


def get_markdown_file(lecture_dir: Path) -> Path | None:
    """Find the markdown.md file in a lecture directory."""
    # Check directly in the lecture folder (not in subdirectory)
    md_file = lecture_dir / "markdown.md"
    if md_file.exists():
        return md_file
    return None


def extract_title(markdown_content: str) -> str:
    """Extract the main title from markdown content."""
    for line in markdown_content.split("\n"):
        line = line.strip()
        if line.startswith("# "):
            return line[2:].strip()
    return "Untitled"


def main():
    # Read all lecture files
    lectures_content = []

    for lecture_name in LECTURE_ORDER:
        lecture_dir = KNOWLEDGE_DIR / lecture_name
        md_file = get_markdown_file(lecture_dir)

        if md_file is None:
            print(f"Warning: No markdown.md found in {lecture_name}")
            continue

        content = md_file.read_text(encoding="utf-8")
        content = clean_content(content)
        title = extract_title(content)

        lectures_content.append(
            {
                "name": lecture_name.replace(".pdf", ""),
                "title": title,
                "content": content,
            }
        )
        print(f"Added: {title}")

    # Build master markdown
    master_content = []

    # Header
    master_content.append("# Machine Learning - Complete Lecture Notes\n")
    master_content.append("*Combined from OCR outputs*\n")
    master_content.append(f"\n*Total lectures: {len(lectures_content)}*\n")
    master_content.append("---\n")

    # Table of contents
    master_content.append("## Table of Contents\n")
    for i, lecture in enumerate(lectures_content, 1):
        master_content.append(
            f"{i}. [{lecture['title']}](#{lecture['name'].lower().replace(' ', '-').replace('.', '').replace('-', '-')})\n"
        )
    master_content.append("\n---\n")

    # Add each lecture
    for i, lecture in enumerate(lectures_content, 1):
        master_content.append(f"\n## Lecture {i}: {lecture['title']}\n")
        master_content.append(f"\n*Source: {lecture['name']}*\n")
        master_content.append("\n---\n")
        master_content.append(lecture["content"])
        master_content.append("\n\n---\n")

    # Write output
    output_content = "".join(master_content)
    OUTPUT_FILE.write_text(output_content, encoding="utf-8")

    print(f"\n✓ Master file created: {OUTPUT_FILE}")
    print(f"  Total size: {len(output_content):,} characters")


if __name__ == "__main__":
    main()
