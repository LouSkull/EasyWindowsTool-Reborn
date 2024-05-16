import os, sys, time
os.system("title EWTSetup")
os.system("color 5")
os.system("cls")
Welcome = "Welcome to EasyWindowsTool fix :) \n"
for char in Welcome:
    print(char, end="", flush=True)
    time.sleep(0.06)
else:
    press = "Press (1) to continue, to exit press (0) \n"
    for char in press:
        print(char, end="", flush=True)
        time.sleep(0.06)
    else:
        press1 = input()
        if press1 == "1":
            time.sleep(1)
            os.system("pip install customtkinter")
            os.system("pip install psutil")
            os.system("pip install pillow")
            os.system("pip install plyer")
            os.system("pip install requests")
            time.sleep(2)
            os.system("cls")
            success = "Successfully! Press enter to exit"
            for char in success:
                print(char, end="", flush=True)
                time.sleep(0.06)
            else:
                input()

        if press1 == "0":
            bye = "Byee :("
            for char in bye:
                print(char, end="", flush=True)
                time.sleep(0.06)
