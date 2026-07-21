#!/usr/bin/env python3
from pathlib import Path
import re, yaml

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "papers.yaml"
README = ROOT / "README.md"
CATEGORY_ORDER = ['Research agendas and surveys', 'Trusted execution and attestation', 'Inference verification', 'Zero-knowledge proofs', 'Proof of learning and training', 'Network and memory telemetry', 'Power telemetry and side-channel attacks', 'Tamper resistance and detection', 'Motivations and policy proposals']
CATEGORY_INTROS = {'Research agendas and surveys': 'Broad research agendas, surveys, and system-level overviews of technical verification for AI governance.', 'Trusted execution and attestation': 'Approaches using trusted execution environments, confidential computing, and remote attestation to establish claims about models and workloads.', 'Inference verification': 'Methods for checking that declared inference computations produced observed outputs, including recomputation and information-flow approaches.', 'Zero-knowledge proofs': 'Cryptographic techniques for proving properties of model inference, evaluation, or training without revealing sensitive models or data.', 'Proof of learning and training': 'Methods for demonstrating facts about model training, including compute expenditure, training records, and data provenance.', 'Network and memory telemetry': 'Evidence derived from network traffic, accelerator memory, or off-chip monitoring and enforcement mechanisms.', 'Power telemetry and side-channel attacks': 'Workload signals from power and hardware telemetry, together with adversarial research showing privacy and security limitations of such signals.', 'Tamper resistance and detection': 'Mechanisms for detecting or responding to physical modification of computing systems and verification hardware.', 'Motivations and policy proposals': 'Policy analyses and proposed governance regimes that motivate, depend on, or assess technical workload-verification mechanisms.'}
START_IDS = ['reuel-open-problems-technical-ai-governance', 'baker-verifying-international-agreements-ai', 'ogara-hardware-enabled-verifying-responsible-ai', 'cankaya-system-overview-low-trust-compute-verification', 'rinberg-verifying-llm-inference-weight-exfiltration', 'schnabl-attestable-audits', 'jia-proof-of-learning-definitions-practice', 'sastry-computing-power-governance-ai']

def author_short(authors):
    if not authors: return "Unknown author"
    surname=lambda a: a.split()[-1]
    if len(authors)==1: return surname(authors[0])
    if len(authors)==2: return f"{surname(authors[0])} and {surname(authors[1])}"
    return f"{surname(authors[0])} et al."

def tags(p):
    values=[p["publication_type"]] + (p.get("secondary_categories") or [])[:1]
    return " ".join(f"`{v}`" for v in values if v)

def entry(p):
    return f"- **[{p['title']}]({p['url']})** — {author_short(p['authors'])} ({p.get('year') or 'n.d.'}). {p['note']} {tags(p)}"

def slug(s): return re.sub(r"[^a-z0-9 -]", "", s.lower()).replace(" ", "-")

def main():
    papers=yaml.safe_load(DATA.read_text(encoding="utf-8"))["papers"]
    byid={p["id"]:p for p in papers}
    bycat={c:[] for c in CATEGORY_ORDER}
    for p in papers: bycat.setdefault(p["primary_category"], []).append(p)
    for ps in bycat.values(): ps.sort(key=lambda p:(-(p.get("year") or 0), p["title"].lower()))
    toc="\n".join(f"- [{c}](#{slug(c)})" for c in CATEGORY_ORDER)
    out=[f"""# Awesome AI Workload Verification

> A curated bibliography of technical research on producing credible, privacy-preserving evidence about how AI hardware and computing infrastructure are used.

![Papers](https://img.shields.io/badge/resources-{len(papers)}-blue)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen)
![License](https://img.shields.io/badge/license-CC%20BY%204.0-blue)

AI workload verification concerns methods for establishing properties of computations performed on AI hardware—for example, whether accelerators are being used for training or inference, which model is running, whether required safeguards are active, or whether information has left an approved environment.

These techniques may support audits, commercial assurance, regulatory compliance, export-control enforcement, and low-trust agreements among AI developers or states. A recurring objective is to provide useful evidence while protecting sensitive models, data, and operational information.

## Contents

- [Scope](#scope)
- [Start Here](#start-here)
{toc}
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
- model watermarking or output detection unless it helps establish workload identity or compliance; and
- historical analogies without a substantial connection to implementable AI verification.

## Start Here

These resources provide complementary introductions to the field: broad agendas, policy motivation, systems architectures, and representative verification mechanisms.
"""]
    out += [entry(byid[i]) for i in START_IDS]
    for c in CATEGORY_ORDER:
        out.append(f"\n## {c}\n\n{CATEGORY_INTROS[c]}\n")
        out += [entry(p) for p in bycat.get(c, [])]
    out.append("""
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
""")
    README.write_text("\n".join(out).replace("\n\n\n", "\n\n"), encoding="utf-8")

if __name__ == "__main__": main()
