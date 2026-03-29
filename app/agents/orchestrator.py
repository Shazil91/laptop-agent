from agents.retriever import retrieve_laptops
from agents.ranker import rank_laptops
from agents.memory import get_memory, store_memory
from agents.filter import filter_laptops


def run_agent(user_id, query):

    print("\n🧠 Agent started...")

    # 🔹 Memory
    memory = get_memory(user_id)

    # 🔹 Step 1: Retrieve (RAG)
    laptops = retrieve_laptops(query)

    if not laptops:
        return "❌ No laptops found."

    # 🔥 Step 2: HARD FILTER (NEW)
    laptops = filter_laptops(laptops, query)

    if not laptops:
        return "❌ No laptops match your requirements after filtering."

    # 🧠 Step 3: LLM Ranking
    enriched_query = f"""
User Query: {query}

User Preferences: {memory}

Instruction:
Rank laptops based on:
- performance
- budget fit
- user intent
"""

    result = rank_laptops(enriched_query, laptops)

    # 💾 Step 4: Memory update
    store_memory(user_id, {
        "query": query,
        "result": result
    })

    print("✅ Done\n")

    return result