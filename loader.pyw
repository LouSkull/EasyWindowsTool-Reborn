import os
import sys
import webbrowser
import customtkinter as ctk
from plyer import notification
from tkinter import StringVar
from appdata.settings import config

config_file_path = 'appdata/settings/config.py'
data_file_path = 'appdata/data.txt'

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("EWTLoader 2.3")
        self.geometry("275x300")
        self.resizable(False, False)

        self.create_tabs()
        self.show_main_tab()

        self.user = self.load_user()
        
        if self.user:
            with open(data_file_path) as f:
                for line in f:
                    line = line.strip()
                    if line == 'EWT-2-3-rework-build-0.2':
                        self.show_notification(f"Info: {line}")
                    else:
                        self.show_notification(f"Hello, {line}")

        else:
            self.user = self.register_user()
            self.show_notification(f"Thank you for registering, {self.user}!")

        if not config.LOADER_CONFIG:
            self.ewt_script()
        elif config.FIRST_TIME:
            webbrowser.open("https://github.com/LouSkull/EasyWindowsTool-Reborn")
            self.update_first_time(False)

    def create_tabs(self):
        self.tab_buttons_frame = ctk.CTkFrame(self)
        self.tab_buttons_frame.pack(side="top", fill="x")

        self.button_main_tab = ctk.CTkButton(self.tab_buttons_frame, text="Main", command=self.show_main_tab)
        self.button_main_tab.pack(side="left")

        self.button_settings_tab = ctk.CTkButton(self.tab_buttons_frame, text="Settings", command=self.show_settings_tab)
        self.button_settings_tab.pack(side="left")

        self.main_tab = ctk.CTkFrame(self)
        self.settings_tab = ctk.CTkFrame(self)

        self.create_main_tab()
        self.create_settings_tab()

    def create_main_tab(self):
        self.label_main = ctk.CTkLabel(self.main_tab, text="Main Menu")
        self.label_main.pack(pady=10)

        self.button_start_ewt = ctk.CTkButton(self.main_tab, text="Start EWT", command=self.ewt_script)
        self.button_start_ewt.pack(pady=5)

        self.button_start_ewt_fixer = ctk.CTkButton(self.main_tab, text="Start EWT-FIXER", command=self.ewt_fixer_script)
        self.button_start_ewt_fixer.pack(pady=5)

    def create_settings_tab(self):
        self.label_settings = ctk.CTkLabel(self.settings_tab, text="Settings")
        self.label_settings.pack(pady=10)
        
        self.button_change_username = ctk.CTkButton(self.settings_tab, text="Add Username", command=self.add_username)
        self.button_change_username.pack(pady=5)

        self.button_disable_loader = ctk.CTkButton(self.settings_tab, text="Disable Loader", command=self.disable_loader)
        self.button_disable_loader.pack(pady=5)

        self.button_enable_logs = ctk.CTkButton(self.settings_tab, text="Enable Logs", command=self.enable_logs)
        self.button_enable_logs.pack(pady=5)

        self.button_disable_logs = ctk.CTkButton(self.settings_tab, text="Disable Logs", command=self.disable_logs)
        self.button_disable_logs.pack(pady=5)

    def show_main_tab(self):
        self.settings_tab.pack_forget()
        self.main_tab.pack(expand=1, fill="both")

    def show_settings_tab(self):
        self.main_tab.pack_forget()
        self.settings_tab.pack(expand=1, fill="both")

    def update_first_time(self, value):
        self.update_config_setting('FIRST_TIME', value)

    def update_loader_config(self, value):
        self.update_config_setting('LOADER_CONFIG', value)

    def update_config_setting(self, setting, value):
        with open(config_file_path, 'r') as file:
            lines = file.readlines()

        new_value = 'True' if value else 'False'

        for i, line in enumerate(lines):
            if line.strip().startswith(setting):
                parts = line.split('=')
                lines[i] = f"{parts[0].strip()} = {new_value}\n"
                break

        with open(config_file_path, 'w') as file:
            file.writelines(lines)

    def ewt_script(self):
        os.system("start start.bat")
        sys.exit(1)

    def ewt_fixer_script(self):
        os.system("EWT_FIX.py")
        sys.exit(1)

    def register_user(self):
        return self.show_input_dialog("Register", "Enter your username:")

    def load_user(self):
        if os.path.exists(data_file_path):
            with open(data_file_path, 'r') as file:
                return file.readline().strip()
        return None

    def add_username(self):
        new_username = self.show_input_dialog("Add Username", "Enter your username:")
        if new_username:
            with open(data_file_path, 'w') as file:
                file.write(new_username)
            self.show_notification("Username added successfully.")

    def disable_loader(self):
        self.update_loader_config(False)
        self.show_notification("Loader disabled. You can enable it in 'config.py' file.")
        self.quit()

    def enable_logs(self):
        self.update_config_setting('EWT_LOGS', True)
        self.show_notification("EWT_LOGS enabled.")

    def disable_logs(self):
        self.update_config_setting('EWT_LOGS', False)
        self.show_notification("EWT_LOGS disabled.")

    def show_notification(self, message):
        notification.notify(
            title="EWT",
            message=message,
            timeout=3
        )

    def show_input_dialog(self, title, prompt):
        dialog = ctk.CTkToplevel(self)
        dialog.title(title)
        dialog.geometry("300x200")

        label = ctk.CTkLabel(dialog, text=prompt)
        label.pack(pady=10)

        user_input = StringVar()
        entry = ctk.CTkEntry(dialog, textvariable=user_input)
        entry.pack(pady=5)
        entry.config(state='disabled')

        def on_submit():
            dialog.user_input = user_input.get()
            with open(data_file_path, 'w') as file:
                file.write(dialog.user_input)
            dialog.destroy()

        submit_button = ctk.CTkButton(dialog, text="Submit", command=on_submit)
        submit_button.pack(pady=10)

        self.wait_window(dialog)
        return getattr(dialog, 'user_input', None)

if __name__ == "__main__":
    app = App()
    app.mainloop()
