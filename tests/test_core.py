import pytest

from policytrace.core import decide


def valid():
    return {"resident": True, "income_ratio": 0.7, "documents_complete": True}


def test_eligible():
    assert decide(valid()).status == "eligible"


def test_residency():
    r = valid()
    r["resident"] = False
    assert decide(r).status == "ineligible"


def test_income():
    r = valid()
    r["income_ratio"] = 1.1
    assert decide(r).status == "ineligible"


def test_docs():
    r = valid()
    r["documents_complete"] = False
    assert decide(r).status == "manual_review"


@pytest.mark.parametrize("field", ["resident", "income_ratio", "documents_complete"])
def test_missing(field):
    r = valid()
    r.pop(field)
    assert f"missing:{field}" in decide(r).reasons


@pytest.mark.parametrize("value", [None, "low", {}, []])
def test_invalid_income(value):
    r = valid()
    r["income_ratio"] = value
    assert decide(r).status == "manual_review"


def test_version_preserved():
    assert decide(valid(), "2027.4").policy_version == "2027.4"


def test_evidence_listed():
    assert decide(valid()).evidence == ("resident", "income_ratio", "documents_complete")
