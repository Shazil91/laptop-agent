from core.llm import chat

def rank_laptops(query, laptops):
    prompt = f"""
You are a laptop expert.

User query:
{query}

Laptops:
{laptops}

Return top 3 best laptops with short reasoning.
"""

    return chat(prompt)