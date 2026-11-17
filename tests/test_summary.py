import unittest

from orders.errors import OrdersError
from orders.summary import summarize_customer, summary_line


class SummarizeCustomerTests(unittest.TestCase):
    def test_totals_orders_for_customer(self):
        summary = summarize_customer("cus_02")
        self.assertEqual(summary.order_count, 2)
        self.assertEqual(summary.total_spent, 264.0)
        self.assertEqual(summary.currency, "USD")

    def test_summary_line(self):
        self.assertEqual(summary_line(summarize_customer("cus_02")), "cus_02: 2 orders, 264.00 USD spent")

    def test_unknown_customer(self):
        with self.assertRaises(OrdersError):
            summarize_customer("cus_nope")


if __name__ == "__main__":
    unittest.main()
