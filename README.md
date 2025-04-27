***AI RECRUITMENT SYSTEM***
---
An AI-powered recruitment platform designed to simplify and automate the hiring process.
This system allows companies to post jobs, manage candidates, evaluate CVs intelligently, generate interview questions, and schedule interviews — all in one place.

**FEATURES**
---
**📝Job Posting:** Create, edit, and delete job openings.

**👨‍💼 Candidate Management:** View applicants and their profiles.

**📄 CV Evaluation:** Analyze uploaded resumes using AI.

**🎯 Interview Question Generation:** Generate questions based on the candidate's CV and job role.

**📧 Email Scheduling:** Automatically send interview invitations.

**🔒 User Authentication:** Secure login and registration system.


**TECHNOLOGIES USED**
---
**Backend:** Flask (Python)

**Frontend:** HTML, CSS, JavaScript

**Database:** Sql-lite

**AI Tools:**  Google Gemini (for chatbot)

**Others:** Flask-Mail (for email scheduling), CV parsing libraries

**INSTALLATION**
---
**1.Clone the repository:**
```bash
git clone https://github.com/your-username/ai-recruitment-system.git
```
**2.Navigate to the project directory:**
```bash
cd ai-recruitment-system
```
**3.Create a virtual environment and activate it:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```
**4.Install the dependencies:**
```bash
pip install -r requirements.txt
```
**5.Run the application:**
```bash
flask run
```
***Architecture diagram for your AI Recruitment System:***
---
```bash
       [Frontend (HTML/CSS/JS)]
                 |
                 v
       [Flask Backend Server]
                 |
    -----------------------------
    |                           |
[Database]                  [AI Modules]
(PostgreSQL)               (CV Evaluation, 
                           Interview Qs Gen)
    |                           |
    -----------------------------
                 |
                 v
   [Email Service (Flask-Mail)]
```
