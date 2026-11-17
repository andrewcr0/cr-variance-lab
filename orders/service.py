"""Public API of the orders package."""

from __future__ import annotations

import logging

from orders import store
from orders.errors import order_not_found
from orders.models import Order
from orders.money import format_money

logger = logging.getLogger(__name__)


def get_order(order_id: str) -> Order:
    order = store.get_order(order_id)
    if order is None:
        raise order_not_found(order_id)
    logger.info("order fetched: %s", order.id)
    return order


def describe_order(order_id: str) -> str:
    order = get_order(order_id)
    return f"{order.id}: {format_money(order.total_cents, order.currency)} ({order.status.value})"
