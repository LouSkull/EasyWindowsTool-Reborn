@echo off
setlocal

wusa.exe "C:\path\to\update.msu" /quiet /norestart

if %errorlevel% equ 0 (
    start Helper\Success.vbs
) else (
    start Helper\Error.vbs
)

endlocal
exit