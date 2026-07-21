# Awesome AI Workload Verification

> A curated bibliography of technical research on producing credible, privacy-preserving evidence about how AI hardware and computing infrastructure are used.

![Papers](https://img.shields.io/badge/resources-66-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue)

AI workload verification establishes properties of computations performed on AI hardware — for example, whether accelerators are being used for training or inference, which model is running, whether required safeguards are active, or whether information has left an approved environment.

These techniques may support audits, commercial assurance, and compliance with regulations and standards at the national or international level. A recurring objective is to provide useful evidence while protecting sensitive models, data, and operational information.

## Contents

- [Scope](#scope)
- [Start Here](#start-here)
- [Research agendas and surveys](#research-agendas-and-surveys)
- [Trusted execution and attestation](#trusted-execution-and-attestation)
- [Inference verification](#inference-verification)
- [Zero-knowledge proofs](#zero-knowledge-proofs)
- [Proof of learning and training](#proof-of-learning-and-training)
- [Network and memory telemetry](#network-and-memory-telemetry)
- [Power telemetry and side-channel attacks](#power-telemetry-and-side-channel-attacks)
- [Tamper resistance and detection](#tamper-resistance-and-detection)
- [Motivations and policy proposals](#motivations-and-policy-proposals)
- [Using the Data](#using-the-data)
- [Contributing](#contributing)

## Scope

### Included

- methods for identifying, measuring, constraining, or reproducing AI workloads;
- verification of model identity, inference, evaluation, training, or training data;
- trusted execution, remote attestation, and privacy-preserving proofs applied to AI;
- trustworthy network, memory, power, or hardware telemetry;
- tamper resistance, evidence completeness, and attacks that directly affect verification; and
- policy proposals that substantially specify, motivate, or evaluate technical verification mechanisms.

### Generally excluded

- generic AI auditing without a technical execution-verification component;
- confidential-computing work without a clear AI-workload application;
- model watermarking or output detection unless it helps establish workload identity or compliance

## Start Here

These resources provide complementary introductions to the field: broad agendas, policy motivation, systems architectures, and representative verification mechanisms.

- **[Open Problems in Technical AI Governance](https://openreview.net/forum?id=1nO4qFMiS0)** — Reuel et al. (2025). Published in TMLR in 2025. `Journal` `Technical AI governance`
- **[Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment](https://www.rand.org/pubs/working_papers/WRA4077-1.html)** — Baker et al. (2025). RAND working paper WR-A4077-1; presents six layers of verification. `Working paper` `International verification`
- **[A System Overview for Near-Term, Low-Trust AI Compute Verification](https://intelligence.org/wp-content/uploads/2026/06/A-system-overview-for-near-term-low-trust-AI-compute-verification.pdf)** — Cankaya (2026). Proposes a retrofittable reference architecture separating evidence capture from later evaluation of randomly challenged workload records. `Working paper` `System architecture`
- **[Verifying LLM Inference to Detect Model Weight Exfiltration](https://arxiv.org/abs/2511.02620)** — Rinberg et al. (2025). Formalizes model-weight exfiltration as a security game and evaluates inference-verification methods for constraining covert information in model outputs. `Preprint` `Partial re-execution and sampling`
- **[Computing Power and the Governance of Artificial Intelligence](https://arxiv.org/abs/2402.08797)** — Sastry et al. (2024). Explains why compute is an attractive object of AI governance and analyzes governance applications, feasibility, risks, and research directions. `Preprint` `Compute governance`

## Research agendas and surveys

Broad research agendas, surveys, and system-level overviews of technical verification for AI governance.

- **[Frontier AI Auditing: Toward Rigorous Third-Party Assessment of Safety and Security Practices at Leading AI Companies](https://arxiv.org/abs/2601.11699)** — Brundage et al. (2026). Defines frontier AI auditing and proposes four AI Assurance Levels. `Preprint` `Auditing`
- **[Hardware-Level Governance of AI Compute: A Feasibility Taxonomy for Regulatory Compliance and Treaty Verification](https://arxiv.org/abs/2604.04712)** — Ansari (2026). Proposes and evaluates a taxonomy of 20 hardware-level governance mechanisms. `Preprint` `Hardware governance`
- **[Hardware-Enabled Mechanisms for Verifying Responsible AI Development](https://arxiv.org/abs/2505.03742)** — O'Gara et al. (2025). Identifies open questions for hardware-enabled verification of responsible AI development. `Preprint` `Hardware verification`
- **[Mechanisms to Verify International Agreements About AI Development](https://arxiv.org/abs/2506.15867)** — Scher and Thiergart (2025). Overview of verification approaches for three example policy goals. `Preprint` `International verification`
- **[Open Problems in Technical AI Governance](https://openreview.net/forum?id=1nO4qFMiS0)** — Reuel et al. (2025). Published in TMLR in 2025. `Journal` `Technical AI governance`
- **[Verification for International AI Governance](https://www.oxfordmartin.ox.ac.uk/publications/verification-for-international-ai-governance)** — Harack et al. (2025). Technical report on approaches to verifying international AI agreements. `Report` `International verification`
- **[Verifying International Agreements on AI: Six Layers of Verification for Rules on Large-Scale AI Development and Deployment](https://www.rand.org/pubs/working_papers/WRA4077-1.html)** — Baker et al. (2025). RAND working paper WR-A4077-1; presents six layers of verification. `Working paper` `International verification`
- **[AI Security RFDs](https://projects.aisecurity.forum/)** — Forum (n.d.). Index of research ideas on AI security and verification. `Project / discussion document` `Research directions`

## Trusted execution and attestation

Approaches using trusted execution environments, confidential computing, and remote attestation to establish claims about models and workloads.

- **[Cove: Compositional Multi-Party Confidential Workflows for Verifiable AI Governance](https://openreview.net/forum?id=t1dz06Vcee)** — Ding et al. (2026). Introduces a system for composing confidential workflows among mutually distrusting parties while preserving verifiability of the workflow and its outputs. `Workshop` `Confidential multi-party workflows`
- **[How Tinfoil Proves Exactly What Model Is Running](https://tinfoil.sh/blog/2026-02-03-proving-model-identity)** — Team (2026). Explains how Tinfoil binds enclave attestations to model weights loaded after boot by committing to a dm-verity root hash in the measured kernel command line. `Technical article` `Model identity`
- **[On TEEs for Privacy-Preserving Monitoring in AI Governance](https://techgov.intelligence.org/blog/on-tees-for-privacy-preserving-monitoring-in-ai-governance)** — Zhao (2026). Surveys the potential and limitations of TEE-based monitoring for AI governance, including deployment integrity, completeness, software auditability, and hardware roots of trust. `Technical article` `Governance applications and limitations`
- **[PAL*M: Property Attestation for Large Generative Models](https://arxiv.org/abs/2601.16199)** — Chantasantitam et al. (2026). Provides a property-attestation framework for large generative models using confidential VMs, security-aware GPUs, and incremental multiset hashing. `Preprint` `Model and dataset property attestation`
- **[Attestable Audits: Verifiable AI Safety Benchmarks Using Trusted Execution Environments](https://arxiv.org/abs/2506.23706)** — Schnabl et al. (2025). Proposes a TEE-based protocol that lets auditors and model providers run verifiable safety benchmarks without revealing proprietary models or benchmark data. `Preprint` `Verifiable audits`
- **[GuardAIn: Protecting Emerging Generative AI Workloads on Heterogeneous NPU](https://www.computer.org/csdl/proceedings-article/sp/2025/223600d823/26hiVLrJZi8)** — Dhar et al. (2025). Presents a confidential-computing architecture for discrete NPUs that removes the host system from the trusted computing base and supports task attestation. `Conference` `Confidential AI accelerators`

## Inference verification

Methods for checking that declared inference computations produced observed outputs, including recomputation and information-flow approaches.

- **[A System Overview for Near-Term, Low-Trust AI Compute Verification](https://intelligence.org/wp-content/uploads/2026/06/A-system-overview-for-near-term-low-trust-AI-compute-verification.pdf)** — Cankaya (2026). Proposes a retrofittable reference architecture separating evidence capture from later evaluation of randomly challenged workload records. `Working paper` `System architecture`
- **[Bit-Exact AI Inference Verification Without Performance Tradeoffs](https://arxiv.org/abs/2606.00279)** — Cankaya (2026). Shows that modern LLM inference can be recomputed bit-for-bit without performance-reducing determinism flags when relevant execution details are available. `Preprint` `Deterministic and reproducible inference`
- **[Example Schemes for Verifying High-Stakes AI Agreements](https://amododesign.com/notes/2026-06-23-verification-algorithms/)** — Design (2026). Outlines prototype recomputation-based schemes for verifying inference and pre-training workloads in cooperative prover–verifier settings. `Technical article` `Recomputation schemes`
- **[Verifying AI Compute by Bounding Unexplained Information Exfiltration](https://openreview.net/forum?id=qtgG5HZSsk)** — Petrie and Mühlhäuser (2026). Proposes hardware-independent verification using prover isolation, cryptographic commitments, and challenge-based recomputation to bound unexplained information in network outputs. `Workshop poster` `Information-flow accounting`
- **[DiFR: Inference Verification Despite Nondeterminism](https://arxiv.org/abs/2511.20621)** — Karvonen et al. (2025). Introduces token- and activation-based divergence measures for detecting incorrect or modified LLM inference despite benign numerical variation. `Preprint` `Partial re-execution and sampling`
- **[Verifying LLM Inference to Detect Model Weight Exfiltration](https://arxiv.org/abs/2511.02620)** — Rinberg et al. (2025). Formalizes model-weight exfiltration as a security game and evaluates inference-verification methods for constraining covert information in model outputs. `Preprint` `Partial re-execution and sampling`

## Zero-knowledge proofs

Cryptographic techniques for proving properties of model inference, evaluation, or training without revealing sensitive models or data.

- **[Verifiable constraints on frontier training via proofs of compartmentalization](https://openreview.net/forum?id=ajrtHuFw2S)** — al. (2026). Explores cryptographic proofs of compartmentalization as a means of enforcing verifiable constraints on frontier-model training. `Workshop` `Training constraints and compartmentalization`
- **[Zero knowledge verification for frontier AI training is possible](https://arxiv.org/abs/2606.05433)** — Peigné et al. (2026). Proposes an architecture for zero-knowledge verification of frontier dense pre-training using committed specifications, network observations, and intermediate-computation commitments. `Preprint` `Frontier model training`
- **[Trustless Audits without Revealing Data or Models](https://proceedings.mlr.press/v235/waiwitlikhit24a.html)** — Waiwitlikhit et al. (2024). Introduces ZkAudit, enabling private model and dataset properties to be audited using commitments and zero-knowledge proofs. `Conference` `Model and dataset audits`
- **[Verifiable evaluations of machine learning models using zkSNARKs](https://arxiv.org/abs/2402.02675)** — South et al. (2024). Demonstrates verifiable evaluation attestations for private models by proving inference and aggregate evaluation results with zkSNARKs. `Preprint` `Verifiable model evaluations`
- **[zkLLM: Zero Knowledge Proofs for Large Language Models](https://doi.org/10.1145/3658644.3670334)** — Sun et al. (2024). Develops specialized zero-knowledge protocols for large-language-model inference, including non-arithmetic operations and attention. `Conference` `Large-language-model inference`
- **[ZKML: An Optimizing System for ML Inference in Zero-Knowledge Proofs](https://doi.org/10.1145/3627703.3650088)** — Chen et al. (2024). Presents an optimizing system for generating zero-knowledge proofs for realistic machine-learning inference and end-to-end audits. `Conference` `Inference proofs`

## Proof of learning and training

Methods for demonstrating facts about model training, including compute expenditure, training records, and data provenance.

- **[Proof-of-Learning is Currently More Broken Than You Think](https://arxiv.org/abs/2208.03567)** — Fang et al. (2023). Demonstrates reproducible, low-cost attacks on proof-of-learning schemes and argues that robust verification depends on unresolved questions about deep-learning optimization. `Conference` `Attacks and limitations`
- **[Tools for Verifying Neural Models' Training Data](https://proceedings.neurips.cc/paper_files/paper/2023/hash/03e33e1f62e3302b47fe1d38a235921e-Abstract-Conference.html)** — Choi et al. (2023). Introduces proof-of-training-data protocols, including verifiable random-seed commitments and tests based on temporary overfitting to determine whether data were used in training. `Conference` `Proof of training data`
- **[What does it take to catch a Chinchilla? Verifying Rules on Large-Scale Neural Network Training via Compute Monitoring](https://arxiv.org/abs/2303.11341)** — Shavit (2023). Proposes a compute-monitoring architecture combining on-chip weight snapshots, training records, and chip-supply-chain monitoring to verify rules on large-scale neural-network training. `Preprint` `Compute monitoring`
- **[Proof-of-Learning: Definitions and Practice](https://ieeexplore.ieee.org/document/9519402/)** — Jia et al. (2021). Introduces proof of learning as a way to demonstrate that a party performed the optimization required to obtain a model, using logged training artifacts and checkpoint verification. `Conference` `Training-compute proofs`

## Network and memory telemetry

Evidence derived from network traffic, accelerator memory, or off-chip monitoring and enforcement mechanisms.

- **[Hardware Mechanisms to Dynamically Throttle AI Performance](https://arxiv.org/abs/2607.18069)** — Ma et al. (2026). Evaluates low-cost microarchitectural controls for dynamically limiting AI workload performance through GPU memory-system resources. `Preprint` `Hardware performance throttling`
- **[Off-Chip Compute Verification](https://docs.google.com/document/d/10317woljRRoX9Gtcwir1u36ytbA680xfYrazMcuLisA/edit?tab=t.0)** — Baker (2026). Working document on verification mechanisms implemented outside AI accelerators. `Working document` `Off-chip monitoring architecture`
- **[The Fundamentals and Feasibility of Secure Network Taps for Verifying AI Datacenter Use](https://nacicankaya.substack.com/p/research-note-the-fundamentals-and)** — Cankaya et al. (2026). Assesses where and how network taps could be deployed to support retrofittable verification of AI-datacenter use. `Technical article` `Secure network taps`
- **[Timing and Memory Telemetry on GPUs for AI Governance](https://arxiv.org/abs/2602.09369)** — Monfared et al. (2026). Evaluates timing- and memory-based measurement primitives for detecting GPU utilization without relying on trusted firmware or vendor counters. `Preprint` `GPU utilization telemetry`
- **[Flexible Hardware-Enabled Guarantees for AI Compute](https://arxiv.org/abs/2506.15093)** — Petrie et al. (2025). Introduces a flexible hardware-enabled guarantees architecture combining an auditable guarantee processor with a secure enclosure around AI accelerators. `Preprint` `Flexible hardware enforcement`
- **[Guaranteeable Memory: An HBM-Based Chiplet for Verifiable AI Workloads](https://openreview.net/forum?id=uc79kOv0MV)** — Petrie (2025). Proposes an HBM-based chiplet that mediates accelerator access to high-bandwidth memory to support verifiable constraints on AI workloads. `Workshop` `Memory-enforcement hardware`
- **[Software-Based Memory Erasure with relaxed isolation requirements: Extended Version](https://arxiv.org/abs/2401.06626)** — Bursuc et al. (2024). Develops software-based proof-of-secure-erasure protocols that remain secure when a prover can communicate with external helpers, provided that communication is sufficiently slow. `Preprint` `Proof of secure erasure`

## Power telemetry and side-channel attacks

Workload signals from power and hardware telemetry, together with adversarial research showing privacy and security limitations of such signals.

- **[Detecting Hidden ML Training With Zero-Overhead Telemetry](https://arxiv.org/abs/2606.19262)** — Rahman and Tajdari (2026). Evaluates adversarially robust classification of training workloads using zero-overhead, content-agnostic GPU telemetry across multiple GPU architectures. `Workshop paper` `Workload classification`
- **[Kraken: Higher-order EM Side-Channel Attacks on DNNs in Near and Far Field](https://arxiv.org/abs/2603.02891)** — Horvath et al. (2026). Extends GPU electromagnetic side-channel attacks to Tensor Cores and explores model leakage from far-field measurements. `Conference` `Near- and far-field electromagnetic leakage`
- **[Suppressing Side Channels in an Untrusted Data Center via Retrofitted Defenses](https://techgov.intelligence.org/blog/suppressing-side-channels-in-an-untrusted-data-center-via-retrofitted-defenses)** — Cankaya (2026). Surveys physical side channels in monitored AI data centers and proposes layered retrofitted defenses intended to bound covert communication bandwidth. `Technical article` `Side-channel suppression`
- **[Understanding Data Center Power Delivery](https://amododesign.com/data-center-power-delivery/)** — Maxwell et al. (2026). Maps AI data-center power-delivery stages, available measurements, and signals that may be relevant to AI-security monitoring. `Technical article` `Data-center power monitoring`
- **[BarraCUDA: Edge GPUs do Leak DNN Weights](https://www.usenix.org/conference/usenixsecurity25/presentation/horvath)** — Horvath et al. (2025). Demonstrates extraction of neural-network parameters from an edge GPU using correlation electromagnetic analysis. `Conference` `Electromagnetic model extraction`
- **[Detecting Anomalies in Machine Learning Infrastructure via Hardware Telemetry](https://arxiv.org/abs/2510.26008)** — Chen et al. (2025). Introduces System-X, an unsupervised hardware-telemetry pipeline for identifying system and network anomalies without inspecting ML workload contents. `Preprint` `Infrastructure anomaly detection`
- **[MoEcho: Exploiting Side-Channel Attacks to Compromise User Privacy in Mixture-of-Experts LLMs](https://doi.org/10.1145/3719027.3765174)** — Ding et al. (2025). Identifies CPU- and GPU-based architectural side channels that reveal routing patterns and sensitive inputs or outputs in mixture-of-experts models. `Conference` `Architectural side channels in mixture-of-experts models`
- **[DeepTheft: Stealing DNN Model Architectures through Power Side Channel](https://doi.org/10.1109/SP54263.2024.00250)** — Gao et al. (2024). Uses low-rate power and CPU-frequency traces to recover complex DNN architectures and layer hyperparameters in shared computing environments. `Conference` `Power-based architecture extraction`
- **[Empirical Measurements of AI Training Power Demand on a GPU-Accelerated Node](https://arxiv.org/abs/2412.08602)** — Latif et al. (2024). Reports node-level power measurements for ResNet and Llama 2 training on an eight-GPU H100 HGX system. `Preprint` `Training power measurement`
- **[Input-Dependent Power Usage in GPUs](https://arxiv.org/abs/2409.18324)** — Gregersen et al. (2024). Shows that changing GEMM input values while holding matrix shapes constant can alter GPU power consumption substantially, with implications for both optimization and telemetry. `Preprint` `Input-dependent power variation`
- **[A Practical Introduction to Side-Channel Extraction of Deep Neural Network Parameters](https://link.springer.com/book/10.1007/978-3-031-25319-5)** — Joud et al. (2022). Presents a practical coarse-to-fine electromagnetic side-channel method for extracting floating-point neural-network parameters from a Cortex-M7 microcontroller. `Conference` `Embedded-model parameter extraction`
- **[Detecting Covert Cryptomining using HPC](https://arxiv.org/abs/1909.00268)** — Gangwal et al. (2019). Uses hardware-performance-counter signatures and machine learning to detect covert cryptomining across multiple mining algorithms and processors. `Preprint` `Hardware-performance-counter classification`

## Tamper resistance and detection

Mechanisms for detecting or responding to physical modification of computing systems and verification hardware.

- **[ImpedanceVerif: On-Chip Impedance Sensing for System-Level Tampering Detection](https://eprint.iacr.org/2022/946)** — Mosavirik et al. (2023). Uses on-chip impedance measurements of a system's power-delivery network to detect physical modifications and system-level tampering. `Journal article` `On-chip impedance sensing`
- **[Anti-Tamper Radio: System-Level Tamper Detection for Computing Systems](https://ieeexplore.ieee.org/document/9833631/)** — Staat et al. (2022). Detects physical manipulation by monitoring changes in radio-wave propagation inside a protected computing-system enclosure. `Conference` `Radio-frequency tamper sensing`
- **[The Past, Present, and Future of Physical Security Enclosures: From Battery-Backed Monitoring to PUF-Based Inherent Security and Beyond](https://link.springer.com/article/10.1007/s41635-018-0045-2)** — Obermaier and Immler (2018). Surveys the evolution of physical security enclosures and discusses PUF-based approaches to inherent tamper evidence and response. `Journal article` `Physical security enclosures`
- **[IBM 4765 Cryptographic Coprocessor Security Module: Security Policy](https://csrc.nist.gov/csrc/media/projects/cryptographic-module-validation-program/documents/security-policies/140sp1505.pdf)** — Corporation (2012). Documents the security policy and tamper-responsive protections of the IBM 4765 cryptographic coprocessor validated under FIPS 140-2. `Security policy` `Tamper-responding cryptographic modules`

## Motivations and policy proposals

Policy analyses and proposed governance regimes that motivate, depend on, or assess technical workload-verification mechanisms.

- **[Components of a Frontier AI Slowdown](https://astrangeattractor.substack.com/p/components-of-a-frontier-ai-slowdown)** — Chan (2026). Distinguishes three design components of a frontier-AI slowdown: its aims, what activities are slowed, and its institutional structure. `Essay` `Slowdown design`
- **[Does Distributed Training Undermine Compute Governance?](https://arxiv.org/abs/2605.29359)** — Rahman (2026). Evaluates whether geographically or organizationally distributed training could evade compute-governance regimes and outlines possible countermeasures. `Workshop paper` `Distributed training and evasion`
- **[On restraining AI development for the sake of safety](https://joecarlsmith.com/2026/03/19/on-restraining-ai-development-for-the-sake-of-safety/)** — Carlsmith (2026). Analyzes the case for capability restraint, its practical forms, potential benefits, feasibility, and risks. `Essay` `Capability restraint`
- **[An International Agreement to Prevent the Premature Creation of Artificial Superintelligence](https://arxiv.org/abs/2511.10783)** — Scher et al. (2025). Proposes a US–China-led international agreement restricting large-scale training and dangerous AI research, backed by chip tracking and verification of chip use. `Report` `International capability restraint`
- **[Detecting Compute Structuring in AI Governance is Likely Feasible](https://openreview.net/forum?id=qseqw1sWzz)** — Seferis and Fist (2025). Examines whether developers could evade compute-based rules by splitting training across smaller clusters and assesses potential detection approaches. `Workshop paper` `Compute-threshold evasion`
- **[International AI Safety Report](https://internationalaisafetyreport.org/publication/international-ai-safety-report-2025)** — Bengio et al. (2025). Synthesizes scientific evidence on the capabilities, risks, and safety of advanced AI systems, including risks that motivate monitoring and verification. `Report` `AI risk assessment`
- **[Computing Power and the Governance of Artificial Intelligence](https://arxiv.org/abs/2402.08797)** — Sastry et al. (2024). Explains why compute is an attractive object of AI governance and analyzes governance applications, feasibility, risks, and research directions. `Preprint` `Compute governance`
- **[Governing Through the Cloud: The Intermediary Role of Compute Providers in AI Regulation](https://www.oxfordmartin.ox.ac.uk/publications/governing-through-the-cloud-the-intermediary-role-of-compute-providers-in-ai-regulation)** — Heim et al. (2024). Argues that compute providers can act as securers, record keepers, verifiers, and enforcers within AI regulatory systems. `Policy paper` `Compute-provider regulation`
- **[Hardware-Enabled Governance Mechanisms: Developing Technical Solutions to Exempt Items Otherwise Classified Under Export Control Classification Numbers 3A090 and 4A090](https://www.rand.org/pubs/working_papers/WRA3056-1.html)** — Kulp et al. (2024). Develops and assesses hardware-enabled mechanisms that could support targeted end-use restrictions on export-controlled AI chips. `Working paper` `Export-control enforcement`
- **[Secure, Governable Chips: Using On-Chip Mechanisms to Manage National Security Risks from AI & Advanced Computing](https://www.cnas.org/publications/reports/secure-governable-chips)** — Aarne et al. (2024). Proposes secure on-chip governance mechanisms for verification, operating licenses, export-control enforcement, and future international agreements. `Report` `On-chip governance`
- **[Verification methods for international AI agreements](https://arxiv.org/abs/2408.16074)** — Wasil et al. (2024). Surveys ten methods for detecting unauthorized AI training or data centers under international agreements. `Preprint` `International verification methods`
- **[International Governance of Civilian AI: A Jurisdictional Certification Approach](https://arxiv.org/abs/2308.15514)** — Trager et al. (2023). Proposes an international organization that certifies national jurisdictions for compliance with common AI oversight standards. `Report` `International certification`

## Using the Data

The repository includes the same bibliography in three formats:

- [`data/papers.yaml`](data/papers.yaml) — machine-readable source data used to generate this README;
- [`bibliography/master-bibliography.csv`](bibliography/master-bibliography.csv) — convenient for analysis and version control; and
- [`bibliography/master-bibliography.xlsx`](bibliography/master-bibliography.xlsx) — formatted spreadsheet with summary and review-notes sheets.

Run `python scripts/generate_readme.py` after editing `data/papers.yaml` to regenerate the categorized entries in this README.

## Contributing

Corrections and additions are welcome. Please read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening an issue or pull request. Entries should use neutral language, distinguish demonstrated results from proposed designs, and link to a stable public source.

## Acknowledgements

This collection builds on a reading list developed by Will Hodgkins and on earlier lists assembled by Mauricio Baker and James Petrie.

## License

The collection's original editorial material and structured metadata are available under the [Creative Commons Attribution 4.0 International License](LICENSE). Individual papers and linked materials retain their own licenses and copyrights.
