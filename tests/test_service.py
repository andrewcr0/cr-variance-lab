import unittest

from orders.errors import OrdersError
from orders.service import describe_order, get_order


class GetOrderTests(unittest.TestCase):
    def test_returns_existing_order(self):
        self.assertEqual(get_order("ord_1002").customer_id, "cus_02")

    def test_missing_order_raises_order_not_found(self):
        with self.assertRaises(OrdersError) as ctx:
            get_order("ord_nope")
        self.assertEqual(ctx.exception.code, "order_not_found")


class DescribeOrderTests(unittest.TestCase):
    def test_formats_amount_through_money_helper(self):
        self.assertEqual(describe_order("ord_1002"), "ord_1002: 249.00 USD (shipped)")


if __name__ == "__main__":
    unittest.main()
