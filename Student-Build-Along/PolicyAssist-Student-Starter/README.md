# PolicyAssist AI

## Student Build-Along Starter

This is the lightweight starter application for the optional AI Project Management Build-Along.

The application uses synthetic Petadel policy documents to demonstrate how an AI product can evolve from a simple working prototype into a more capable and governed solution.

This is a **student learning application**. It is not the finished Petadel PolicyAssist AI reference application.

## Purpose

The starter application gives you a working product that you can run, inspect, test, and progressively improve as you move through the Build-Along.

The objective is to connect hands-on product changes to Project Management decisions.

## What the Starter Does

The initial version:

* Loads policy documents from the `data` folder.
* Displays the available policies.
* Accepts a natural-language policy question.
* Searches the policy documents.
* Displays potentially relevant policy information.
* Identifies the source policy document.

The application is intentionally simple at the beginning.

You will progressively improve it as the Build-Along introduces additional AI Project Management concepts.

## Student Build-Along

The Build-Along follows:

**Watch → Make a PM Decision → Complete the Hands-On Activity → Test → Document → Move Forward**

You will use the application to understand how Project Management decisions affect the product.

You are not expected to become a software engineer.

## What You Will Explore

As you progress through the milestones, you will explore concepts such as:

* Business requirements
* Product scope
* Minimum Viable Product (MVP)
* AI architecture
* Data and knowledge readiness
* Information retrieval
* Semantic search
* Retrieval-Augmented Generation (RAG)
* Grounded responses
* Source citations
* AI evaluation
* Security
* Access controls
* Governance
* Testing
* User Acceptance Testing (UAT)
* Release readiness
* Deployment
* Monitoring
* Key Performance Indicators (KPIs)
* Dashboards
* Continuous improvement

Not every concept requires you to implement the underlying technology yourself. The purpose is to understand the capability well enough to manage and evaluate it as a Project Manager.

## Technology

The starter application currently uses:

* Python
* Streamlit

Additional technologies may be introduced in later milestones.

## Run the Application

Open a terminal in:

```text
Student-Build-Along/PolicyAssist-Student-Starter
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python -m streamlit run app.py
```

The application should open in your browser.

## Policy Data

The `data` folder contains synthetic policy documents created specifically for this course.

These documents are fictional course data and are not real company policies.

The starter application uses these documents so you can practice working with policy information, retrieval, evaluation, testing, security, and governance concepts.

## Important Distinction

The course includes two different PolicyAssist applications.

### Student Build-Along

This lightweight application is designed for learning.

You will progressively work with and improve it as part of the optional Build-Along.

### Petadel PolicyAssist AI Reference Application

The finished Petadel PolicyAssist AI application is the instructor/reference implementation.

It represents the more complete solution and is used for demonstrations, comparison, and capstone context.

Do not assume that the student starter should contain all of the capabilities or complexity of the finished reference application.

## Learning Goal

The objective of the Build-Along is not to produce production-ready software.

The objective is to help you understand how an AI product moves from:

**Business Problem → Requirements → Planning → Architecture → Data → AI Capability → Evaluation → Security & Governance → Testing → Release → Deployment → Monitoring → Continuous Improvement**

You will connect each stage to a Project Management decision.

## Student Outcome

By completing the Build-Along, you should be able to:

* Understand the major components of an AI product.
* Connect technical capabilities to business requirements.
* Evaluate AI product quality.
* Identify risks and governance concerns.
* Participate effectively in technical discussions.
* Make evidence-based Project Management decisions.
* Explain how an AI product should be tested, released, monitored, and improved.

## Final Build-Along Assessment

The optional Build-Along continues through Milestone 13.

Milestone 13 contains a separate Build-Along Final Assessment that evaluates your ability to apply AI Project Management concepts across the hands-on experience.

The required Module 13 Final Assessment is separate and is completed by all students.

## Course Context

The reference project for the course is:

**Petadel PolicyAssist AI**

The project is designed to help employees locate and understand authoritative organizational policy information.

All Petadel policies and project information used in this course are synthetic.

## Important

You do not need to complete the optional Build-Along to complete the AI Project Management course.

The PM Track is the required course path.

The Build-Along provides additional hands-on experience for students who want to interact with the technical product while learning how to manage it from a Project Management perspective.
