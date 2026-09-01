# PolicyTrace

**Explainable decisions for a synthetic public-benefit workflow.**

> All people, organizations, records, measurements, and outcomes in this
> repository are synthetic.

## The operational problem

Policy-assisted decisions must show the rule version, evidence, and unresolved facts behind every result.

## The proof

An allowlisted synthetic policy version, immutable demo rule/source IDs, strict evidence validation, deterministic decisions, and manual review for missing, malformed, or unknown-version inputs.

## Why this is forward deployed

The project begins with the operator's decision, uncertainty, failure cost,
integration boundary, and handoff—not with a model demo. It makes policy and
evidence inspectable, preserves human authority for consequential cases, and
remains useful when the optional model layer is unavailable.

## Architecture

```mermaid
flowchart LR
  A[Synthetic case] --> B[Required evidence check]
  B --> C[Versioned policy rules]
  C --> D{Decision}
  D -->|eligible| E[Reasons + citations]
  D -->|ineligible| E
  D -->|uncertain| F[Manual review]
  E --> G[Policy-version trace]
```

## Quickstart

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install -c constraints.txt -e '.[dev]'
pytest -q
policytrace
```

No API key or network connection is required.

## Evaluation and limitations

Run `pytest -q` for the reproducible evaluation. The fixture set is deliberately
synthetic and cannot establish production performance. A real deployment would
require operator observation, representative data, policy review, privacy review,
security testing, and a monitored rollout.

## Project documents

- [Field discovery and handoff](FIELD_NOTES.md)
- [Security boundaries](SECURITY.md)
- [Operating runbook](RUNBOOK.md)
- [Development provenance](DEVELOPMENT.md)
- [Release history](CHANGELOG.md)

## Topics

`govtech`, `policy-as-code`, `explainable-ai`, `audit`, `python`
