@echo off
cls
color 2
echo This can take up to 5 minutes...
timeout /t 2 /nobreak >nul
pip install --upgrade pip
pip install -r requirements.txt
cls
color 2
echo Successfully...
pause
