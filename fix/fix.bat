@echo off
cls
color F
echo If EWT is not functioning properly, your first step should be to run EWT with administrative privileges.
timeout /t 2 /nobreak >nul

:CHOICE
echo.
echo Please choose an option:
echo [1] Start installing library
echo [2] Exit
set /p choice="Enter your choice: "

if "%choice%"=="1" goto INSTALL
if "%choice%"=="2" goto EXIT
echo Invalid choice. Please enter 1 or 2.
goto CHOICE

:INSTALL
echo This can take up to 5 minutes...
timeout /t 2 /nobreak >nul
pip install --upgrade pip
pip install -r requirements.txt
cls
color F
echo Successfully...
pause
goto END

:EXIT
echo Exiting...
timeout /t 1 /nobreak >nul
goto END

:END
exit
