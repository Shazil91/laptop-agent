LAPTOPS = [
    {
        "name": "Lenovo IdeaPad Gaming 3",
        "price": 850,
        "ram": "16GB",
        "gpu": "RTX 3050",
        "usage": "gaming coding budget"
    },
    {
        "name": "Acer Aspire 5",
        "price": 600,
        "ram": "8GB",
        "gpu": "Integrated",
        "usage": "coding student lightweight"
    },
    {
        "name": "HP Victus 15",
        "price": 950,
        "ram": "16GB",
        "gpu": "RTX 4050",
        "usage": "gaming heavy performance"
    }
]

def get_laptops_under_budget(budget: int):
    return [l for l in LAPTOPS if l["price"] <= budget]