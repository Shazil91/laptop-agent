# 💻 LaptopHunter AI

An intelligent **Multi-Agent RAG-based Laptop Recommendation System** that uses embeddings, vector search, and LLM reasoning to provide personalized laptop suggestions.

---

# 🚀 Features

* 🔍 **RAG (Retrieval-Augmented Generation)** using Qdrant
* 🧠 **LLM-based reasoning & ranking**
* 🎯 **Hybrid filtering system** (deterministic + AI)
* 💾 **User memory & personalization**
* ⚡ **Tool-calling agent architecture**
* 🧩 Modular multi-agent design

---

# 🧠 Architecture

```text
User Query
   ↓
Memory Load
   ↓
Retriever (Qdrant Vector DB)
   ↓
Filter (price, RAM, etc.)
   ↓
LLM Ranking
   ↓
Response
   ↓
Memory Update
```

---

# 📂 Project Structure

```bash
laptop-agent/
│
├── app/
│   ├── agents/
│   │   ├── orchestrator.py
│   │   ├── retriever.py
│   │   ├── ranker.py
│   │   ├── memory.py
│   │   ├── filter.py
│   │   └── brain.py
│   │
│   ├── core/
│   │   ├── llm.py
│   │   └── config.py
│   │
│   ├── tools/
│   │   └── vector_db.py
│   │
│   └── main.py
│
├── data/
│   └── laptops.json
│
├── .env
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup Instructions

## 1. Clone the Repository

```bash
git clone https://github.com/your-username/laptop-agent.git
cd laptop-agent
```

## 2. Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Mac/Linux
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Setup Environment Variables

Create a `.env` file:

```env
QDRANT_URL=your_qdrant_url
QDRANT_API_KEY=your_qdrant_api_key
GEMINI_API_KEY=your_gemini_api_key
```

---

# ▶️ Run the Project

```bash
python app/main.py
```

Example:

```text
Ask: suggest gaming laptop under $800
```

---

# 🧠 How It Works

## 1. Retrieval (RAG)

* Converts query into embeddings
* Searches similar laptops using Qdrant

## 2. Filtering (Deterministic)

* Applies strict constraints like:

  * budget
  * RAM
  * keywords

## 3. LLM Ranking

* Uses LLM to:

  * understand intent
  * rank laptops
  * generate explanations

## 4. Memory System

* Stores:

  * user queries
  * preferences
* Improves future recommendations

---

# 🧩 Tech Stack

* **Python**
* **Qdrant** (Vector Database)
* **Sentence Transformers** (Embeddings)
* **LLM API (Gemini / OpenAI-compatible)**
* **dotenv** (Environment management)

---

# 💡 Example Queries

* "Gaming laptop under $800"
* "Laptop with 16GB RAM"
* "Best laptop for programming"

---

# 🏆 Resume Highlight

> Built a Multi-Agent RAG-based AI system using Qdrant and LLMs with hybrid filtering, memory, and tool-calling architecture for personalized laptop recommendations.

---

# 🚀 Future Improvements

* 🌐 FastAPI backend
* 💬 Chat UI (React / Streamlit)
* 🔄 Streaming responses
* 🧠 Advanced memory (vector-based user profiles)
* 📊 Analytics & feedback loop

---

# 🤝 Contributing

Pull requests are welcome! Feel free to open issues or suggest improvements.

---

# 📜 License

MIT License

---

# 🔥 Author

**Shazil Ali**

Building real-world AI systems 🚀
