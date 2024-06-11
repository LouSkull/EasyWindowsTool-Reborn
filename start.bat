@echo off
set "TargetPath=launcher.pyw"

echo Set WshShell = CreateObject("WScript.Shell") > "%TEMP%\RunHidden.vbs"
echo WshShell.Run chr(34) ^& "%TargetPath%" ^& chr(34), 0, false >> "%TEMP%\RunHidden.vbs"

cscript /nologo "%TEMP%\RunHidden.vbs"
del "%TEMP%\RunHidden.vbs"
exit