"""Money formatting. Amounts are integer minor units; never pass floats."""

from __future__ import annotations

ZERO_DECIMAL = {"JPY", "KRW"}


def format_money(amount_cents: int, currency: str) -> str:
    if not isinstance(amount_cents, int):
        raise TypeError("amount_cents must be an int number of minor units")
    if currency in ZERO_DECIMAL:
        return f"{amount_cents:,} {currency}"
    return f"{amount_cents / 100:,.2f} {currency}"
