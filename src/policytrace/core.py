from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Decision:
    status: str
    policy_version: str
    evidence: tuple[str, ...]
    reasons: tuple[str, ...]


def decide(record: dict[str, Any], version: str = "2026.1") -> Decision:
    required = ("resident", "income_ratio", "documents_complete")
    missing = tuple(k for k in required if k not in record)
    if missing:
        return Decision(
            "manual_review", version, tuple(record), tuple(f"missing:{x}" for x in missing)
        )
    evidence = tuple(required)
    if record["resident"] is not True:
        return Decision("ineligible", version, evidence, ("residency rule not met",))
    if not isinstance(record["income_ratio"], (int, float)):
        return Decision("manual_review", version, evidence, ("income ratio invalid",))
    if record["income_ratio"] > 1.0:
        return Decision("ineligible", version, evidence, ("income threshold exceeded",))
    if record["documents_complete"] is not True:
        return Decision("manual_review", version, evidence, ("documents incomplete",))
    return Decision("eligible", version, evidence, ("all versioned rules satisfied",))
