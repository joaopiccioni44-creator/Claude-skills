"""Parse abbreviated view/like counts ('1.2M', '500K', '1,2 Mi')."""
from __future__ import annotations

import re

_SUFFIX = {
    "k": 1_000, "mil": 1_000,
    "m": 1_000_000, "mi": 1_000_000, "mm": 1_000_000,
    "b": 1_000_000_000, "bi": 1_000_000_000, "bn": 1_000_000_000,
}


def parse_count(raw: str | int | float | None) -> int | None:
    if raw is None:
        return None
    if isinstance(raw, (int, float)):
        return int(raw)
    s = str(raw).strip().lower().replace(",", ".").replace(" ", "")
    m = re.match(r"^([\d.]+)([a-z]*)$", s)
    if not m:
        digits = re.sub(r"[^\d]", "", s)
        return int(digits) if digits else None
    num, suf = m.groups()
    try:
        value = float(num)
    except ValueError:
        return None
    mult = _SUFFIX.get(suf, 1)
    return int(value * mult)
