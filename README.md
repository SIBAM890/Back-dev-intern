# CodexIntern - Backend Development Internship Projects

## 📋 Table of Contents

- [About This Repository]
- [Projects Overview]
- [Technical Skills Acquired]
- [Learning Journey]

## 🎯 About This Repository

This repository showcases **two comprehensive backend systems** developed during my internship at **CodexIntern**. Each project demonstrates modern software engineering practices, RESTful API design, secure authentication mechanisms, and scalable architecture patterns.

### Internship Duration
**Program:** Backend Development Internship  
**Organization:** CodexIntern  
**Focus Areas:** API Development, Database Design, Authentication & Authorization, Role-Based Access Control

## 🚀 Projects Overview

### 1. Job Portal Management System
> **Tech Stack:** Flask (Python) • SQLAlchemy • JWT • SQLite/PostgreSQL

A complete recruitment platform API enabling role-based job posting and application management.

**Key Features:**
- 🔐 JWT-based authentication with role differentiation (Admin/Applicant)
- 📝 CRUD operations for job listings with advanced filtering
- 📊 Application tracking system with withdraw functionality
- 🔍 Smart search by job title and location
- 🏗️ MRC (Model-Route-Controller) architecture

**[View Full Documentation →](./JOB-PORTAL/README.md)**

**Tech Highlights:**
```python
Flask + SQLAlchemy + Flask-JWT-Extended + Bcrypt
```

### 2. Event Management System
> **Tech Stack:** Node.js (Express) • MongoDB • Mongoose • JWT

A robust event management backend with capacity controls and admin approval workflows.

**Key Features:**
- 🎫 Event creation with capacity-based registration limits
- ✅ Admin approval workflow for event visibility
- 📅 Date and location-based event filtering
- 👥 User registration/cancellation system
- 🛡️ Role-based access control (Admin/Organizer/User)

**[View Full Documentation →](./EVENT-MANAGEMENT/README.md)**

**Tech Highlights:**
```javascript
Express.js + MongoDB Atlas + Mongoose + bcryptjs
```


## 🛠️ Technical Skills Acquired

### Backend Development
| Skill | Description |
|-------|-------------|
| **RESTful API Design** | Designed and implemented resource-based endpoints following REST principles |
| **Database Modeling** | Created normalized schemas for relational (SQLite) and NoSQL (MongoDB) databases |
| **ORM/ODM Mastery** | Worked with SQLAlchemy (Python) and Mongoose (Node.js) for data abstraction |
| **Authentication** | Implemented JWT-based stateless authentication with refresh token patterns |
| **Authorization** | Built RBAC systems with granular permission controls |

### Security Practices
- Password hashing using Bcrypt
- Environment variable management with `dotenv`
- Input validation and sanitization
- Protected route implementation with middleware

### Architecture & Patterns
- **MVC/MRC Pattern**: Separation of concerns in Flask project
- **Middleware Design**: Custom authentication and error handling middleware
- **Migration Management**: Version-controlled database schemas using Alembic and manual migrations

### DevOps & Tools
- Git version control and GitHub workflows
- API testing with Postman/Insomnia
- Virtual environment management (Python venv, npm)
- Database migrations and seeding strategies

## 📚 Learning Journey

### Week 1-2: Job Portal (Flask)
**Challenge:** Understanding ORM concepts and relationship modeling  
**Solution:** Deep dive into SQLAlchemy's declarative base and relationship configurations

**Key Learnings:**
- How to structure a Flask application using blueprints
- Implementing many-to-many relationships (User ↔ Jobs through Applications)
- JWT token generation, validation, and protection decorators
- Writing Alembic migrations for schema changes

**Breakthrough Moment:**  
Implementing the `@jwt_required()` decorator and understanding how Flask-JWT-Extended handles token validation through request headers.

### Week 3-4: Event Management (Node.js)
**Challenge:** Transitioning from Python to JavaScript and synchronous to asynchronous programming  
**Solution:** Mastered Promises, async/await, and Express middleware chains

**Key Learnings:**
- MongoDB's flexible schema design vs relational databases
- Mongoose schema validation and pre/post hooks
- Express middleware architecture for authentication
- Handling capacity constraints with atomic operations

**Breakthrough Moment:**  
Realizing how middleware composition in Express creates a clean, reusable authentication pipeline compared to decorator-based approaches.

### Cross-Project Insights

**Similarities Discovered:**
- Both projects use JWT for stateless authentication
- RBAC is crucial for multi-tenant applications
- RESTful conventions improve API predictability
- Environment variables are essential for secure deployment

**Differences That Taught Me:**
- **SQLAlchemy vs Mongoose**: Explicit vs implicit validation
- **Flask decorators vs Express middleware**: Different approaches to cross-cutting concerns
- **Relational vs NoSQL**: When to use joins vs embedded documents

**What I'd Do Differently:**
- Implement refresh token rotation for better security
- Add comprehensive unit tests using pytest and Jest
- Integrate Swagger/OpenAPI documentation
- Add rate limiting and request logging

## ⚙️ Setup & Installation

### Prerequisites
- **Python 3.10+** (for Job Portal)
- **Node.js 16+** (for Event Management)
- **MongoDB Atlas** account (for Event Management)
- Git and Postman/Insomnia

### Quick Start

**Clone the repository:**
```bash
git clone https://github.com/SIBAM890/Back-dev-intern.git
cd Back-dev-intern
```

**Choose a project to run:**

#### Job Portal (Flask)
```bash
cd JOB-PORTAL
python -m venv .venv
source .venv/bin/activate  # On Windows: .\.venv\Scripts\activate
pip install -r requirements.txt
# Configure .env file (see project README)
flask db upgrade
python run.py
```

#### Event Management (Node.js)
```bash
cd EVENT-MANAGEMENT
npm install
# Configure .env file (see project README)
node server.js
```

**Detailed setup instructions are available in each project's README.**

## 📊 Project Statistics

| Metric | Job Portal | Event Management |
|--------|-----------|------------------|
| **Lines of Code** | ~1200 | ~900 |
| **API Endpoints** | 12+ | 8+ |
| **Database Tables/Collections** | 3 | 3 |
| **Authentication Methods** | JWT + Bcrypt | JWT + bcryptjs |
| **Development Time** | 2 weeks | 2 weeks |

## 🎓 Key Takeaways

> **"The best way to learn backend development is to build complete systems, not just isolated endpoints."**

1. **Architecture Matters**: Well-organized code is easier to debug, test, and scale
2. **Security First**: Never store plain passwords, always validate inputs, use environment variables
3. **Documentation is Code**: Good README files are as important as the code itself
4. **Test Early**: API testing tools like Postman should be used from day one
5. **Learn by Comparison**: Building similar projects in different tech stacks reveals universal patterns

---

