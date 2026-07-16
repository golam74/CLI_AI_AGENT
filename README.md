# 🤖 CLI AI Agent

A production-ready local AI Agent built with **Python** and **Ollama**.

This project demonstrates how to build an intelligent command-line AI assistant capable of chatting with users, remembering conversations, and interacting with the local file system using custom tools.

---

# ✨ Features

- 💬 Local AI Chat
- 🧠 Conversation Memory
- 📂 Create Folder
- 📄 Create File
- ✍️ Write File
- 📖 Read File
- 📋 List Files
- ⚡ Interactive Command Line Interface (CLI)
- 🔒 100% Offline (Runs Locally)
- 🏗 Clean Modular Architecture

---

# 🛠 Tech Stack

- Python 3.11+
- Ollama
- Gemma 2B / Qwen 3
- python-dotenv
- pathlib

---

# 📂 Project Structure

```text
CLI_AI_AGENT/
│
├── app/
│   ├── __init__.py
│   ├── agent.py
│   ├── config.py
│   ├── llm.py
│   ├── memory.py
│   ├── prompts.py
│   └── tools.py
│
├── main.py
├── requirements.txt
├── .env
└── README.md
```

---

# 🚀 Getting Started

## 1. Clone Repository

```bash
git clone https://github.com/golam74/CLI_AI_AGENT

cd CLI_AI_AGENT
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4. Install Ollama

Download Ollama

https://ollama.com

Pull a model

```bash
ollama pull gemma2:2b
```

or

```bash
ollama pull qwen3:8b
```

---

## 5. Configure Environment

Create a `.env` file.

```env
OLLAMA_HOST=http://localhost:11434
OLLAMA_MODEL=gemma2:2b
```

---

## 6. Run the Project

```bash
python main.py
```

---

# 💡 Example Commands

## Create Folder

```text
Create folder Demo
```

---

## Create File

```text
Create file Demo/test.txt
```

---

## Write File

```text
Write file Demo/test.txt Hello AI Engineer
```

---

## Read File

```text
Read file Demo/test.txt
```

---

## List Files

```text
List files Demo
```

---

## Ask Questions

```text
What is Artificial Intelligence?

Explain Python.

Who developed Machine Learning?
```

---

# 🏗 Architecture

```text
             User
               │
               ▼
          main.py (CLI)
               │
               ▼
          agent.py
         /         \
        ▼           ▼
     Ollama      Tools
        │           │
        │           ├── Create Folder
        │           ├── Create File
        │           ├── Write File
        │           ├── Read File
        │           └── List Files
        │
        ▼
     Memory
        │
        ▼
     Response
```

---

# 📸 Demo

Add terminal screenshots or a GIF demonstrating:

- AI conversation
- Creating folders
- Creating files
- Writing files
- Reading files
- Listing files

---

# 🎯 Learning Outcomes

This project helped me learn:

- AI Agent Fundamentals
- Local LLM Integration
- Ollama API
- Prompt Engineering
- Conversation Memory
- Tool Calling
- Python Project Architecture
- Modular Programming
- CLI Application Development

---

# 🚀 Future Improvements

- JSON Tool Calling
- Function Calling
- Tool Registry
- Calculator Tool
- Weather Tool
- Web Search
- Persistent Memory
- SQLite
- ChromaDB
- Qdrant
- Voice Assistant
- FastAPI Backend
- Streamlit UI
- React Frontend

---

# 🤝 Contributing

Contributions, suggestions, and feedback are welcome.

Feel free to fork this repository and submit a pull request.

---

# 📄 License

This project is licensed under the MIT License.

---

# 👨‍💻 Author

**Golam Israil**

Aspiring AI Engineer

Building AI Agents • LLM Applications • RAG Systems • AI Automation

GitHub: https://github.com/golam74