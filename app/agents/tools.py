from agents.retriever import retrieve_laptops
from agents.ranker import rank_laptops
from agents.memory import get_memory, store_memory


def search_tool(query):
    return retrieve_laptops(query)


def rank_tool(query, laptops):
    return rank_laptops(query, laptops)


def memory_tool(user_id):
    return get_memory(user_id)


def save_memory_tool(user_id, data):
    store_memory(user_id, data)
    return "memory saved"