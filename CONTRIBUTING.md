# Contributing

Corrections, new resources, and metadata improvements are welcome.

## Suggesting a resource

Open a **Resource suggestion** issue or submit a pull request that updates `data/papers.yaml`. A proposed entry should:

1. make a substantive technical contribution to AI workload verification, or analyze a directly relevant attack or policy application;
2. be publicly accessible through a stable landing page;
3. include enough detail for its assumptions and claims to be assessed; and
4. not duplicate an existing entry.

## Entry style

- Use the canonical title and complete author list.
- Format author given names as initials in the structured data.
- Prefer publisher or proceedings landing pages over direct PDF links.
- Keep notes factual, neutral, and limited to one sentence.
- Use existing categories and keywords where possible.
- Do not label work as “core,” “best,” or otherwise rank its quality.

After editing `data/papers.yaml`, run:

```bash
python scripts/generate_readme.py
```

Include the regenerated `README.md` in the same pull request.

## Corrections

For simple bibliographic corrections, an issue containing the entry title, proposed change, and authoritative source is sufficient.
