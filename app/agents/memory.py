USER_MEMORY = {}


def update_memory(user_id, key, value):
    if user_id not in USER_MEMORY:
        USER_MEMORY[user_id] = {}

    USER_MEMORY[user_id][key] = value


def store_memory(user_id, data):
    """
    Stores conversation + extracts useful preferences
    """
    if user_id not in USER_MEMORY:
        USER_MEMORY[user_id] = {
            "history": [],
            "preferences": {}
        }

    # 🔹 Save full interaction history
    USER_MEMORY[user_id]["history"].append(data)

    query = data.get("query", "").lower()

    # 🔥 Auto-extract preferences
    if "gaming" in query:
        USER_MEMORY[user_id]["preferences"]["type"] = "gaming"

    if "under" in query or "$" in query:
        USER_MEMORY[user_id]["preferences"]["budget"] = query

    if "8gb" in query:
        USER_MEMORY[user_id]["preferences"]["ram"] = "8GB"

    if "16gb" in query:
        USER_MEMORY[user_id]["preferences"]["ram"] = "16GB"


def get_memory(user_id):
    """
    Returns structured memory (preferences + history)
    """
    return USER_MEMORY.get(user_id, {
        "history": [],
        "preferences": {}
    })