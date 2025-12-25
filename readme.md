# Django Todo App

A comprehensive **Todo application** built with Django to manage your daily tasks effectively. The app allows users to create, update, manage status, and delete tasks with ease.

---

## ✅ Features

- **User Authentication**: Secure Login, Registration, and Logout functionality.
- **Task Management**: Create, Read, Update, and Delete (CRUD) tasks.
- **Status Tracking**: Mark tasks as 'Not Started', 'Pending', or 'Completed'.
- **Due Dates**: Set and track deadlines for your tasks.
- **Responsive UI**: Clean interface built with Django Templates.

---

## 🛠 Tech Stack

- **Backend:** Django
- **Database:** SQLite (Default)
- **Frontend:** HTML, CSS
- **Authentication:** Django Auth System

---

## 📁 Project Structure

```
TODO/
│
├── TODO/               # Project settings and configuration
│
├── accounts/           # User authentication app (views, urls)
│
├── todolist/           # Main application logic
│   ├── models.py       # Todo model definition
│   ├── views.py        # Task handling views
│   ├── urls.py         # App routing
│   └── templates/      # App-specific templates
│
├── templates/          # Global templates (base.html)
├── static/             # Static files (CSS, JS)
├── db.sqlite3          # Database file
└── manage.py           # Django command-line utility
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone <repo-url>
cd TODO
```

### 2. Create Virtual Environment

```bash
python -m venv venv
# Activate local environment
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Install Django

```bash
pip install django
```

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 5. Run the Server

```bash
python manage.py runserver
```

Open your browser and visit:

```
http://127.0.0.1:8000/
```

---

## 🔄 App Usage

1.  **Register/Login**: Create an account to manage your personal tasks.
2.  **Dashboard**: View your open and completed tasks.
3.  **Add Task**: Click "Add New Task" to create a new entry with a Title, Due Date, and Status.
4.  **Update Status**: Change task status to keep track of progress.
