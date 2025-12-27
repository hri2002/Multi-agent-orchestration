# 🧠 Multi-Agentic Coding Framework (AutoGen + Ollama)

A **POC-level multi-agent system** built using **AutoGen** and **local LLaMA models via Ollama**, where specialized agents collaboratively analyze requirements, generate code, review and iteratively fix it, create test cases, generate documentation, and provide deployment steps — all through a **Streamlit UI**.

This project demonstrates **agent orchestration, feedback loops, and transparent reasoning**, without using any paid LLM APIs.

---

## 🚀 Key Features

- Multi-agent architecture using AutoGen  
- Local LLM inference using **Ollama (LLaMA models)**  
- Step-by-step agent execution visible in UI  
- **Code Review → Fix → Review** loop (max 2 iterations)  
- Mandatory test case generation (even for simple scripts)  
- Streamlit UI with live agent outputs  
- Fully offline, API-key free  
- Windows compatible  

---

## 🧩 Agents in the System

| Agent | Responsibility |
|------|---------------|
| Requirement Analysis Agent | Converts natural language input into structured requirements |
| Coding Agent | Generates Python code strictly based on requirements |
| Code Review Agent | Reviews code for correctness and best practices |
| Documentation Agent | Generates clear, structured documentation |
| Test Case Agent | Generates at least one pytest test |
| Deployment Agent | Provides run/deployment instructions |

---

## 🏗️ Architecture Overview

```
User Input
   ↓
Requirement Analysis Agent
   ↓
Coding Agent
   ↓
Code Review Agent
   ↓
Coding Agent (Fixes based on review)
   ↓
Code Review Agent (Final check)
   ↓
Documentation Agent
   ↓
Test Case Agent
   ↓
Deployment Agent
```

---

## 🛠️ Tech Stack

- Python 3.10+
- AutoGen
- Ollama (LLaMA models)
- Streamlit
- Pytest

---

## 📂 Project Structure

```
multi_agent_autogen/
│
├── agents/
│   ├── requirement_agent.py
│   ├── coding_agent.py
│   ├── review_agent.py
│   ├── documentation_agent.py
│   ├── test_agent.py
│   └── deployment_agent.py
│
├── orchestrator.py
├── streamlit.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.10 or above  
- Ollama installed  

Download Ollama from: https://ollama.com/download

### Pull Model
```bash
ollama pull llama3.1:8b
ollama serve
```

### Environment Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
pip install ag2[openai]
```

> Note: The openai package is installed only as a protocol dependency for AutoGen.  
> No OpenAI API calls are made.

---

## ▶️ Run the Application

```bash
streamlit run streamlit.py
```

Open:
```
http://localhost:8501
```

---

## 🧪 Example Inputs

**Simple**
```
Write a python code to print Hello World
```

**Medium**
```
Create a Python function to add two numbers with validation
```

**Complex**
```
Build a FastAPI application for user management with CRUD operations
```

---

## 🔁 Review → Fix Loop

- Initial code is generated
- Code Review Agent evaluates it
- Coding Agent fixes issues based on feedback
- Review Agent re-evaluates
- Loop runs a maximum of **2 iterations**

---

## 🧪 Testing Strategy

- Every task generates at least one test case
- Simple scripts → minimal pytest test
- Complex systems → structured test cases
- Tests are generated but not auto-executed (POC scope)

---

## ⚠️ Scope & Limitations

- Code is generated in-memory
- Tests are not executed automatically
- No persistent storage or databases
- Intended for POC, demos, and evaluation

---

## 👤 Author

**Varanasi Sai Hrishikesh**  
AI / Generative AI Engineer  
AWS • LLMs • Agentic Systems • Prompt Engineering
