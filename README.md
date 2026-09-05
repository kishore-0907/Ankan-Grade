# Ankan-Grade (Nyaya / VeritasEval AI) 🛡️📝
> **Board-Grade Descriptive Answer Sheet Evaluation & RTI Legal Defense Infrastructure**

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Cloudflare%20Tunnel-6366f1.svg)](https://concord-george-kidney-viewed.trycloudflare.com/)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask 3.1+](https://img.shields.io/badge/framework-Flask-lightgrey.svg)](https://flask.palletsprojects.com/)
[![Compliance](https://img.shields.io/badge/Compliance-RTI%20%26%20IT%20Act%2065B-emerald.svg)](#legal-defense--audit-trail)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> 🌐 **Live Tunnel Host:** [https://concord-george-kidney-viewed.trycloudflare.com/](https://concord-george-kidney-viewed.trycloudflare.com/)

---

## 📌 Strategic Overview & Problem Solved

Traditional AI grading systems (such as *Eklavvya*) face fatal trust and adoption hurdles with examination boards and universities:
1. **OCR Hallucinations & Smudges:** Standard OCR fails on regional cursive, crossed-out math, and smudged ink.
2. **Black-Box Scoring:** Generating a single aggregate score without defensible step-by-step criteria invites legal disputes.
3. **The Liability Bottleneck:** Examination boards cannot legally defend AI-issued marks in court or under Right to Information (RTI) petitions.

**Ankan-Grade** reframes the product from an "ed-tech tool" into a **sovereign risk management & legal defense infrastructure**.

---

## 🚀 Key Architectural Pillars

### 1. Layered Recognition Pipeline
- **Pass 1 (Fast OCR Draft):** High-speed preliminary transcription (Tesseract / Cloud Vision).
- **Pass 2 (Vision-LLM Cross-Check):** Multimodal LLM (Claude 3.5 Sonnet / GPT-4o) examines stroke vector geometry together with the physics/math context to infer smudged, crossed-out, or ambiguous terms.
- **Micro-Inspection Tasking:** Only flagged tokens (confidence < 80%) are highlighted for human review, allowing examiners to resolve ambiguities in **< 10 seconds** without re-reading entire scripts.

### 2. Defensible Step-by-Step Rubric Engine
- Grades are computed per criteria step (Formula definition, substitution, intermediate calculation, units).
- Evaluates against official board marking schemes, producing an unshakeable justification trail for every fraction of a mark.

### 3. Dual-AI Consensus & Moderation
- Every script is independently evaluated by two separate AI models:
  - **Primary Evaluator:** Claude 3.5 Sonnet
  - **Auditor Model:** GPT-4o Vision
- Discrepancy ($\Delta > 1.5\text{ M}$) automatically triggers an escalation to the **Senior Moderator** arbitration queue.

### 4. Human-in-the-Loop & Mandatory Justification Override
- AI **never** issues final marks.
- Examiners must sign off with **1-Click Approval** or use the **Override Drawer**.
- Any mark override strictly requires a **mandatory legal justification note**, recorded directly in the audit log.

### 5. Cryptographic RTI Legal Defense Dossier
- Every single event—from scanner ingestion, OCR correction, model prompts, examiner sign-offs, to score overrides—is timestamped into an immutable **SHA-256 hash chain**.
- Examiners and Board Controllers can export a court-admissible **RTI Defense Dossier** with a single click.

---

## 🖥️ Role-Based Workspaces
The application provides an instant role switcher in the top navigation:
- 👨‍🏫 **Examiner Mode:** Fast evaluation, micro-inspection of flagged words, 1-click approvals, and overrides.
- ⚖️ **Senior Moderator Mode:** Dedicated arbitration queue for scripts with high AI-AI or AI-Human discrepancy ($\Delta > 1.5\text{ M}$).
- 🏛️ **Board Controller (RTI) Mode:** Real-time monitoring of batch completion velocity, audit logs, and instant RTI packet generation.

---

## ⚡ Quickstart Guide

### Prerequisites
- Python 3.10 or higher
- Pip package manager

### 1. Clone the Repository
```bash
git clone https://github.com/kishore-0907/Ankan-Grade.git
cd Ankan-Grade
```

### 2. Install Dependencies
```bash
python -m pip install -r requirements.txt
```

### 3. Run the Server
```bash
python app.py
```

### 4. Open in Browser
Visit **[http://127.0.0.1:5000](http://127.0.0.1:5000)** or **[http://localhost:5000](http://localhost:5000)**.

---

## 📂 Project Structure

```plaintext
Ankan-Grade/
├── backend/               # FastAPI async backend (Claude vision client, DB, models)
├── templates/
│   └── index.html         # Main Evaluation Dashboard
├── index.html             # Standalone web app / GitHub Pages root
├── login.html             # Role-based authentication & sign-in page
├── slides.html            # Interactive 10-slide architectural pitch deck
├── slides_assets/         # Pitch deck illustrations & diagrams
├── AI_Grading_System_10_Slide_Presentation.pptx # Master PowerPoint deck
├── app.py                 # Core Flask backend server & REST API
├── server.py              # Lightweight static HTTP server
├── requirements.txt       # Python dependencies
├── push.bat               # Interactive 1-click GitHub push tool
├── run_app.bat            # 1-click local server launcher
├── .gitignore             # Git ignore configuration
└── README.md              # Project documentation & architecture guide
```

---

## 📜 REST API Reference

| Endpoint | Method | Description |
|---|---|---|
| `/` | `GET` | Serves the main evaluation web application |
| `/api/scripts` | `GET` | Fetches active batch candidate scripts |
| `/api/script/<id>` | `GET` | Retrieves detailed rubric & audit trail for a script |
| `/api/resolve-ambiguity` | `POST` | Micro-tasking endpoint to resolve low-confidence OCR words |
| `/api/approve` | `POST` | Human examiner 1-click approval with cryptographic timestamp |
| `/api/override` | `POST` | Human score override requiring mandatory defense note |
| `/api/export-rti/<id>` | `GET` | Generates full certified RTI Legal Defense Dossier |

---

## ⚖️ Legal & Compliance Note
Built in compliance with the **Indian Evidence Act Section 65B** (electronic records admissibility) and **RTI Act Section 4(1)(b)** proactive disclosure requirements. Data localization ready for sovereign cloud hosting.
