# Imports
import customtkinter as ctk
from customtkinter import *
import tkinter,os,customtkinter

# Theme
customtkinter.set_appearance_mode("System")

# Main Script
def Taskmgr():
  
  def EnableTaskMgr():
    os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f")
    
  def DisableTaskMgr():
    os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    
  def Close():
    Ttaskmgr.destroy()
  
  Ttaskmgr = ctk.CTk()
  
  Ttaskmgr.title("EWT")
  Ttaskmgr.geometry("600x300")
  
  CTkButton(Ttaskmgr, text= "Enable", command=EnableTaskMgr).pack()
  CTkButton(Ttaskmgr, text= "Disable", command=DisableTaskMgr).pack()
  CTkButton(Ttaskmgr, text= "Close", command=Close).pack()
  
  Ttaskmgr.mainloop()
  
def Windef():
  def EnableWindef():
    os.system("Start Helper\\windefender\\Enable.bat")
    
  def DisableWindef():
    os.system("Start Helper\\windefender\\Disable.bat")
    
  def Close():
    WindefWinWin.destroy()
  
  WindefWinWin = ctk.CTk()
  
  WindefWinWin.title("EWT")
  WindefWinWin.geometry("600x300")
  
  CTkButton(WindefWinWin, text= "Enable", command=EnableWindef).pack()
  CTkButton(WindefWinWin, text= "Disable", command=DisableWindef).pack()
  CTkButton(WindefWinWin, text= "Close", command=Close).pack()
  
  WindefWinWin.mainloop()
  
def CleanerScript():
  os.system(f"start helper\\cleaner.bat")
  

def AutoStartListScript():
  import os
  import winreg
  import tkinter as tk
  from tkinter import ttk

  def get_autostart_programs():
      autostart_programs = []

      key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
      try:
          key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
          i = 0
          while True:
              try:
                  name, value, _ = winreg.EnumValue(key, i)
                  autostart_programs.append(f"{name}: {value}")
                  i += 1
              except OSError:
                  break
      except FileNotFoundError:
          pass

      return autostart_programs

  class AutostartApp:
      def __init__(self, master):
          self.master = master
          self.master.title("Autostart Program List")
          self.master.geometry("1200x600")

          self.listbox = tk.Listbox(self.master)
          self.listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

          autostart_programs = get_autostart_programs()
          for program in autostart_programs:
              self.listbox.insert(tk.END, program)

          self.close_button = ttk.Button(self.master, text="Close", command=self.master.destroy)
          self.close_button.pack(pady=10)

  def main():
      root = tk.Tk()
      app = AutostartApp(root)
      root.mainloop()

  if __name__ == "__main__":
      main()

def PCSpecifications():
  import platform
  import psutil
  import tkinter as tk

  def get_pc_specifications():
      system_info = f"System: {platform.system()} {platform.version()}\n"
      processor_info = f"Processor: {platform.processor()}\n"
      ram_info = f"RAM: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB\n"
      disk_info = f"Disk: {round(psutil.disk_usage('/').total / (1024 ** 3), 2)} GB"

      return system_info + processor_info + ram_info + disk_info

  def get_resource_usage():
      cpu_percent = psutil.cpu_percent(interval=1)
      memory_info = psutil.virtual_memory()

      return f"CPU Usage: {cpu_percent}%\nMemory Usage: {memory_info.percent}%"

  def update_resource_info(root):
      resource_info = get_resource_usage()
      resource_label.config(text=resource_info)
      root.after(1000, lambda: update_resource_info(root))

  def show_resource_monitor():
      root = tk.Tk()
      root.title("EWT")

      spec_label = tk.Label(root, text=get_pc_specifications(), padx=10, pady=10)
      spec_label.pack()

      global resource_label
      resource_label = tk.Label(root, text="", padx=10, pady=10)
      resource_label.pack()

      update_resource_info(root)

      root.mainloop()

  if __name__ == "__main__":
      show_resource_monitor()

def UsernitResetScript():
  os.system("start helper\\ResetUsernit.bat")
  
def UpdatePCScript():
  os.system("start helper\\update.bat")
  
