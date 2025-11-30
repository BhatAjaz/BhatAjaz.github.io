---
title: A Contextualized BERT model for Knowledge Graph Completion
pub_id: 2024-1-contextualized-bert-knowledge-graph-completion
image: "https://images.pexels.com/photos/17808485/pexels-photo-17808485.jpeg"
authors: Gul H. & Bhat A. A.
journal: NeurIPS Workshop (to appear)
year: 2024
link: "https://arxiv.org/abs/2412.11016"
video: 
tags: ["KGC","graph","bert","transformer","context","embedding","link-prediction"]
date: 2024-01-01
layout: publication
abstract: "We introduce CAB‐KGC, a Context‐Aware BERT for KGC that leverages contextual information from neighboring entities and relations to predict missing tail entities. CAB‐KGC eliminates the need for entity descriptions and negative sampling, reducing compute while improving Hit@1 by 5.3% on FB15k-237 and 4.88% on WN18RR." 
---

## Abstract

Knowledge graphs (KGs) encode structured relations across domains but are often incomplete. Traditional embedding methods struggle with unseen entities; text‐based models incur high computational costs and semantic inconsistencies. We introduce CAB‐KGC, a Context‐Aware BERT for KGC that leverages contextual information from neighboring entities and relations to predict missing tail entities. CAB‐KGC eliminates the need for entity descriptions and negative sampling, reducing compute while improving Hit@1 by 5.3% on FB15k-237 and 4.88% on WN18RR.
## Methodology

CAB‐KGC constructs head context (Hc) and relation context (Rc) by sampling k‐hop neighbors of the head entity and adjacent relation sequences. Hc and Rc are concatenated into BERT‐formatted input sequences and fine-tuned with cross‐entropy loss to predict tail entities. No negative sampling is used. Models are trained and evaluated on FB15k-237 and WN18RR, with Hit@k and MRR reported against TransE, ComplEx, and KG-BERT baselines.
Knowledge graphs (KGs) encode structured relations across domains but are often incomplete. Traditional embedding methods struggle with unseen entities; text‐based models incur high computational costs and semantic inconsistencies. We introduce CAB‐KGC, a Context‐Aware BERT for KGC that leverages contextual information from neighboring entities and relations to predict missing tail entities. CAB‐KGC eliminates the need for entity descriptions and negative sampling, reducing compute while improving Hit@1 by 5.3% on FB15k-237 and 4.88% on WN18RR.
