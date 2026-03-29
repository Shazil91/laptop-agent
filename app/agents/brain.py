from core.llm import chat


def decide_action(query, memory):
    prompt = f"""
You are an AI Agent.

User query:
{query}

User memory:
{memory}

Decide next action:

Options:
1. search_laptops
2. answer_directly

Reply ONLY with one word:
search_laptops OR answer_directly
"""

    decision = chat(prompt).strip().lower()
    return decision