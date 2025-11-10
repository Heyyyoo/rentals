# Deploying Django to Render.com

This project is Docker-ready and can be deployed to Render as a Web Service.

## 1) Push to GitHub
Commit `Dockerfile` and `requirements.txt` at the repo root (same folder as `manage.py`). Push to GitHub.

## 2) Create a Web Service on Render
- New → Web Service → Select your GitHub repo
- Environment: Docker
- Region: your choice
- Build Command: (leave empty, Dockerfile handles build)
- Start Command: (leave empty, Dockerfile sets CMD to run gunicorn)

Render sets `$PORT` automatically; the Dockerfile binds to it.

## 3) Environment Variables
Add the following in Render “Environment”:
- `DJANGO_SETTINGS_MODULE=car_rental.settings`
- `SECRET_KEY=<strong random string>`
- `DEBUG=false`
- `EMAIL_HOST_USER=<your email>`
- `EMAIL_HOST_PASSWORD=<your app password>`

If you add a Render PostgreSQL database, connect it and Render will provide `DATABASE_URL`. The app will automatically use it.

## 4) Post-deploy tasks
Run once via Render Shell or “Jobs”:
```bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
```

Open your service URL (`onrender.com`) and test.

Notes:
- Static files are served by WhiteNoise inside the container.
- User uploads in `media/` aren’t persisted unless you use a Render Persistent Disk. Consider storing uploads externally (S3) for production.


