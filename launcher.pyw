import subprocess
import sys
import os
from appdata.settings import config

def run_with_hidden_console(script):
    si = subprocess.STARTUPINFO()
    si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
    si.wShowWindow = subprocess.SW_HIDE
    subprocess.call([sys.executable, script], startupinfo=si)

if __name__ == "__main__":
    if not config.EWT_LOGS:
        run_with_hidden_console('EWT.py')
    else:
        os.system('python EWT.py')
