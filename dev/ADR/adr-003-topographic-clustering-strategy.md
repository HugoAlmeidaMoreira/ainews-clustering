---
id: "0003"
title: "Topographic Clustering & Semantic Painting"
status: "proposed"
date: "2026-01-31"
authors: ["Hugo"]

category: "application"
tags: ["ai-clustering", "topography", "hdbscan", "umap"] 

drivers: ["Requirement to define a semantic landscape before temporal analysis"] 

replaces: "" 
superseded_by: "" 
related_files: [
    "src/scripts/analysis/generate_news_semantics.py", 
    "src/scripts/analysis/semantic_painter.py",
    "ADR-002-semantic-dimensions-mapping.md",
    "ADR-006-entity-context-extraction.md"
] 
---

# ADR-003: Topographic Clustering & Semantic Painting

## Context & Problem Statement
We have successfully generated high-dimensional embeddings (Qwen-8B, 4096D) and multi-dimensional semantic scores (7 Sliders) for ~12,000 articles. 
The current challenge is to organize this "ocean" of data into a coherent **Topographic Map**. 
We need to distinguish between **Spatial Analysis** (where ideas sit in relation to each other) and **Temporal Analysis** (how they move over time). To avoid confusion, we will focus exclusively on the static topography first.

## Constraints & Assumptions
* **Constraint 1**: Must handle high-density clusters and noise (outliers).
* **Constraint 2**: Separation of Concerns: Spatial topography must be documented and validated before time-series analysis begins.
* **Assumption**: News topics naturally aggregate into "Islands" (Clusters) with varying densities.

---

## Decision
We will implement a **Hybrid Topographic Strategy** that combines density-based diagnostics with global partitioning to ensure a robust and comprehensive semantic mapping:

1.  **Topological Noise Pruning (HDBSCAN)**:
    *   **Logic**: Discovers "Islands" based on semantic density, identifying high-cohesion narrative cores.
    *   **Goal**: Isolate semantic noise and outliers (mavericks, fragile bridges) that would otherwise degrade cluster stability.
    *   **Output**: A "pruned" dataset and a clear diagnostic of semantic dispersion.

2.  **Structural Segmentation (K-Means)**:
    *   **Logic**: Divides the semantic space into $K=15$ Voronoi cells.
    *   **Goal**: Provide a "Total Coverage" map where every stable news item belongs to a well-defined region.
    *   **Value**: Ensures comprehensive structural mapping of the media ecosystem.

### Technical Implementation

#### 1. Geometric Backbone
*   **Dimensionality Reduction**: UMAP will be used for both strategies to project the 4096D (Qwen-8B) vectors into a more manageable 5D space for clustering.
*   **Strategy A (K-Means)**: Elbow method or Silhouette score to determine $K$.
*   **Strategy B (HDBSCAN)**: Parameter tuning for `min_cluster_size` to define the "granularity" of the islands.

#### 2. Hybrid Workflow
1.  **Noise Identification**: Run HDBSCAN on 5D UMAP latent space to tag outliers.
2.  **Structural Mapping**: Apply K-Means ($K=15$) to the manifold, using HDBSCAN results to validate cluster boundaries and identify "blurred" regions.
3.  **Semantic Painting**: Project the final K-Means regions onto the **Slider Matrix** (the 7 semantic axes) to extract DNA profiles.

#### 3. LLM-Assisted Interpretation & Validation
To bridge the gap between "Geometric Points" and "Human Meaning", we will use a Large Language Model (e.g., Qwen-72B-Instruct via vLLM) as a **Semantic Cartographer**:
*   **Topic Synthesis**: We feed the top N articles (closest to centroid) and the slider signatures of a cluster to the LLM to generate a natural language title and a 2-sentence summary of the "Island".
*   **Coherence Validation**: The LLM acts as a judge, identifying "intruder" news items within clusters to measure topographic precision.
*   **Context Extraction**: Uses pre-computed `ai_context_snippets` (ADR-006) for efficient and consistent article context, avoiding on-the-fly regex extraction.

