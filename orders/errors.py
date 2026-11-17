"""Errors raised by the orders package. Codes are snake_case <resource>_<reason>."""

from __future__ import annotations


class OrdersError(Exception):
    def __init__(self, code: str, message: str) -> None:
        super().__init__(message)
        self.code = code
        self.message = message


def order_not_found(order_id: str) -> OrdersError:
    return OrdersError("order_not_found", f"Order {order_id} does not exist")