def PowerControllerScript():
    def restartPC():
      os.system("shutdown /r /f /t 0")
    
    def shutdownPC():
      os.system("shutdown /s /f /t 0")
      
    def UserLogoutPC():
      os.system("shutdown /l")
      
    def Close():
      PowerControllerWindow.destroy()
    
    PowerControllerWindow = ctk.CTk()
    
    PowerControllerWindow.title("EWT")
    PowerControllerWindow.geometry("600x300")
    
    CTkButton(PowerControllerWindow, text= "Restart", command=restartPC).pack()
    CTkButton(PowerControllerWindow, text= "Shutdown", command=shutdownPC).pack()
    CTkButton(PowerControllerWindow, text= "User Logout", command=UserLogoutPC).pack()
    CTkButton(PowerControllerWindow, text= "Close", command=Close).pack()
    
    PowerControllerWindow.mainloop()
    
def WifiConectionScript():
  import tkinter as tk
  import subprocess

  def check_wifi():
      try:
          result = subprocess.run(["ping", "-c", "1", "google.com"], capture_output=True, text=True, timeout=5)
          if "1 packets transmitted, 1 received" in result.stdout:
              status_label.config(text="Connected to WiFi", fg="green")
          else:
              status_label.config(text="Not connected to WiFi", fg="red")
      except subprocess.TimeoutExpired:
          status_label.config(text="Timeout: Not connected to WiFi", fg="red")

      root1 = tk.Tk()
      root1.title("WiFi Connection Checker")
      
      status_label = tk.Label(root1, text="", font=("Helvetica", 16))
      status_label.pack(pady=20)

      check_button = tk.Button(root1, text="Check WiFi", command=check_wifi)
      check_button.pack(pady=10)

      root1.mainloop()

  
def VirusScannerScript():
  import tkinter as tk
  from tkinter import filedialog
  import subprocess

  def scan_file():
      file_path = filedialog.askopenfilename()
      if file_path:
          try:
              result = subprocess.run(["clamscan", file_path], capture_output=True, text=True)
              if "Infected files: 0" in result.stdout:
                  status_label.config(text="File is clean", fg="green")
              else:
                  status_label.config(text="File is infected", fg="red")
          except Exception as e:
              status_label.config(text=f"Error: {str(e)}", fg="red")

  root = tk.Tk()
  root.title("EWT")
  root.geometry("600x300")

  status_label = tk.Label(root, text="", font=("Helvetica", 16))
  status_label.pack(pady=20)

  scan_button = tk.Button(root, text="Scan File", command=scan_file)
  scan_button.pack(pady=10)

  root.mainloop()


# Main Window
window = ctk.CTk()

# Window Settings
window.title("EWT - github.com/LouSkull")
window.geometry("1200x600")

# Buttons
Taskmgr = CTkButton(window, text= "Taskmgr Control", command=Taskmgr)
WindefB = CTkButton(window, text= "Windows Defender Control", command=Windef)
Cleaner = CTkButton(window, text= "Cleaner", command=CleanerScript)
AutoStartListButton = CTkButton(window, text= "Auto Start List", command=AutoStartListScript)
PCSpecificationsButton = CTkButton(window, text= "PC Specifications", command=PCSpecifications)
UsernitResetButton = CTkButton(window, text= "Reset Usernit", command=UsernitResetScript)
UpdatePCButton = CTkButton(window, text= "PC Updater", command=UpdatePCScript)
PowerPCButton = CTkButton(window, text= "Power Controller", command=PowerControllerScript)
WifiConectionButton = CTkButton(window, text= "Wifi Connecton Checker", command=WifiConectionScript)
VirusScannerButton = CTkButton(window, text= "Virus Scanner", command=VirusScannerScript)

# Show Buttons
Taskmgr.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
WindefB.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
Cleaner.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)
AutoStartListButton.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)
PCSpecificationsButton.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
UsernitResetButton.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)
UpdatePCButton.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)
PowerPCButton.place(relx=0.1, rely=0.8, anchor=tkinter.CENTER)
VirusScannerButton.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)

# Labels

Readme = CTkLabel(window, text="""
- EasyWindowsTool предназначен только для использования в операционной системе Windows.
- Приложение помогает вашему компьютеру не всегда.
- Перед использованием EasyWindowsTool, убедитесь, что вы ознакомились с лицензией и соглашением об использовании программного обеспечения.
- Мы не ручаемся за ваш компьютер.
""")

# Show Labels
Readme.place(relx=0.6, rely=0.5, anchor=tkinter.CENTER)

# Show Our Main Window
window.mainloop()