**Semantic Painting Workflow (Micro-Architecture)**:
```mermaid
sequenceDiagram
    participant P as 🖌️ Semantic Painter<br/>(Python Client)
    participant DB as 🐘 Postgres<br/>(Topography Data)
    participant LLM as 🧠 vLLM Service<br/>(Qwen-72B)
    participant META as 🗃️ Metadata Table

    Note over P: Start Labeling Loop

    P->>DB: 1. Get Cluster IDs & Sizes
    DB-->>P: List [0, 1, 42, ...]

    loop For Each Cluster
        P->>DB: 2. Fetch Headlines + Slider Profile<br/>(Avg Scores for Cluster)
        DB-->>P: Titles [...] + Scores {Catastrophic: 0.8, ...}
        
        Note right of P: Construct Prompt:<br/>"Topic with these Titles<br/>AND this Emotional Profile?"

        P->>LLM: 3. POST /v1/chat/completions
        LLM-->>P: 4. Returns JSON:<br/>{ "label": "AI Doomerism", "summary": "High catastrophic scores..." }

        P->>META: 5. Upsert Metadata<br/>(Cluster ID + Label + Summary)
    end
``` 

### System Design Architecture
```mermaid
graph TD
    %% ---------------------------------------------------------
    %% COLOR PALETTE
    %% ---------------------------------------------------------
    classDef primary fill:#2563eb,stroke:#60a5fa,color:#fff
    classDef secondary fill:#4b5563,stroke:#9ca3af,color:#fff
    classDef math fill:#7e22ce,stroke:#a855f7,color:#fff
    classDef result fill:#16a34a,stroke:#4ade80,color:#fff
    classDef llm fill:#7e22ce,stroke:#a855f7,color:#fff

    DATA[("Postgres: ai_news<br/>(4096D Embeddings)")]:::secondary

    subgraph "Hybrid Topographic Pipeline"
        UMAP["UMAP Reduction<br/>(4096D -> 5D/2D)"]:::primary
        HDBSCAN["<b>HDBSCAN</b><br/>Noise/Outlier Diagnostics"]:::primary
        KMEANS["<b>K-Means (K=15)</b><br/>Structural Segmentation"]:::primary
    end

    subgraph "Semantic Interpretation Layer"
        PAINT["Semantic DNA Extraction<br/>(Slider Centroids)"]:::math
        LLM["<b>vLLM (Qwen-72B)</b><br/>Semantic Cartographer"]:::llm
    end

    subgraph "Output: Semantic Atlas"
        ISL["Topographic Map<br/>(Visual Representation)"]:::result
        LAB["Island Labels & Summaries<br/>(LLM-Generated)"]:::result
    end

    DATA --> UMAP
    UMAP --> HDBSCAN
    UMAP --> KMEANS
    
    KMEANS --> PAINT
    HDBSCAN -- "Outlier Filter" --> PAINT
    
    PAINT --> LLM
    LLM --> ISL
    LLM --> LAB
```

---

## Alternatives Considered

| Criteria | Option 1: K-Means (Baseline) | Option 2: HDBSCAN (Target) |
| :--- | :--- | :--- |
| **Philosophy** | **Centroid-based (Partition)** | **Density-based (Topology)** |
| **Noise Handling** | Forces noise into clusters | Tags noise as "-1" (Outliers) |
| **Scalability** | O(n) - Very Fast | O(n log n) - Fast |
| **Cluster Shape** | Assumes Spherical | Can find arbitrary shapes |
| **Academic Value** | Standard industry benchmark | State-of-the-art for NLP |

---

## Consequences

### Positive
*   **Evaluation Rigor**: Comparing two distinct algorithms makes the research significantly more robust for the Thesis/Eval.
*   **Methodological Transparency**: Highlights why a density-based approach might be better for media analysis than simple partitioning.
*   **Visual Richness**: Allows for "Side-by-Side" maps in the final presentation.

### Negative
* **Computational Cost**: UMAP and HDBSCAN on 12k records is light on Blackwell but requires careful parameter tuning (`min_cluster_size`).
* **Cluster Fragility**: Small changes in parameters can merge or split "islands".

---

## References

- [UMAP Documentation](https://umap-learn.readthedocs.io/)
- [HDBSCAN: Density-Based Clustering](https://hdbscan.readthedocs.io/)
- [Semantic Topography in Journalism (Internal Research)](notes/paper-exploration.md)
