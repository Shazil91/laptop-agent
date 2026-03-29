def filter_laptops(laptops, query: str):
    query = query.lower()

    filtered = []

    for l in laptops:
        text = f"{l['name']} {l['price']} {l['ram']} {l['gpu']} {l['usage']}".lower()

        # 🔥 RULES (hard constraints)
        if "under" in query:
            try:
                budget = int(''.join(filter(str.isdigit, query)))
                if l["price"] > budget:
                    continue
            except:
                pass

        if "8gb" in query and "8gb" not in text:
            continue

        if "16gb" in query and "16gb" not in text:
            continue

        filtered.append(l)

    return filtered