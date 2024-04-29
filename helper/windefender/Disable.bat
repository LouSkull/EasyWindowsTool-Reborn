@echo off
powershell -Command "Start-Process -Wait -Verb RunAs PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command Set-MpPreference -DisableRealtimeMonitoring $false'"