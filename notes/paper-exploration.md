# Dialectical Note: The Physics of Public Attention
**Project:** Unsupervised Analysis of AI Media Discourse in Portugal
**Date:** January 10, 2026
**Context:** Especialização em Data Science e Análise Não-Supervisionada (Técnico+)

---

## 1. Thesis: The Static Analysis of Topics
**The Starting Point:**
We possess a dataset of ~12,000 Portuguese news items (2021–2024) covering the rise of Generative AI and the EU AI Act. The initial goal was to apply standard clustering techniques (K-Means, Hierarchical) to group these news items by content.

* **The Constraint:** Traditional clustering treats the timeline as a static container and every news item as having equal weight. It answers "What are the topics?" but fails to answer "How does the structure of meaning change under pressure?"
* **The Gap:** A static analysis ignores the "shock" events present in the data: the launch of ChatGPT (Nov 2022) and the regulatory milestones of the AI Act (Dec 2023, Mar 2024).

## 2. Antithesis: Temporal Dynamics and "Informational Mass"
**The Counter-Proposition (User Insights):**
Meaning is not static; it is a trajectory. However, analyzing trajectory window-by-window creates an "Alignment Problem" (Cluster A in Jan ≠ Cluster A in Feb). Furthermore, not all news items are equal—some carry more "weight" in the public sphere.

* **Insight A (The Alignment Problem):** To measure "Meaning in Transit," we cannot allow the semantic map to shift every month. We need a "Fixed Reference Frame" to measure how attention travels.
* **Insight B (Value-Weighted Analysis):** The dataset contains `AAV` (Advertising Value Equivalency). A front-page story on the AI Act has more "gravity" than a niche blog post on coding.
* **The Hypothesis of Polarization:** The proximity to legislation doesn't just shift sentiment; it structurally fractures the discourse. We postulated two potential outcomes:
    * *Funneling:* Discourse converges into a single, dense "Compliance" cluster.
    * *Polarization:* Discourse splits into distinct, non-overlapping clusters (e.g., "Innovation/Hype" vs. "Bureaucracy/Fear").

## 3. Synthesis: A Physics-Based Model of Media Discourse
**The Proposed Framework:**
We resolve the tension between static clustering and dynamic reality by adopting a **Complexity Science approach**. We treat the media landscape as a dynamic system where information has "mass," regulation exerts "force," and entities provide "persistence."

### 3.1. The Methodology: "The Fixed Canvas & Variable Topology"
We establish a global semantic space (vectorizing the entire 2021-2024 corpus once) to fix the "Territories" (Innovation, Law, Economics). Time is then projected onto this map.
* **Variable Topology:** While the *space* is fixed, the *number of active clusters ($k$)* changes over time.
* **Interpretation:**
    * **High $k$ (Fragmentation):** System in "boiling" phase (high entropy, low consensus).
    * **Low $k$ (Consolidation):** System in "crystallization" phase (forced consensus via regulation).

### 3.2. The Metric: The Media Barycenter
To measure the movement of ideas across the fixed canvas, we calculate the weighted center of mass.

$$
\vec{C}_t = \frac{\sum_{i=1}^{n} (v_i \cdot m_i)}{\sum_{i=1}^{n} m_i}
$$

* $\vec{C}_t$: The Center of Attention at time $t$.
* $v_i$: The semantic vector of the news item (fixed position).
* $m_i$: The AAV of the news item (variable weight).

**Key Dynamic:** High-value news items exert "gravitational pull," dragging the barycenter of the discourse from "Innovation Territories" to "Regulatory Territories."

### 3.3. The Hybrid Persistence-Seasonality Model
To better isolate "Shocks" from "Trends," we decompose the signal using Named Entity Recognition (NER).
* **Structure (Persistence):** Extracted Entities (e.g., "OpenAI", "EU Commission") act as the skeleton ($P_{ent}$). They are the anchors that do not change.
* **Context (Seasonality/Shock):** The text surrounding the entities ($C_{ctx}$) changes.
* **The Formula:**
    $$S(t) = P_{ent} + C_{ctx}(t) + \epsilon$$
* **Drift Analysis:** We measure the "Semantic Drift" of the *context* around specific entities. (e.g., Does the context of "OpenAI" shift from "Launch" to "Fired"?)

## 4. Research Questions & Hypotheses
**RQ:** *How do regulatory shocks disrupt the lifecycle of informational mass in the Portuguese AI ecosystem?*

* **H1 (The Inertia of Innovation):** Prior to shocks, the system exhibits high persistence. The context ($C_{ctx}$) surrounding key entities remains semantically stable.
* **H2 (The Regulatory Phase Transition):** As $t \to 0$ (distance to AI Act Approval), the system undergoes a structural break:
    * The "Informational Mass" (Total AAV) spikes.
    * The Barycenter ($\vec{C}_t$) shifts velocity and direction.
    * **Anchor Swap:** The discourse decouples from "Tech Entities" (e.g., Google) and re-couples with "Political Entities" (e.g., EU Parliament).

## 5. Next Steps (Action Plan)
1.  **Global Vectorization:** Apply TF-IDF/Embeddings to the full corpus to create the "Fixed Canvas."
2.  **NER Extraction:** Use `spaCy` to extract and cluster distinct entities to define the "Persistent Skeleton."
3.  **Feature Engineering:** Create `distance_to_chatgpt`, `distance_to_aiact_final`.
4.  **The "River" Analysis:** Calculate the optimal $k$ (using Silhouette Score) per month to visualize fragmentation.
5.  **Trajectory Plot:** Visualize the path of $\vec{C}_t$ on the fixed 2D PCA map to prove the "Gravitational Pull" of regulation.