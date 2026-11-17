# cr-variance-lab

A small, self-contained order-handling package used to compare CodeRabbit reviews of identical pull requests.

```sh
python -m unittest
```

| Function | Purpose |
| --- | --- |
| `orders.service.get_order` | Look up one order by id |
| `orders.service.describe_order` | One-line description of an order |
| `orders.summary.summarize_customer` | Order count, total spent and recent orders for one customer |
