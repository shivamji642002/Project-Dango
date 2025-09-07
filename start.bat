@echo off
echo Starting Django server with HTTPS...
REM ✅ Activate your virtual environment (edit path if needed)
call venv\Scripts\activate

REM ✅ Run Django with SSL certificate
python manage.py runserver_plus --cert-file cert.pem

pause
