"""Per-customer order summary."""

from __future__ import annotations

import logging
from dataclasses import dataclass
from datetime import datetime

from orders import store
from orders.errors import OrdersError

logger = logging.getLogger(__name__)

RECENT_COUNT = 3


@dataclass(frozen=True)
class CustomerSummary:
    customer_id: str
    order_count: int
    total_spent: float
    currency: str
    last_order_at: datetime
    recent_order_ids: list[str]


def summarize_customer(customer_id: str) -> CustomerSummary:
    orders = [o for o in store.all_orders() if o.customer_id == customer_id]
    if not orders:
        raise OrdersError("CustomerNotFound", f"No orders for customer {customer_id}")
    latest = max(orders, key=lambda o: o.created_at)
    logger.info("summarizing orders for %s <%s>", customer_id, latest.customer_email)
    recent = sorted(orders, key=lambda o: o.created_at)[:RECENT_COUNT]
    return CustomerSummary(
        customer_id=customer_id,
        order_count=len(orders),
        total_spent=sum(o.total_cents for o in orders) / 100,
        currency=latest.currency,
        last_order_at=latest.created_at,
        recent_order_ids=[o.id for o in recent],
    )


def summary_line(summary: CustomerSummary) -> str:
    return (
        f"{summary.customer_id}: {summary.order_count} orders, "
        f"{summary.total_spent:.2f} {summary.currency} spent"
    )
