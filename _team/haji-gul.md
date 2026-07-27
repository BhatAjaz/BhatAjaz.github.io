---
title: "Haji Gul"
member_id: "haji-gul"
role: "PhD Student"
image: "assets/img/team/haji-gul.jpg"
email: "23h1710@ubd.edu.bn"
interests:
  - "Knowledge Graphs"
  - "Knowledge Graph Completion"
  - "Link Prediction"
  - "Natural Language Processing"
  - "Complex Networks"
  - "Machine Learning"
layout: team-member
---

## Overview

Haji Gul is a PhD researcher in Artificial Intelligence at Universiti Brunei Darussalam. His research focuses on knowledge graphs — including knowledge graph completion (KGC), link prediction, evaluation, and complexity — alongside natural language processing, Transformers, and large language models. He also works on complex network analysis and graph clustering, with applications in pattern recognition. In 2025 he was awarded the DAAD AInet Fellowship in Natural Language Processing.

## Research Interests

- Knowledge Graphs & Knowledge Graph Completion
- Link Prediction and KG Evaluation
- Natural Language Processing
- Complex Networks & Graph Clustering
- Transformers, Pre-trained Language Models, and LLMs
- Machine Learning & Deep Learning

## Awards & Fellowships

- **DAAD AInet Fellowship — Natural Language Processing (May 2025).** Currently collaborating with Leuphana University, Germany. [[DAAD Profile]](https://www.daad.de/en/the-daad/postdocnet/fellows/fellows/#Gul_Haji)

## Academic Service

Reviewer / Program Committee Member for:

- **Conferences:** ICML, NeurIPS, AAAI, ICDM, MusIML @ ICML, World CIST (World Conference on Information Systems and Technologies)
- **Journals:** Scientific Reports, npj Complexity, Applied Network Science, Cluster Computing, Social Network Analysis and Mining, Transactions on Consumer Electronics

## Publications

<!-- ============================================================
     Haji Gul — Publications (dark theme, self-contained)
     Paste this whole block inside a page on the lab site
     (e.g. the body of _team/haji-gul.md under a Publications heading).
     Styles + script are included once; each paper is one card.
     Real content is filled for papers 1-2; papers 3-8 have
     DUMMY placeholders — replace the marked text with real
     abstracts / captions / BibTeX when ready.
     ============================================================ -->

<style>
.hg-paper{border:1px solid #2a2f3a;border-radius:14px;background:#12151c;
  margin:18px 0;overflow:hidden;
  font-family:system-ui,-apple-system,Segoe UI,Roboto,sans-serif;}
.hg-paper > summary{list-style:none;cursor:pointer;display:flex;align-items:center;
  gap:16px;padding:18px 22px;}
.hg-paper > summary::-webkit-details-marker{display:none;}
.hg-num{font-style:italic;color:#7f8a9e;font-size:1.05rem;min-width:18px;}
.hg-pt{flex:1;}
.hg-title{font-weight:700;color:#f2f4f8;font-size:1.05rem;line-height:1.3;}
.hg-venue{font-style:italic;color:#8a94a6;font-size:.9rem;margin-top:3px;}
.hg-toggle{width:30px;height:30px;border-radius:50%;border:1px solid #3a414f;
  display:flex;align-items:center;justify-content:center;font-size:1.2rem;
  color:#c3cad6;flex-shrink:0;transition:transform .2s;background:#1a1e27;}
.hg-paper[open] .hg-toggle{transform:rotate(45deg);}
.hg-body{padding:0 22px 22px;border-top:1px solid #232833;}
.hg-label{text-transform:uppercase;letter-spacing:.1em;font-size:.72rem;font-weight:700;
  color:#8a94a6;margin:18px 0 8px;}
.hg-abstract{color:#c8cfdb;line-height:1.65;font-size:.95rem;}
.hg-dummy{color:#e0a15a;}
.hg-fig{margin:20px 0;text-align:center;}
.hg-fig img{max-width:100%;height:auto;border:1px solid #2a2f3a;border-radius:8px;background:#fff;}
.hg-cap{font-style:italic;color:#8a94a6;font-size:.85rem;line-height:1.5;margin-top:10px;text-align:left;}
.hg-links{margin:14px 0;}
.hg-links a{display:inline-block;padding:7px 16px;border:1px solid #3a414f;border-radius:8px;
  text-decoration:none;color:#7fb0ff;font-size:.9rem;font-weight:600;margin-right:8px;}
.hg-links a:hover{background:#1a1e27;}
.hg-cite-wrap{border:1px solid #2a2f3a;border-radius:10px;overflow:hidden;margin-top:16px;}
.hg-cite-bar{display:flex;justify-content:space-between;align-items:center;
  background:#1a1e27;padding:8px 14px;border-bottom:1px solid #2a2f3a;}
.hg-cite-bar .lbl{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;
  color:#8a94a6;font-weight:700;}
.hg-copy{border:1px solid #3a414f;background:#12151c;border-radius:6px;padding:4px 12px;
  font-size:.82rem;cursor:pointer;color:#c8cfdb;}
.hg-copy.done{background:#123d24;border-color:#2f7a4a;color:#7fe0a0;}
.hg-cite{margin:0;padding:14px;font-size:.82rem;line-height:1.55;color:#c8cfdb;
  white-space:pre;overflow-x:auto;font-family:ui-monospace,Menlo,Consolas,monospace;background:#0d1017;}
</style>

<details class="hg-paper">
  <summary>
    <span class="hg-num">1</span>
    <div class="hg-pt">
      <div class="hg-title">MuCo-KGC: Multi-Context-Aware Knowledge Graph Completion</div>
      <div class="hg-venue">PAKDD 2025</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract">Knowledge Graph Completion (KGC) seeks to predict missing entities (e.g., heads or tails) or relationships in knowledge graphs (KGs), which often contain incomplete data. Traditional embedding-based methods, such as TransE and ComplEx, have improved tail entity prediction but struggle to generalize to unseen entities during testing. Textual-based models mitigate this issue by leveraging additional semantic context; however, their reliance on negative triplet sampling introduces high computational overhead, semantic inconsistencies, and data imbalance. Recent approaches, like KG-BERT, show promise but depend heavily on entity descriptions, which are often unavailable in KGs. Critically, existing methods overlook valuable structural information in the KG related to the entities and relationships. To address these challenges, we propose Multi-Context-Aware Knowledge Graph Completion (MuCo-KGC), a novel model that utilizes contextual information from linked entities and relations within the graph to predict tail entities. MuCo-KGC eliminates the need for entity descriptions and negative triplet sampling, significantly reducing computational complexity while enhancing performance. Our experiments on standard datasets, including FB15k-237, WN18RR, CoDEx-S, and CoDEx-M, demonstrate that MuCo-KGC outperforms state-of-the-art methods on three datasets. Notably, MuCo-KGC improves MRR on WN18RR, CoDEx-S, and CoDEx-M datasets by 1.63%, 3.77%, and 20.15% respectively, demonstrating its effectiveness for KGC tasks.</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/MuCo-KGC.png" alt="MuCo-KGC: Multi-Context-Aware Knowledge Graph Completion figure">
      <div class="hg-cap">Figure 1 &mdash; Overview of the MuCo-KGC model pipeline for predicting the tail entity, given a head entity h and relationship r. The left box shows the head context H<sub>c</sub> (union of relations R(h) and neighbouring entities E(h)); the right box shows the relationship context R<sub>c</sub>. These contextual features, alongside h and r, are fed into a BERT model with a linear classifier and softmax to generate tail-entity probabilities.</div>
    </div>
    <div class="hg-links">
      <a href="https://link.springer.com/chapter/10.1007/978-981-96-8298-0_1" target="_blank" rel="noopener">Paper &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite">@inproceedings{gul-2025-mucokgc,
    title = "MuCo-KGC: Multi-Context-Aware Knowledge Graph Completion",
    author = "Gul, Haji and Naim, Abdul Ghani and Bhat, Ajaz Ahmad",
    booktitle = "Advances in Knowledge Discovery and Data Mining (PAKDD)",
    year = "2025",
    publisher = "Springer",
    doi = "10.1007/978-981-96-8298-0_1",
    url = "https://dl.acm.org/doi/10.1007/978-981-96-8298-0_1"
}</pre>
    </div>
  </div>
</details>

<details class="hg-paper">
  <summary>
    <span class="hg-num">2</span>
    <div class="hg-pt">
      <div class="hg-title">MuCoS: Efficient Drug&ndash;Target Discovery via Multi-Context-Aware Sampling in Knowledge Graphs</div>
      <div class="hg-venue">BioNLP Workshop @ ACL 2025</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract">Accurate prediction of drug-target interactions is critical for accelerating drug discovery. In this work, we frame drug-target prediction as a link prediction task on heterogeneous biomedical knowledge graphs (KGs) that integrate drugs, proteins, diseases, pathways, and other relevant entities. Conventional KG embedding methods such as TransE and ComplEx are hindered by their reliance on computationally intensive negative sampling and their limited generalization to unseen drug-target pairs. To address these challenges, we propose Multi-Context-Aware Sampling (MuCoS), a novel framework that prioritizes high-density neighbours to capture salient structural patterns and integrates these with contextual embeddings derived from BERT. By unifying structural and textual modalities and selectively sampling highly informative patterns, MuCoS eliminates the need for negative sampling, significantly reduces computational overhead, and improves generalization to unseen drug-target pairs and targets. Extensive experiments on the KEGG50k and PharmKG-8k datasets demonstrate that MuCoS outperforms competitive baselines, achieving up to 13% improvement in MRR for general relation prediction on KEGG50k, up to 22% improvement in MRR on PharmKG-8k, and up to 6% improvement in dedicated drug-target relation prediction on KEGG50k.</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/MuCoS-model.png" alt="MuCoS: Efficient Drug&ndash;Target Discovery via Multi-Context-Aware Sampling in Knowledge Graphs figure">
      <div class="hg-cap hg-dummy">Figure 1 &mdash; Overview of the MuCoS model pipeline for predicting general and drug-target relations and tail entities. The input sequence to BERT combines head (h), head context (Hc), tail (t), tail context (Tc), relation (r), and relation context (Rc), passed through BERT with a linear classifier and softmax. [ Upload your figure as MuCoS-model.png &mdash; rename if different. ]</div>
    </div>
    <div class="hg-links">
      <a href="https://aclanthology.org/2025.bionlp-1.27/" target="_blank" rel="noopener">Paper &#8599;</a><a href="https://github.com/hajigul/MuCoS_KGC-Efficient-Drug-Target-Discovery-via-Multi-Context-Aware-Sampling-in-Knowledge-Graphs/tree/main" target="_blank" rel="noopener">Code &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite">@inproceedings{gul-etal-2025-mucos,
    title = "{M}u{C}o{S}: Efficient Drug{--}Target Discovery via Multi-Context-Aware Sampling in Knowledge Graphs",
    author = "Gul, Haji and Naim, Abdul Ghani and Bhat, Ajaz Ahmad",
    booktitle = "Proceedings of the 24th Workshop on Biomedical Language Processing",
    month = aug, year = "2025", address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.bionlp-1.27/",
    doi = "10.18653/v1/2025.bionlp-1.27", pages = "319--327",
    ISBN = "979-8-89176-275-6"
}</pre>
    </div>
  </div>
</details>

<details class="hg-paper">
  <summary>
    <span class="hg-num">3</span>
    <div class="hg-pt">
      <div class="hg-title">KG-EDAS: A Meta-Metric Framework for Evaluating Knowledge Graph Completion Models</div>
      <div class="hg-venue">IEEE BigData 2025</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract hg-dummy">[ DUMMY — replace with the real abstract for this paper. ]</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/KG-EDAS.png" alt="KG-EDAS: A Meta-Metric Framework for Evaluating Knowledge Graph Completion Models figure">
      <div class="hg-cap hg-dummy">[ DUMMY caption &mdash; upload your figure as <b>KG-EDAS.png</b> to the Dr_Ajaz_and_Haji_work folder, or rename here. ]</div>
    </div>
    <div class="hg-links">
      <a href="https://ieeexplore.ieee.org/document/11402521" target="_blank" rel="noopener">Paper &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite hg-dummy">[ DUMMY BibTeX — paste the real citation here. ]</pre>
    </div>
  </div>
</details>

<details class="hg-paper">
  <summary>
    <span class="hg-num">4</span>
    <div class="hg-pt">
      <div class="hg-title">Evaluating Knowledge Graph Complexity via Semantic, Spectral, and Structural Metrics for Link Prediction</div>
      <div class="hg-venue">IEEE BigData 2025</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract hg-dummy">[ DUMMY — replace with the real abstract for this paper. ]</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/KG-Complexity.png" alt="Evaluating Knowledge Graph Complexity via Semantic, Spectral, and Structural Metrics for Link Prediction figure">
      <div class="hg-cap hg-dummy">[ DUMMY caption &mdash; upload your figure as <b>KG-Complexity.png</b> to the Dr_Ajaz_and_Haji_work folder, or rename here. ]</div>
    </div>
    <div class="hg-links">
      <a href="https://ieeexplore.ieee.org/document/11401467" target="_blank" rel="noopener">Paper &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite hg-dummy">[ DUMMY BibTeX — paste the real citation here. ]</pre>
    </div>
  </div>
</details>

<details class="hg-paper">
  <summary>
    <span class="hg-num">5</span>
    <div class="hg-pt">
      <div class="hg-title">When Metrics Disagree: A Meta-Analysis of Knowledge-Graph-Completion Model Benchmarking</div>
      <div class="hg-venue">IEEE ICDM 2026</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract hg-dummy">[ DUMMY — replace with the real abstract for this paper. ]</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/When-Metrics.png" alt="When Metrics Disagree: A Meta-Analysis of Knowledge-Graph-Completion Model Benchmarking figure">
      <div class="hg-cap hg-dummy">[ DUMMY caption &mdash; upload your figure as <b>When-Metrics.png</b> to the Dr_Ajaz_and_Haji_work folder, or rename here. ]</div>
    </div>
    <div class="hg-links">
      <a href="https://arxiv.org/abs/2606.10287" target="_blank" rel="noopener">arXiv &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite hg-dummy">[ DUMMY BibTeX — paste the real citation here. ]</pre>
    </div>
  </div>
</details>

<details class="hg-paper">
  <summary>
    <span class="hg-num">6</span>
    <div class="hg-pt">
      <div class="hg-title">Evaluating Cumulative Spectral Gradient as a Complexity Measure</div>
      <div class="hg-venue">MusIML Workshop @ ICML 2025</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract hg-dummy">[ DUMMY — replace with the real abstract for this paper. ]</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/CSG.png" alt="Evaluating Cumulative Spectral Gradient as a Complexity Measure figure">
      <div class="hg-cap hg-dummy">[ DUMMY caption &mdash; upload your figure as <b>CSG.png</b> to the Dr_Ajaz_and_Haji_work folder, or rename here. ]</div>
    </div>
    <div class="hg-links">
      <a href="https://icml.cc/virtual/2025/50545" target="_blank" rel="noopener">Paper &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite hg-dummy">[ DUMMY BibTeX — paste the real citation here. ]</pre>
    </div>
  </div>
</details>

<details class="hg-paper">
  <summary>
    <span class="hg-num">7</span>
    <div class="hg-pt">
      <div class="hg-title">KG-EDAS: A Meta-Metric Framework for Evaluating Knowledge Graph Completion Models</div>
      <div class="hg-venue">GCLR Workshop @ AAAI 2025</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract hg-dummy">[ DUMMY — replace with the real abstract for this paper. ]</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/KG-EDAS-GCLR.png" alt="KG-EDAS: A Meta-Metric Framework for Evaluating Knowledge Graph Completion Models figure">
      <div class="hg-cap hg-dummy">[ DUMMY caption &mdash; upload your figure as <b>KG-EDAS-GCLR.png</b> to the Dr_Ajaz_and_Haji_work folder, or rename here. ]</div>
    </div>
    <div class="hg-links">
      <a href="https://sites.google.com/view/gclr2026/accepted-papers" target="_blank" rel="noopener">Paper &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite hg-dummy">[ DUMMY BibTeX — paste the real citation here. ]</pre>
    </div>
  </div>
</details>

<details class="hg-paper">
  <summary>
    <span class="hg-num">8</span>
    <div class="hg-pt">
      <div class="hg-title">A Contextualized BERT Model for Knowledge Graph Completion</div>
      <div class="hg-venue">MusIML Workshop @ NeurIPS 2024</div>
    </div>
    <span class="hg-toggle">+</span>
  </summary>
  <div class="hg-body">
    <div class="hg-label">Abstract</div>
    <p class="hg-abstract hg-dummy">[ DUMMY — replace with the real abstract for this paper. ]</p>
    <div class="hg-fig">
      <img src="https://raw.githubusercontent.com/BhatAjaz/BhatAjaz.github.io/main/assets/img/publications/Dr_Ajaz_and_Haji_work/BERT-KGC.png" alt="A Contextualized BERT Model for Knowledge Graph Completion figure">
      <div class="hg-cap hg-dummy">[ DUMMY caption &mdash; upload your figure as <b>BERT-KGC.png</b> to the Dr_Ajaz_and_Haji_work folder, or rename here. ]</div>
    </div>
    <div class="hg-links">
      <a href="https://neurips.cc/virtual/2024/109150" target="_blank" rel="noopener">Paper &#8599;</a>
    </div>
    <div class="hg-cite-wrap">
      <div class="hg-cite-bar">
        <span class="lbl">Cite (BibTeX)</span>
        <button class="hg-copy" onclick="hgCopyCite(this)">Copy</button>
      </div>
<pre class="hg-cite hg-dummy">[ DUMMY BibTeX — paste the real citation here. ]</pre>
    </div>
  </div>
</details>

<script>
function hgCopyCite(btn){
  var pre=btn.closest('.hg-cite-wrap').querySelector('pre.hg-cite');
  var text=pre.innerText;
  function done(){btn.textContent='Copied!';btn.classList.add('done');
    setTimeout(function(){btn.textContent='Copy';btn.classList.remove('done');},1600);}
  if(navigator.clipboard&&navigator.clipboard.writeText){
    navigator.clipboard.writeText(text).then(done).catch(function(){hgFallback(text,done);});
  }else{hgFallback(text,done);}
}
function hgFallback(text,cb){
  var ta=document.createElement('textarea');ta.value=text;ta.style.position='fixed';ta.style.opacity='0';
  document.body.appendChild(ta);ta.select();try{document.execCommand('copy');}catch(e){}
  document.body.removeChild(ta);cb();
}
</script>


## Contact

- Email: [23h1710@ubd.edu.bn](mailto:23h1710@ubd.edu.bn)
