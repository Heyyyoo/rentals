# Deploying to Railway

This repo includes the files Railway expects:

- `Procfile` → runs the web server with Gunicorn
- `requirements.txt` → Python/Django dependencies

> Note: Your `manage.py` and Django project package (e.g. `car_rental/`) should be at the repository root. If they are one level up from this `rentals/` app, place `Procfile` and `requirements.txt` at the project root before deploying.

## Django settings (apply in your project settings module)

Add the following to your `car_rental/settings.py`:

```python
import os
from pathlib import Path
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = os.getenv("DEBUG", "false").lower() == "true"
ALLOWED_HOSTS = ["*"]
CSRF_TRUSTED_ORIGINS = ["https://*.up.railway.app", "https://*.railway.app"]

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    # ... keep existing middleware ...
]
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}
DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASES["default"] = dj_database_url.parse(DATABASE_URL, conn_max_age=600, ssl_require=True)
```

## Railway steps
1. Push your code to GitHub.
2. On Railway: New Project → Deploy from GitHub → select your repo.
3. Add a PostgreSQL service (optional but recommended).
4. In your web service → Variables, set:
   - `DJANGO_SETTINGS_MODULE=car_rental.settings`
   - `SECRET_KEY=<strong-random-string>`
   - `DEBUG=false`
   - `DATABASE_URL` (click “Connect” on the Postgres service to inject)
5. Post-deploy commands (or run once in a shell):

```bash
python manage.py migrate --noinput
python manage.py collectstatic --noinput
```

Open the generated Railway URL to verify the app.


