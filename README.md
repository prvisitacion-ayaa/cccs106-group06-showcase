# Learn2Earn: An Academic Note-Sharing and Reward Platform

A student-centered academic platform developed for **Camarines Sur Polytechnic Colleges (CSPC)** that allows students to upload, organize, search, explore, and share academic learning resources. The platform also includes academic resource recommendations, note evaluation, content moderation, and a reward system to encourage meaningful student contributions.

---

## About the Project

**Learn2Earn** is an academic note-sharing and reward platform designed to provide CSPC students with a centralized space for sharing and accessing student-created learning materials.

Students can upload their own academic notes, reviewers, summaries, and other study materials. These resources can be organized by subject, topic, and course or learning level, making them easier to discover and access.

The platform uses a text-based Academic Resource Recommendation Module powered by **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity**. This module compares student search queries with uploaded academic notes and ranks the results according to their textual relevance.

Learn2Earn also includes a Note Accuracy Evaluation and Comparison Module, a content moderation process, and a LearnPoints reward system to encourage students to contribute useful academic materials.

## Objectives

The project aims to:

- Develop an organized academic platform for CSPC students to upload, manage, explore, and share learning resources.
- Provide an automated feature for evaluating and comparing the accuracy of uploaded academic notes using established criteria and trusted reference materials.
- Implement an academic resource recommendation system using TF-IDF and Cosine Similarity.
- Establish a content moderation and evaluation process to assess the relevance, quality, and appropriateness of submitted materials.
- Introduce a LearnPoints reward system to encourage valuable academic contributions.
- Evaluate the platform's functionality and usability through testing with selected CSPC students.

## Target Users

**Students**
- Create and manage accounts and profiles.
- Upload original academic notes and study materials.
- Organize resources by subject, topic, and course level.
- Browse and search for available academic materials.
- Receive recommendations based on search relevance.
- View note evaluation results and comparisons.
- Earn LearnPoints from approved academic contributions.
- Use accumulated points to unlock selected premium features.

**Administrators**
- Manage student accounts.
- Review submitted academic materials.
- Approve or reject uploaded resources.
- Monitor content moderation and evaluation.
- Track platform activities and contributions.
- Manage LearnPoints and related reward activities.

## Main Features

### 1. Academic Resource Sharing

Students can upload, organize, browse, search, and share original academic materials, including:

- Lecture notes
- Reviewers
- Summaries
- Study guides
- Other academic learning materials

Uploaded resources are organized using relevant information such as subject, topic, course, learning level, and keywords.

### 2. Academic Resource Recommendation System

Learn2Earn uses **TF-IDF and Cosine Similarity** to identify and rank academic notes based on their textual relevance to a student's search query.

The recommendation process includes:

1. Accepting a student's search query.
2. Processing the query and available academic note texts.
3. Using TF-IDF to convert the text into numerical representations based on term importance.
4. Applying Cosine Similarity to measure the similarity between the query and uploaded notes.
5. Calculating similarity scores.
6. Ranking and displaying the most relevant academic resources.

This feature helps students find materials that match their searched subjects or topics more efficiently.

**Note:** The recommendation system measures textual relevance. A high similarity score does not guarantee that the academic content is factually correct.

### 3. Note Accuracy Evaluation and Comparison

This module evaluates and compares uploaded academic notes using established evaluation criteria and trusted academic reference materials.

Its intended functions include:

- Evaluating submitted academic notes.
- Comparing note content with trusted reference materials.
- Applying defined evaluation criteria.
- Generating accuracy assessment scores or labels.
- Ranking multiple notes covering the same subject or topic.

The results help students identify notes that appear more consistent with the selected references and evaluation criteria.

**Note:** Evaluation results depend on the availability, accuracy, and relevance of reference materials. They do not guarantee academic correctness and should not replace the judgment of teachers or subject matter experts.

### 4. Content Moderation and Evaluation

Submitted academic resources undergo a review process to assess their:

- Relevance to the subject or topic.
- Quality and organization.
- Originality.
- Appropriateness.
- Compliance with platform guidelines.

Administrators can approve or reject submissions based on the review process. Only eligible and approved contributions can receive LearnPoints.

### 5. LearnPoints Reward System

Learn2Earn introduces **LearnPoints**, an in-platform reward system that recognizes students who contribute valuable academic learning materials.

- Students earn points for eligible and approved contributions.
- Accumulated points are recorded in their accounts.
- Students can use their points to unlock selected premium features.
- The reward system encourages participation and academic resource sharing.

