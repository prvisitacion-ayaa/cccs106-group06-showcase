# Learn2Earn: An Academic Note-Sharing and Reward Platform

Learn2Earn is a student-centered academic note-sharing and reward platform designed for students of **Camarines Sur Polytechnic Colleges (CSPC)**. The system provides a centralized environment where students can upload, organize, search, explore, and share academic notes and study materials.

The platform also introduces a **LearnPoints reward mechanism** that recognizes students for contributing useful and approved academic resources. In addition, Learn2Earn includes an **AI Note Assistant** prototype that can help categorize notes, identify key concepts, generate summaries, and create review questions.
---

## Project Overview

Students commonly use social media and other online platforms to share academic information. However, these platforms are not specifically designed for organizing student-created academic notes, reviewers, and other learning materials.

Learn2Earn aims to provide a centralized academic platform where CSPC students can:

- Upload their own academic notes and study materials
- Organize resources by subject, topic, and course level
- Search and browse available learning resources
- Share useful academic materials
- Receive feedback and evaluation on submitted resources
- Earn LearnPoints for approved contributions
- Use accumulated points to unlock selected premium features
- Use an AI Note Assistant to process uploaded notes

The platform is intended to support **peer learning, organized resource sharing, and student participation** within the CSPC community.

---

## Problem Statement

Academic resources created and shared by students are often distributed across unrelated social media posts, groups, pages, and other platforms. This makes useful study materials difficult to locate and access.

Another challenge is the quality and reliability of student-generated content. Student-created resources may contain inaccurate or low-quality information. Therefore, a platform for student academic resource sharing should provide mechanisms for **content moderation, evaluation, organization, and feedback**.

Learn2Earn addresses these problems by providing a centralized platform with:

1. Academic resource organization
2. Content moderation and evaluation
3. Student contribution tracking
4. LearnPoints rewards
5. AI-assisted note organization

---

## Objectives

### General Objective

To develop an academic platform that allows CSPC students to share, explore, and manage their own learning resources in an organized manner while encouraging meaningful academic contributions through content moderation and a reward system.

### Specific Objectives

The project aims to:

1. Build an academic platform where CSPC students can upload, organize, explore, and share learning resources.
2. Establish a content moderation and evaluation process for assessing the relevance, quality, and appropriateness of submitted resources.
3. Create a reward system that encourages students to contribute valuable academic content.
4. Develop an AI Note Assistant that can categorize notes, generate summaries, identify key concepts, and create review questions.
5. Evaluate the usability and functionality of the platform through testing with selected CSPC students.

---

## Key Features

### 1. User Account Management

Students can:

- Create an account
- Log in to the platform
- Manage their profile
- Track their contributions
- View accumulated LearnPoints

---

### 2. Academic Resource Upload

Students can upload their own:

- Notes
- Reviewers
- Study materials
- Other academic learning resources

Resources can be organized according to:

- Subject
- Topic
- Course
- Learning level

---

### 3. Browse and Search

Students can browse and search available academic resources.

The organization of resources is intended to make relevant study materials easier to locate.

---

### 4. Content Moderation and Evaluation

Submitted academic resources undergo a moderation and evaluation process.

Resources may be assessed based on:

- Relevance
- Quality
- Appropriateness

Approved contributions become eligible for LearnPoints.

> **Note:** The moderation mechanism does not guarantee the academic correctness of every uploaded resource.

---

### 5. LearnPoints Reward System

LearnPoints are an **in-platform recognition and reward mechanism**.

Students can earn points by contributing useful and approved academic materials.

Accumulated points can be used to unlock selected premium features.

LearnPoints:

- Are recorded in the user's account
- Are awarded for eligible approved contributions
- Cannot be converted to cash
- Do not represent monetary rewards
- Are intended only for use within the platform

---

### 6. AI Note Assistant

The AI Note Assistant is a prototype feature designed to assist students with uploaded learning materials.

It can help with:

- Note categorization
- Key concept identification
- Summary generation
- Review question generation

The AI-generated results are intended as **study aids** and do not guarantee academic accuracy.

---

### 7. Student Dashboard

The student dashboard can provide access to information such as:

- Uploaded resources
- Contribution status
- LearnPoints
- Available rewards
- Platform activities

---

### 8. Administrator Dashboard

Administrators can:

- Manage users
- Review submitted resources
- Moderate content
- Monitor platform activities
- Manage reports
- Monitor reward transactions

---

## Target Users

### Primary Users

**CSPC Students**

Students are the primary users of Learn2Earn. The platform is intended for students who:

- Need additional study resources
- Want to share their own reviewers and notes
- Want to discover materials created by other students
- Want to participate in peer-supported learning

### Administrator

The administrator is responsible for:

- User management
- Resource review
- Content moderation
- Platform activity monitoring
- Reward management

---

### System Workflow

