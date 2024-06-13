import customtkinter
import tkinter
import threading
import time, ctypes
from appdata.settings import config
import os
import winreg
import subprocess
import shutil
import webbrowser
import tkinter.messagebox as tkmb
import psutil
import platform
import GPUtil
from datetime import datetime

# Function to initialize logs if needed
def initialize_logs():
    if config.EWT_LOGS:
        ctypes.windll.kernel32.SetConsoleTextAttribute(ctypes.windll.kernel32.GetStdHandle(-11), 3)
        ctypes.windll.kernel32.SetConsoleTitleW("EWT-LOG")
        ctypes.windll.kernel32.SetConsoleScreenBufferSize(
            ctypes.windll.kernel32.GetStdHandle(-11), ctypes.wintypes._COORD(75, 35)
        )

        print("Welcome to EasyWindowsTool!")
        print("Thank you for choosing our tool :)")
        print()
        print("Below are the EasyWindowsTool logs,")
        print("where you can track any issues.")
    else:
        pass

# Initialize logs in a separate thread
log_thread = threading.Thread(target=initialize_logs)
log_thread.start()

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x700")
        self.title("github.com/LouSkull")
        self.iconbitmap("icon\\new.ico")
        self.resizable(False, False)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(12, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(
            self.navigation_frame, text="EWT", compound="left", font=customtkinter.CTkFont(size=20, weight="bold")
        )
        self.navigation_frame_label.grid(row=0, column=0, padx=20, pady=20)

        # Navigation buttons
        self.frame_5_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Welcome",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("frame_5")
        )
        self.frame_5_button.grid(row=5, column=0, sticky="ew")

        self.frame_6_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Autoruns",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("frame_6")
        )
        self.frame_6_button.grid(row=6, column=0, sticky="ew")

        self.frame_7_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Cleaner",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("frame_7")
        )
        self.frame_7_button.grid(row=7, column=0, sticky="ew")

        self.frame_8_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="Advanced Task Manager",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("frame_8")
        )
        self.frame_8_button.grid(row=8, column=0, sticky="ew")

        self.frame_10_button = customtkinter.CTkButton(
            self.navigation_frame, corner_radius=0, height=40, border_spacing=10, text="System Info",
            fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
            anchor="w", command=lambda: self.select_frame_by_name("frame_10")
        )
        self.frame_10_button.grid(row=10, column=0, sticky="ew")

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(
            self.navigation_frame, values=["Dark", "Light"], command=self.change_appearance_mode_event
        )
        self.appearance_mode_menu.grid(row=12, column=0, padx=20, pady=20, sticky="s")

        self.five_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.six_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seven_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.eight_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.ten_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        self.select_frame_by_name("frame_5")

        welcome_label = """
- EasyWindowsTool is intended for use only on the Windows operating system.
- The application does not always help your computer.
- Before using EasyWindowsTool, make sure you have read the software license and agreement.
- We do not vouch for your computer.
        """
        self.text_label = customtkinter.CTkLabel(self.five_frame, text=welcome_label, font=('Helvetica bold', 20))
        self.text_label.pack(pady=20)

        # Autoruns frame setup
        self.autoruns_listbox = tkinter.Listbox(self.six_frame, bg="gray", fg="white")
        self.autoruns_listbox.pack(padx=10, pady=10, expand=True, fill=tkinter.BOTH)
        self.autoruns_listbox.bind("<Button-3>", self.show_context_menu)

        self.context_menu = tkinter.Menu(self.six_frame, tearoff=0)
        self.context_menu.add_command(label="Open Path", command=self.open_path)

        # Populate autoruns list in a separate thread
        threading.Thread(target=self.populate_autoruns_list).start()

        self.autoruns_info_label = customtkinter.CTkLabel(self.six_frame, text="Right-click to open the path of the selected autorun item.", font=('Helvetica', 12))
        self.autoruns_info_label.pack(pady=10)

        # Cleaner frame setup
        self.clean_all_button = customtkinter.CTkButton(self.seven_frame, text="Clean All", command=self.clean_all)
        self.clean_all_button.pack(pady=10)

        self.message_box = customtkinter.CTkTextbox(self.seven_frame, height=600, width=700, wrap=tkinter.WORD)
        self.message_box.pack(pady=10, padx=10, expand=True, fill=tkinter.BOTH)
        self.message_box.configure(state=customtkinter.DISABLED)
        
        self.cleaner_info_label = customtkinter.CTkLabel(self.seven_frame, text="Click 'Clean All' to clean browsers, temp files, logs, downloads, and installer files.", font=('Helvetica', 12))
        self.cleaner_info_label.pack(pady=10)

        # Advanced Task Manager frame setup
        self.setup_task_manager_frame()

        # System Info frame setup
        self.setup_system_info_frame()

    def setup_task_manager_frame(self):
        self.task_manager_search_entry = customtkinter.CTkEntry(self.eight_frame, placeholder_text="Search", width=600, height=35)
        self.task_manager_search_entry.pack(pady=10)
        self.task_manager_search_entry.bind("<KeyRelease>", self.update_task_list)

        self.task_manager_listbox = tkinter.Listbox(self.eight_frame, selectmode=tkinter.SINGLE, bg='gray', fg='white', font=("Helvetica", 14))
        self.task_manager_listbox.pack(padx=10, pady=10, expand=True, fill=tkinter.BOTH)

        self.task_manager_button_frame = customtkinter.CTkFrame(self.eight_frame)
        self.task_manager_button_frame.pack(pady=10)

        self.terminate_button = customtkinter.CTkButton(self.task_manager_button_frame, text="Terminate", command=self.terminate_task, width=100, height=35)
        self.terminate_button.pack(side=tkinter.LEFT, padx=5)

        self.refresh_button = customtkinter.CTkButton(self.task_manager_button_frame, text="Refresh", command=self.update_task_list, width=100, height=35)
        self.refresh_button.pack(side=tkinter.LEFT, padx=5)

        self.sort_var = tkinter.StringVar(value="name")
        self.sort_options = ["name", "pid", "cpu", "memory"]
        self.sort_menu = customtkinter.CTkOptionMenu(self.task_manager_button_frame, variable=self.sort_var, values=self.sort_options, command=self.update_task_list)
        self.sort_menu.pack(side=tkinter.LEFT, padx=5)

        self.update_task_list()
        
        self.task_manager_info_label = customtkinter.CTkLabel(self.eight_frame, text="Search and terminate tasks. Sort by name, PID, CPU, or memory usage.", font=('Helvetica', 12))
        self.task_manager_info_label.pack(pady=10)

    def setup_system_info_frame(self):
        self.system_info_label = customtkinter.CTkLabel(self.ten_frame, text="PC Specifications", font=("Arial", 24))
        self.system_info_label.pack(pady=20)

        self.system_info_frame = customtkinter.CTkFrame(self.ten_frame)
        self.system_info_frame.pack(pady=10, padx=10, fill="both", expand=True)

        self.system_info_text = customtkinter.CTkTextbox(self.system_info_frame, wrap="word", font=("Arial", 12))
        self.system_info_text.pack(pady=10, padx=10, expand=True, fill="both")
        
        self.system_info_footer = customtkinter.CTkLabel(self.ten_frame, text="System information and disk usage details.", font=('Helvetica', 12))
        self.system_info_footer.pack(pady=10)

        # Display system info in a separate thread
        threading.Thread(target=self.display_system_info).start()

    def select_frame_by_name(self, name):
        self.frame_5_button.configure(fg_color=("gray75", "gray25") if name == "frame_5" else "transparent")
        self.frame_6_button.configure(fg_color=("gray75", "gray25") if name == "frame_6" else "transparent")
        self.frame_7_button.configure(fg_color=("gray75", "gray25") if name == "frame_7" else "transparent")
        self.frame_8_button.configure(fg_color=("gray75", "gray25") if name == "frame_8" else "transparent")
        self.frame_10_button.configure(fg_color=("gray75", "gray25") if name == "frame_10" else "transparent")

        if name == "frame_5":
            self.five_frame.grid(row=0, column=1, sticky="nsew")
            self.six_frame.grid_forget()
            self.seven_frame.grid_forget()
            self.eight_frame.grid_forget()
            self.ten_frame.grid_forget()
        elif name == "frame_6":
            self.six_frame.grid(row=0, column=1, sticky="nsew")
            self.five_frame.grid_forget()
            self.seven_frame.grid_forget()
            self.eight_frame.grid_forget()
            self.ten_frame.grid_forget()
        elif name == "frame_7":
            self.seven_frame.grid(row=0, column=1, sticky="nsew")
            self.five_frame.grid_forget()
            self.six_frame.grid_forget()
            self.eight_frame.grid_forget()
            self.ten_frame.grid_forget()
        elif name == "frame_8":
            self.eight_frame.grid(row=0, column=1, sticky="nsew")
            self.five_frame.grid_forget()
            self.six_frame.grid_forget()
            self.seven_frame.grid_forget()
            self.ten_frame.grid_forget()
        elif name == "frame_10":
            self.ten_frame.grid(row=0, column=1, sticky="nsew")
            self.five_frame.grid_forget()
            self.six_frame.grid_forget()
            self.seven_frame.grid_forget()
            self.eight_frame.grid_forget()

    def get_autostart_programs(self):
        autostart_programs = []

        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
            i = 0
            while True:
                try:
                    name, value, _ = winreg.EnumValue(key, i)
                    autostart_programs.append((name, value))
                    i += 1
                except OSError:
                    break
        except FileNotFoundError:
            pass

        return autostart_programs

    def populate_autoruns_list(self):
        autostart_programs = self.get_autostart_programs()
        for program in autostart_programs:
            self.autoruns_listbox.insert(tkinter.END, f"{program[0]}: {program[1]}")

    def show_context_menu(self, event):
        try:
            self.autoruns_listbox.selection_clear(0, tkinter.END)
            self.autoruns_listbox.selection_set(self.autoruns_listbox.nearest(event.y))
            self.context_menu.post(event.x_root, event.y_root)
        finally:
            self.context_menu.grab_release()

    def open_path(self):
        selection = self.autoruns_listbox.curselection()
        if selection:
            program = self.autoruns_listbox.get(selection[0])
            path = program.split(": ", 1)[1]
            folder = os.path.dirname(path)
            subprocess.Popen(f'explorer "{folder}"')

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)

    # Cleaner functions
    def clean_all(self):
        threading.Thread(target=self.clean_browsers).start()
        threading.Thread(target=self.clean_temp_files).start()
        threading.Thread(target=self.clean_logs).start()
        threading.Thread(target=self.clean_downloads).start()
        threading.Thread(target=self.clean_installer_files).start()
        tkmb.showinfo(title="System Cleaner", message="All cleaning tasks completed.")

    def clean_browsers(self):
        browsers = ['firefox', 'chrome', 'safari', 'edge', 'opera']
        for browser in browsers:
            try:
                webbrowser.get(using=browser).open('about:blank')
            except webbrowser.Error:
                self.append_to_message_box(f"Browser {browser} not found or could not be opened.")
        self.append_to_message_box("Browsing history cleared.")

    def clean_temp_files(self):
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
                    self.append_to_message_box(f"Failed to delete {file_path}: {e}")
            self.append_to_message_box("Temporary files cleaned.")
        except Exception as e:
            self.append_to_message_box(f"Error cleaning temporary files: {e}")

    def clean_logs(self):
        try:
            logs_path = os.path.join(os.environ.get('windir', 'C:\\Windows'), 'Logs')
            for filename in os.listdir(logs_path):
                file_path = os.path.join(logs_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    self.append_to_message_box(f"Failed to delete log {file_path}: {e}")
            self.append_to_message_box("Log files cleaned.")
        except Exception as e:
            self.append_to_message_box(f"Error cleaning log files: {e}")

    def clean_downloads(self):
        try:
            downloads_path = os.path.join(os.environ.get('windir', 'C:\\Windows'), 'SoftwareDistribution', 'Download')
            for filename in os.listdir(downloads_path):
                file_path = os.path.join(downloads_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    self.append_to_message_box(f"Failed to delete download {file_path}: {e}")
            self.append_to_message_box("Download files cleaned.")
        except Exception as e:
            self.append_to_message_box(f"Error cleaning download files: {e}")

    def clean_installer_files(self):
        try:
            installer_path = os.path.join(os.environ.get('windir', 'C:\\Windows'), 'Installer')
            for filename in os.listdir(installer_path):
                file_path = os.path.join(installer_path, filename)
                try:
                    if os.path.isfile(file_path):
                        os.unlink(file_path)
                except Exception as e:
                    self.append_to_message_box(f"Failed to delete installer {file_path}: {e}")
            self.append_to_message_box("Installer files cleaned.")
        except Exception as e:
            self.append_to_message_box(f"Error cleaning installer files: {e}")

    def append_to_message_box(self, message):
        self.message_box.configure(state=customtkinter.NORMAL)
        self.message_box.insert(customtkinter.END, message + '\n')
        self.message_box.configure(state=customtkinter.DISABLED)

    # Task Manager functions
    def update_task_list(self, event=None):
        search_query = self.task_manager_search_entry.get().lower()
        sort_by = self.sort_var.get()
        
        self.task_manager_listbox.delete(0, tkinter.END)
        
        tasks = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            if search_query in proc.info['name'].lower():
                cpu_usage = proc.info['cpu_percent']
                memory_usage = proc.info['memory_info'].rss / (1024 * 1024)
                tasks.append((proc.info['name'], proc.info['pid'], cpu_usage, memory_usage))
        
        if sort_by == "name":
            tasks.sort(key=lambda x: x[0])
        elif sort_by == "pid":
            tasks.sort(key=lambda x: x[1])
        elif sort_by == "cpu":
            tasks.sort(key=lambda x: x[2], reverse=True)
        elif sort_by == "memory":
            tasks.sort(key=lambda x: x[3], reverse=True)
        
        for task in tasks:
            self.task_manager_listbox.insert(tkinter.END, f"{task[0]} (PID: {task[1]}, CPU: {task[2]:.2f}%, Memory: {task[3]:.2f} MB)")

    def terminate_task(self):
        selected_task = self.task_manager_listbox.get(tkinter.ACTIVE)
        if selected_task:
            pid = int(selected_task.split("PID: ")[1].split(",")[0].strip())
            try:
                proc = psutil.Process(pid)
                proc.terminate()
                self.update_task_list()
            except psutil.NoSuchProcess:
                tkinter.messagebox.showerror("Error", "No such process found.")
            except psutil.AccessDenied:
                tkinter.messagebox.showerror("Error", "Permission denied.")
            except Exception as e:
                tkinter.messagebox.showerror("Error", str(e))

    # System Info functions
    def display_system_info(self):
        info = f"System: {platform.system()}\n"
        info += f"Node Name: {platform.node()}\n"
        info += f"Release: {platform.release()}\n"
        info += f"Version: {platform.version()}\n"
        info += f"Machine: {platform.machine()}\n"
        info += f"Processor: {platform.processor()}\n"
        info += f"RAM: {round(psutil.virtual_memory().total / (1024.0 **3))} GB\n"

        cpu_freq = psutil.cpu_freq()
        info += f"CPU Frequency: {cpu_freq.current:.2f} MHz\n"
        info += f"CPU Cores: {psutil.cpu_count(logical=False)}\n"
        info += f"Logical CPUs: {psutil.cpu_count(logical=True)}\n"

        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            info += f"GPU: {gpu.name}\n"
            info += f"GPU Memory Total: {gpu.memoryTotal} MB\n"
            info += f"GPU Memory Free: {gpu.memoryFree} MB\n"
            info += f"GPU Memory Used: {gpu.memoryUsed} MB\n"
            info += f"GPU Temperature: {gpu.temperature} °C\n"

        battery = psutil.sensors_battery()
        if battery:
            info += f"Battery: {battery.percent}%\n"
            info += f"Power Plugged In: {'Yes' if battery.power_plugged else 'No'}\n"

        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        info += f"Boot Time: {bt.strftime('%Y-%m-%d %H:%M:%S')}\n"

        self.system_info_text.insert("1.0", info)

        self.update_disk_usage()

    def update_disk_usage(self):
        total, used, free = self.get_disk_usage()
        disk_info = f"\nDisk Usage:\n"
        disk_info += f"Total space: {total / (1024**3):.2f} GB\n"
        disk_info += f"Used space: {used / (1024**3):.2f} GB\n"
        disk_info += f"Free space: {free / (1024**3):.2f} GB\n"
        self.system_info_text.insert(tkinter.END, disk_info)

    def get_disk_usage(self):
        disk_usage = psutil.disk_usage('/')
        total_space = disk_usage.total
        used_space = disk_usage.used
        free_space = disk_usage.free
        return total_space, used_space, free_space

if __name__ == "__main__":
    app = App()
    app.mainloop()
