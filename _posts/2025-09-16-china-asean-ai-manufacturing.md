---
layout: post
title: "Applied AI and AI-Enabled Robotics for Intelligent Manufacturing"
date: 2025-09-15
authors: "Dr. Ajaz Ahmad Bhat"
source: "2025 CHINA (GUANGXI) – ASEAN Vocational Education and Development Conference"
categories: [talks, conferences, keynote]
featured_image: "/assets/img/news/2025-09-16/nanning1.jpg"
external_link: ""
---

**Event:** 2025 CHINA (GUANGXI) – ASEAN Vocational Education and Development Conference on *“Artificial Intelligence + Advanced Manufacturing”*  
**Talk:** *Applied-AI & AI-enabled robotics* — **Applied AI and AI-Enabled Robotics — Creative Problem Solving as the Panacea for Intelligent Manufacturing**  
**Venue:** Auditorium, Guangxi Technological College of Machinery and Electricity (Nanning, China)  
**Dates:** 15–17 September 2025 (3 days)  
**Speaker:** Assistant Professor **Dr. Ajaz Ahmad Bhat**

---

## 🎤 Event Overview

Dr. Ajaz Ahmad Bhat was invited to deliver a keynote at the China–ASEAN vocational education conference focused on *AI + advanced manufacturing*. The keynote connected research advances in applied AI, knowledge representation, causal reasoning, and control to practical manufacturing problems, with an emphasis on creative problem solving as the key capability factories need to adapt and innovate.

---

## 🧭 Talk Summary

The talk argued that the single most transformative capability for manufacturing over the coming decade is **creative problem solving** — the ability for systems to imagine, evaluate, and execute novel solutions when the production plan breaks. Dr. Bhat presented a stacked view of required capabilities: **reliable control**, **causal understanding**, and **fluid human–robot collaboration**, supported by **memory** (knowledge graphs, episodic logs) and **long-range prediction**. He closed by proposing measurable metrics for success and illustrating these ideas with a concrete fuse-assembly example.

---

## 🔑 Opening — Hook (30–45 s)

> Good morning. If there’s one single capability that will transform manufacturing over the next decade, it isn’t a faster robot arm or a smarter sensor — it’s creative problem solving. The factories that truly adapt, recover from surprises, and innovate on the shop floor will be the ones whose systems can imagine, test, and execute novel solutions when things go off script.

---

## ✨ One-line framing (15 s)

Creative problem solving in manufacturing needs three things: **reliable control**, **causal understanding**, and **fluid collaboration**. Underpinning those are two capabilities: **memory** + **long-range prediction** — and finally, we need metrics to measure success. I’ll show how my research contributes to each part of that chain.

---

## 🧩 Worked Example — Fuse Assembly Scenario

**Problem:** A small insulating spacer used in a fuse housing is delayed; the production line must keep running.  

**Why creative:** The system must invent a safe substitute or an alternate assembly sequence using available parts and resources without compromising product safety.

**Needed capabilities:**

- **Long-range prediction:** infer downstream effects of delayed supplier shipments and suggest compatible alternatives.  
- **Knowledge graph lookup:** query parts, tolerances, and past substitution outcomes (e.g., MuCo-KGC / MuCoS knowledge artifacts).  
- **Causal reasoning:** estimate whether a substitute will change failure rates or safety margins.  
- **Adaptive control:** execute an assembly with slightly different geometry while maintaining process quality.  
- **Human–machine collaboration:** request rapid human approval when risk thresholds are crossed and incorporate feedback.  
- **Memory / logging:** record the trial and outcome to improve future decisions.

**Robot action (step-by-step):**

1. **Detect** the missing spacer via inventory/line-monitoring alert.  
2. **Query** the knowledge graph for similar spacers, compatible parts, and historical substitution outcomes (MuCo-KGC / MuCoS lookup).  
3. **Predict** fit and tolerance impact using a learned model (long-range prediction module).  
4. **Plan** a safe trial — generate an adjusted assembly trajectory and parameter set for the PMP controller.  
5. **Execute** a constrained safe trial with adaptive control (PMP controller), while monitoring key sensors.  
6. **Evaluate** outcome (functional tests, quick QA checks).  
7. **Log** results to memory with metadata (part IDs, parameters, sensor traces).  
8. **If safe**, scale rollout for the remaining produced units; **if risky**, escalate for human approval and supplier remediation.

---

## 🧾 Key Takeaways

- Creative problem solving is an operational capability, not just a research aspiration — it can be decomposed into concrete modules (prediction, KG lookup, causal models, control, memory).  
- Knowledge graphs + predictive models allow fast lookup and risk estimation for ad-hoc substitutions.  
- Adaptive controllers (e.g., PMP-like schemes) enable safe trials with slight geometry or tolerance changes.  
- Logging and memory close the loop: every trial improves the system’s future responses.

---

## 🌆 Personal Notes

During his visit to Nanning, Dr. Ajaz enjoyed walks at Nanhu Park, visits to Chaoyang Square, and exploring the city centre — experiences that provided informal cultural exchange and networking opportunities with fellow delegates.

---

![China–ASEAN Conference](/assets/img/news/2025-09-16/nanning2.jpg)

*Dr. Ajaz Ahmad Bhat — Keynote speaker, 2025 China (Guangxi) – ASEAN Vocational Education and Development Conference*
