# Learn2Earn: An Academic Note-Sharing and Reward Platform

##  About the Project

**Learn2Earn** is an academic note-sharing and reward platform designed to help students create, share, discover, and organize study materials.

The platform encourages students to contribute their own academic notes by providing **NotePoints** for approved and useful contributions. Students can browse and search for study resources while administrators manage submitted content and maintain the quality of the platform.

The project also plans to include an **AI Note Assistant** that can help categorize notes, extract keywords, generate summaries, and create study questions.

---

##  Objectives

The main objectives of Learn2Earn are to:

- Provide a centralized platform for sharing student-created academic notes.
- Help students easily discover relevant study materials.
- Encourage students to contribute useful and original notes.
- Implement a points-based reward system called **NotePoints**.
- Provide content moderation to maintain the quality of uploaded materials.
- Provide administrators with tools for managing users and submitted content.
- Explore the use of AI to improve note organization and study preparation.

---

##  Planned Features

### Student Features

- Student registration and login
- Student profile
- Upload academic notes
- Browse available notes
- Search and filter notes
- View note details
- Save notes
- Rate notes
- Report inappropriate content
- View NotePoints
- View contribution history
- Contributor levels

###  Administrator Features

- Administrator login
- Admin dashboard
- Review submitted notes
- Approve or reject notes
- Review reported content
- Remove violating content
- Manage users
- Monitor user contributions
- Monitor NotePoints activities

###  AI Note Assistant

Planned AI-assisted features include:

- Automatic note categorization
- Keyword extraction
- Note summarization
- Generation of study questions
- Assistance with note metadata

---

##  NotePoints

Learn2Earn uses a virtual points system called **NotePoints** to encourage academic contributions.

### Example Activities

| Activity | Points |
|----------|--------|
| Approved note upload | +10 |
| High-quality contribution | +5 bonus |
| Note saved/downloaded by another student | +1 |
| Positive rating | +2 |
| Reported/removed content | Points may be deducted |

> **Note:** The NotePoints system in the initial MVP is a virtual reward mechanism. Real-money rewards are outside the initial MVP and may be considered as a future enhancement.

---

##  System Workflow

```text
Student
   │
   ▼
Register / Login
   │
   ▼
Student Dashboard
   │
   ├──────────────► Browse / Search Notes
   │                       │
   │                       ▼
   │                  View / Save
   │
   └──────────────► Upload Note
                           │
                           ▼
                     Pending Review
                           │
                           ▼
                    Administrator
                           │
                    ┌──────┴──────┐
                    ▼             ▼
                Approved       Rejected
                    │             │
                    ▼             ▼
               +NotePoints     Resubmit
                    │
                    ▼
              Available Notes