**Important:** LearnPoints are virtual platform rewards only. They cannot be converted into cash, exchanged for money, or used for financial transactions.

### 6. Student and Administrator Dashboards

The platform provides separate dashboards for students and administrators.

- **Student Dashboard:** Provides access to academic resources, search features, account information, and LearnPoints.
- **Administrator Dashboard:** Provides access to user management, resource review, content moderation, and platform monitoring.

## System Workflow

The general workflow of Learn2Earn is:

1. **Account Access** – Students create an account or log in to the platform.
2. **Resource Submission** – Students upload their original academic notes and study materials.
3. **Resource Organization** – Uploaded materials are categorized using subject, topic, course level, and other relevant information.
4. **Content Review** – Administrators review and evaluate submitted materials.
5. **Approval and Rewards** – Approved contributions become eligible for LearnPoints.
6. **Resource Discovery** – Students search for academic materials and receive results ranked using TF-IDF and Cosine Similarity.
7. **Note Evaluation** – Students can view the evaluation and comparison results of available academic notes.
8. **Premium Feature Redemption** – Students can use accumulated LearnPoints to unlock selected premium features.

## Technologies Used

| Category | Technology |
|---|---|
| Frontend / User Interface | Flet |
| Backend | Python |
| Database | SQLite |
| Text Processing and Recommendation | Scikit-learn |
| Recommendation Algorithm | TF-IDF and Cosine Similarity |
| Version Control and Collaboration | Git and GitHub |
| Development Environment | Visual Studio Code |
| Application Packaging | PyInstaller |

## Project Scope and Limitations

Learn2Earn is designed as a working prototype for CSPC students. It focuses on academic resource sharing, organization, recommendation, note evaluation, content moderation, and rewards.

The project has the following limitations:

- The prototype will be tested with selected CSPC students and will not initially be deployed across all CSPC campuses.
- It will not integrate with the institution's official student information systems.
- The platform is not intended to replace teachers, formal classroom instruction, or the school's learning management system.
- The recommendation algorithm identifies textual relevance but does not independently verify factual accuracy.
- Note accuracy evaluation depends on the available trusted reference materials and established evaluation criteria.
- Evaluation scores and rankings are intended to assist users and are not final proof of academic correctness.
- LearnPoints cannot be exchanged for cash or used for financial transactions.
- The initial project will not include real-time collaboration, video conferencing, online examinations, payment systems, advanced social networking, or large-scale cloud deployment.

## Resource Requirements

### Hardware
- Desktop or laptop computer
- Internet connection
- Mobile device for interface testing

### Software
- Python
- Flet
- SQLite
- Scikit-learn
- Git and GitHub
- Visual Studio Code
- PyInstaller

### Personnel

One team member may perform multiple responsibilities depending on the team's size, skills, and workload.

| Role | Responsibilities |
|---|---|
| Team Leader | Coordinates the team, schedule, tasks, and project documentation. |
| Requirements Analyst | Identifies user needs and prepares system requirements. |
| UI/UX Designer | Designs the interface, wireframes, and user experience. |
| Software Developer | Develops the main application and system features. |
| Database/System Architect | Designs the database, APIs, system architecture, and UML diagrams. |
| Algorithm/Data Developer | Develops the Academic Resource Recommendation Module using TF-IDF and Cosine Similarity and prepares the academic notes dataset. |
| QA/Tester | Tests functionality, identifies bugs, checks system requirements, and conducts usability testing. |

## Expected Deliverables

The project is expected to produce:

- A working Learn2Earn application prototype.
- Student and administrator dashboards.
- Academic resource sharing and management features.
- An Academic Resource Recommendation Module using TF-IDF and Cosine Similarity.
- A Note Accuracy Evaluation and Comparison Module.
- A content moderation and evaluation process.
- A LearnPoints reward and premium feature redemption system.
- An academic notes dataset with relevant metadata.
- System architecture and database design.
- UML diagrams and system flow documentation.
- Functional and usability testing results.
- Technical documentation and user guidelines.

## Project Team

**Developers:**
- Visitacion, Princess Shayla B.
- Villazer, Devine Grace S.
- Nomo, Micabelle Allison L.

**Institution:** Camarines Sur Polytechnic Colleges (CSPC)

**College:** College of Computer Studies

**Course:** CS 3110 – Software Engineering 1

**Project Adviser:** Tiffany Lyn Pandes

---

*Learn2Earn aims to make academic resource sharing more organized, accessible, and rewarding by providing CSPC students with a platform for sharing knowledge and discovering relevant learning materials.*
