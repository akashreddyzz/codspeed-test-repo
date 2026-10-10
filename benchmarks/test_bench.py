import pytest
from shop import order_total, normalize_labels, top_products

SIZES = {"small": 100, "large": 5000}

def orders(n): return [{"qty": i % 5 + 1, "price": 2.5} for i in range(n)]
def labels(n): return [f"  Label {i} Name " for i in range(n)]
def sales(n): return [(f"p{i % 200}", i % 7 + 1) for i in range(n)]

@pytest.mark.parametrize("size", list(SIZES))
def test_order_total(benchmark, size):
    benchmark(order_total, orders(SIZES[size]))

@pytest.mark.parametrize("size", list(SIZES))
def test_normalize_labels(benchmark, size):
    benchmark(normalize_labels, labels(SIZES[size]))

@pytest.mark.parametrize("size", list(SIZES))
def test_top_products(benchmark, size):
    benchmark(top_products, sales(SIZES[size]))
