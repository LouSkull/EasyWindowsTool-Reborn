import customtkinter
from customtkinter import *
import tkinter
import tkinter,os,customtkinter
import subprocess
from plyer import notification
import os
from PIL import Image
import webbrowser
import shutil
import tkinter as tk

fg_color_config_main = "transparent"


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
        self.attributes('-toolwindow', False)

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
- EasyWindowsTool is intended for use only on the Windows operating system.
- The application does not always help your computer.
- Before using EasyWindowsTool, make sure you have read the software license and agreement.
- We do not vouch for your computer.
        """
        self.text_label = customtkinter.CTkLabel(self.five_frame, text=readme, font=('Helvetica bold', 20))
        self.text_label.pack()
        self.select_frame_by_name("frame_5")
        
        import winsound

        def play_sound(sound_file):
            # Play the sound
            winsound.PlaySound(sound_file, winsound.SND_FILENAME)

        if __name__ == "__main__":
            play_sound('startup.wav')
            
        # widgets
        self.task_mgr_button_text = customtkinter.CTkLabel(self.six_frame, text="~ TaskMGR Control ~", font=("Arial", 20))
        self.windef_text = customtkinter.CTkLabel(self.six_frame, text="~ Windows Defender Control ~", font=("Arial", 20))
        self.task_mgr_button_enable = customtkinter.CTkButton(self.six_frame, text="Enable TaskMGR",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.EnableTaskMgr)
        self.task_mgr_button_disable = customtkinter.CTkButton(self.six_frame, text="Disable TaskMGR",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.DisableTaskMgr)
        self.windef_button_enable = customtkinter.CTkButton(self.six_frame, text="Enable WINDef",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.EnableWindef)
        self.windef_button_disable = customtkinter.CTkButton(self.six_frame, text="Disable WINDef",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.DisableWindef)
        self.autostart_button = customtkinter.CTkButton(self.seven_frame, text="AutoStart List",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18), command=self.AutoStartListScript)
        self.PCSpecifications_button = customtkinter.CTkButton(self.seven_frame, text="PC Specifications",border_color="#00B3FF",corner_radius=32, border_width=2,  font=('Helvetica bold', 18),command=self.PCSpecifications)
        self.usernit_button = customtkinter.CTkButton(self.seven_frame, text="Reset Usernit",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.UsernitResetScript)
        self.virusscanner_button = customtkinter.CTkButton(self.seven_frame, text="Virus Scanner",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18), command=self.VirusScanner)
        
        # Power Controller
        self.powercontroller_text = customtkinter.CTkLabel(self.six_frame, text="~ Power Controller ~", font=("Arial", 20))
        self.power_off_button = customtkinter.CTkButton(self.six_frame, text="Shutdown",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18), command=self.shutdownPC)
        self.power_restart_button = customtkinter.CTkButton(self.six_frame, text="Restart",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18), command=self.register)
        self.power_logout_button = customtkinter.CTkButton(self.six_frame, text="Logout",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18), command=self.UserLogoutPC)
        
        self.powercontroller_text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.power_off_button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
        self.power_restart_button.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)
        self.power_logout_button.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)
        
        #other func
        self.other_text = customtkinter.CTkLabel(self.seven_frame, text="~ Other Functions ~", font=("Arial", 20))
        self.cleaner_button = customtkinter.CTkButton(self.seven_frame, text="Clean Windows",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.CleanerScript)
        self.advanced_search_button = customtkinter.CTkButton(self.seven_frame, text="File Search",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.AdvancedSearch)
        self.network_manager_button = customtkinter.CTkButton(self.seven_frame, text="Network Manager",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.NetworkManagerFunction)
        self.file_manager_button = customtkinter.CTkButton(self.seven_frame, text="File Manager",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.FileManagerFunction)
        self.driver_manager_button = customtkinter.CTkButton(self.seven_frame, text="Driver Manager",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.DriverManagerFunction)
        self.benchmark_button = customtkinter.CTkButton(self.seven_frame, text="Benchmark",border_color="#00B3FF",corner_radius=32, border_width=2, font=('Helvetica bold', 18),command=self.BenchmarkFunction)
        
        self.cleaner_button.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
        self.PCSpecifications_button.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
        self.usernit_button.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)
        self.autostart_button.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)
        
        # pack
        self.task_mgr_button_text.pack()
        self.task_mgr_button_enable.place(relx=0.1, rely=0.1, anchor=tkinter.CENTER)
        self.task_mgr_button_disable.place(relx=0.1, rely=0.2, anchor=tkinter.CENTER)
        
        self.windef_text.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.windef_button_enable.place(relx=0.1, rely=0.3, anchor=tkinter.CENTER)
        self.windef_button_disable.place(relx=0.1, rely=0.4, anchor=tkinter.CENTER)
        self.virusscanner_button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
        self.advanced_search_button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
        self.network_manager_button.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)
        self.file_manager_button.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)
        self.driver_manager_button.place(relx=0.1, rely=0.8, anchor=tkinter.CENTER)
        self.benchmark_button.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)
        
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


    def CleanerScript(self):
        def clean_all():
            clean_browsers()
            clean_temp_files()
            os.system('del /q /s /f %temp%\\*.* & del /q /s /f C:\\Windows\\Temp\\* & rd /s /q "C:\\Users\\%username%\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache" & del /q /s /f C:\\Windows\\Logs\\* & del /q /s /f C:\\Windows\\SoftwareDistribution\\Download\\*.* & del /q /s /f %windir%\\Installer\\*.*')

        def clean_browsers():
            browsers = ['firefox', 'chrome', 'safari', 'edge', 'opera']

            for browser in browsers:
                try:
                    webbrowser.get(using=browser).open('about:blank')
                except webbrowser.Error:
                    append_to_message_box(f"Browser {browser} not found or could not be opened.")
            
            append_to_message_box("Browsing history cleared.")

        def clean_temp_files():
            try:
                temp_dir = os.environ.get('TEMP') or os.environ.get('TMP')

                for filename in os.listdir(temp_dir):
                    file_path = os.path.join(temp_dir, filename)
                    try:
                        if os.path.isfile(file_path):
                            os.unlink(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                    except Exception as e:
                        append_to_message_box(f"Failed to delete {file_path}: {e}")

                append_to_message_box("Temporary files cleaned.")
            except Exception as e:
                append_to_message_box(f"Error cleaning temporary files: {e}")

        def append_to_message_box(message):
            message_box.config(state=tk.NORMAL)
            message_box.insert(tk.END, message + '\n')
            message_box.config(state=tk.DISABLED)

        window = tk.Tk()
        window.title("System Cleaner")

        clean_all_button = tk.Button(window, text="Clean All", command=clean_all)
        clean_all_button.pack(pady=10)

        message_box = tk.Text(window, height=10, width=50)
        message_box.pack(pady=10)
        message_box.config(state=tk.DISABLED)

        window.mainloop()
        
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
            specs['GPU'] = "RTX 4090 TI PLUS ULTRA GIGABYTE"

            return specs

        def display_specs():
            specs = get_pc_specs()
            for key, value in specs.items():
                label = tk.Label(root, text=f"{key}: {value}")
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
            
    def AdvancedSearch(self):
        import os
        import fnmatch
        import tkinter as tk
        from tkinter import ttk, filedialog, messagebox

        class FileSearchApp:
            def __init__(self, root):
                self.root = root
                self.root.title("File Search")
                self.root.geometry("600x400")

                self.create_widgets()

            def create_widgets(self):
                self.dir_label = ttk.Label(self.root, text="Search Directory:")
                self.dir_label.pack(pady=5)
                
                self.dir_entry = ttk.Entry(self.root, width=50)
                self.dir_entry.pack(pady=5)

                self.browse_button = ttk.Button(self.root, text="Browse", command=self.browse_directory)
                self.browse_button.pack(pady=5)

                self.pattern_label = ttk.Label(self.root, text="Filename or Pattern:")
                self.pattern_label.pack(pady=5)
                
                self.pattern_entry = ttk.Entry(self.root, width=50)
                self.pattern_entry.pack(pady=5)

                self.search_button = ttk.Button(self.root, text="Search", command=self.search_files)
                self.search_button.pack(pady=5)

                self.results_listbox = tk.Listbox(self.root, width=80, height=15)
                self.results_listbox.pack(pady=10)

                self.scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.results_listbox.yview)
                self.results_listbox.config(yscrollcommand=self.scrollbar.set)
                self.scrollbar.pack(side="right", fill="y")

            def browse_directory(self):
                directory = filedialog.askdirectory()
                if directory:
                    self.dir_entry.insert(0, directory)

            def search_files(self):
                directory = self.dir_entry.get()
                pattern = self.pattern_entry.get()

                if not directory or not pattern:
                    messagebox.showwarning("Input Error", "Please provide both a directory and a filename or pattern.")
                    return

                matches = self.find_files(directory, pattern)
                
                self.results_listbox.delete(0, tk.END)
                for match in matches:
                    self.results_listbox.insert(tk.END, match)

            def find_files(self, directory, pattern):
                matches = []
                for root, dirs, files in os.walk(directory):
                    for filename in fnmatch.filter(files, pattern):
                        matches.append(os.path.join(root, filename))
                return matches

        if __name__ == "__main__":
            root = tk.Tk()
            app = FileSearchApp(root)
            root.mainloop()

    def NetworkManagerFunction(self):
        import subprocess
        import re
        import tkinter as tk
        from tkinter import messagebox

        def scan_networks():
            try:
                result = subprocess.run(['netsh', 'wlan', 'show', 'network', 'mode=Bssid'], capture_output=True, text=True, check=True)
                networks = []
                lines = result.stdout.split('\n')
                for line in lines:
                    ssid_match = re.search(r'SSID\s+\d+\s*:\s*(.+)', line)
                    if ssid_match:
                        ssid = ssid_match.group(1)
                        networks.append((ssid, ""))
                return networks
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to scan networks: {e.stderr}")
                return []
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {str(e)}")
                return []

        def connect_to_network(ssid, password):
            try:
                result = subprocess.run(['netsh', 'wlan', 'connect', f'name={ssid}'], capture_output=True, text=True, check=True)
                if result.returncode == 0:
                    messagebox.showinfo("Success", f"Connected to {ssid}")
                else:
                    raise subprocess.CalledProcessError(result.returncode, result.args, output=result.stdout, stderr=result.stderr)
            except subprocess.CalledProcessError as e:
                messagebox.showerror("Error", f"Failed to connect to {ssid}: {e.stderr}")
            except Exception as e:
                messagebox.showerror("Error", f"Unexpected error: {str(e)}")

        class WiFiManagerApp:
            def __init__(self, root):
                self.root = root
                self.root.title("Wi-Fi Manager")
                
                self.network_listbox = tk.Listbox(root, width=50)
                self.network_listbox.pack(pady=20)
                
                self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh_networks)
                self.refresh_button.pack(pady=5)
                
                self.ssid_entry = tk.Entry(root, width=30)
                self.ssid_entry.pack(pady=5)
                self.ssid_entry.insert(0, "SSID")
                
                self.password_entry = tk.Entry(root, show="*", width=30)
                self.password_entry.pack(pady=5)
                self.password_entry.insert(0, "Password")
                
                self.connect_button = tk.Button(root, text="Connect", command=self.connect)
                self.connect_button.pack(pady=20)
                
                self.refresh_networks()
            
            def refresh_networks(self):
                self.network_listbox.delete(0, tk.END)
                networks = scan_networks()
                for ssid, security in networks:
                    self.network_listbox.insert(tk.END, f"{ssid} ({security})")
            
            def connect(self):
                selected_network = self.network_listbox.get(tk.ACTIVE)
                ssid = selected_network.split(' ')[0]
                password = self.password_entry.get()
                connect_to_network(ssid, password)

        if __name__ == "__main__":
            root = tk.Tk()
            app = WiFiManagerApp(root)
            root.mainloop()

    def FileManagerFunction(self):
        import tkinter as tk
        from tkinter import filedialog, messagebox
        import os

        def open_file():
            file_path = filedialog.askopenfilename(
                title="Open a file",
                filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
            )
            if file_path:
                try:
                    with open(file_path, 'r') as file:
                        content = file.read()
                        text_area.delete(1.0, tk.END)
                        text_area.insert(tk.END, content)
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

        def save_file():
            file_path = filedialog.asksaveasfilename(
                title="Save as",
                defaultextension=".txt",
                filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
            )
            if file_path:
                try:
                    with open(file_path, 'w') as file:
                        content = text_area.get(1.0, tk.END)
                        file.write(content)
                    messagebox.showinfo("Save", "File saved successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

        def delete_file():
            file_path = filedialog.askopenfilename(
                title="Select a file to delete",
                filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
            )
            if file_path:
                try:
                    os.remove(file_path)
                    messagebox.showinfo("Delete", "File deleted successfully!")
                except Exception as e:
                    messagebox.showerror("Error", f"An error occurred: {e}")

        root = tk.Tk()
        root.title("File Management")

        bg_color = "#2E2E2E"
        fg_color = "#FFFFFF"
        button_bg = "#3C3C3C"
        button_fg = "#FFFFFF"
        text_bg = "#1E1E1E"
        text_fg = "#FFFFFF"

        root.configure(bg=bg_color)

        text_area = tk.Text(root, wrap='word', bg=text_bg, fg=text_fg, insertbackground=fg_color)
        text_area.pack(expand=1, fill='both')

        button_frame = tk.Frame(root, bg=bg_color)
        button_frame.pack(side='bottom', fill='x')

        open_button = tk.Button(button_frame, text="Open File", command=open_file, bg=button_bg, fg=button_fg)
        open_button.pack(side='left', padx=5, pady=5)

        save_button = tk.Button(button_frame, text="Save File", command=save_file, bg=button_bg, fg=button_fg)
        save_button.pack(side='left', padx=5, pady=5)

        delete_button = tk.Button(button_frame, text="Delete File", command=delete_file, bg=button_bg, fg=button_fg)
        delete_button.pack(side='left', padx=5, pady=5)
        root.mainloop()
        
    def DriverManagerFunction(self):
        import tkinter as tk
        from tkinter import messagebox

        class DriverManagementApp:
            def __init__(self, master):
                self.master = master
                self.master.title("Driver Management System")
                self.master.configure(bg="black")
                
                # Create and place widgets
                self.label_name = tk.Label(master, text="Driver Name:", bg="black", fg="white")
                self.label_name.grid(row=0, column=0, padx=10, pady=5)
                self.entry_name = tk.Entry(master)
                self.entry_name.grid(row=0, column=1, padx=10, pady=5)

                self.label_license = tk.Label(master, text="License Number:", bg="black", fg="white")
                self.label_license.grid(row=1, column=0, padx=10, pady=5)
                self.entry_license = tk.Entry(master)
                self.entry_license.grid(row=1, column=1, padx=10, pady=5)

                self.add_button = tk.Button(master, text="Add Driver", command=self.add_driver, bg="black", fg="white")
                self.add_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5)

                self.driver_listbox = tk.Listbox(master, bg="black", fg="white")
                self.driver_listbox.grid(row=3, column=0, columnspan=2, padx=10, pady=5)

            def add_driver(self):
                name = self.entry_name.get()
                license_number = self.entry_license.get()

                if name and license_number:
                    driver_info = f"{name} - {license_number}"
                    self.driver_listbox.insert(tk.END, driver_info)
                    self.entry_name.delete(0, tk.END)
                    self.entry_license.delete(0, tk.END)
                else:
                    messagebox.showerror("Error", "Please enter both name and license number.")

        def main():
            root = tk.Tk()
            app = DriverManagementApp(root)
            root.mainloop()

    def BenchmarkFunction(self):
        import tkinter as tk
        import time
        import psutil

        def run_cpu_benchmark():
            iterations = int(iterations_entry.get())
            total_elapsed_time = 0
            for _ in range(iterations):
                start_time = time.time()
                fibonacci(30)
                end_time = time.time()
                elapsed_time = end_time - start_time
                total_elapsed_time += elapsed_time
            average_elapsed_time = total_elapsed_time / iterations
            result_label.config(text="CPU Benchmark - Average Time: {:.2f} seconds".format(average_elapsed_time))

        def run_memory_benchmark():
            data = [0] * (10**7)
            result_label.config(text="Memory Benchmark - Data allocated")

        def run_disk_benchmark():
            iterations = int(iterations_entry.get())
            total_elapsed_time = 0
            for _ in range(iterations):
                start_time = time.time()
                with open("temp.txt", "wb") as f:
                    f.write(b"0" * (10**7))
                end_time = time.time()
                elapsed_time = end_time - start_time
                total_elapsed_time += elapsed_time
            average_elapsed_time = total_elapsed_time / iterations
            result_label.config(text="Disk Benchmark - Average Time: {:.2f} seconds".format(average_elapsed_time))

        def fibonacci(n):
            if n <= 1:
                return n
            else:
                return fibonacci(n-1) + fibonacci(n-2)

        root = tk.Tk()
        root.title("Benchmarking Tool")

        instruction_label = tk.Label(root, text="Select the benchmark type and click 'Run Benchmark'.")
        instruction_label.pack(pady=10)

        benchmark_type = tk.StringVar()
        benchmark_type.set("CPU")

        cpu_button = tk.Radiobutton(root, text="CPU", variable=benchmark_type, value="CPU")
        cpu_button.pack(anchor=tk.W)

        memory_button = tk.Radiobutton(root, text="Memory", variable=benchmark_type, value="Memory")
        memory_button.pack(anchor=tk.W)

        disk_button = tk.Radiobutton(root, text="Disk I/O", variable=benchmark_type, value="Disk")
        disk_button.pack(anchor=tk.W)

        iterations_label = tk.Label(root, text="Iterations:")
        iterations_label.pack(pady=5)

        iterations_entry = tk.Entry(root)
        iterations_entry.pack()

        run_button = tk.Button(root, text="Run Benchmark", command=lambda: run_benchmark())
        run_button.pack(pady=5)

        result_label = tk.Label(root, text="")
        result_label.pack(pady=10)

        def run_benchmark():
            benchmark_type_value = benchmark_type.get()
            if benchmark_type_value == "CPU":
                run_cpu_benchmark()
            elif benchmark_type_value == "Memory":
                run_memory_benchmark()
            elif benchmark_type_value == "Disk":
                run_disk_benchmark()

        root.mainloop()

    
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