from __future__ import annotations

import json
from dataclasses import asdict

from .core import decide


def main() -> None:
    record = {"resident": True, "income_ratio": 0.72, "documents_complete": True}
    print(json.dumps({"synthetic": True, "decision": asdict(decide(record))}, indent=2))
