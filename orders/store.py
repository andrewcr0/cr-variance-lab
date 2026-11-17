"""In-memory order storage, kept in creation order."""

from __future__ import annotations

from datetime import datetime, timezone

from orders.models import Order, OrderStatus


def _day(day: int) -> datetime:
    return datetime(2026, 10, day, 12, 0, tzinfo=timezone.utc)


_ORDERS: list[Order] = [
    Order("ord_1001", "cus_01", "ana@example.com", OrderStatus.PAID, 1250, "USD", _day(1)),
    Order("ord_1002", "cus_02", "ben@example.com", OrderStatus.SHIPPED, 24900, "USD", _day(3)),
    Order("ord_1003", "cus_01", "ana@example.com", OrderStatus.PAID, 899, "EUR", _day(5)),
    Order("ord_1004", "cus_01", "ana@example.com", OrderStatus.CANCELLED, 5000, "USD", _day(8)),
    Order("ord_1005", "cus_01", "ana@example.com", OrderStatus.SHIPPED, 3100, "USD", _day(12)),
    Order("ord_1006", "cus_02", "ben@example.com", OrderStatus.PENDING, 1500, "USD", _day(15)),
]


def all_orders() -> list[Order]:
    return list(_ORDERS)


def get_order(order_id: str) -> Order | None:
    return next((o for o in _ORDERS if o.id == order_id), None)
