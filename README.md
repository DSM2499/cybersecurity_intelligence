# 🛡️ Cybersecurity Intelligence AI System

**AI-powered Cyber Threat Intelligence pipeline leveraging CrewAI multi-agent orchestration, Exa API for real-time threat data, and Large Language Models (LLMs) for automated analysis & reporting.**  
**Fully Dockerized & production-ready.**

---

## 🚀 Project Overview

This project implements an **automated Cybersecurity Threat Intelligence system** with the following capabilities:

✅ Retrieves latest cybersecurity threats using **Exa API**  
✅ Analyzes relevant **CVEs and vulnerabilities**  
✅ Recommends **mitigation strategies** aligned with industry best practices  
✅ Generates a **structured Cyber Threat Intelligence Report** for security teams and executives  
✅ Orchestrates **multi-agent AI pipeline** using **CrewAI 0.126.x**  
✅ Supports **Groq Llama3 / OpenAI GPT / local Ollama LLMs**  
✅ Fully **Dockerized** → portable & reproducible anywhere  
✅ Includes **GitHub Actions CI** → auto-test on every push 🚀  

---

## 🎯 Architecture

```text
[Exa API] → Cyber Threat Analyst Agent → Threat Summary
                            ↓
            Vulnerability Researcher Agent → CVE Analysis
                            ↓
            Incident Response Advisor Agent → Mitigation Strategies
                            ↓
            Cybersecurity Report Writer Agent → Final Intelligence Report
                            ↓
            Agents coordinated via CrewAI Sequential Pipeline
                            ↓
            Inputs flow between agents
                            ↓
            Final report generated automatically
```

---

## ⚙️ Tech Stack
- 🧠 CrewAI 0.126.x → Multi-agent orchestration
- 🗂️ Exa API → Real-time Cyber Threat data retrieval
- 🤖 LLMs → Groq LLaMA 3 / OpenAI GPT / Ollama Mistral / LLaMA
- 🐳 Docker → Full app containerization
- 📝 Markdown → Final Intelligence Reports saved to `reports/` folder
- 🚀 GitHub Actions CI → Auto-build & test on every push

---

## 🏗️ Project Structure
cybersecurity_intelligence/
├── utils/                       # Utility functions (Exa helpers, etc.)
├── reports/                     # Generated Cyber Threat Intelligence Reports
├── crew.py                      # CrewAI agents + tasks orchestration
├── main.py                      # Entry point → runs full pipeline
├── .github/workflows/docker-build.yml   # GitHub Actions CI
├── requirements.txt             # Python dependencies
├── Dockerfile                   # Docker container definition
└── README.md                    # This file 🚀

--

## 🏃 How to Run Locally

### 1️⃣ Install Python & dependencies
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 2️⃣ Set environment variables
```bash
cp .env.example .env
# Edit .env → add your EXA_API_KEY and OPENAI_API_KEY and GROQ_API_KEY
```

### 3️⃣ Run the app
```bash
python main.py
```

#### 👉 Final Cyber Threat Intelligence Report will be saved to `reports/` folder.

---

## 🐳 How to Run with Docker

### 1️⃣ Build Docker image
```bash
docker build -t cybersecurity_intel_app .
```

### 2️⃣ Run container
```bash
docker run --rm --env-file .env -v $(pwd)/reports:/app/reports cybersecurity_intel_app
```

#### 👉 Final report will be saved to your local reports/ folder.

---
