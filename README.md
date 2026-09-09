# AI Project Management Course

## Overview

The AI Project Management Course is a practical, end-to-end course designed to prepare Project Managers to lead AI and technology projects.

The course focuses on Project Management rather than programming.

The goal is to help Project Managers understand enough about AI, data, architecture, evaluation, security, governance, testing, deployment, and monitoring to make informed project decisions and lead cross-functional teams.

## Course Structure

The course contains 13 modules covering the complete project lifecycle.

The learning approach includes:

* BUILD
* DESIGN
* SIMULATE
* THEORY

The course includes both:

### PM Track

Project Management concepts, decisions, frameworks, requirements, planning, governance, risk, testing, release, and monitoring.

### Build Track

Hands-on exposure to the working Petadel PolicyAssist AI reference project.

The Build Track is designed to provide practical understanding without turning the course into a programming course.

## Capstone Project

### Petadel PolicyAssist AI

Petadel PolicyAssist AI is the course reference project and demonstrates an AI-powered policy assistance solution for Petadel Technology Services (PTS).

You may use the Petadel PolicyAssist AI reference project or apply the same Project Management process to your own AI product or use case.

The business problem is that employees may have difficulty locating and understanding authoritative company policies.

PolicyAssist is designed to retrieve relevant policy information from approved documents and provide responses supported by appropriate policy sources.

The project addresses:

* Policy discovery
* Document ingestion
* Knowledge management
* Semantic retrieval
* Response generation
* Grounding
* Citation
* Access control
* Evaluation
* Security
* Governance
* User Acceptance Testing
* Release management
* Monitoring
* Continuous improvement

The capstone is introduced during the course and fully executed in Module 12.

## Capstone Lifecycle

The project follows the complete project lifecycle:

**Initiation → Discovery → Requirements → Planning → Architecture → Build → Evaluation → Security and Governance → UAT → Release → Monitoring → Continuous Improvement**

This lifecycle connects the concepts taught throughout the course.

## Templates Library

The course includes a reusable library of Project Management and AI project templates.

The library includes:

1. Project Charter
2. Problem Statement
3. Stakeholder Register
4. RACI Matrix
5. Requirements Document
6. User Story
7. Acceptance Criteria
8. Product Backlog
9. RAID Log
10. Risk Register
11. Data Readiness Assessment
12. AI Evaluation Plan
13. AI Risk, Security and Governance
14. Test Plan
15. UAT Plan
16. Defect Log
17. Pilot Plan
18. Release and Deployment Plan
19. Go/No-Go Checklist
20. Monitoring and Continuous Improvement
21. Decision Log
22. Executive Project Summary

These templates can be reused for real-world technology and AI projects.

## Course Repository Structure

```text
AI-Project-Management-Course/
│
├── README.md
├── 01-COURSE-GUIDE.md
├── 02-SYLLABUS.md
├── 03-GLOSSARY.md
│
├── Modules/
│
├── Templates/
│
├── Student-Resources/
│
├── Student-Build-Along/
│
├── Capstone/
│   └── Petadel-Policy-Assist/
│
├── Portfolio/
│
└── PolicyAssist-App/
```

## Working Application

The course includes the working Petadel PolicyAssist AI prototype.

The application is located in:

`PolicyAssist-App/`

The current application structure includes:

```text
PolicyAssist-App/
├── App/
├── Docs/
├── Test/
├── data/
├── requirements.txt
└── README.md
```

The application uses:

* Python
* Streamlit
* Sentence Transformers
* `all-MiniLM-L6-v2`
* ChromaDB
* Google Gen AI
* Gemini 2.5 Flash
* Ollama
* Llama 3.2 3B

The deployed configuration uses **Gemini 2.5 Flash** when the Gemini API key is available.

Local development can use **Ollama with Llama 3.2 3B** as a fallback.

## Application Installation

The application can be run locally for the optional Build-Along and for technical exploration of the Petadel PolicyAssist AI reference project.

