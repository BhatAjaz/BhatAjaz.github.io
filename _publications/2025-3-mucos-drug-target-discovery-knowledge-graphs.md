---
title: "MuCoS: Drug Target Discovery via Knowledge Graphs"
pub_id: 2025-3-mucos-drug-target-discovery-knowledge-graphs
image: "https://towardsdatascience.com/wp-content/uploads/2023/11/19wHbtSZRuyFyd0hMTt2ptQ.png"
authors: Gul H., Naim A. G., & Bhat A. A.
journal: ACL BioNLP 2025, Vienna, Austria, Proceedings of the 24th Workshop on Biomedical Language Processing (BioNLP 2025)
year: 2025
link: "https://aclanthology.org/2025.bionlp-1.27/"
video: 
tags: ["graph","bert","drug-discovery","link-prediction"]
date: 2025-01-01
layout: publication
abstract: "We introduce MuCoS (*Multi-Context-Aware Sampling*), a novel approach that efficiently discovers drug targets by sampling diverse contextual neighborhoods in biomedical KGs. Our method significantly improves target identification accuracy while reducing computational overhead."
---

## Abstract

Knowledge Graphs (KGs) have emerged as powerful tools for drug discovery, but existing methods often fail to capture the multi-contextual nature of biomedical relationships. We introduce **MuCoS** (*Multi-Context-Aware Sampling*), a novel approach that efficiently discovers drug targets by sampling diverse contextual neighborhoods in biomedical KGs. Our method significantly improves target identification accuracy while reducing computational overhead.

MuCoS frames drug–target prediction as a link prediction task on heterogeneous biomedical knowledge graphs that integrate drugs, proteins, diseases, pathways, and other relevant entities. By prioritizing high-density neighbors to capture salient structural patterns and integrating these with contextual embeddings derived from BERT, MuCoS eliminates the need for negative sampling—thereby reducing bias, computational cost, and improving generalization to unseen drug–target pairs.

---

## Problem Framing

Drug–target prediction is cast as a **link prediction task** on heterogeneous biomedical knowledge graphs where:
- **Nodes** represent entities such as drugs, proteins (genes), diseases, and pathways.
- **Edges** denote biological relationships (e.g., *drug–target*, *disease–gene*).

The goal is to **predict missing drug–target links** without relying on explicit negative sampling, which is often computationally expensive and introduces bias in training.

---

## Proposed Framework: MuCoS

**MuCoS** (*Multi-Context-Aware Sampling*) merges structural and contextual embedding paradigms by:
- Extracting informative neighborhoods around head, tail, and relation entities.
- Integrating density-based sampling to prioritize **high-frequency (high-density)** neighbors.
- Leveraging **BERT** to contextualize sampled structural information for accurate prediction.

This approach enables both **high predictive performance** and **computational efficiency**, making it suitable for real-world drug discovery pipelines.

---

## Context Extraction Strategy

### Head Context (`Hc`)
For a given head entity (e.g., a drug):
1. Identify all associated relations \( R(h) \).
2. Collect all directly connected tail entities \( E(h) \).
3. Select the top-\(n\) **high-density neighbors** based on entity frequency in the KG.

### Tail Context (`Tc`)
Applied symmetrically to candidate target entities (e.g., genes) using the same density-based procedure.

### Relation Context (`Rc`)
For each relation type:
- Gather all entities participating in that relation.
- Select top-\(m\) high-density entity pairs to form a compact relation-specific context.

---

## Modeling with BERT

The extracted contexts are **concatenated** with the head, tail, or relation (as appropriate) to form input sequences for BERT. This enables:
- Rich contextual encoding beyond static KG embeddings.
- Joint modeling of structural neighborhood and semantic information.
- End-to-end training with standard **cross-entropy loss**.

### Prediction Tasks
- **Link Prediction**: Infer whether a triple \((h, r, t)\) is valid.
- **Tail Prediction**: Given \((h, r)\), predict the most likely tail \(t\).

---

## Experimental Setup

### Dataset
- **KEGG50k**: 63,080 triples covering drugs, genes, diseases, and pathways.
  - Training: 57,080 triples  
  - Validation: 3,000  
  - Test: 3,000  
- Entity count: 16,201  
- Relation types: 9

### Evaluation Metrics
- **Mean Reciprocal Rank (MRR)**
- **Hits@k** (k = 1, 3, 10)

### Training Details
- BERT tokenizer with max length = 128
- AdamW optimizer, learning rate = 5e-5
- Batch size = 16, epochs = 50
- Hardware: NVIDIA RTX 3090 (24GB)

---

## Results and Discussion

| Task | Metric | MuCoS | Best Baseline (ComplEx-SE) | Gain |
|------|--------|-------|----------------------------|------|
| General Link Prediction | MRR | **0.65** | 0.52 | **+13%** |
| Drug–Target Prediction | MRR | **0.84** | 0.78 | **+6%** |
| Drug–Target Prediction | Hits@10 | **1.00** | 0.88 | **+12%** |

MuCoS consistently outperforms state-of-the-art KG completion models (e.g., TransE, DistMult, ComplEx, ComplEx-SE) on both general and drug-specific link prediction.

### Computational Efficiency
- **Speedup**: ~**175×** faster than the non-sampling variant **MuCo-KGC**.
- Achieved via **density-based neighbor sampling**, reducing context size while preserving predictive signal.
- Enables scalable inference on large biomedical KGs without sacrificing accuracy.

---

## Key Contributions

- ✅ **Eliminates negative sampling**—uses only positive triples with cross-entropy loss.
- ✅ **Description-independent**: Works without drug/target textual descriptions, ideal for sparse datasets.
- ✅ **Multi-context integration**: Simultaneously leverages head, tail, and relation neighborhoods.
- ✅ **Efficient & accurate**: Balances speed and performance for real-world deployment.

---

## Limitations and Future Work

- **Dataset scope**: Evaluation limited to KEGG50k; future work should include larger, diverse KGs (e.g., Hetionet, PharmKG-8k).
- **Model variants**: Explore lightweight transformers or alternate encoders for edge deployment.
- **Biological validation**: Predicted drug–target pairs should undergo experimental or literature-based validation to assess biological plausibility.
- **Dynamic KGs**: Extend MuCoS to handle temporal or evolving biomedical knowledge.

---

## Conclusion

MuCoS offers a novel, efficient, and effective framework for **drug–target interaction prediction** by unifying structural sampling and contextual language modeling. By focusing on high-density neighborhoods and leveraging BERT’s representational power, it achieves **state-of-the-art accuracy** with dramatically **reduced computational cost**. This makes MuCoS a practical tool for accelerating drug discovery and biomedical knowledge graph completion.

---

## References (Selected)

1. Mohamed, S. K., Nounu, A., & Nováček, V. (2019). Drug target discovery using knowledge graph embeddings. *SAC '19*.
2. Bordes, A., et al. (2013). Translating embeddings for modeling multi-relational data. *NeurIPS*.
3. Trouillon, T., et al. (2016). Complex embeddings for simple link prediction. *ICML*.
4. Gul, H., Naim, A. G., & Bhat, A. A. (2024). A Contextualized BERT model for Knowledge Graph Completion. *arXiv:2412.xxxx*.


--- 

*Prepared from ACL Anthology (2025.bionlp-1.27) and arXiv:2503.08075v1.*