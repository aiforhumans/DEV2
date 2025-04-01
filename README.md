# 🤖 AI DEV Kit

The **AI DEV Kit** is a modular, Dockerized local development environment designed for experimenting with LLMs, agents, automations, and UI interfaces using tools like FastAPI, Streamlit, Qdrant, and n8n. Built for scalability, fast prototyping, and local-first development.

---

## 🧱 Features

- ⚙️ **FastAPI** backend for API agents
- 📊 **Streamlit** frontend for UI visualization
- 🧠 **Qdrant** vector database for embeddings
- 🔁 **n8n** automation platform with workflows
- 🐳 Fully Dockerized using `docker-compose`
- 🔧 Environment configuration with `.env.template`

---

## 🚀 Getting Started

### 1. Clone or extract this repo

```bash
cd C:/DEV/
```

### 2. Start the project

```bash
docker compose --env-file .env.template up --build
```

---

## 🌐 Services

| Service     | URL                            | Description                     |
|-------------|--------------------------------|---------------------------------|
| Backend     | http://localhost:8000/ping     | FastAPI Health Check Endpoint   |
| Frontend    | http://localhost:8501          | Streamlit Application UI        |
| Qdrant DB   | http://localhost:6333          | Vector Database API             |
| n8n         | http://localhost:5678          | Automation Workflows GUI        |

---

## 🔧 Configuration

Edit the `.env.template` file to set your local API URLs and environment flags:

```env
LM_STUDIO_URL=http://localhost:1234
QDRANT_URL=http://localhost:6333
USE_GRADIO=False
```

Rename this file to `.env` if you'd like to use it as the default for production.

---

## 📂 Folder Structure

```
ai-dev-kit/
│
├── backend/           # FastAPI app + Dockerfile
├── frontend/          # Streamlit app + Dockerfile
├── docker-compose.yml
├── .env.template
└── README.md
```

---

## 📦 Requirements

- Docker Desktop (Windows/Linux/macOS)
- Optional: LM Studio running on localhost

---

## ✅ Example Usage

After starting, visit:
- `http://localhost:8501` for the Streamlit UI
- `http://localhost:5678` for n8n workflow automation
- `http://localhost:8000/ping` for backend health
- `http://localhost:6333/dashboard` for Qdrant UI

---

## 🧠 Coming Soon

- LangChain agent container
- Web search & scraping tools
- Embedded persona builder
- LLM system prompt configurator

---

## 🙌 Credits

Created by [AI For Humans](https://github.com/aiforhumans)

---

