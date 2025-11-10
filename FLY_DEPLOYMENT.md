# Deploying Django to Fly.io

This repo is configured for Fly.io using a Dockerfile. Summary:

- Dockerfile binds to `$PORT` (defaults 8080 for Fly)
- WhiteNoise serves static files
- Database is taken from `DATABASE_URL` if present

## One-time setup

1. Install Fly CLI and login:
   ```bash
   fly auth signup   # or: fly auth login
   ```
2. From the project root (where `manage.py` lives):
   ```bash
   fly launch --now --no-deploy
   ```
   - Accept Dockerfile detection
   - This creates `fly.toml` (commit it)

## Secrets and environment

Set secrets for production:
```bash
fly secrets set SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(50))')" \
               EMAIL_HOST_USER="your@email" \
               EMAIL_HOST_PASSWORD="your-app-password" \
               DJANGO_SETTINGS_MODULE="car_rental.settings" \
               DEBUG="false"
```

If you add a Fly Postgres database:
```bash
fly postgres create
fly postgres attach --app <your-app-name>
```
This injects `DATABASE_URL` automatically.

## Deploy
```bash
fly deploy
```
Then run migrations and collectstatic:
```bash
fly ssh console -C "python manage.py migrate --noinput && python manage.py collectstatic --noinput"
```

Open the app:
```bash
fly open
```


