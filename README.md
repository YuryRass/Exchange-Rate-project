# Exchange-Rate project

## Prerequisites

- Python 3.x
- Django

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/YuryRass/Exchange-Rate-project.git
   cd Exchange-Rate-project
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Apply migrations:

   ```bash
   python manage.py migrate
   ```

4. Create a superuser:

   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:

   ```bash
   uvicorn project.asgi:application --host 127.0.0.1 --port 8000
   ```
   or
     ```bash
   ./scripts/run_app.sh
   ```

## Configuration

1. Open the `settings.py` file and add `'django_crontab'` to the `INSTALLED_APPS` list:

   ```python
   INSTALLED_APPS = [
       # ... other installed apps ...
       'django_crontab',
   ]
   ```

2. Configure your cron jobs in the `CRONJOBS` setting:

   ```python
   CRONJOBS = [
       ("*/1 * * * *", "exchange.tasks.fetch_exchange_rate"),
   ]
   ```

3. Apply the cron job configuration:

   ```bash
   ./scripts/run_cron.sh
   ```