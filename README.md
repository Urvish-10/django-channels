# Django Channels Demo with uv & Django Runserver

A minimal project demonstrating how to integrate **Django Channels** for WebSocket support in a Django web app — using **uv** for dependency management and running the development server via Django’s built-in `runserver` (ASGI-enabled).

---

## 🚀 Overview

This project shows how to use **Django Channels** alongside standard Django views to enable real-time features such as chat or live updates.
It uses the **ASGI application** built into Django and runs directly with `python manage.py runserver` (no separate Daphne command needed).

---

## 🧰 Features

* ✅ Standard Django web pages (HTTP)
* 🔁 WebSocket communication via Django Channels
* ⚡ ASGI server automatically handled by Django
* 🧩 Managed with **uv** (fast Python package manager)
* 🗂 Example setup for learning and extending Channels

---

## 🧱 Project Setup

### Prerequisites

* Python 3.8+
* [uv](https://github.com/astral-sh/uv) installed
* Redis (optional) — only needed if you want to use a Redis channel layer

### 1️⃣ Clone the repository

```bash
git clone https://github.com/Urvish-10/django-channels.git
cd django-channels
```

### 2️⃣ Initialize the environment with uv

If the project already has a `pyproject.toml`, simply sync it:

```bash
uv sync
```

If you are setting up from scratch:

```bash
uv init
uv add django channels
```

You can add other dependencies as needed:

```bash
uv add channels-redis
```

---

### 3️⃣ Run database migrations

```bash
python manage.py migrate
```

---

### 4️⃣ Start the development server

Run the ASGI server via Django’s built-in command:

```bash
python manage.py runserver
```

Then visit:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧠 How It Works

* `asgi.py` defines the **ASGI application** that supports both HTTP and WebSocket protocols.
* `routing.py` connects WebSocket URLs to their respective **Consumers**.
* Each `Consumer` handles WebSocket events (connect, receive, disconnect).
* Django automatically runs the ASGI app when you use `runserver`.
* The **uv** tool handles dependency resolution and virtual environment management in one step.

---

## 📁 Project Structure

```
.
├── channels_chatapp/                # Example app handling WebSockets
│   ├── consumers.py        # WebSocket consumer logic
│   ├── routing.py          # Channel routing definitions
│   ├── templates/          # HTML templates
│   └── views.py            # Django views
├── chatweb/        # Main Django project folder
│   ├── asgi.py             # ASGI entry point
│   ├── settings.py         # Project settings
│   └── urls.py             # URL routing
├── manage.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

## 🛠 Common Commands

| Task                    | Command                             |
| ----------------------- | ----------------------------------- |
| Add a new dependency    | `uv add package_name`               |
| Remove a dependency     | `uv remove package_name`            |
| Update all dependencies | `uv lock --upgrade`                 |
| Run any Django command  | `python manage.py <command>` |

---

## 🧩 Notes

* Django automatically uses its ASGI server under the hood — no need to call Daphne manually during development.
* For production, you can still serve your app with **Daphne** or **Uvicorn**, using the same `asgi.py` entry point.
* Make sure to configure a persistent channel layer (like Redis) for real-world deployments.

---

## 📚 Resources

* Django Channels Docs: [https://channels.readthedocs.io/](https://channels.readthedocs.io/)
* Django ASGI Reference: [https://docs.djangoproject.com/en/stable/howto/deployment/asgi/](https://docs.djangoproject.com/en/stable/howto/deployment/asgi/)
* uv Documentation: [https://docs.astral.sh/uv/latest/](https://docs.astral.sh/uv/latest/)

---

## 👤 Author

**Urvish-10**

> A learning project built to explore real-time Django with Channels & uv.
> Feel free to fork, experiment, and extend!
