---
id: "0005"
title: "Semantic Context Extraction for Cluster Labeling"
status: "proposed"
date: "2026-01-31"
authors: ["Hugo"]

category: "application"
tags: ["nlp", "preprocessing", "llm", "context-window"] 

drivers: ["Need higher quality cluster labels than titles alone can provide", "Constraints on LLM context window and latency"] 

replaces: "" 
superseded_by: "" 
related_files: ["src/scripts/analysis/semantic_painter.py", "ADR-003-topographic-clustering-strategy.md"] 
---

# ADR-005: Semantic Context Extraction for Cluster Labeling

## Context & Problem Statement
We are using an LLM (Qwen-72B) to "paint" (label) clusters of news articles.
Initially, we fed only the **Titles** to the LLM. However, titles are often clickbait, vague, or insufficient to capture the nuance of a cluster (e.g., distinguishing between "AI Economic Boom" and "AI Job displacement" if titles are just "Market Report").

The database contains the full article content in the `description` column (Average length: ~6.4k chars, Max: ~280k chars).
Feeding full articles for 8-10 representatives per cluster would explode the LLM context window (32k tokens) and increase latency/cost significantly.

We need a strategy to extract the **most relevant semantic signal** from the noise.

## Constraints & Assumptions
*   **LLM Context**: Limited budget per cluster request (ideal < 4k tokens).
*   **Latency**: We want near-real-time labeling.
*   **Journalistic Structure**: We assume most news articles follow the "Inverted Pyramid" structure, where the most critical information is in the first paragraph (Lead).

---

## Decision
We will implement a **Lead Paragraph + Semantic Profile** extraction strategy.

1.  **Text Extraction**: We will extract the first **400 characters** of the `description` column.
    *   *Rationale*: This captures the "Lead Paragraph", which in journalism contains the Who, What, When, Where, and Why.
2.  **Semantic Enrichment**: We will inject the **Semantic Slider Scores** (Average of the cluster) into the prompt.
    *   *Rationale*: Disambiguates tone (e.g., High "Urgency" + High "Regulation" = "Crisis Policy" vs Low Urgency = "Long-term Legislation").

### Implementation Details
The Python `semantic_painter` script will fetch:
```sql
SELECT 
    title, 
    SUBSTRING(description, 1, 400) as context, 
    source 
FROM ai_news ...
```

The Prompt constructed will be:
```text
Title: {title}
Snippet: {context}...
[Source: {source}]
```

### System Design Architecture
No new infrastructure required. This is a logic change in the preprocessing step of the Semantic Painter.

---

## Alternatives Considered

| Criteria | Option 1: Full Text | Option 2: Smart Snippets (Regex) | Option 3: Lead Paragraph (Selected) |
| :--- | :--- | :--- | :--- |
| **Context Quality** | Maximum | High (Targeted) | High (Journalistic Standard) |
| **Implementation Complexity** | Low | High (Need robust regex/NLP) | Low (substring) |
| **Computational Cost** | Very High | Medium (Pre-processing CPU) | Low |
| **Risk** | Context Window Overflow | False Negatives (Missed keywords) | Weak for "Buried Lede" articles |

### Option 2: Smart Snippets (Extract paragraph with 'AI' keyword)
*   **Description**: Search for the keyword "Inteligência Artificial", "AI", or "LLM" and extract *that* paragraph.
*   **Pros**: Guarantees the snippet talks about AI.
*   **Cons**: Many articles discuss AI implicitly without the keyword in every paragraph, or the context is lost without the intro. Computationally slower to process text in Python vs SQL substring.

---

## Consequences

### Positive
*   **Higher Quality Labels**: LLM has "meat" to chew on, not just bones (titles).
*   **Efficient**: Keeps token usage low (~500 tokens per cluster batch).
*   **Robust**: Works for 100% of articles (since description column is fully populated).

### Negative
*   **Truncation Risk**: sentences cut in half (mitigated by LLM's ability to handle noise).
*   **Loss of Nuance**: If the real point is in the conclusion, we miss it.

## Future Work
If "Lead Paragraph" proves insufficient, we will invest in a **Hybrid Extractor** (Option 2) that prioritizes the Lead but appends an "AI Snippet" if the Lead is generic.
