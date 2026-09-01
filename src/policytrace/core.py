from __future__ import annotations

from dataclasses import dataclass
from math import isfinite
from typing import Any

POLICIES = {
    "2026.1": {
        "maximum_income_ratio": 1.0,
        "evidence": (
            "RULE-RESIDENCY-01@PUBLIC-DEMO-POLICY",
            "RULE-INCOME-01@PUBLIC-DEMO-POLICY",
            "RULE-DOCUMENTS-01@PUBLIC-DEMO-POLICY",
        ),
    }
}


@dataclass(frozen=True)
class Decision:
    status: str
    policy_version: str
    evidence: tuple[str, ...]
    reasons: tuple[str, ...]


def decide(record: dict[str, Any], version: str = "2026.1") -> Decision:
    policy = POLICIES.get(version)
    if policy is None:
        return Decision("manual_review", version, (), ("unknown policy version",))
    required = ("resident", "income_ratio", "documents_complete")
    missing = tuple(k for k in required if k not in record)
    if missing:
        return Decision(
            "manual_review", version, tuple(record), tuple(f"missing:{x}" for x in missing)
        )
    evidence = tuple(policy["evidence"])
    if record["resident"] is not True:
        return Decision("ineligible", version, evidence, ("residency rule not met",))
    income_ratio = record["income_ratio"]
    if (
        isinstance(income_ratio, bool)
        or not isinstance(income_ratio, (int, float))
        or not isfinite(income_ratio)
        or income_ratio < 0
    ):
        return Decision("manual_review", version, evidence, ("income ratio invalid",))
    if income_ratio > policy["maximum_income_ratio"]:
        return Decision("ineligible", version, evidence, ("income threshold exceeded",))
    if record["documents_complete"] is not True:
        return Decision("manual_review", version, evidence, ("documents incomplete",))
    return Decision("eligible", version, evidence, ("all versioned rules satisfied",))
