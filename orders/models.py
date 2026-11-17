"""Domain types. Money is integer minor units (cents) in an ISO 4217 currency."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class OrderStatus(str, Enum):
    PENDING = "pending"
    PAID = "paid"
    SHIPPED = "shipped"
    CANCELLED = "cancelled"


@dataclass(frozen=True)
class Order:
    id: str
    customer_id: str
    customer_email: str
    status: OrderStatus
    total_cents: int
    currency: str
    created_at: datetime
