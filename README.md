# FastAPI Todo Web Application

A simple **web-based Todo Application** built using **FastAPI** and **SQLite3**, where users can register, log in, and manage their personal todo lists. Each user can **add**, **view**, and **delete** their todos securely after logging in.

---

## Features

- **User Registration & Authentication**
  - Create a new account using a username and password.
  - Secure login system using JWT-based authentication.
- 🧾 **Personalized Todo List**
  - View todos associated with your user account.
  - Add new todos to your list.
  - Delete existing todos.
- **Persistent Storage**
  - Uses **SQLite3** for lightweight, file-based database storage.
- ⚡ **FastAPI Backend**
  - High-performance, modern Python web framework.
  - Built-in interactive API docs using Swagger UI.


## 🖼️ Screenshots

| Login Page | Register Page |
|-------------|---------------|
| ![Login Page](static/screenshots/LoginPage.png) | ![Register Page](static/screenshots/RegisterPage.png) |

| Todo List | Add New Todo |
|-------------|---------------|
| ![ToDo List](static/screenshots/ToDoList.png) | ![New ToDo](static/screenshots/NewToDo.png) |

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| **Backend Framework** | [FastAPI](https://fastapi.tiangolo.com/) |
| **Database** | SQLite3 |
| **ORM / DB Layer** | SQLAlchemy or built-in `sqlite3` module |
| **Authentication** | JWT (JSON Web Tokens) |
| **Frontend** | HTML templates (Jinja2 or static HTML) |
| **Server** | Uvicorn |



## ⚙️ Installation & Setup

1️⃣ Clone the Repository
```bash
git clone <branchname>.git
cd ToDoApp
2️⃣ Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
4️⃣ Run the Application
bash
Copy code
uvicorn app.main:app --reload
5️⃣ Access the App
Visit the web UI at: http://127.0.0.1:8000/

Access the API documentation at: http://127.0.0.1:8000/docs

