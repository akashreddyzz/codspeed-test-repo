def order_total(orders):
    return sum(o["qty"] * o["price"] for o in orders)

def normalize_labels(labels):
    return [l.strip().lower().replace(" ", "-") for l in labels]

def top_products(sales, n=3):
    products = sorted({p for p, _ in sales})
    totals = {p: sum(q for pp, q in sales if pp == p) for p in products}
    return sorted(products, key=lambda p: (-totals[p], p))[:n]
