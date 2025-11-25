# Job Portal Management System - Backend API

A robust, RESTful API designed to streamline the recruitment process. This system manages the entire lifecycle of job postings and applications, featuring secure Role-Based Access Control (RBAC) to distinguish between Recruiters (Admins) and Applicants. Built with Flask and SQLAlchemy.

## ✨ Features

  * **Role-Based Access Control (RBAC):** distinctive permissions for **Admins** (create jobs) and **Applicants** (apply for jobs), secured via JWT.
  * **Secure Authentication:** Full registration and login system using password hashing (Bcrypt) and JSON Web Tokens (JWT) for session management.
  * **Job Management:** Admins can post detailed job listings with salary, location, and descriptions. Public users can search and view all available openings.
  * **Application Tracking:** Applicants can apply for jobs with a single click, view their application history, and withdraw applications if needed.
  * **Smart Search:** Integrated search functionality allows users to filter jobs by title or location keyword.
  * **Scalable Architecture:** Built using the Model-Route-Controller (MRC) pattern to ensure modularity and ease of maintenance.

## 🛠️ Tech Stack

**Backend:**

  * **Language:** Python 3.10+
  * **Framework:** Flask
  * **ORM:** SQLAlchemy (Flask-SQLAlchemy)
  * **Database:** SQLite (Development) / PostgreSQL (Production ready)
  * **Migrations:** Flask-Migrate (Alembic)

**Security & Auth:**

  * **Authentication:** Flask-JWT-Extended
  * **Encryption:** Flask-Bcrypt
  * **Environment:** python-dotenv

**Tools:**

  * **API Testing:** Postman / Insomnia
  * **Version Control:** Git & GitHub

## 🚀 Getting Started

Follow these steps to set up and run the Job Portal API locally.

**Prerequisites:**

  * Python 3.10 or higher installed.
  * Git installed.
  * Postman (for testing the API).

### 1\. Clone the Repository

```bash
git clone https://github.com/SIBAM890/Back-dev-intern
cd Back-dev-intern
cd JOB-PORTAL
```

### 2\. Set Up Python Environment

Create and activate a virtual environment:

```bash
python -m venv .venv

# On Windows (PowerShell/Git Bash)
.\.venv\Scripts\activate

# On macOS/Linux
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

### 3\. Configure Environment Variables

Create a file named `.env` in the root directory. Copy the following configuration into it:

```ini
FLASK_APP=run.py
FLASK_DEBUG=1
SECRET_KEY="your-super-secret-key"
JWT_SECRET_KEY="your-jwt-secret-key"
SQLALCHEMY_DATABASE_URI="sqlite:///job_portal.db"
```

### 4\. Initialize the Database

Run the following commands to create the database tables and apply migrations:

```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

*Note: This will create a `job_portal.db` file in your instance folder.*

### 5\. Run the Backend Server

Start the Flask server. Keep this terminal running.

```bash
python run.py
```

The server will start at `http://127.0.0.1:5000`.

-----

## 📡 API Usage Guide

Since this is a backend-only project, you will use **Postman** to interact with the system.

**1. Create an Admin User (Recruiter)**

  * **Endpoint:** `POST /auth/register`
  * **Body:** `{"username": "admin", "email": "admin@test.com", "password": "123", "is_admin": true}`

**2. Login**

  * **Endpoint:** `POST /auth/login`
  * **Body:** `{"email": "admin@test.com", "password": "123"}`
  * *Response:* Copy the `access_token`.

**3. Create a Job (Protected)**

  * **Endpoint:** `POST /jobs/`
  * **Auth:** Select "Bearer Token" and paste your token.
  * **Body:** `{"title": "DevOps Engineer", "description": "Cloud stuff", "location": "Remote", "salary": "120k"}`

**4. Apply for a Job**

  * Register/Login as a **normal user** (`is_admin: false`).
  * Use the new token to hit `POST /jobs/<job_id>/apply`.