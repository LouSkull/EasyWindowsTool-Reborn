# END-USER LICENSE AGREEMENT (EULA) FOR EWT

# PLEASE READ THIS END-USER LICENSE AGREEMENT ("EULA") CAREFULLY BEFORE USING THE SOFTWARE. THIS EULA IS A LEGAL AGREEMENT BETWEEN YOU (EITHER AN INDIVIDUAL OR A SINGLE ENTITY) AND [Vladimir] ("DEVELOPER") FOR THE SOFTWARE PRODUCT IDENTIFIED ABOVE, WHICH INCLUDES COMPUTER SOFTWARE AND MAY INCLUDE ASSOCIATED MEDIA, PRINTED MATERIALS, AND "ONLINE" OR ELECTRONIC DOCUMENTATION ("SOFTWARE"). BY DOWNLOADING, INSTALLING, COPYING, OR OTHERWISE USING THE SOFTWARE, YOU AGREE TO BE BOUND BY THE TERMS OF THIS EULA. IF YOU DO NOT AGREE TO THE TERMS OF THIS EULA, DO NOT INSTALL OR USE THE SOFTWARE.

# 1. GRANT OF LICENSE. Developer grants you a non-exclusive, non-transferable, limited license to use the Software solely for your personal or internal business purposes on a single computer or device at a time, unless otherwise specified in writing by Developer.

# 2. RESTRICTIONS. You may not: (a) modify, translate, reverse engineer, decompile, disassemble, or create derivative works based on the Software; (b) sell, sublicense, rent, lease, lend, or otherwise transfer the Software to any third party; (c) remove or alter any proprietary notices or labels on the Software; (d) use the Software in any unlawful manner, for any unlawful purpose, or in any manner inconsistent with this EULA.

# 3. SUPPORT AND MAINTENANCE. Developer is under no obligation to provide support, maintenance, updates, or upgrades for the Software under this EULA, unless otherwise agreed in writing.

# 4. INTELLECTUAL PROPERTY RIGHTS. The Software and any copies thereof are the intellectual property of Developer and are protected by copyright and other intellectual property laws and treaties. Developer reserves all rights not expressly granted to you in this EULA.

# 5. DISCLAIMER OF WARRANTIES. THE SOFTWARE IS PROVIDED "AS IS" WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, OR NON-INFRINGEMENT. THE ENTIRE RISK ARISING OUT OF THE USE OR PERFORMANCE OF THE SOFTWARE REMAINS WITH YOU.

# 6. LIMITATION OF LIABILITY. IN NO EVENT SHALL DEVELOPER BE LIABLE FOR ANY DAMAGES WHATSOEVER (INCLUDING, WITHOUT LIMITATION, DAMAGES FOR LOSS OF BUSINESS PROFITS, BUSINESS INTERRUPTION, LOSS OF BUSINESS INFORMATION, OR ANY OTHER PECUNIARY LOSS) ARISING OUT OF THE USE OF OR INABILITY TO USE THE SOFTWARE, EVEN IF DEVELOPER HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGES. IN NO EVENT SHALL DEVELOPER'S TOTAL LIABILITY TO YOU FOR ALL DAMAGES EXCEED THE AMOUNT PAID BY YOU FOR THE SOFTWARE.

# 7. GOVERNING LAW. This EULA shall be governed by and construed in accordance with the laws of [Your Country], without regard to its conflicts of law provisions.

# 8. ENTIRE AGREEMENT. This EULA constitutes the entire agreement between you and Developer regarding the subject matter hereof and supersedes all prior or contemporaneous agreements, understandings, and communications, whether written or oral, relating to such subject matter.

# By installing or using the Software, you acknowledge that you have read this EULA, understand it, and agree to be bound by its terms and conditions.

# If you have any questions regarding this EULA, you may contact Developer at [discord: ggrolton123].

import customtkinter
from customtkinter import *
import tkinter
import subprocess
from plyer import notification
import os
from PIL import Image
import webbrowser
import shutil
import tkinter as tk
from tkinter import messagebox
import pyautogui
import cv2
import numpy as np
import threading

fg_color_config_main = "transparent"

os.system("color 3")
os.system("title EWT-LOG")
os.system("mode 75,35")
print("Welcome to EasyWindowsTool!")
print("Thank you for choosing our tool :)")
print()
print("Below are the EasyWindowsTool logs,")
print("where you can track any issues.")

