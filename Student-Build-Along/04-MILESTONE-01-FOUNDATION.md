# Milestone 1 — AI Project Foundation

## PM Objective

Understand the AI product, the business problem it is intended to address, its current state, and the initial project considerations that will guide the work.

## Hands-On Objective

Launch the PolicyAssist starter application, explore the current product experience, and begin thinking like an AI Project Manager by identifying what the product currently does, what it does not yet do, and what decisions need to be made.

---

# Before You Begin

You do **not** need a coding background to complete this Build-Along.

You will use a few basic tools to run the starter application. Follow the steps in order. You are not expected to write or modify code at this stage.

### You will need:

* A computer running Windows, macOS, or another supported operating system
* Internet access
* **Visual Studio Code (VS Code)**, a free application used to work with the project files
* **Python**, the programming language used by the starter application
* The course repository containing the Student Build-Along files

### If you do not have Visual Studio Code

Download and install Visual Studio Code before continuing.

Use the official Visual Studio Code website to download the version for your computer.

### If you do not have Python

Install Python before continuing.

During Python installation on Windows, make sure the option to **Add Python to PATH** is selected if it is displayed.

> You do not need to learn Python for this course. Python is simply the technology used to run the starter application.

---

# Part 1 — Get the Student Starter

The course repository contains a folder specifically prepared for the Build-Along.

Open the course repository and locate:

`Student-Build-Along → PolicyAssist-Student-Starter`

This is the application you will use throughout the hands-on portion of the course.

### Important

Do **not** begin by changing the application code.

At this stage, your job is to understand the product as an AI Project Manager, not to develop or fix it.

---

# Part 2 — Open the Starter in Visual Studio Code

1. Open **Visual Studio Code**.

2. Select:

   **File → Open Folder**

3. Locate the course folder on your computer.

4. Open:

   `Student-Build-Along → PolicyAssist-Student-Starter`

5. Select **Open**.

You should now see the project files in the left-hand **Explorer** panel.

Look for:

`app.py`

You should also see the:

`data`

folder.

If you can see these items, you have opened the correct project.

---

# Part 3 — Open the Terminal

The terminal is a place where you can give your computer simple commands.

You do not need to understand programming to use it.

In Visual Studio Code:

1. Select **Terminal** from the top menu.
2. Select **New Terminal**.

A terminal window will appear at the bottom of Visual Studio Code.

### Check your location

The terminal should be operating inside the:

`PolicyAssist-Student-Starter`

folder.

If you are using Windows, the end of the folder path should look similar to:

`...\Student-Build-Along\PolicyAssist-Student-Starter>`

If it does not, stop here and make sure you opened the correct folder in Visual Studio Code.

---

# Part 4 — Launch the Application

In the terminal, enter this command exactly:

`python -m streamlit run app.py`

Then press **Enter**.

The application should start.

You may see information appear in the terminal indicating that Streamlit is running.

You should also see a local web address similar to:

`http://localhost:8501`

---

# Part 5 — Open the Application

Open your web browser.

Enter:

`http://localhost:8501`

The PolicyAssist starter application should appear.

### If the application opens

Congratulations. You have successfully launched your first AI application for the Build-Along.

You can now begin exploring it.

### If the application does not open

Do not start changing code.

First check:

* Did you open the `PolicyAssist-Student-Starter` folder?
* Does the folder contain `app.py`?
* Did you enter `python -m streamlit run app.py` exactly?
* Did the terminal display an error message?
* Did you open `http://localhost:8501`?

If there is an error, capture the message before making changes.

**The goal at this stage is to understand what happened, not to troubleshoot by changing the application.**

---

# Part 6 — Explore the Product

Now that the application is running, use it as an employee would.

Ask several policy questions.

Try questions such as:

* How many days of paid time off do employees receive?
* How many days of paid sick leave are available?
* How many days per week can eligible employees work remotely?
* What should an employee do if they believe their credentials were compromised?
* What is the policy for bringing pets to work?

Do not worry about whether every answer is perfect yet.

You are establishing a **baseline**.

Observe what happens when you ask different types of questions.

---

# Part 7 — What Does the Product Do?

Based on your exploration, document the current capabilities of the application.

Consider:

* What type of questions can it answer?
* What policy information can it retrieve?
* Does it identify the source of the information?
* Does it provide policy metadata such as a policy ID, version, or status?
* What does the user see after submitting a question?
* Does the experience appear straightforward for an employee?

Record your observations.

---

# Part 8 — What Does the Product Not Yet Do?

Now identify gaps or limitations you can observe.

Consider:

* Are there questions it cannot answer?
* What happens when information is not available?
* Does the application clearly distinguish between supported and unsupported questions?
* Does it provide enough evidence for a user to trust an answer?
* Are there questions where the result could be confusing or incomplete?
* What would an employee need that the current application does not provide?

You are **not expected to solve these problems yet**.

Your job is to identify them.

---

# Part 9 — Identify Initial PM Decisions

As the AI Project Manager, identify at least **three decisions or questions** that you believe the project team needs to address.

For each one, record:

| Decision or Question                                              | Business Reason                               | Evidence Needed                                                | Risk / Trade-off                                                   | Expected Outcome                   |
| ----------------------------------------------------------------- | --------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------------- |
| Example: What should happen when the AI cannot answer a question? | Employees need a reliable path to assistance. | Test unsupported questions and review escalation requirements. | Users may lose trust if the AI gives an answer when it should not. | Clear and safe escalation process. |

Your decisions do not need to be technical.

Think about the product, users, business value, risk, quality, security, and experience.

---

# Part 10 — Complete Your AI Product Foundation Assessment

Create a short assessment containing:

### Current Product Capabilities

What does the application currently do?

### Current Product Gaps

What does it not yet do, or what needs further investigation?

### Initial PM Decisions / Questions

List at least three.

### Evidence Needed

What information, testing, stakeholder input, or data would help the project team make those decisions?

---

# PM Perspective

At this stage, remember:

> **Understand the current state before defining the future state.**

An AI Project Manager should not immediately assume that a feature needs to be added, a model needs to be changed, or code needs to be rewritten.

First understand:

**What exists → What works → What does not work → What users need → What decisions must be made**

That foundation will guide the work in the following milestones.

---

# Deliverable

Complete your:

**AI Product Foundation Assessment / PM Decision Log**

Your assessment should include:

* Current capabilities
* Current gaps
* At least three PM decisions or questions
* Evidence needed to support those decisions

---

# Milestone 1 Checkpoint

Before moving forward, you should be able to answer:

**What problem are we solving?**

**Who are we solving it for?**

**What does the current AI product do?**

**What does it not yet do?**

**What decisions do we need to make before moving forward?**

If you can answer these questions based on your exploration of the starter application, you are ready for **Milestone 2 — Problem & Stakeholders**.
