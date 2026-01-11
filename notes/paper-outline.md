# Research Paper Outline

**Title:** The Physics of Public Attention: Measuring Regulatory Shocks in the Informational Mass of AI Discourse using Weighted Semantic Barycenters

**Subtitle:** A Complexity Science Approach to the Dynamics of the Portuguese Media Ecosystem (2021-2024)

---

## 1. Abstract
* **Context:** Artificial Intelligence (AI) discourse is not a linear narrative but a complex adaptive system influenced by technological breakthroughs and regulatory interventions.
* **Problem:** Traditional text mining treats time as distinct bins, creating alignment problems where the meaning of topics shifts uncontrollably. Furthermore, it ignores the "weight" of media attention (Advertising Value Equivalency - AAV).
* **Methodology:** We propose a "Fixed Canvas" approach, projecting temporal data onto a static semantic map. We introduce the "Media Barycenter" to measure the trajectory of attention and a "Hybrid Persistence-Seasonality Model" (using NER) to decompose structural inertia from contextual shocks.
* **Contribution:** The paper demonstrates how regulatory shocks act as phase transitions, decoupling discourse from technical entities and anchoring it to political ones, while disrupting the "informational mass" of the system.

## 2. Introduction
### 2.1. The Media Ecosystem as a Complex System
* Definition of public discourse as a dynamic system with properties of inertia, momentum, and entropy.
* The role of "Agenda Setting" in the digital age: not just *what* is said, but *how loudly* it is said (AAV).

### 2.2. The Case Study: AI in Portugal
* The timeline: From the "tech-hype" (2021) to the "generative shock" (ChatGPT, Nov 2022) and the "regulatory shock" (EU AI Act, 2023-2024).
* Why Portugal? A case study of a peripheral European economy absorbing central EU regulation.

### 2.3. Research Questions
* **RQ1 (Trajectory):** How does the "Media Barycenter" of AI discourse travel across a fixed semantic map in response to regulatory milestones?
* **RQ2 (Structure):** How do "Shocks" disrupt the context surrounding persistent entities (e.g., OpenAI, EU Commission)?

## 3. Theoretical Framework & Related Work
* **Complexity Science in Social Systems:** Structural breaks, hysteresis, and phase transitions in time-series data.
* **NLP & Unsupervised Learning:** Review of global vectorization techniques and density-based clustering (DBSCAN) for variable topologies.
* **Media Economics:** The use of Advertising Value Equivalency (AAV) as a proxy for "social mass."

## 4. Methodology
### 4.1. Data Description & Preprocessing
* **Source:** Multi-source Portuguese news dataset (11,922 items).
* **Preprocessing:** Tokenization, Global TF-IDF/Embedding Vectorization (The "Fixed Canvas"), and Named Entity Recognition (NER) using spaCy.

### 4.2. Mathematical Model 1: The Media Barycenter
To capture the true "center of gravity" of the discourse without alignment issues, we utilize a fixed global vector space. We define the **Media Barycenter ($\vec{C}_t$)** as:

$$
\vec{C}_t = \frac{\sum_{i=1}^{n} (v_i \cdot m_i)}{\sum_{i=1}^{n} m_i}
$$

* $\vec{C}_t$: The Locus of public attention at time $t$.
* $v_i$: The **fixed** semantic vector of the news item.
* $m_i$: The **variable** Advertising Value Equivalency (AAV).

### 4.3. Mathematical Model 2: Hybrid Persistence-Seasonality
To isolate shocks, we decompose the signal into persistent anchors and variable contexts:

$$
S(t) = P_{ent} + C_{ctx}(t) + \epsilon
$$

* $P_{ent}$: **Persistence (Anchors).** Extracted Entities (e.g., "Sam Altman") that remain constant.
* $C_{ctx}(t)$: **Seasonality (Drift).** The changing semantic context surrounding these entities.

### 4.4. Experimental Setup
* **Time Series Segmentation:** Continuous sliding windows based on `distance_to_event` (ChatGPT, AI Act Pre-Agreement, AI Act Approval).
* **Variable Topology:** Determining the optimal $k$ (number of clusters) for each time window using Silhouette Analysis to measure system fragmentation vs. consolidation.

## 5. Results
### 5.1. The Inertia of Innovation (Pre-Regulation)
* Analysis showing high stability in the context ($C_{ctx}$) of tech entities and a stable Barycenter located in "Innovation" territories.

### 5.2. The Trajectory of Shocks (2023-2024)
* **Visualizing the "River":** A temporal plot of Optimal $k$, showing periods of high fragmentation (boiling) vs. consolidation (crystallization).
* **The "Tadpole" Plot:** 2D visualization of the $\vec{C}_t$ trajectory, demonstrating the gravitational pull of the "Regulation" cluster.

### 5.3. Structural Decoupling
* Evidence of "Anchor Swapping": How the discourse decouples from corporate entities (Google/Microsoft) and re-couples with institutional entities (EU Parliament) as the shock hits $t=0$.

## 6. Discussion
### 6.1. The Physics of Information
* Interpreting regulation not just as a constraint, but as a "gravitational force" that alters the trajectory of innovation narratives across the semantic map.

### 6.2. The "Regulatory Taker" Dilemma: Center-Periphery Dynamics
* **The Asymmetry of Influence:** We discuss the fundamental dilemma of editorial attention in a peripheral economy. Unlike in "Regulatory Maker" markets (US/Brussels), the high "Informational Mass" (AAV) generated in Portugal has near-zero elasticity to influence the regulation itself.
* **Reactive vs. Proactive Signal:** Consequently, the observed cluster movement is not an attempt to *shape* policy (Lobbying), but a collective mechanism to *metabolize* external imposition (Adaptation).
* **The "Echo Chamber" Effect:** The Portuguese media ecosystem acts as a "resonance chamber" for decisions made elsewhere, explaining why the discourse shifts so abruptly from "Global Innovation" to "Local Compliance" — it is a forced adaptation to an exogenous shock.

### 6.3. Policy Implications
* Understanding the "lag" and "resistance" of the media ecosystem. How policymakers can use this "Barycenter" metric to gauge if the national ecosystem is absorbing the regulation or rejecting it (via structural decoupling).
## 7. Conclusion
* Summary: Regulatory shocks act as phase transitions, forcing a structural break in the informational mass and altering the semantic orbit of persistent entities.
* Future Work: Applying the Barycenter model to other domains (e.g., Climate Change).

## 8. References
* (Standard bibliography on NLP, Complexity, and Media Studies).