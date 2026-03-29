from core.llm import chat

def recommend(user_query, laptops):
    prompt = f"""
You are a laptop expert AI.

User request:
{user_query}

Available laptops:
{laptops}

Tasks:
1. Compare laptops
2. Rank them
3. Pick best option under budget
4. Explain why simply
"""

    return chat(prompt)