```text
                         START
                           │
                           ▼
                ┌─────────────────────┐
                │ Open Learn2Earn     │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Login / Create      │
                │ Account             │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │ Student Dashboard   │
                └──────────┬──────────┘
                           │
              ┌────────────┼─────────────┐
              │            │             │
              ▼            ▼             ▼
        Upload Notes   Browse/Search   Profile
              │            │
              │            ▼
              │      ┌───────────────┐
              │      │ View Academic │
              │      │ Resources     │
              │      └───────┬───────┘
              │              │
              │              ▼
              │       Use / Interact
              │       with Resource
              │
              ▼
       ┌─────────────────────┐
       │ Classify Resource   │
       │ Subject / Topic /   │
       │ Course Level        │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Content Moderation  │
       │ & Evaluation        │
       └──────────┬──────────┘
                  │
             ┌────┴─────┐
             │          │
             ▼          ▼
         Approved     Rejected
             │          │
             │          └──────► No LearnPoints
             │
             ▼
       ┌─────────────────────┐
       │ Resource Published  │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Award LearnPoints   │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Update Student      │
       │ Contribution        │
       │ History             │
       └──────────┬──────────┘
                  │
                  ▼
       ┌─────────────────────┐
       │ Redeem Selected     │
       │ Premium Features    │
       └─────────────────────┘
```

The system begins when a student creates an account or logs in. Students can then upload, browse, search, and manage academic resources. Uploaded materials are classified and submitted for moderation and evaluation. Approved contributions become eligible for LearnPoints, while rejected submissions do not receive points.

---


## System Modules

The system is divided into several major modules:

```text
Learn2Earn
│
├── User Management
│   ├── Registration
│   ├── Login
│   └── Profile Management
│
├── Academic Resource Management
│   ├── Upload Resources
│   ├── Browse Resources
│   ├── Search Resources
│   └── Resource Organization
│
├── Content Moderation
│   ├── Resource Review
│   ├── Approval
│   ├── Rejection
│   └── Evaluation
│
├── LearnPoints
│   ├── Point Awarding
│   ├── Contribution History
│   └── Premium Feature Redemption
│
├── AI Note Assistant
│   ├── Categorization
│   ├── Key Concept Extraction
│   ├── Summarization
│   └── Review Question Generation
│
├── Administration
│   ├── User Management
│   ├── Content Management
│   ├── Reports
│   └── Activity Monitoring
│
└── Database
    ├── Users
    ├── Learning Resources
    ├── Classifications
    ├── Evaluations
    ├── Moderation
    └── LearnPoints

---

## Software Requirements

The following software and development tools will be used for the Learn2Earn project.

| Software / Tool            | Purpose                                                          |
| -------------------------- | ---------------------------------------------------------------- |
| **Python**                 | Backend development, application logic, and AI/ML implementation |
| **Flet**                   | Frontend and graphical user interface development                |
| **SQLite**                 | Database management and data storage                             |
| **Python AI/ML Libraries** | Development of the AI Note Assistant                             |
| **Git**                    | Version control and source-code management                       |
| **GitHub**                 | Repository hosting, collaboration, and version control           |
| **Visual Studio Code**     | Integrated development environment (IDE)                         |
| **PyInstaller**            | Packaging the Python application                                 |

The concept paper specifically identifies Flet, Python, SQLite, Python AI/ML libraries, GitHub, Visual Studio Code, and PyInstaller as the project's primary tools and technologies.

---

## Project Structure

The project is organized into separate directories for the user interface, backend, AI Note Assistant, database, administration, testing, documentation, and project assets.

```text
Learn2Earn/
│
├── app/
│   │
│   ├── ui/
│   │   ├── login.py
│   │   ├── register.py
│   │   ├── dashboard.py
│   │   ├── profile.py
│   │   ├── resources.py
│   │   ├── upload.py
│   │   ├── search.py
│   │   └── learnpoints.py
│   │
│   ├── backend/
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── resources.py
│   │   ├── search.py
│   │   ├── moderation.py
│   │   ├── evaluation.py
│   │   ├── learnpoints.py
│   │   └── rewards.py
│   │
│   ├── ai/
│   │   ├── note_assistant.py
│   │   ├── categorizer.py
│   │   ├── keyword_extractor.py
│   │   ├── summarizer.py
│   │   └── question_generator.py
│   │
│   ├── database/
│   │   ├── database.py
│   │   ├── models.py
│   │   ├── schema.sql
│   │   └── seed.py
│   │
│   └── admin/
│       ├── dashboard.py
│       ├── users.py
│       ├── submissions.py
│       ├── moderation.py
│       ├── reports.py
│       └── activities.py
│
├── tests/
│   ├── test_auth.py
│   ├── test_users.py
│   ├── test_resources.py
│   ├── test_search.py
│   ├── test_moderation.py
│   ├── test_learnpoints.py
│   └── test_ai.py
│
├── data/
│   ├── notes/
│   └── dataset/
│       └── academic_notes.csv
│
├── docs/
│   ├── SRS/
│   │   └── SRS.md
│   │
│   ├── UML/
│   │   ├── use_case_diagram.png
│   │   ├── class_diagram.png
│   │   ├── sequence_diagram.png
│   │   └── activity_diagram.png
│   │
│   ├── database/
│   │   ├── erd.png
│   │   └── database-design.md
│   │
│   ├── architecture/
│   │   └── system-architecture.png
│   │
│   └── testing/
│       ├── test-plan.md
│       └── test-results.md
│
├── assets/
│   ├── screenshots/
│   └── diagrams/
│
├── .gitignore
├── requirements.txt
├── main.py
├── config.py
├── README.md
└── LICENSE
```
