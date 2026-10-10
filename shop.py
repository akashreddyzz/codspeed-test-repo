def order_total(orders):
    return sum(o["qty"] * o["price"] for o in orders)

def normalize_labels(labels):
    return [l.strip().lower().replace(" ", "-") for l in labels]

def top_products(sales, n=3):
    totals = {}
    for product, qty in sales:
        totals[product] = totals.get(product, 0) + qty
    return sorted(totals, key=lambda p: (-totals[p], p))[:n]
