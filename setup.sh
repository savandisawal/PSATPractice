#!/usr/bin/env bash
set -e

echo "========================================"
echo " PSAT Practice - Unix/Mac Setup Script"
echo "========================================"
echo

cd psat_project

echo "[1/4] Installing Python dependencies..."
pip install -r requirements.txt

echo
echo "[2/4] Running database migrations + loading sample data..."
python manage.py setup_psat

echo
echo "[3/4] Creating admin (superuser) account..."
echo "   When prompted, enter a username, email, and password for the admin."
python manage.py createsuperuser

echo
echo "[4/4] Starting development server..."
echo "   Open your browser and go to: http://localhost:8000"
echo "   Admin panel:                  http://localhost:8000/admin"
echo
python manage.py runserver
