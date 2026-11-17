# cr-variance-lab

Small order-handling package. Python 3.11+, standard library only. Run the tests with `python -m unittest`.

- `orders/models.py` holds the domain types. `orders/store.py` is storage. `orders/service.py` is the public API.

## Conventions

- Money is formatted only through `orders.money.format_money`. Never format amounts inline (f-string precision, `round`, `str`).
- Never log `customer_email` or any other customer PII. Log ids only.
- Errors are `OrdersError` instances built by a factory function in `orders/errors.py`, never constructed inline. Codes are snake_case `<resource>_<reason>`.
- Tests of an error path assert the error `code`, not only the exception type.
- Every public function has type hints for all parameters and the return value.