### Prerequisites

You will need:

* Python installed on your computer.
* Git installed if you are cloning the repository.
* Ollama installed if you plan to use the local Llama 3.2 3B fallback.
* A Gemini API key if you plan to use Gemini 2.5 Flash.

### Step 1: Clone the Repository

From a terminal, run:

```bash
git clone https://github.com/Lolade-Fapohunda/AI-Project-Management-Course.git
```

Move into the repository:

```bash
cd AI-Project-Management-Course
```

### Step 2: Open the Application Folder

Move into the application directory:

```bash
cd PolicyAssist-App
```

### Step 3: Install Dependencies

Install the Python dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

The application requirements include Streamlit, ChromaDB, Sentence Transformers, `python-dotenv`, and Google Gen AI.

### Step 4: Configure the Gemini API Key

Create a `.env` file in the `PolicyAssist-App` directory and add:

```text
GEMINI_API_KEY=your_api_key_here
```

Do not commit API keys or other secrets to GitHub.

### Step 5: Configure the Local AI Fallback

If you plan to use the local fallback, make sure Ollama is installed and the required Llama 3.2 3B model is available.

The application is designed to use the local model when the appropriate local configuration is available.

### Step 6: Run the Application

Start the Streamlit application from the `PolicyAssist-App` directory:

```bash
streamlit run App/app.py
```

The terminal will provide the local application address.

Open that address in your browser to use PolicyAssist.

## Application Usage

Once the application is running:

1. Enter a natural-language policy question.
2. Submit the question.
3. Review the PolicyAssist response.
4. Review the supporting policy source.
5. Check whether the answer is grounded in an approved and authoritative source.
6. Test unsupported questions to observe how the system handles insufficient evidence.
7. Use the results as evidence for the applicable Project Management activities.

The application should be treated as a working prototype and technical learning environment.

A functioning prototype is not automatically production-ready.

## Application and Course Material Mapping

The application is connected directly to the Project Management concepts taught throughout the course.

| Application Area             | Related Course Material |
| ---------------------------- | ----------------------- |
| Project purpose and problem  | Module 1, Module 2      |
| Requirements                 | Module 3                |
| Backlog and MVP              | Module 4                |
| AI architecture              | Module 5                |
| Data and knowledge retrieval | Module 6                |
| AI evaluation and quality    | Module 7                |
| Security and governance      | Module 8                |
| Testing and UAT              | Module 9                |
| Release and deployment       | Module 10               |
| Monitoring and KPIs          | Module 11               |
| Capstone and portfolio       | Module 12               |
| Final competency assessment  | Module 13               |

The application provides the technical context, while the course teaches you how to manage the business, technical, operational, risk, governance, and delivery decisions surrounding that application.

## Professional Outcome

By completing the course, you should be able to:

* Define AI project business problems.
* Build project charters.
* Define requirements.
* Create product backlogs.
* Manage scope.
* Understand AI architecture.
* Manage data and knowledge governance.
* Define evaluation criteria.
* Manage AI risks.
* Address security and access requirements.
* Plan testing and UAT.
* Manage release readiness.
* Establish monitoring.
* Manage continuous improvement.
* Make evidence-based Go, Hold, or No-Go decisions.
* Communicate AI project information to technical and business stakeholders.

## Capstone Portfolio

The Portfolio folder presents the strongest professional evidence from the Petadel PolicyAssist AI reference project.

You may also use evidence from your own AI product or use case when completing the capstone.

The relationship is:

**Course Learning → Capstone Application → Project Evidence → Professional Portfolio**

## Final Project Principle

A working application is not automatically a production-ready product.

A Project Manager must evaluate:

* Business value
* Requirements
* Quality
* Security
* Governance
* Testing
* User acceptance
* Performance
* Monitoring
* Risk
* Evidence

The final project decision should be based on evidence rather than assumptions.
