import config, os, sys
os.system("color 3")
os.system("title EWTLoader")
os.system("cls")
from customtkinter import *

config_file_path = 'config.py'

def update_loader_config(value):
    with open(config_file_path, 'r') as file:
        lines = file.readlines()

    setting_to_change = 'LOADER_CONFIG'
    new_value = str(value)
    
    for i, line in enumerate(lines):
        if line.strip().startswith(setting_to_change):
            parts = line.split('=')
            lines[i] = f"{parts[0].strip()} = {new_value}\n"
            break

    with open(config_file_path, 'w') as file:
        file.writelines(lines)

def EWT_SCRIPT():
    os.system("python EWT.py")

def main():
    
    def loader_check_value():
        if config.LOADER_CONFIG == "True":
            pass
        elif config.LOADER_CONFIG == "False":
            EWT_SCRIPT()
    
    menu = ("""
________          _________ 
|  ____\ \        / /__   __|
| |__   \ \  /\  / /   | |
|  __|   \ \/  \/ /    | |
| |____   \  /\  /     | |
|______|   \/  \/      |_|

[1] Start EWT
[2] Start EWT-FIXER
[3] Settings
    """)

    print(menu)
    choice = input("Your choice --->  ")

    if choice == "1":
        EWT_SCRIPT()
    elif choice == "2":
        os.system("EWT_FIX.py")
    elif choice == "3":
        settings_menu = ("""
[1] Disable Loader (NOTE: You can enable it in "config.py" file)
[2] Exit
    """)
        print(settings_menu)
        settings_choice = input("Your choice --->  ")
        if settings_choice == "1":
            # Update the LOADER_CONFIG in config.py to False
            update_loader_config(False)
            sys.exit(1)
        elif settings_choice == "2":
            sys.exit(1)

if __name__ == "__main__":
    if config.LOADER_CONFIG == True:
        main()
    elif config.LOADER_CONFIG == False:
        EWT_SCRIPT()
