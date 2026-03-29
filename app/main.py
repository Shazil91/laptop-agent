from agents.orchestrator import run_agent
from tools.vector_db import init_db, upsert_laptops
from tools.laptop_db import LAPTOPS
from dotenv import load_dotenv
load_dotenv()

def run():
    print("🚀 LaptopHunter AI (RAG + Multi-Agent)")

    init_db()
    upsert_laptops(LAPTOPS)

    user_id = "shazil"

    while True:
        query = input("\nAsk: ")

        if query.lower() == "exit":
            break

        response = run_agent(user_id, query)
        print("\n🤖 RESULT:\n", response)


if __name__ == "__main__":
    run()