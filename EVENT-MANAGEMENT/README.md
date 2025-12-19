## 🗓️ Event Management System Backend

This project is a robust, RESTful backend API designed to manage events, registrations, and user roles (Admin/Standard User). It provides endpoints for creating, viewing, filtering events, and handling capacity-based user sign-ups.

## ✨ Features

  * **Event Lifecycle Management:** Allows authenticated users to create, update, and manage events (Title, Description, Date, Location, Capacity).
  * **Capacity Validation:** Prevents users from registering for an event once the maximum capacity is reached.
  * **User Registration:** Allows authenticated standard users to register for and cancel registrations for approved events.
  * **Filtering & Viewing:** Supports filtering the list of public events by date and location.
  * **Role-Based Access Control (RBAC):**
      * **Admin Role:** Required to approve newly created events before they become visible and registrable by the public.
      * **Organizer Role:** Creator of an event can manage its details.
  * **Authentication:** Secured using JWT (JSON Web Tokens) for all protected routes.

## 🛠️ Tech Stack

| Component | Technology | Role |
| **Backend Framework** | Node.js (Express) | Building the core RESTful API. |
| **Language** | JavaScript (ES6+) | Backend development. |
| **Database** | MongoDB | Flexible NoSQL data storage (via MongoDB Atlas). |
| **ORM/ODM** | Mongoose | Schema modeling and database interaction. |
| **Authentication** | JSON Web Tokens (JWT) & `bcryptjs` | User sessions and password hashing. |
| **Configuration** | `dotenv` | Managing environment variables and secrets. |

## 🚀 Getting Started Locally

Follow these steps to set up and run the Event Management System backend.

### Prerequisites

  * **Node.js & npm** installed.
  * **MongoDB Atlas** account (or local MongoDB server).
  * Git installed.

### 1\. Clone the Repository

```bash
git clone https://github.com/SIBAM890/Back-dev-intern
cd event-management-backend
cd EVENT-MANAGEMENT
```

### 2\. Install Dependencies

```bash
npm install
```

### 3\. Configure API Keys (Critical)

Create a file named **`.env`** in the root directory and add your connection details and secrets:

```env
# Get this from your MongoDB Atlas cluster connection string
MONGO_URI="   " 

PORT=5000
# Generate a long, random string for JWT_SECRET
JWT_SECRET="  "
```

### 4\. Run the Backend Server

Start the Express server using Node:

```bash
node server.js
# Or use nodemon for development:
# npm install -g nodemon
# nodemon server.js
```

Upon startup, you should see `MongoDB Connected...` and `Server running on port 5000`.

-----

## 🧪 API Endpoints (Testing)

Use an API client like **Postman** or **Thunder Client** to test the endpoints.

| Feature | Method | Endpoint | Required |
| **Register** | `POST` | `/api/auth/register` | `username`, `email`, `password`, `role` |
| **Login** | `POST` | `/api/auth/login` | `email`, `password` |
| **Create Event** | `POST` | `/api/events` | JWT Token (Protected) |
| **View Events** | `GET` | `/api/events?location=NYC` | None (Public/Filtered) |
| **Approve Event** | `PATCH` | `/api/events/:id/approve` | JWT Token (Admin Role) |
| **Register for Event** | `POST` | `/api/events/:id/register` | JWT Token (Protected) |
| **Cancel Registration** | `DELETE` | `/api/events/:id/register` | JWT Token (Protected) |
