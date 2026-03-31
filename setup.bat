@echo off
echo ========================================
echo  PSAT Practice - Windows Setup Script
echo ========================================
echo.

cd psat_project

echo [1/4] Installing Python dependencies...
pip install -r requirements.txt
if errorlevel 1 ( echo ERROR: pip install failed. Make sure Python 3 is installed. & pause & exit /b 1 )

echo.
echo [2/4] Running database migrations + loading sample data...
python manage.py setup_psat
if errorlevel 1 ( echo ERROR: Setup failed. & pause & exit /b 1 )

echo.
echo [3/4] Creating admin (superuser) account...
echo    When prompted, enter a username, email, and password for the admin.
python manage.py createsuperuser

echo.
echo [4/4] Starting development server...
echo    Open your browser and go to: http://localhost:8000
echo    Admin panel:                  http://localhost:8000/admin
echo.
python manage.py runserver
pause