class App(customtkinter.CTk):
    def __init__(self):

        super().__init__()

        self.title("")
        self.geometry("1200x700")
        self.title("github.com/LouSkull")
        self.resizable(False, False)
        self.iconbitmap("icon\\new.ico")
        
        # self.attributes('-toolwindow', True)

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.navigation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(8, weight=1)

        self.navigation_frame_label = customtkinter.CTkLabel(self.navigation_frame, text="EWT 2.2",
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

        self.appearance_mode_menu = customtkinter.CTkOptionMenu(self.navigation_frame, values = ["System",  "Dark", "Light"],
                                                                command=self.change_appearance_mode_event)
        self.appearance_mode_menu.grid(row=9, column=0, padx=20, pady=20, sticky="s")

        self.five_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.six_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.seven_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")

        # self.ad_frame = customtkinter.CTkFrame(self, fg_color="#242424", corner_radius=10)
        # self.ad_frame.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)t

        # self.ad_text = customtkinter.CTkLabel(
        #     self.ad_frame,
        #     text="TEST",
        #     font=("Roboto", 16, "bold"),
        #     text_color="white",
        # )
        # self.ad_text.pack(side="left", padx=10)

        # self.ad_button = customtkinter.CTkButton(
        #     self.ad_frame,
        #     text="TEST",
        #     fg_color="#2874FF",
        #     hover_color=("gray70", "gray30"),
        #     corner_radius=10,
        #     font=("Roboto", 12),
        #     command=self.test
        # )
        # self.ad_button.pack(side="right", padx=10)

        readme = """
- EasyWindowsTool is intended for use only on the Windows operating system.
- The application does not always help your computer.
- Before using EasyWindowsTool, make sure you have read the software license and agreement.
- We do not vouch for your computer.
        """
        self.text_label = customtkinter.CTkLabel(self.five_frame, text=readme, font=('Helvetica bold', 20))
        self.text_label.pack()
        self.select_frame_by_name("frame_5")

        # widgets
        self.task_mgr_button_text = customtkinter.CTkLabel(self.six_frame, text="~ TaskMGR Manager ~", font=("Arial", 20))
        
        self.windef_text = customtkinter.CTkLabel(self.six_frame, text="~ Windows Defender Manager ~", font=("Arial", 20))
        
        self.task_mgr_button_enable = customtkinter.CTkButton(self.six_frame, text="Enable TaskMgr", corner_radius=4, font=('Helvetica bold', 18), command=self.EnableTaskMgr)
        
        self.task_mgr_button_disable = customtkinter.CTkButton(self.six_frame, text="Disable TaskMgr",corner_radius=4, font=('Helvetica bold', 18),command=self.DisableTaskMgr)
        
        self.windef_button_enable = customtkinter.CTkButton(self.six_frame, text="Enable WinDef", corner_radius=4, font=('Helvetica bold', 18), command=self.EnableWindef)
        
        self.windef_button_disable = customtkinter.CTkButton(self.six_frame, text="Disable WinDef", corner_radius=4, font=('Helvetica bold', 18), command=self.DisableWindef)



        # Power Controller
        self.powercontroller_text = customtkinter.CTkLabel(self.six_frame, text="~ Power Controller ~", font=("Arial", 20))
        self.power_off_button = customtkinter.CTkButton(self.six_frame, text="Shutdown", corner_radius=4, font=('Helvetica bold', 18), command=self.shutdownPC)
        self.power_restart_button = customtkinter.CTkButton(self.six_frame, text="Restart", corner_radius=4, font=('Helvetica bold', 18), command=self.restartPC)
        self.power_logout_button = customtkinter.CTkButton(self.six_frame, text="Logout", corner_radius=4, font=('Helvetica bold', 18), command=self.UserLogoutPC)

        self.powercontroller_text.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.power_off_button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
        self.power_restart_button.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)
        self.power_logout_button.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)

        #other func
        self.other_text = customtkinter.CTkLabel(self.seven_frame, text="~ Other Tools ~", font=("Arial", 20))
        self.autostart_button = customtkinter.CTkButton(self.seven_frame, text="AutoStart List", corner_radius=4, font=('Helvetica bold', 18), command=self.AutoStartListScript)
        self.PCSpecifications_button = customtkinter.CTkButton(self.seven_frame, text="PC Specifications", corner_radius=4, font=('Helvetica bold', 18), command=self.PCSpecifications)
        self.usernit_button = customtkinter.CTkButton(self.seven_frame, text="Reset Usernit", corner_radius=4, font=('Helvetica bold', 18), command=self.UsernitResetScript)
        self.virusscanner_button = customtkinter.CTkButton(self.seven_frame, text="Virus Scanner", corner_radius=4, font=('Helvetica bold', 18), command=self.VirusScanner)
        self.cleaner_button = customtkinter.CTkButton(self.seven_frame, text="Cleanup OS", corner_radius=4, font=('Helvetica bold', 18), command=self.CleanerScript)
        self.advanced_search_button = customtkinter.CTkButton(self.seven_frame, text="File Search", corner_radius=4, font=('Helvetica bold', 18), command=self.AdvancedSearch)
        self.network_manager_button = customtkinter.CTkButton(self.seven_frame, text="Network Manager", corner_radius=4, font=('Helvetica bold', 18), command=self.NetworkManagerFunction)
        self.file_manager_button = customtkinter.CTkButton(self.seven_frame, text="File Manager", corner_radius=4, font=('Helvetica bold', 18), command=self.FileManagerFunction)
        self.driver_manager_button = customtkinter.CTkButton(self.seven_frame, text="Driver Manager", corner_radius=4, font=('Helvetica bold', 18), command=self.DriverManagerFunction)
        self.benchmark_button = customtkinter.CTkButton(self.seven_frame, text="Benchmark", corner_radius=4, font=('Helvetica bold', 18), command=self.BenchmarkFunction)
        self.battery_info_button = customtkinter.CTkButton(self.seven_frame, text="Battery Information", corner_radius=4, font=('Helvetica bold', 18), command=self.BatteryInfoFunction)
        self.screen_recorder_button = customtkinter.CTkButton(self.seven_frame, text="Screen Recorder", corner_radius=4, font=('Helvetica bold', 18), command=self.ScreenRecorder)
        self.webcamera_button = customtkinter.CTkButton(self.seven_frame, text="WebCamera", corner_radius=4, font=('Helvetica bold', 18), command=self.WebCameraFunction)
        self.url_short_button = customtkinter.CTkButton(self.seven_frame, text="UrlShort", corner_radius=4, font=('Helvetica bold', 18), command=self.UrlShort)
        self.archiver_button = customtkinter.CTkButton(self.seven_frame, text="Archive", corner_radius=4, font=('Helvetica bold', 18), command=self.ArchiveFunction)
        self.updater_button = customtkinter.CTkButton(self.seven_frame, text="Updater", corner_radius=4, font=('Helvetica bold', 18), command=self.UpdateFunction)
        self.pw_strength_checker = customtkinter.CTkButton(self.seven_frame, text="Password Checker", corner_radius=4, font=('Helvetica bold', 18), command=self.PasswordStrengthCheckerFunction)
        self.encrypter_button = customtkinter.CTkButton(self.seven_frame, text="Data Encrypter", corner_radius=4, font=('Helvetica bold', 18), command=self.DataEncrypterFunction)
        self.discs_usage_button = customtkinter.CTkButton(self.seven_frame, text="Discs Usage", corner_radius=4, font=('Helvetica bold', 18), command=self.DiscsUsageFunction)
        self.turn_off_cortana_button = customtkinter.CTkButton(self.seven_frame, text="Cortana Control", corner_radius=4, font=('Helvetica bold', 18), command=self.CortanaControlFunction)
        self.restart_explorer_button = customtkinter.CTkButton(self.seven_frame, text="Restart Explorer", corner_radius=4, font=('Helvetica bold', 18), command=self.RestartExplorerFunction)
        self.pinger_button = customtkinter.CTkButton(self.seven_frame, text="Pinger", corner_radius=4, font=('Helvetica bold', 18), command=self.PingerFunction)
        self.clear_copy_history_button = customtkinter.CTkButton(self.seven_frame, text="Clear Clipboard", corner_radius=4, font=('Helvetica bold', 18), command=self.ClearClipboardFunction)
        self.start_expolorer_button = customtkinter.CTkButton(self.seven_frame, text="Start explorer", corner_radius=4, font=('Helvetica bold', 18), command=self.StartExplorerFunction)
        self.blue_screen_button = customtkinter.CTkButton(self.seven_frame, text="Blue Screen", corner_radius=4, font=('Helvetica bold', 18), command=self.BluesScreenFunction)
        self.microphone_booster_button = customtkinter.CTkButton(self.seven_frame, text="Microphone Booster", corner_radius=4, font=('Helvetica bold', 18), command=self.MicroBoostFunction)
        self.auto_clicker_button = customtkinter.CTkButton(self.seven_frame, text="Auto Clicker", corner_radius=4, font=('Helvetica bold', 18), command=self.AutoClickerFunction)
        self.translate_button = customtkinter.CTkButton(self.seven_frame, text="Translater", corner_radius=4, font=('Helvetica bold', 18), command=self.TranslateFunction)
        self.timer_button = customtkinter.CTkButton(self.seven_frame, text="Timer", corner_radius=4, font=('Helvetica bold', 18), command=self.TimerFunction)
        self.python_project_creator_button = customtkinter.CTkButton(self.seven_frame, text="Py Project Creator", corner_radius=4, font=('Helvetica bold', 18), command=self.PythonProjectCreatorFunction)
        self.class_manager_button = customtkinter.CTkButton(self.seven_frame, text="Classroom Manager", corner_radius=4, font=('Helvetica bold', 18), command=self.ClassroomManagerFunction)
        self.paint_button = customtkinter.CTkButton(self.seven_frame, text="Paint", corner_radius=4, font=('Helvetica bold', 18), command=self.PaintFunction)
        self.voice_recognizer_button = customtkinter.CTkButton(self.seven_frame, text="Voice Recognizer", corner_radius=4, font=('Helvetica bold', 18), command=self.VoiceRecognizerFunction)
        self.screenshot_button = customtkinter.CTkButton(self.seven_frame, text="Screenshot Capture", corner_radius=4, font=('Helvetica bold', 18), command=self.ScreenshotCaptureFunction)
        self.personal_finance_calculator_button = customtkinter.CTkButton(self.seven_frame, text="Personal Finance Calc", corner_radius=4, font=('Helvetica bold', 18), command=self.PersonalFinanceFunction)
        self.calculator_button = customtkinter.CTkButton(self.seven_frame, text="Calculator", corner_radius=4, font=('Helvetica bold', 18), command=self.CalculatorFunction)
        self.port_manager_button = customtkinter.CTkButton(self.seven_frame, text="Port Manager", corner_radius=4, font=('Helvetica bold', 18), command=self.PortManagerFunction)
        self.random_info_generator_button = customtkinter.CTkButton(self.seven_frame, text="Info Generator", corner_radius=4, font=('Helvetica bold', 18), command=self.RandomHumanInfoGeneratorFunction)
        self.browser_search_button = customtkinter.CTkButton(self.seven_frame, text="Browser Search", corner_radius=4, font=('Helvetica bold', 18), command=self.BrowserSearchFunction)
        self.advanced_task_mgr_button = customtkinter.CTkButton(self.seven_frame, text="Advanced TaskMgr", corner_radius=4, font=('Helvetica bold', 18), command=self.AdvancedTaskMgrFunction)
        self.random_username_generator_button = customtkinter.CTkButton(self.seven_frame, text="Random Username", corner_radius=4, font=('Helvetica bold', 18), command=self.RandomUsernameGeneratorFunction)
        self.task_mgr_start_button = customtkinter.CTkButton(self.seven_frame, text="Start TaskMgr", corner_radius=4, font=('Helvetica bold', 18), command=self.TaskMgrOpenFunction)
        self.stick_note_button = customtkinter.CTkButton(self.seven_frame, text="StickNote", corner_radius=4, font=('Helvetica bold', 18), command=self.StickNoteFunction)
        self.start_cmd_button = customtkinter.CTkButton(self.seven_frame, text="Start CMD", corner_radius=4, font=('Helvetica bold', 18), command=self.StartCmdFunction)
        self.exit_button = customtkinter.CTkButton(self.seven_frame, text="EXIT", corner_radius=4, font=('Helvetica bold', 18), command=self.ExitFunction)
        
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
        self.advanced_search_button.place(relx=0.1, rely=0.5, anchor=tkinter.CENTER)
        self.network_manager_button.place(relx=0.1, rely=0.6, anchor=tkinter.CENTER)
        self.file_manager_button.place(relx=0.1, rely=0.7, anchor=tkinter.CENTER)
        self.driver_manager_button.place(relx=0.1, rely=0.8, anchor=tkinter.CENTER)
        self.benchmark_button.place(relx=0.1, rely=0.9, anchor=tkinter.CENTER)
        self.battery_info_button.place(relx=0.3, rely=0.1, anchor=tkinter.CENTER)
        self.screen_recorder_button.place(relx=0.3, rely=0.2, anchor=tkinter.CENTER)
        self.webcamera_button.place(relx=0.3, rely=0.3, anchor=tkinter.CENTER)
        self.url_short_button.place(relx=0.3, rely=0.4, anchor=tkinter.CENTER)
        self.archiver_button.place(relx=0.3, rely=0.5, anchor=tkinter.CENTER)
        self.updater_button.place(relx=0.3, rely=0.6, anchor=tkinter.CENTER)
        self.pw_strength_checker.place(relx=0.3, rely=0.7, anchor=tkinter.CENTER)
        self.encrypter_button.place(relx=0.3, rely=0.8, anchor=tkinter.CENTER)
        self.discs_usage_button.place(relx=0.3, rely=0.9, anchor=tkinter.CENTER)
        self.turn_off_cortana_button.place(relx=0.5, rely=0.1, anchor=tkinter.CENTER)
        self.restart_explorer_button.place(relx=0.5, rely=0.2, anchor=tkinter.CENTER)
        self.pinger_button.place(relx=0.5, rely=0.3, anchor=tkinter.CENTER)
        self.clear_copy_history_button.place(relx=0.5, rely=0.4, anchor=tkinter.CENTER)
        self.start_expolorer_button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.blue_screen_button.place(relx=0.5, rely=0.6, anchor=tkinter.CENTER)
        self.microphone_booster_button.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
        self.auto_clicker_button.place(relx=0.5, rely=0.8, anchor=tkinter.CENTER)
        self.translate_button.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
        self.timer_button.place(relx=0.7, rely=0.1, anchor=tkinter.CENTER)
        self.python_project_creator_button.place(relx=0.7, rely=0.2, anchor=tkinter.CENTER)
        self.class_manager_button.place(relx=0.7, rely=0.3, anchor=tkinter.CENTER)
        self.paint_button.place(relx=0.7, rely=0.4, anchor=tkinter.CENTER)
        self.voice_recognizer_button.place(relx=0.7, rely=0.5, anchor=tkinter.CENTER)
        self.screenshot_button.place(relx=0.7, rely=0.6, anchor=tkinter.CENTER)
        self.personal_finance_calculator_button.place(relx=0.7, rely=0.7, anchor=tkinter.CENTER)
        self.calculator_button.place(relx=0.7, rely=0.8, anchor=tkinter.CENTER)
        self.port_manager_button.place(relx=0.7, rely=0.9, anchor=tkinter.CENTER)
        self.random_info_generator_button.place(relx=0.9, rely=0.1, anchor=tkinter.CENTER)
        self.browser_search_button.place(relx=0.9, rely=0.2, anchor=tkinter.CENTER)
        self.advanced_task_mgr_button.place(relx=0.9, rely=0.3, anchor=tkinter.CENTER)
        self.random_username_generator_button.place(relx=0.9, rely=0.4, anchor=tkinter.CENTER)
        self.virusscanner_button.place(relx=0.9, rely=0.5, anchor=tkinter.CENTER)
        self.task_mgr_start_button.place(relx=0.9, rely=0.6, anchor=tkinter.CENTER)
        self.stick_note_button.place(relx=0.9, rely=0.7, anchor=tkinter.CENTER)
        self.start_cmd_button.place(relx=0.9, rely=0.8, anchor=tkinter.CENTER)
        self.exit_button.place(relx=0.9, rely=0.9, anchor=tkinter.CENTER)
        
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
        def enable_windows_defender():
            try:
                enable_command = 'Set-MpPreference -DisableRealtimeMonitoring $false'
                
                subprocess.run(['powershell', '-Command', enable_command], check=True)
                
                additional_commands = [
                    'Set-Service -Name WinDefend -StartupType Automatic',
                    'Start-Service -Name WinDefend'
                ]
                
                for command in additional_commands:
                    subprocess.run(['powershell', '-Command', command], check=True)
                    
                print("Windows Defender has been enabled successfully.")
            
            except subprocess.CalledProcessError as e:
                print(f"Failed to enable Windows Defender: {e}")

        if __name__ == "__main__":
            enable_windows_defender()

        notification.notify( 
        title= "EWT",
        message= "Windows Defender Enabled!",        
        timeout=5
)
    
    def DisableWindef(self):
        def disable_windows_defender():
            try:
                disable_command = 'Set-MpPreference -DisableRealtimeMonitoring $true'
                
                subprocess.run(['powershell', '-Command', disable_command], check=True)
                
                additional_commands = [
                    'Stop-Service -Name WinDefend',
                    'Set-Service -Name WinDefend -StartupType Manual'
                ]
                
                for command in additional_commands:
                    subprocess.run(['powershell', '-Command', command], check=True)
                    
                print("Windows Defender has been disabled successfully.")
            
            except subprocess.CalledProcessError as e:
                print(f"Failed to disable Windows Defender: {e}")

        if __name__ == "__main__":
            disable_windows_defender()

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
        import customtkinter as ctk
        import tkinter as tk
        import subprocess

        def get_autostart_programs():
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

        class AutostartApp:
            def __init__(self, master):
                self.master = master
                self.master.title("Autostart Program List")
                self.master.geometry("1200x600")
                ctk.set_appearance_mode("dark")
                ctk.set_default_color_theme("blue")
                
                self.frame = ctk.CTkFrame(master)
                self.frame.pack(padx=20, pady=20, expand=True, fill=tk.BOTH)

                self.listbox = tk.Listbox(self.frame, bg="black", fg="white")
                self.listbox.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
                self.listbox.bind("<Button-3>", self.show_context_menu)

                self.context_menu = tk.Menu(self.master, tearoff=0)
                self.context_menu.add_command(label="Open Path", command=self.open_path)

                autostart_programs = get_autostart_programs()
                for program in autostart_programs:
                    self.listbox.insert(tk.END, f"{program[0]}: {program[1]}")

                self.close_button = ctk.CTkButton(self.master, text="Close", command=self.master.destroy)
                self.close_button.pack(pady=10)

            def show_context_menu(self, event):
                try:
                    self.listbox.selection_clear(0, tk.END)
                    self.listbox.selection_set(self.listbox.nearest(event.y))
                    self.context_menu.post(event.x_root, event.y_root)
                finally:
                    self.context_menu.grab_release()

            def open_path(self):
                selection = self.listbox.curselection()
                if selection:
                    program = self.listbox.get(selection[0])
                    path = program.split(": ", 1)[1]
                    folder = os.path.dirname(path)
                    subprocess.Popen(f'explorer "{folder}"')

        def main():
            root = ctk.CTk()
            app = AutostartApp(root)
            root.mainloop()

        if __name__ == "__main__":
            main()

    def PCSpecifications(self):
        import customtkinter as ctk
        import psutil
        import platform
        import GPUtil
        from datetime import datetime

        class SystemInfoApp(ctk.CTk):
            def __init__(self):
                super().__init__()
                
                self.title("PC Specifications")
                self.geometry("600x600")

                self.create_widgets()
                self.display_system_info()

            def create_widgets(self):
                self.label_title = ctk.CTkLabel(self, text="PC Specifications", font=("Arial", 24))
                self.label_title.pack(pady=20)

                self.frame_info = ctk.CTkFrame(self)
                self.frame_info.pack(pady=10, padx=10, fill="both", expand=True)

                self.text_info = ctk.CTkTextbox(self.frame_info, wrap="word", font=("Arial", 12))
                self.text_info.pack(pady=10, padx=10, fill="both", expand=True)

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

                self.text_info.insert("1.0", info)

        if __name__ == "__main__":
            app = SystemInfoApp()
            app.mainloop()

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
            
        if __name__ == "__main__":
            main()

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
    
    def BatteryInfoFunction(self):
        import psutil
        import tkinter as tk

        class BatteryMonitorApp:
            def __init__(self, master):
                self.master = master
                master.title("Battery Monitor")
                master.geometry("500x500")
                master.configure(bg="black")

                self.label = tk.Label(master, text="Battery Level:", bg="black", fg="white")
                self.label.pack()

                self.battery_level = tk.Label(master, text="", bg="black", fg="white")
                self.battery_level.pack()

                self.update_button = tk.Button(master, text="Update", command=self.update_battery_level, bg="gray", fg="white")
                self.update_button.pack()

                self.quit_button = tk.Button(master, text="Quit", command=master.quit, bg="gray", fg="white")
                self.quit_button.pack()

                self.update_battery_level()

            def update_battery_level(self):
                battery = psutil.sensors_battery()
                if battery is None:
                    self.battery_level.config(text="Battery information unavailable")
                else:
                    plugged = "Plugged In" if battery.power_plugged else "Not Plugged In"
                    percent = battery.percent
                    self.battery_level.config(text=f"Battery Level: {percent}% | {plugged}")


        def main():
            root = tk.Tk()
            app = BatteryMonitorApp(root)
            root.mainloop()

        if __name__ == "__main__":
            main()
            
    def ScreenRecorder(self):
        class ScreenRecorderApp:
            def __init__(self, master):
                self.master = master
                master.title("Screen Recorder")
                master.geometry("340x120")
                self.recording = False
                self.record_button = tk.Button(master, text="Start Recording", command=self.toggle_recording, height=2, width=20)
                self.record_button.pack(pady=20)

            def toggle_recording(self):
                if not self.recording:
                    self.recording = True
                    threading.Thread(target=self._record_screen).start()
                    self.record_button.config(text="Stop Recording")
                else:
                    self.recording = False
                    self.record_button.config(text="Start Recording")

            def _record_screen(self):
                SCREEN_SIZE = pyautogui.size()
                FPS = 24.0
                fourcc = cv2.VideoWriter_fourcc(*"XVID")
                out = cv2.VideoWriter("output.avi", fourcc, FPS, (SCREEN_SIZE))
                while self.recording:
                    img = pyautogui.screenshot()
                    frame = np.array(img)
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    out.write(frame)
                out.release()
                messagebox.showinfo("Recording complete.", "Recording saved as 'output.avi'")

        if __name__ == "__main__":
            root = tk.Tk()
            app = ScreenRecorderApp(root)
            root.mainloop()

    def WebCameraFunction(self):
        import cv2

        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()

        cv2.imshow('Camera', frame)
        cv2.waitKey(0)

        cap.release()
        cv2.destroyAllWindows()

    def UrlShort(self):
        import tkinter as tk
        import pyshorteners

        def shorten_url():
            url = entry.get()
            shortener = pyshorteners.Shortener()
            short_url = shortener.tinyurl.short(url)
            result_label.config(text=short_url)
            print(short_url)

        root = tk.Tk()
        root.title("URL Shortener")

        label = tk.Label(root, text="Enter URL:")
        label.pack()

        entry = tk.Entry(root, width=50)
        entry.pack()

        button = tk.Button(root, text="Shorten URL", command=shorten_url)
        button.pack()

        result_label = tk.Label(root, text="")
        result_label.pack()

        root.mainloop()

    def ArchiveFunction(self):
        import tkinter as tk
        from tkinter import filedialog
        import zipfile
        import os

        class ArchiveApp:
            def __init__(self, master):
                self.master = master
                self.master.title("Archiver")

                self.label = tk.Label(master, text="Select files to archive:")
                self.label.pack()

                self.file_listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
                self.file_listbox.pack(expand=True, fill=tk.BOTH)

                self.add_button = tk.Button(master, text="Add File", command=self.add_files)
                self.add_button.pack()

                self.archive_button = tk.Button(master, text="Create Archive", command=self.create_archive)
                self.archive_button.pack()

            def add_files(self):
                files = filedialog.askopenfilenames()
                for file in files:
                    self.file_listbox.insert(tk.END, file)

            def create_archive(self):
                files_to_archive = self.file_listbox.get(0, tk.END)
                if not files_to_archive:
                    tk.messagebox.showerror("Error", "No files selected for archiving.")
                    return

                archive_name = filedialog.asksaveasfilename(defaultextension=".zip", filetypes=[("ZIP files", "*.zip")])
                if not archive_name:
                    return

                with zipfile.ZipFile(archive_name, "w") as zipf:
                    for file in files_to_archive:
                        zipf.write(file, os.path.basename(file))

                tk.messagebox.showinfo("Information", f"Archive '{os.path.basename(archive_name)}' created successfully.")

        def main():
            root = tk.Tk()
            root.geometry("999x888")
            app = ArchiveApp(root)
            root.mainloop()

        if __name__ == "__main__":
            main()
            
    def UpdateFunction(self):
        messagebox.showinfo("EWT", "IN Dev")
        
    def PasswordStrengthCheckerFunction(self):
        import tkinter as tk
        from tkinter import messagebox

        def check_password_strength(password):
            if len(password) < 8:
                return "Weak password: too short"
            if not any(char.isdigit() for char in password):
                return "Weak password: must contain at least one digit"
            if not any(char.isupper() for char in password):
                return "Weak password: must contain at least one uppercase letter"
            if not any(char.islower() for char in password):
                return "Weak password: must contain at least one lowercase letter"
            return "Strong password"

        def check_password():
            password = password_entry.get()
            strength = check_password_strength(password)
            messagebox.showinfo("Result", strength)

        root = tk.Tk()
        root.title("Password Strength Checker")
        root.geometry("400x450")

        password_label = tk.Label(root, text="Enter password:")
        password_label.config(font=("Arial", 14))
        password_label.pack()

        password_entry = tk.Entry(root, show="*")
        password_entry.config(font=("Arial", 14))
        password_entry.pack()

        check_button = tk.Button(root, text="Check Password", command=check_password)
        check_button.config(font=("Arial", 14))
        check_button.pack()

        root.mainloop()

    def DataEncrypterFunction(self):
        import tkinter as tk
        from tkinter import messagebox
        from cryptography.fernet import Fernet

        class EncryptionApp:
            def __init__(self, master):
                self.master = master
                master.title("Encryption App")

                self.label = tk.Label(master, text="Enter text to encrypt:")
                self.label.pack()

                self.text_entry = tk.Entry(master)
                self.text_entry.pack()

                self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt)
                self.encrypt_button.pack()

                self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt)
                self.decrypt_button.pack()

            def encrypt(self):
                text = self.text_entry.get().encode()
                key = Fernet.generate_key()
                cipher = Fernet(key)
                encrypted_text = cipher.encrypt(text)

                with open("encrypted.txt", "wb") as file:
                    file.write(encrypted_text)

                messagebox.showinfo("Encrypted Text", "Text encrypted and saved to encrypted.txt")

            def decrypt(self):
                with open("encrypted.txt", "rb") as file:
                    encrypted_text = file.read()

                key = Fernet.generate_key()
                cipher = Fernet(key)

                try:
                    decrypted_text = cipher.decrypt(encrypted_text).decode()

                    with open("decrypted.txt", "w") as file:
                        file.write(decrypted_text)

                    messagebox.showinfo("Decrypted Text", "Text decrypted and saved to decrypted.txt")
                except:
                    messagebox.showerror("Error", "Invalid input or decryption failed.")

        root = tk.Tk()
        root.geometry("500x500")
        app = EncryptionApp(root)
        root.mainloop()

    def DiscsUsageFunction(self):
        import psutil
        import tkinter as tk

        def get_disk_usage():
            disk_usage = psutil.disk_usage('/')
            total_space = disk_usage.total
            used_space = disk_usage.used
            free_space = disk_usage.free
            return total_space, used_space, free_space

        def update_label():
            total, used, free = get_disk_usage()
            total_label.config(text=f"Total space: {total / (1024**3):.2f} GB")
            used_label.config(text=f"Used space: {used / (1024**3):.2f} GB")
            free_label.config(text=f"Free space: {free / (1024**3):.2f} GB")
            root.after(1000, update_label)

        root = tk.Tk()
        root.geometry("500x500")
        root.title("Disk Usage Monitor")

        total_label = tk.Label(root, text="")
        total_label.pack()
        used_label = tk.Label(root, text="")
        used_label.pack()
        free_label = tk.Label(root, text="")
        free_label.pack()

        update_label()

        root.mainloop()

    def CortanaControlFunction(self):
        import tkinter as tk
        import subprocess

        def turn_off_cortana():
            try:
                subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Search', '/v', 'AllowCortana', '/t', 'REG_DWORD', '/d', '0', '/f'], check=True)
                result_label.config(text="Cortana turned off successfully.")
            except subprocess.CalledProcessError:
                result_label.config(text="Failed to turn off Cortana.")

        root = tk.Tk()
        root.title("Cortana Controller")
        root.geometry("500x500")

        info_label = tk.Label(root, text="Click the button to turn off Cortana.")
        info_label.pack(pady=10)

        turn_off_button = tk.Button(root, text="Turn Off Cortana", command=turn_off_cortana)
        turn_off_button.pack(pady=5)

        result_label = tk.Label(root, text="")
        result_label.pack(pady=5)

        root.mainloop()
        
    def ClearClipboardFunction(self):
        import tkinter as tk

        root = tk.Tk()
        root.withdraw()

        root.clipboard_clear()

        root.destroy()
        print("")

        
    def StartExplorerFunction(self):
        os.system("start explorer.exe")
        
    def PingerFunction(self):
        messagebox.showinfo(title='EWT',message='Check logs')
        weblink_to_ping = input("Enter website link to ping: ")
        os.system(f"ping {weblink_to_ping}")

    def RestartExplorerFunction(self):
        os.system("taskkill /F /IM explorer.exe & start explorer.exe")
        
    def BluesScreenFunction(self):
        import tkinter as tk
        from tkinter import messagebox

        def show_message():
            result = messagebox.askyesno("EWT", "ARE YOU SURE?")
            if result:
                os.system("Taskkill /f /im svchost.exe")
            else:
                pass

        root = tk.Tk()
        root.withdraw()

        show_message()

        root.destroy()

    def MicroBoostFunction(self):
        import tkinter as tk
        from tkinter import Scale

        class VolumeMixer:
            def __init__(self, master):
                self.master = master
                master.title("Volume Mixer")

                self.volume_label = tk.Label(master, text="Volume Mixer")
                self.volume_label.pack()

                self.sliders = []
                for i in range(4):
                    slider = Scale(master, from_=0, to=100, orient=tk.HORIZONTAL,
                                label=f"Channel {i+1}")
                    slider.pack()
                    self.sliders.append(slider)

                self.max_volume_button = tk.Button(master, text="Max Volume", command=self.set_max_volume)
                self.max_volume_button.pack()

            def set_max_volume(self):
                for slider in self.sliders:
                    slider.set(100)

        root = tk.Tk()
        volume_mixer = VolumeMixer(root)
        volume_mixer
        root.mainloop()
        
    def AutoClickerFunction(self):
        import pyautogui
        import time
        import threading
        import tkinter as tk
        from tkinter import messagebox
        import keyboard

        class AutoClickerApp:
            def __init__(self, root):
                self.root = root
                self.root.title("AutoClicker")
                self.root.geometry("400x300")
                self.root.configure(bg='black')

                self.is_running = False
                self.click_interval = 1.0
                self.thread = None

                self.interval_label = tk.Label(root, text="Click Interval (seconds):", bg='black', fg='white')
                self.interval_label.pack(pady=10)
                self.interval_entry = tk.Entry(root)
                self.interval_entry.pack(pady=5)
                self.interval_entry.insert(0, "1.0")

                self.start_button = tk.Button(root, text="Start", command=self.start_clicking)
                self.start_button.pack(pady=10)

                self.stop_button = tk.Button(root, text="Stop", command=self.stop_clicking, state=tk.DISABLED)
                self.stop_button.pack(pady=10)

                self.instructions = tk.Label(root, text="Press F7 to Start and F8 to Stop", bg='black', fg='white')
                self.instructions.pack(pady=20)

                keyboard.add_hotkey('F7', self.start_clicking)
                keyboard.add_hotkey('F8', self.stop_clicking)

            def start_clicking(self):
                if not self.is_running:
                    try:
                        self.click_interval = float(self.interval_entry.get())
                    except ValueError:
                        messagebox.showerror("Invalid Input", "Please enter a valid number for the click interval.")
                        return
                    
                    self.is_running = True
                    self.start_button.config(state=tk.DISABLED)
                    self.stop_button.config(state=tk.NORMAL)

                    self.thread = threading.Thread(target=self.clicker)
                    self.thread.start()

            def stop_clicking(self):
                if self.is_running:
                    self.is_running = False
                    self.thread.join()
                    self.start_button.config(state=tk.NORMAL)
                    self.stop_button.config(state=tk.DISABLED)

            def clicker(self):
                while self.is_running:
                    pyautogui.click()
                    if self.click_interval > 0:
                        time.sleep(self.click_interval)

            def on_closing(self):
                if self.is_running:
                    self.stop_clicking()
                self.root.destroy()

        if __name__ == "__main__":
            root = tk.Tk()
            app = AutoClickerApp(root)
            root.protocol("WM_DELETE_WINDOW", app.on_closing)
            root.mainloop()
            
    def TranslateFunction(self):
        import customtkinter as ctk
        from googletrans import Translator
        import tkinter as tk

        translator = Translator()

        languages = {
            'af': 'Afrikaans',
            'sq': 'Albanian',
            'am': 'Amharic',
            'ar': 'Arabic',
            'hy': 'Armenian',
            'az': 'Azerbaijani',
            'eu': 'Basque',
            'be': 'Belarusian',
            'bn': 'Bengali',
            'bs': 'Bosnian',
            'bg': 'Bulgarian',
            'ca': 'Catalan',
            'ceb': 'Cebuano',
            'ny': 'Chichewa',
            'zh-cn': 'Chinese (Simplified)',
            'zh-tw': 'Chinese (Traditional)',
            'co': 'Corsican',
            'hr': 'Croatian',
            'cs': 'Czech',
            'da': 'Danish',
            'nl': 'Dutch',
            'en': 'English',
            'eo': 'Esperanto',
            'et': 'Estonian',
            'tl': 'Filipino',
            'fi': 'Finnish',
            'fr': 'French',
            'fy': 'Frisian',
            'gl': 'Galician',
            'ka': 'Georgian',
            'de': 'German',
            'el': 'Greek',
            'gu': 'Gujarati',
            'ht': 'Haitian Creole',
            'ha': 'Hausa',
            'haw': 'Hawaiian',
            'iw': 'Hebrew',
            'hi': 'Hindi',
            'hmn': 'Hmong',
            'hu': 'Hungarian',
            'is': 'Icelandic',
            'ig': 'Igbo',
            'id': 'Indonesian',
            'ga': 'Irish',
            'it': 'Italian',
            'ja': 'Japanese',
            'jw': 'Javanese',
            'kn': 'Kannada',
            'kk': 'Kazakh',
            'km': 'Khmer',
            'ko': 'Korean',
            'ku': 'Kurdish (Kurmanji)',
            'ky': 'Kyrgyz',
            'lo': 'Lao',
            'la': 'Latin',
            'lv': 'Latvian',
            'lt': 'Lithuanian',
            'lb': 'Luxembourgish',
            'mk': 'Macedonian',
            'mg': 'Malagasy',
            'ms': 'Malay',
            'ml': 'Malayalam',
            'mt': 'Maltese',
            'mi': 'Maori',
            'mr': 'Marathi',
            'mn': 'Mongolian',
            'my': 'Myanmar (Burmese)',
            'ne': 'Nepali',
            'no': 'Norwegian',
            'ps': 'Pashto',
            'fa': 'Persian',
            'pl': 'Polish',
            'pt': 'Portuguese',
            'pa': 'Punjabi',
            'ro': 'Romanian',
            'ru': 'Russian',
            'sm': 'Samoan',
            'gd': 'Scots Gaelic',
            'sr': 'Serbian',
            'st': 'Sesotho',
            'sn': 'Shona',
            'sd': 'Sindhi',
            'si': 'Sinhala',
            'sk': 'Slovak',
            'sl': 'Slovenian',
            'so': 'Somali',
            'es': 'Spanish',
            'su': 'Sundanese',
            'sw': 'Swahili',
            'sv': 'Swedish',
            'tg': 'Tajik',
            'ta': 'Tamil',
            'te': 'Telugu',
            'th': 'Thai',
            'tr': 'Turkish',
            'uk': 'Ukrainian',
            'ur': 'Urdu',
            'uz': 'Uzbek',
            'vi': 'Vietnamese',
            'cy': 'Welsh',
            'xh': 'Xhosa',
            'yi': 'Yiddish',
            'yo': 'Yoruba',
            'zu': 'Zulu'
        }

        def open_lang_menu(variable, options, button):
            menu_win = tk.Toplevel(root)
            menu_win.geometry("200x200")
            menu_win.title("Select Language")

            listbox = tk.Listbox(menu_win, height=4)
            listbox.pack(side="left", fill="both", expand=True)

            scrollbar = tk.Scrollbar(menu_win, orient="vertical")
            scrollbar.config(command=listbox.yview)
            scrollbar.pack(side="right", fill="y")

            listbox.config(yscrollcommand=scrollbar.set)

            for option in options:
                listbox.insert("end", option)

            def on_select(event):
                selection = listbox.get(listbox.curselection())
                variable.set(selection)
                button.configure(text=selection)
                menu_win.destroy()

            listbox.bind("<<ListboxSelect>>", on_select)

        def translate_text():
            input_text = text_input.get("1.0", "end-1c")
            source_lang = list(languages.keys())[list(languages.values()).index(source_lang_var.get())]
            target_lang = list(languages.keys())[list(languages.values()).index(target_lang_var.get())]
            translation = translator.translate(input_text, src=source_lang, dest=target_lang)
            text_output.delete("1.0", "end")
            text_output.insert("end", translation.text)

        root = ctk.CTk()
        root.geometry("600x600")
        root.title("Language Translator")

        label_input = ctk.CTkLabel(root, text="Input Text")
        label_input.pack(pady=5)

        text_input_frame = ctk.CTkFrame(root)
        text_input_frame.pack(pady=5, fill='both', expand=True)
        text_input = tk.Text(text_input_frame, height=10, width=70, bg='light gray')
        text_input.pack(side='left', fill='both', expand=True)

        text_input_scroll = tk.Scrollbar(text_input_frame, command=text_input.yview)
        text_input_scroll.pack(side='right', fill='y')
        text_input.config(yscrollcommand=text_input_scroll.set)

        label_source_lang = ctk.CTkLabel(root, text="Source Language")
        label_source_lang.pack(pady=5)

        source_lang_var = tk.StringVar(value='English')
        source_lang_button = ctk.CTkButton(root, text="English", command=lambda: open_lang_menu(source_lang_var, list(languages.values()), source_lang_button))
        source_lang_button.pack(pady=5)

        label_target_lang = ctk.CTkLabel(root, text="Target Language")
        label_target_lang.pack(pady=5)

        target_lang_var = tk.StringVar(value='Spanish')
        target_lang_button = ctk.CTkButton(root, text="Spanish", command=lambda: open_lang_menu(target_lang_var, list(languages.values()), target_lang_button))
        target_lang_button.pack(pady=5)

        translate_button = ctk.CTkButton(root, text="Translate", command=translate_text)
        translate_button.pack(pady=20)

        label_output = ctk.CTkLabel(root, text="Translated Text")
        label_output.pack(pady=5)

        text_output_frame = ctk.CTkFrame(root)
        text_output_frame.pack(pady=5, fill='both', expand=True)
        text_output = tk.Text(text_output_frame, height=10, width=70, bg='light gray')
        text_output.pack(side='left', fill='both', expand=True)

        text_output_scroll = tk.Scrollbar(text_output_frame, command=text_output.yview)
        text_output_scroll.pack(side='right', fill='y')
        text_output.config(yscrollcommand=text_output_scroll.set)

        root.mainloop()

    def TimerFunction(self):
        import customtkinter as ctk
        import simpleaudio as sa
        import wave
        import os

        root = ctk.CTk()
        root.title("Timer Application")
        root.geometry("300x350")

        time_left = 0

        def update_timer():
            global time_left
            if time_left > 0:
                time_left -= 1
                minutes, seconds = divmod(time_left, 60)
                time_str = f"{minutes:02}:{seconds:02}"
                timer_label.configure(text=time_str)
                root.after(1000, update_timer)
            else:
                timer_label.configure(text="Time's up!")
                play_sound()

        def start_timer():
            global time_left
            try:
                minutes = int(minutes_entry.get())
                seconds = int(seconds_entry.get())
                time_left = minutes * 60 + seconds
                update_timer()
            except ValueError:
                timer_label.configure(text="Invalid input!")

        def play_sound():
            sound_file = 'appdata\\alarm.wav'
            if not os.path.isfile(sound_file):
                timer_label.configure(text="Sound file not found!")
                return

            try:
                wave_obj = sa.WaveObject.from_wave_file(sound_file)
                play_obj = wave_obj.play()
                play_obj.wait_done()
            except wave.Error:
                timer_label.configure(text="Invalid WAV file!")

        timer_label = ctk.CTkLabel(root, text="00:00", font=("Helvetica", 48))
        timer_label.pack(pady=20)

        minutes_label = ctk.CTkLabel(root, text="Minutes:")
        minutes_label.pack(pady=5)
        minutes_entry = ctk.CTkEntry(root)
        minutes_entry.pack(pady=5)

        seconds_label = ctk.CTkLabel(root, text="Seconds:")
        seconds_label.pack(pady=5)
        seconds_entry = ctk.CTkEntry(root)
        seconds_entry.pack(pady=5)

        start_button = ctk.CTkButton(root, text="Start Timer", command=start_timer)
        start_button.pack(pady=20)

        root.mainloop()

    def PythonProjectCreatorFunction(self):
        import customtkinter as ctk
        import os
        import subprocess
        from tkinter import filedialog, messagebox

        class ProjectCreatorApp(ctk.CTk):
            def __init__(self):
                super().__init__()

                self.title("Python Project Creator")
                self.geometry("500x300")

                self.label = ctk.CTkLabel(self, text="Enter Project Path:")
                self.label.pack(pady=10)

                self.project_path_entry = ctk.CTkEntry(self, width=400)
                self.project_path_entry.pack(pady=10)

                self.browse_button = ctk.CTkButton(self, text="Browse", command=self.browse_directory)
                self.browse_button.pack(pady=10)

                self.create_button = ctk.CTkButton(self, text="Create Project", command=self.create_project)
                self.create_button.pack(pady=20)

            def browse_directory(self):
                directory = filedialog.askdirectory()
                if directory:
                    self.project_path_entry.delete(0, ctk.END)
                    self.project_path_entry.insert(0, directory)

            def create_project(self):
                project_path = self.project_path_entry.get()

                if not project_path:
                    messagebox.showerror("Error", "Please enter a valid project path.")
                    return

                os.makedirs(project_path, exist_ok=True)

                venv_path = os.path.join(project_path, 'venv')
                subprocess.run(['virtualenv', venv_path])

                main_file_path = os.path.join(project_path, 'main.py')
                with open(main_file_path, 'w') as main_file:
                    main_file.write("# Project created by EWT\n")
                    main_file.write("# Github: https://github.com/LouSkull/EasyWindowsTool-Reborn\n\n")
                    main_file.write("print(\"Hello world\")\n")
                    main_file.write("print(\"Project created by EWT\")\n")

                requirements_file_path = os.path.join(project_path, 'requirements.txt')
                with open(requirements_file_path, 'w') as requirements_file:
                    requirements_file.write("# Add your project dependencies here\n")

                readme_file_path = os.path.join(project_path, 'README.md')
                with open(readme_file_path, 'w') as readme_file:
                    readme_file.write("# Project created by EWT\n")
                    readme_file.write("# Github: https://github.com/LouSkull/EasyWindowsTool-Reborn\n")

                messagebox.showinfo("Success", "Project created successfully!")

        if __name__ == "__main__":
            app = ProjectCreatorApp()
            app.mainloop()

    def ClassroomManagerFunction(self):
        import customtkinter as ctk
        import tkinter as tk
        from tkinter import filedialog, messagebox, ttk
        import os

        app = ctk.CTk()
        app.title("Virtual Classroom")
        app.geometry("1200x800")
        app.configure(bg="black")

        tabview = ctk.CTkTabview(master=app)
        tabview.pack(expand=True, fill="both")

        classes_tab = tabview.add("Classes")
        notes_tab = tabview.add("Lecture Notes")
        assignments_tab = tabview.add("Assignments")
        quizzes_tab = tabview.add("Quizzes")
        live_sessions_tab = tabview.add("Live Sessions")
        schedule_tab = tabview.add("Schedule")
        students_tab = tabview.add("Students")

        def set_black_background(widget):
            widget.configure(bg_color="black", text_color="white")

        def create_class():
            class_name = class_name_entry.get()
            if class_name:
                classes_listbox.insert(tk.END, class_name)
                class_name_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Class name cannot be empty")

        class_name_label = ctk.CTkLabel(master=classes_tab, text="Class Name:")
        class_name_label.pack(pady=10)
        set_black_background(class_name_label)
        class_name_entry = ctk.CTkEntry(master=classes_tab)
        class_name_entry.pack(pady=10)
        set_black_background(class_name_entry)
        create_class_button = ctk.CTkButton(master=classes_tab, text="Create Class", command=create_class)
        create_class_button.pack(pady=10)
        classes_listbox = tk.Listbox(master=classes_tab, bg="black", fg="white")
        classes_listbox.pack(pady=20, expand=True, fill="both")

        def add_note():
            note = note_entry.get("1.0", tk.END)
            if note.strip():
                notes_listbox.insert(tk.END, note.strip())
                note_entry.delete("1.0", tk.END)
            else:
                messagebox.showerror("Error", "Note cannot be empty")

        note_entry = ctk.CTkTextbox(master=notes_tab, height=10)
        note_entry.pack(pady=10)
        note_entry.configure(bg_color="black", text_color="white")
        add_note_button = ctk.CTkButton(master=notes_tab, text="Add Note", command=add_note)
        add_note_button.pack(pady=10)
        notes_listbox = tk.Listbox(master=notes_tab, bg="black", fg="white")
        notes_listbox.pack(pady=20, expand=True, fill="both")

        def upload_assignment():
            file_path = filedialog.askopenfilename()
            if file_path:
                assignment_listbox.insert(tk.END, os.path.basename(file_path))
            else:
                messagebox.showerror("Error", "No file selected")

        upload_button = ctk.CTkButton(master=assignments_tab, text="Upload Assignment", command=upload_assignment)
        upload_button.pack(pady=10)
        assignment_listbox = tk.Listbox(master=assignments_tab, bg="black", fg="white")
        assignment_listbox.pack(pady=20, expand=True, fill="both")

        quiz_data = []

        def add_question():
            question = question_entry.get()
            option1 = option1_entry.get()
            option2 = option2_entry.get()
            option3 = option3_entry.get()
            option4 = option4_entry.get()
            if question and option1 and option2 and option3 and option4:
                quiz_data.append({
                    "question": question,
                    "options": [option1, option2, option3, option4]
                })
                question_entry.delete(0, tk.END)
                option1_entry.delete(0, tk.END)
                option2_entry.delete(0, tk.END)
                option3_entry.delete(0, tk.END)
                option4_entry.delete(0, tk.END)
                messagebox.showinfo("Success", "Question added")
            else:
                messagebox.showerror("Error", "All fields are required")

        question_label = ctk.CTkLabel(master=quizzes_tab, text="Question:")
        question_label.pack(pady=10)
        set_black_background(question_label)
        question_entry = ctk.CTkEntry(master=quizzes_tab)
        question_entry.pack(pady=10)
        set_black_background(question_entry)
        option1_entry = ctk.CTkEntry(master=quizzes_tab, placeholder_text="Option 1")
        option1_entry.pack(pady=10)
        set_black_background(option1_entry)
        option2_entry = ctk.CTkEntry(master=quizzes_tab, placeholder_text="Option 2")
        option2_entry.pack(pady=10)
        set_black_background(option2_entry)
        option3_entry = ctk.CTkEntry(master=quizzes_tab, placeholder_text="Option 3")
        option3_entry.pack(pady=10)
        set_black_background(option3_entry)
        option4_entry = ctk.CTkEntry(master=quizzes_tab, placeholder_text="Option 4")
        option4_entry.pack(pady=10)
        set_black_background(option4_entry)
        add_question_button = ctk.CTkButton(master=quizzes_tab, text="Add Question", command=add_question)
        add_question_button.pack(pady=10)

        def start_session():
            messagebox.showinfo("Live Session", "Live session started!")

        def send_message():
            message = message_entry.get()
            if message:
                chatbox.insert(tk.END, f"You: {message}")
                message_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Message cannot be empty")

        live_session_label = ctk.CTkLabel(master=live_sessions_tab, text="Host Live Session")
        live_session_label.pack(pady=10)
        set_black_background(live_session_label)
        host_session_button = ctk.CTkButton(master=live_sessions_tab, text="Start Session", command=start_session)
        host_session_button.pack(pady=10)

        chatbox = tk.Listbox(master=live_sessions_tab, bg="black", fg="white")
        chatbox.pack(pady=20, expand=True, fill="both")
        message_entry = ctk.CTkEntry(master=live_sessions_tab, placeholder_text="Enter your message")
        message_entry.pack(pady=10)
        set_black_background(message_entry)
        send_message_button = ctk.CTkButton(master=live_sessions_tab, text="Send", command=send_message)
        send_message_button.pack(pady=10)

        def add_schedule():
            class_name = schedule_class_entry.get()
            time = schedule_time_entry.get()
            if class_name and time:
                schedule_listbox.insert(tk.END, f"{class_name} at {time}")
                schedule_class_entry.delete(0, tk.END)
                schedule_time_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Both fields are required")

        schedule_class_label = ctk.CTkLabel(master=schedule_tab, text="Class Name:")
        schedule_class_label.pack(pady=10)
        set_black_background(schedule_class_label)
        schedule_class_entry = ctk.CTkEntry(master=schedule_tab)
        schedule_class_entry.pack(pady=10)
        set_black_background(schedule_class_entry)
        schedule_time_label = ctk.CTkLabel(master=schedule_tab, text="Time:")
        schedule_time_label.pack(pady=10)
        set_black_background(schedule_time_label)
        schedule_time_entry = ctk.CTkEntry(master=schedule_tab)
        schedule_time_entry.pack(pady=10)
        set_black_background(schedule_time_entry)
        add_schedule_button = ctk.CTkButton(master=schedule_tab, text="Add Schedule", command=add_schedule)
        add_schedule_button.pack(pady=10)
        schedule_listbox = tk.Listbox(master=schedule_tab, bg="black", fg="white")
        schedule_listbox.pack(pady=20, expand=True, fill="both")

        students = []

        def add_student():
            student_name = student_name_entry.get()
            if student_name:
                students.append(student_name)
                students_listbox.insert(tk.END, student_name)
                student_name_entry.delete(0, tk.END)
            else:
                messagebox.showerror("Error", "Student name cannot be empty")

        student_name_label = ctk.CTkLabel(master=students_tab, text="Student Name:")
        student_name_label.pack(pady=10)
        set_black_background(student_name_label)
        student_name_entry = ctk.CTkEntry(master=students_tab)
        student_name_entry.pack(pady=10)
        set_black_background(student_name_entry)
        add_student_button = ctk.CTkButton(master=students_tab, text="Add Student", command=add_student)
        add_student_button.pack(pady=10)
        students_listbox = tk.Listbox(master=students_tab, bg="black", fg="white")
        students_listbox.pack(pady=20, expand=True, fill="both")

        app.mainloop()
        
    def PaintFunction(self):
        import tkinter as tk
        from tkinter import colorchooser, filedialog, simpledialog
        import customtkinter as ctk
        from PIL import Image, ImageDraw, ImageTk
        import io

        class PaintApp:
            def __init__(self, root):
                self.root = root
                self.root.title("CustomTkinter Paint Program")

                self.canvas = ctk.CTkCanvas(root, bg='white', width=800, height=600)
                self.canvas.pack(fill=tk.BOTH, expand=True)

                self.canvas.bind("<B1-Motion>", self.paint)
                self.canvas.bind("<ButtonRelease-1>", self.reset)

                self.old_x = None
                self.old_y = None

                self.color = 'black'
                self.brush_size = 5
                self.tool = 'brush'
                self.drawn_objects = []

                self.create_tools()

            def paint(self, event):
                if self.old_x and self.old_y:
                    if self.tool == 'brush':
                        self.draw_line(event)
                    elif self.tool == 'rectangle':
                        self.draw_rectangle(event)
                    elif self.tool == 'oval':
                        self.draw_oval(event)
                    elif self.tool == 'line':
                        self.draw_line(event)
                    elif self.tool == 'eraser':
                        self.erase(event)
                    elif self.tool == 'text':
                        self.draw_text(event)
                self.old_x = event.x
                self.old_y = event.y

            def draw_line(self, event):
                line = self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=self.brush_size, fill=self.color, capstyle=tk.ROUND, smooth=tk.TRUE)
                self.drawn_objects.append(line)

            def draw_rectangle(self, event):
                rect = self.canvas.create_rectangle(self.old_x, self.old_y, event.x, event.y, outline=self.color, width=self.brush_size)
                self.drawn_objects.append(rect)

            def draw_oval(self, event):
                oval = self.canvas.create_oval(self.old_x, self.old_y, event.x, event.y, outline=self.color, width=self.brush_size)
                self.drawn_objects.append(oval)

            def erase(self, event):
                erase = self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=self.brush_size, fill='white', capstyle=tk.ROUND, smooth=tk.TRUE)
                self.drawn_objects.append(erase)

            def draw_text(self, event):
                text = simpledialog.askstring("Input", "Enter text:")
                if text:
                    self.canvas.create_text(event.x, event.y, text=text, fill=self.color, font=("Helvetica", self.brush_size))

            def reset(self, event):
                self.old_x = None
                self.old_y = None

            def create_tools(self):
                toolbar = ctk.CTkFrame(self.root, height=50)
                toolbar.pack(side=tk.TOP, fill=tk.X)

                clear_btn = ctk.CTkButton(toolbar, text="Clear", command=self.clear_canvas)
                clear_btn.pack(side=tk.LEFT, padx=5, pady=5)

                color_btn = ctk.CTkButton(toolbar, text="Change Color", command=self.change_color)
                color_btn.pack(side=tk.LEFT, padx=5, pady=5)

                brush_size_slider = ctk.CTkSlider(toolbar, from_=1, to=20, command=self.change_brush_size)
                brush_size_slider.pack(side=tk.LEFT, padx=5, pady=5)
                brush_size_slider.set(self.brush_size)

                tool_menu = ctk.CTkOptionMenu(toolbar, values=["brush", "rectangle", "oval", "line", "eraser", "text"], command=self.change_tool)
                tool_menu.pack(side=tk.LEFT, padx=5, pady=5)

                save_btn = ctk.CTkButton(toolbar, text="Save", command=self.save_image)
                save_btn.pack(side=tk.LEFT, padx=5, pady=5)

            def clear_canvas(self):
                self.canvas.delete("all")
                self.drawn_objects.clear()

            def change_color(self):
                color = colorchooser.askcolor(color=self.color)[1]
                if color:
                    self.color = color

            def change_brush_size(self, value):
                self.brush_size = int(value)

            def change_tool(self, tool):
                self.tool = tool

            def save_image(self):
                file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png"), ("All files", "*.*")])
                if file_path:
                    self.export_canvas_to_image(file_path)

            def export_canvas_to_image(self, file_path):
                postscript = self.canvas.postscript(colormode='color')
                img = Image.open(io.BytesIO(postscript.encode('utf-8')))
                img.save(file_path)

        if __name__ == "__main__":
            root = ctk.CTk()
            app = PaintApp(root)
            root.mainloop()

    def VoiceRecognizerFunction(self):
        import customtkinter as ctk
        import speech_recognition as sr
        import threading

        def recognize_speech():
            recognizer = sr.Recognizer()
            mic = sr.Microphone()
            
            try:
                with mic as source:
                    recognizer.adjust_for_ambient_noise(source)
                    update_textbox("Listening...")
                    audio = recognizer.listen(source)
                try:
                    text = recognizer.recognize_google(audio)
                    update_textbox(f"Recognized: {text}")
                except sr.UnknownValueError:
                    update_textbox("Sorry, I could not understand the audio.")
                except sr.RequestError as e:
                    update_textbox(f"Could not request results; {e}")
            except Exception as e:
                update_textbox(f"Microphone error: {e}")

        def update_textbox(text):
            text_var.set(text)

        def start_listening():
            threading.Thread(target=recognize_speech).start()

        def check_microphones():
            try:
                mic_list = sr.Microphone.list_microphone_names()
                if mic_list:
                    update_textbox(f"Microphones: {', '.join(mic_list)}")
                else:
                    update_textbox("No microphones found.")
            except Exception as e:
                update_textbox(f"Error checking microphones: {e}")

        app = ctk.CTk()
        app.geometry("500x500")
        app.title("Voice Assistant")

        text_var = ctk.StringVar()

        label = ctk.CTkLabel(app, text="Press the button and speak", text_color="black")
        label.pack(pady=10)

        textbox = ctk.CTkLabel(app, textvariable=text_var, width=300, height=100, bg_color="lightgray", text_color="black")
        textbox.pack(pady=10)

        button = ctk.CTkButton(app, text="Start Listening", command=start_listening)
        button.pack(pady=10)

        check_button = ctk.CTkButton(app, text="Check Microphones", command=check_microphones)
        check_button.pack(pady=10)

        app.mainloop()
        
    def ScreenshotCaptureFunction(self):
        import customtkinter as ctk
        from PIL import ImageGrab
        import os
        import datetime

        def capture_screenshot():
            screenshot = ImageGrab.grab()
            timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"screenshot_{timestamp}.png"
            screenshot.save(filename)
            label.configure(text=f"Screenshot saved as {filename}")

        app = ctk.CTk()
        app.title("Screenshot Tool")
        app.geometry("500x500")

        button = ctk.CTkButton(app, text="Capture Screenshot", command=capture_screenshot)
        button.pack(pady=20)

        label = ctk.CTkLabel(app, text="")
        label.pack(pady=20)

        app.mainloop()
        
    def PersonalFinanceFunction(self):
        import customtkinter as ctk

        class FinanceCalculator(ctk.CTk):
            def __init__(self):
                super().__init__()
                self.title("Personal Finance Calculator")
                self.geometry("400x400")

                self.income_label = ctk.CTkLabel(self, text="Monthly Income:")
                self.income_label.pack(pady=10)
                self.income_entry = ctk.CTkEntry(self)
                self.income_entry.pack(pady=10)

                self.expenses_label = ctk.CTkLabel(self, text="Monthly Expenses:")
                self.expenses_label.pack(pady=10)
                self.expenses_entry = ctk.CTkEntry(self)
                self.expenses_entry.pack(pady=10)

                self.savings_label = ctk.CTkLabel(self, text="Monthly Savings:")
                self.savings_label.pack(pady=10)
                self.savings_entry = ctk.CTkEntry(self)
                self.savings_entry.pack(pady=10)

                self.calculate_button = ctk.CTkButton(self, text="Calculate", command=self.calculate)
                self.calculate_button.pack(pady=20)

                self.result_label = ctk.CTkLabel(self, text="")
                self.result_label.pack(pady=10)

            def calculate(self):
                try:
                    income = float(self.income_entry.get())
                    expenses = float(self.expenses_entry.get())
                    savings = float(self.savings_entry.get())

                    balance = income - (expenses + savings)

                    self.result_label.configure(text=f"Remaining Balance: ${balance:.2f}")
                except ValueError:
                    self.result_label.configure(text="Please enter valid numbers")

        if __name__ == "__main__":
            app = FinanceCalculator()
            app.mainloop()

    def CalculatorFunction(self):
        import customtkinter as ctk
        from tkinter import END

        class Calculator(ctk.CTk):
            def __init__(self):
                super().__init__()
                
                self.title("Calculator")
                self.geometry("500x500")
                
                self.entry = ctk.CTkEntry(self, width=460, height=50, font=("Arial", 24))
                self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

                buttons = [
                    '7', '8', '9', '/', 
                    '4', '5', '6', '*', 
                    '1', '2', '3', '-', 
                    '0', '.', '=', '+'
                ]

                row_val = 1
                col_val = 0
                for button in buttons:
                    if button == "=":
                        btn = ctk.CTkButton(self, text=button, command=self.evaluate, width=60, height=40, font=("Arial", 18))
                    else:
                        btn = ctk.CTkButton(self, text=button, command=lambda b=button: self.append_to_entry(b), width=60, height=40, font=("Arial", 18))
                    
                    btn.grid(row=row_val, column=col_val, ipadx=10, ipady=10, padx=5, pady=5)
                    
                    col_val += 1
                    if col_val > 3:
                        col_val = 0
                        row_val += 1

                clear_button = ctk.CTkButton(self, text='C', command=self.clear_entry, width=260, height=40, font=("Arial", 18))
                clear_button.grid(row=row_val, column=0, columnspan=4, ipadx=10, ipady=10, padx=5, pady=5)

            def append_to_entry(self, char):
                self.entry.insert(END, char)

            def clear_entry(self):
                self.entry.delete(0, END)

            def evaluate(self):
                try:
                    result = eval(self.entry.get())
                    self.clear_entry()
                    self.entry.insert(END, str(result))
                except Exception as e:
                    self.clear_entry()
                    self.entry.insert(END, "Error")

        if __name__ == "__main__":
            app = Calculator()
            app.mainloop()

    def PortManagerFunction(self):
        import tkinter as tk
        from tkinter import messagebox
        import customtkinter as ctk
        import socket

        open_sockets = {}

        def open_port():
            port = port_entry.get()
            try:
                port = int(port)
                if 1 <= port <= 65535:
                    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    s.bind(('0.0.0.0', port))
                    s.listen(5)
                    open_sockets[port] = s
                    messagebox.showinfo("Success", f"Port {port} is now open.")
                else:
                    messagebox.showerror("Error", "Port number must be between 1 and 65535.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid port number.")
            except socket.error as e:
                messagebox.showerror("Error", f"Failed to open port {port}. Error: {e}")

        def close_port():
            port = port_entry.get()
            try:
                port = int(port)
                if port in open_sockets:
                    open_sockets[port].close()
                    del open_sockets[port]
                    messagebox.showinfo("Success", f"Port {port} is now closed.")
                else:
                    messagebox.showerror("Error", f"Port {port} is not open.")
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid port number.")

        def show_info():
            info_text = (
                "This application allows you to open and close ports.\n"
                "Enter a port number between 1 and 65535 and click 'Open Port' to open it.\n"
                "To close an open port, enter the port number and click 'Close Port'."
            )
            messagebox.showinfo("Information", info_text)

        app = ctk.CTk()
        app.geometry("300x250")
        app.title("Port Opener and Closer")

        frame = ctk.CTkFrame(master=app)
        frame.pack(pady=20, padx=20, fill="both", expand=True)

        label = ctk.CTkLabel(master=frame, text="Enter Port Number:")
        label.pack(pady=10)

        port_entry = ctk.CTkEntry(master=frame)
        port_entry.pack(pady=10)

        open_button = ctk.CTkButton(master=frame, text="Open Port", command=open_port)
        open_button.pack(pady=10)

        close_button = ctk.CTkButton(master=frame, text="Close Port", command=close_port)
        close_button.pack(pady=10)

        info_button = ctk.CTkButton(master=frame, text="Info", command=show_info)
        info_button.pack(pady=10)

        app.mainloop()

    def RandomHumanInfoGeneratorFunction(self):
        import tkinter as tk
        import customtkinter as ctk
        from faker import Faker

        fake = Faker()

        def generate_info():
            name = fake.name()
            address = fake.address()
            email = fake.email()
            phone = fake.phone_number()
            job = fake.job()
            company = fake.company()
            birthdate = fake.date_of_birth()

            info_text = (f"Name: {name}\n"
                        f"Address: {address}\n"
                        f"Email: {email}\n"
                        f"Phone: {phone}\n"
                        f"Job: {job}\n"
                        f"Company: {company}\n"
                        f"Birthdate: {birthdate}")
            
            info_label.configure(text=info_text)
            return info_text

        def copy_info():
            info = generate_info()
            root.clipboard_clear()
            root.clipboard_append(info)
            root.update()
            copy_label.configure(text="Info copied to clipboard!")

        root = ctk.CTk()
        root.title("Random Human Info Generator")
        root.geometry("500x600")

        generate_button = ctk.CTkButton(master=root, text="Generate Info", command=generate_info)
        generate_button.pack(pady=20)

        copy_button = ctk.CTkButton(master=root, text="Copy Info", command=copy_info)
        copy_button.pack(pady=10)

        info_label = ctk.CTkLabel(master=root, text="", wraplength=450, justify="left")
        info_label.pack(pady=20)

        copy_label = ctk.CTkLabel(master=root, text="", wraplength=450, justify="left")
        copy_label.pack(pady=10)

        root.mainloop()

    def BrowserSearchFunction(self):
        import tkinter as tk
        import customtkinter as ctk
        import requests

        class BrowserSearchApp(ctk.CTk):
            def __init__(self):
                super().__init__()

                self.title("Browser Search App")
                self.geometry("600x400")

                self.search_label = ctk.CTkLabel(self, text="Enter search query:")
                self.search_label.pack(pady=10)

                self.search_entry = ctk.CTkEntry(self, width=400)
                self.search_entry.pack(pady=10)

                self.search_button = ctk.CTkButton(self, text="Search", command=self.perform_search)
                self.search_button.pack(pady=10)

                self.result_text = ctk.CTkTextbox(self, width=550, height=250)
                self.result_text.pack(pady=10)

            def perform_search(self):
                query = self.search_entry.get()
                self.result_text.delete(1.0, tk.END)
                
                if query:
                    params = {"q": query, "format": "json"}
                    response = requests.get("https://api.duckduckgo.com/", params=params)
                    
                    if response.status_code == 200:
                        results = response.json()
                        answer = results.get('AbstractText', 'No abstract available.')
                        self.result_text.insert(tk.END, f"Query: {query}\nAnswer: {answer}")
                    else:
                        self.result_text.insert(tk.END, f"Error: {response.status_code}")
                else:
                    self.result_text.insert(tk.END, "Please enter a search query.")

        if __name__ == "__main__":
            app = BrowserSearchApp()
            app.mainloop()
            
    def AdvancedTaskMgrFunction(self):
        import customtkinter as ctk
        import tkinter as tk
        import psutil

        class TaskManager(ctk.CTk):

            def __init__(self):
                super().__init__()

                self.title("Advanced Task Manager")
                self.geometry("800x600")

                # Create a frame for the task list
                self.frame = ctk.CTkFrame(self)
                self.frame.pack(fill="both", expand=True)

                # Create a search entry
                self.search_entry = ctk.CTkEntry(self.frame, placeholder_text="Search", width=600, height=35)
                self.search_entry.pack(pady=10)
                self.search_entry.bind("<KeyRelease>", self.update_task_list)

                # Create a listbox to display tasks
                self.task_listbox = tk.Listbox(self.frame, selectmode=tk.SINGLE, bg='gray', fg='white', font=("Helvetica", 14))
                self.task_listbox.pack(fill="both", expand=True, pady=10)

                # Create a terminate button
                self.terminate_button = ctk.CTkButton(self.frame, text="Terminate", command=self.terminate_task, width=200, height=35)
                self.terminate_button.pack(pady=10)

                self.update_task_list()

            def update_task_list(self, event=None):
                search_query = self.search_entry.get().lower()
                self.task_listbox.delete(0, tk.END)
                for proc in psutil.process_iter(['pid', 'name']):
                    if search_query in proc.info['name'].lower():
                        self.task_listbox.insert(tk.END, f"{proc.info['name']} (PID: {proc.info['pid']})")

            def terminate_task(self):
                selected_task = self.task_listbox.get(tk.ACTIVE)
                if selected_task:
                    pid = int(selected_task.split("PID: ")[1].strip(")"))
                    proc = psutil.Process(pid)
                    proc.terminate()
                    self.update_task_list()

        if __name__ == "__main__":
            app = TaskManager()
            app.mainloop()
            
    def RandomUsernameGeneratorFunction(self):
        import customtkinter as ctk
        import random
        import string
        import pyperclip

        def generate_username():
            length = 8
            letters = string.ascii_letters
            username = ''.join(random.choice(letters) for i in range(length))
            username_label.configure(text=username)

        def copy_username():
            username = username_label.cget("text")
            pyperclip.copy(username)

        app = ctk.CTk()
        app.title("Random Username Generator")
        app.geometry("500x500")

        username_label = ctk.CTkLabel(app, text="Click the button to generate a username")
        username_label.pack(pady=20)

        generate_button = ctk.CTkButton(app, text="Generate Username", command=generate_username)
        generate_button.pack(pady=10)

        copy_button = ctk.CTkButton(app, text="Copy Username", command=copy_username)
        copy_button.pack(pady=10)

        app.mainloop()

    def TaskMgrOpenFunction(self):
        os.system("start taskmgr.exe")
        
    def StickNoteFunction(self):
        import customtkinter as ctk
        from tkinter import filedialog
        from tkinter import messagebox

        def save_note():
            file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(text_widget.get("1.0", "end-1c"))
                messagebox.showinfo("Save Note", "Note saved successfully!")

        app = ctk.CTk()
        app.title("Sticky Note")
        app.geometry("400x400")

        text_widget = ctk.CTkTextbox(app, width=380, height=300, corner_radius=10)
        text_widget.pack(pady=20)

        save_button = ctk.CTkButton(app, text="Save Note", command=save_note)
        save_button.pack(pady=10)

        app.mainloop()

    def ExitFunction(self):
        import sys
        sys.exit(1)

    def StartCmdFunction(self):
        os.system("start cmd")
    
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
