# Calorie Counter — Upgraded (Django 5.x)

A lightweight Calorie Counter web app using **Django 5.x**, **SQLite**, and **Tailwind CSS (via CDN)**.
Designed to be simple and easy to run locally; ready for you to deploy on Render.

## Quick features
- Add / View / Delete food items
- Shows daily total calories
- Reset (clear all items)
- Tailwind via CDN for a modern responsive UI
- Simple `.env` support (python-dotenv)

## Quick start (local)
1. Create & activate a venv:
```bash
python3 -m venv venv
source venv/bin/activate    # macOS / Linux
# venv\Scripts\activate   # Windows PowerShell
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a `.env` file (optional) to override secret and debug, example:
```
SECRET_KEY=your-secret-key
DEBUG=True
```
4. Migrate and run:
```bash
python manage.py migrate
python manage.py runserver
```
5. Open http://127.0.0.1:8000/

## Deploying to Render
- Create a Git repo and push this project.
- Create a Web Service on Render using the Python environment.
- Command: `gunicorn calorie_counter_project.wsgi --log-file -`
- Set environment variables on Render (e.g. `SECRET_KEY`, `DEBUG=false`).
- Render automatically installs `requirements.txt`.

If you want, I can add Render-specific example files (render.yaml) later.
