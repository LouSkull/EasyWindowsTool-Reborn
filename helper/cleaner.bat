@echo off
del /q /s /f %temp%\*.*
del /q /s /f C:\Windows\Temp\*
rd /s /q "C:\Users\%username%\AppData\Local\Google\Chrome\User Data\Default\Cache"
del /q /s /f C:\Windows\Logs\*
del /q /s /f C:\Windows\SoftwareDistribution\Download\*.*
del /q /s /f %windir%\Installer\*.*
start Helper\Success.vbs
exit