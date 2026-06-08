@echo off
echo === CABANA FISH Backend ===

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat

REM Install dependencies
echo Installing dependencies...
pip install -r requirements.txt --quiet

REM Copy .env if it doesn't exist
if not exist ".env" (
    echo Creating .env from example...
    copy .env.example .env
    echo !!! Please edit backend\.env with your email credentials before continuing.
    pause
    exit /b
)

REM Apply database migrations
echo Applying migrations...
python manage.py migrate --run-syncdb

REM Create superuser if no admin exists
python manage.py shell -c "from django.contrib.auth import get_user_model; U=get_user_model(); print('Admin exists') if U.objects.filter(is_superuser=True).exists() else U.objects.create_superuser('admin','contact@cabanafish.com','admin123') or print('Admin created: admin / admin123')"

echo.
echo Server starting on http://127.0.0.1:8000
echo Admin panel : http://127.0.0.1:8000/admin
echo.
python manage.py runserver
