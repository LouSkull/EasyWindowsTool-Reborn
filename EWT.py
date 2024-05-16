import customtkinter
from customtkinter import *
import tkinter
import tkinter,os,customtkinter
import subprocess
from plyer import notification
import os
from PIL import Image


os.system("color 2")
os.system("title EWT-LOG")
os.system("mode 75,35")
print("https://github.com/LouSkull/EasyWindowsTool-Reborn")
print("WELCOME TO EASYWINDOWSTOOL, THANK YOU FOR USING OUR TOOL : )")
print("THIS IS EASYWINDOWSTOOL LOGS, HERE YOU CAN SEE PROBLEMS")

class App(customtkinter.CTk):
    def __init__(self):
      
        super().__init__()

        self.title("")
        self.geometry("1200x700")
        self.title("github.com/LouSkull")
        self.resizable(False, False)
        self.attributes('-toolwindow', True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="EWT",
                                                             compound="left", font=customtkinter.CTkFont(size=20, weight="bold"))
        
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        self.frame_5_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Welcome",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_5_button_event)
        self.frame_5_button.grid(row=1, column=0, sticky="ew")
        
        self.frame_6_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="System",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_6_button_event)
        self.frame_6_button.grid(row=2, column=0, sticky="ew")
        
        self.frame_7_button = customtkinter.CTkButton(self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Other",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.frame_7_button_event)
        self.frame_7_button.grid(row=3, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=8, column=0, padx=20, pady=20, sticky="s")

        self.five_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.six_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seven_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        readme = """
- EasyWindowsTool предназначен только для использования в операционной системе Windows.
- Приложение помогает вашему компьютеру не всегда.
- Перед использованием EasyWindowsTool, убедитесь, что вы ознакомились с лицензией и соглашением об использовании программного обеспечения.
- Мы не ручаемся за ваш компьютер.
        """
        self.text_label = customtkinter.CTkLabel(self.five_frame, text=readme)
        self.text_label.pack()
        self.select_frame_by_name("frame_5")
        
        # widgets
        self.task_mgr_button_text = customtkinter.CTkLabel(self.six_frame, text="~ TaskMGR Control ~", font=("Arial", 20))
        self.windef_text = customtkinter.CTkLabel(self.six_frame, text="~ Windows Defender Control ~", font=("Arial", 20))
        self.task_mgr_button_enable = customtkinter.CTkButton(self.six_frame, text="Enable TaskMGR", command=self.EnableTaskMgr)
        self.task_mgr_button_disable = customtkinter.CTkButton(self.six_frame, text="Disable TaskMGR", command=self.DisableTaskMgr)
        self.windef_button_enable = customtkinter.CTkButton(self.six_frame, text="Enable Windows Defender", command=self.EnableWindef)
        self.windef_button_disable = customtkinter.CTkButton(self.six_frame, text="Disable Windows Defender", command=self.DisableWindef)
        self.autostart_button = customtkinter.CTkButton(self.seven_frame, text="AutoStart List", command=self.AutoStartListScript)
        self.PCSpecifications_button = customtkinter.CTkButton(self.seven_frame, text="AutoStart List", command=self.PCSpecifications)
        self.usernit_button = customtkinter.CTkButton(self.seven_frame, text="Reset Usernit", command=self.UsernitResetScript)
        self.virusscanner_button = customtkinter.CTkButton(self.seven_frame, text="Virus Scanner", command=self.VirusScanner)
        
        # Power Controller
        self.powercontroller_text = customtkinter.CTkLabel(self.six_frame, text="~ Power Controller ~", font=("Arial", 20))
        self.power_off_button = customtkinter.CTkButton(self.six_frame, text="Shutdown", command=self.shutdownPC)
        self.power_restart_button = customtkinter.CTkButton(self.six_frame, text="Restart", command=self.register)
        self.power_logout_button = customtkinter.CTkButton(self.six_frame, text="Logout", command=self.UserLogoutPC)
        
        self.powercontroller_text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.power_off_button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
        self.power_restart_button.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)
        self.power_logout_button.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)
        
        #other func
        self.other_text = customtkinter.CTkLabel(self.seven_frame, text="~ Other Functions ~", font=("Arial", 20))
        self.cleaner_button = customtkinter.CTkButton(self.seven_frame, text="Clean Windows", command=self.CleanerScript)
        
        self.windef_button_disable.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
        self.cleaner_button.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
        self.autostart_button.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
        self.PCSpecifications_button.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)
        self.usernit_button.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)
        
        # pack
        self.task_mgr_button_text.pack()
        self.task_mgr_button_enable.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
        self.task_mgr_button_disable.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
        
        self.windef_text.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.windef_button_enable.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)
        self.windef_button_disable.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)
        self.virusscanner_button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
        
        self.other_text.pack()

    def select_frame_by_name(self, name):
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.frame_6_button.configure(fg_color=("gray75", "gray25") if name == "frame_6" else "transparent")
        self.frame_7_button.configure(fg_color=("gray75", "gray25") if name == "frame_7" else "transparent")
        if name == "frame_5":
            self.five_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.five_frame.grid_forget()
            
        if name == "frame_6":
            self.six_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.six_frame.grid_forget()
            
        if name == "frame_7":
            self.seven_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.seven_frame.grid_forget()
      
    def EnableTaskMgr(self):
      os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 0 /f")
      notification.notify( 
      title= "EWT",
      message= "TaskMgr Enabled!",        
      timeout=5
)
    
    def DisableTaskMgr(self):
      from plyer import notification
      os.system("REG add HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
      notification.notify(
      title= "EWT",
      message= "TaskMgr Disabled!",        
      timeout=5
    )
      
    def EnableWindef(self):
        os.system("powershell -Command \"Start-Process -Wait -Verb RunAs PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command  Set-MpPreference -DisableRealtimeMonitoring $true'\"")
        notification.notify( 
        title= "EWT",
        message= "Windows Defender Enabled!",        
        timeout=5
)
    
    def DisableWindef(self):
        os.system("powershell -Command \"Start-Process -Wait -Verb RunAs PowerShell -ArgumentList '-NoProfile -ExecutionPolicy Bypass -Command  Set-MpPreference -DisableRealtimeMonitoring $false'\"")
        notification.notify( 
        title= "EWT",
        message= "Windows Defender Disabled!",        
        timeout=5
)
        
    def CleanerScript():
        os.system('del /q /s /f %temp%\\*.* & del /q /s /f C:\\Windows\\Temp\\* & rd /s /q "C:\\Users\\%username%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache" & del /q /s /f C:\\Windows\\Logs\\* & del /q /s /f C:\\Windows\\SoftwareDistribution\\Download\\*.* & del /q /s /f %windir%\\Installer\\*.*')
        import webbrowser
        import os
        import shutil
        def clean_all():
              clean_browsers()
              clean_temp_files()

        def clean_browsers():
              browsers = ['firefox', 'chrome', 'safari', 'edge', 'opera']

              for browser in browsers:
                      webbrowser.get(using=browser).open('about:blank')

        def clean_temp_files():
          temp_dir = os.environ.get('TEMP') or os.environ.get('TMP')
          for filename in os.listdir(temp_dir):
            file_path = os.path.join(temp_dir, filename)
            if os.path.isfile(file_path):
              os.unlink(file_path)
            elif os.path.isdir(file_path):
              shutil.rmtree(file_path)
            notification.notify( 
                title= "EWT",
                message= "Windows Cleaned!",        
                timeout=5
            )
        
    def AutoStartListScript(self):
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
    def PCSpecifications(self):
        import platform
        import psutil
        import tkinter as tk

        def get_pc_specs():
            specs = {}
            specs['System'] = platform.system()
            specs['Node Name'] = platform.node()
            specs['Release'] = platform.release()
            specs['Version'] = platform.version()
            specs['Machine'] = platform.machine()
            specs['Processor'] = platform.processor()
            specs['CPU'] = f"{psutil.cpu_count()} cores, {psutil.cpu_freq().current} MHz"
            specs['RAM'] = f"{psutil.virtual_memory().total / (1024 ** 3):.2f} GB"
            specs['Disk'] = f"{psutil.disk_usage('/').total / (1024 ** 3):.2f} GB total"
            return specs

        def display_specs():
            specs = get_pc_specs()
            for key, value in specs.items():
                label = tk.Label(root, text=key + ": " + value)
                label.pack()

        root = tk.Tk()
        root.title("PC Specifications")

        display_specs()

        root.mainloop()

    def UsernitResetScript(self):
        os.system('reg add "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows NT\\CurrentVersion\\Winlogon" /v Userinit /t REG_SZ /d     "C:\\Windows\\system32\\userinit.exe,"')
        notification.notify( 
            title= "EWT",
            message= "Usernit Reset Successfully.",        
            timeout=10
        )
        
    def restartPC(self):
      os.system("shutdown /r /f /t 0")
    
    def shutdownPC(self):
      os.system("shutdown /s /f /t 0")
      
    def UserLogoutPC(self):
      os.system("shutdown /l")
      
    def VirusScanner(self):
        import requests,os,time,base64


        APII = (base64.b64decode('NmI4NjNjZjU4YTZlZGU5MDQzZGYzMjFkNTU4ZDA5NzRkM2UxNjgwZTcyMmVlNzM5OTYzMTcxZmIwMDBkZmJiMg==').decode('utf-8'))

        os.system("color 80")
        os.system("cls")

        def scan_file(api_key, file_path):
            url = 'https://www.virustotal.com/vtapi/v2/file/scan'
            params = {'apikey': api_key}
            
            with open(file_path, 'rb') as file:
                files = {'file': (file_path, file)}
                response = requests.post(url, files=files, params=params)

            return response.json()

        def check_report(api_key, resource):
            url = 'https://www.virustotal.com/vtapi/v2/file/report'
            params = {'apikey': api_key, 'resource': resource}
            response = requests.get(url, params=params)

            return response.json()

        def main():
            api_key = APII
            
            file_path = input("Enter the path to the file: ")

            scan_result = scan_file(api_key, file_path)

            resource = scan_result.get('resource')
            if resource:
                report = check_report(api_key, resource)
                
                if report.get('response_code') == 1:
                    print("\nScan Report:")
                    print("Scan Date:", report.get('scan_date'))
                    print("File Name:", report.get('verbose_msg'))
                    
                    positives = report.get('positives')
                    total = report.get('total')
                    
                    if positives is not None and total is not None:
                        print("Detection Ratio: {}/{}".format(positives, total))
                        
                        if positives > 0:
                            print("Detections:")
                            for antivirus, result in report.get('scans').items():
                                if result.get('detected'):
                                    print("{}: {}".format(antivirus, result.get('result')))
                            input("\nPress Enter to continue...")
                        else:
                            print("No detections.")
                            input("\nPress Enter to continue...")
                    else:
                        print("Detection information not available.")
                        input("\nPress Enter to continue...")
                else:
                    print("Error in retrieving the scan report. Please try again later.")
                    input("\nPress Enter to continue...")
            else:
                print("Error in submitting the file for scanning. Please try again later.")
                input("\nPress Enter to continue...")

        if __name__ == "__main__":
            main()
      
    
    def frame_5_button_event(self):
        self.select_frame_by_name("frame_5")

    def frame_6_button_event(self):
        self.select_frame_by_name("frame_6")
        
    def frame_7_button_event(self):
        self.select_frame_by_name("frame_7")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()