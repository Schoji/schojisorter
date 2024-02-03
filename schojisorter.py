import os
import sys
import subprocess
from tkinter import *

#Try to import colorama, if module not found, install it and then import it again.
try:
    from colorama import Fore, init
except ModuleNotFoundError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'colorama'])
    from colorama import Fore, init
    
#Colorama config
init(convert=True)
os.system("mode 360")
os.system("cls")

#List of excluded directories
excluded_dirs = ["C:/Windows",
                  "C:/", 
                  "/",
                  "C:/Program Files",
                  "C:/Program Files (x86)",
                  os.getenv('APPDATA'),
                  os.getenv('LOCALAPPDATA')
                  ]

#Hello message, it contains a full list of instructions which is showed every time the 
#script launched or upon typing "help"

def hello():
    print("Choose your directory")
    print("You can change directories by typing names of subsequent folders OR")
    print("You can also enter an absolute path to a directory like 'D:/Data/Directory'")
    print("List of available actions:")
    print("\t - Confirm by pressing " + Fore.BLUE + "RETURN" + Fore.RESET)
    print("\t - If you want to view contents of directory type " + Fore.BLUE + "ls" + Fore.RESET + " or " + Fore.BLUE + "dir" + Fore.RESET)
    print("\t - If you want to go back type " + Fore.BLUE + "cd.." + Fore.RESET)
    print("\t - If you have any trouble type " + Fore.BLUE + "help" + Fore.RESET)
    print("\t - If you want to exit the app type " + Fore.BLUE + "exit" + Fore.RESET )

hello()

try:
    if len(sys.argv) > 1 and sys.argv[1] == "gui":
        root = Tk()
        root.title("Schoji's sorter")
        welcome = Label(root, text="Welcome to my app")
        dir_label = Label(root, text="Directory:")
        get_directory = Button(root)
        directory = Entry(root)
        x = Radiobutton(root, text="1")

        welcome.grid(column = 0, row = 0)
        dir_label.grid(column = 0, row = 1)
        directory.grid(column = 1, row = 1)
        get_directory.grid(column = 2, row = 1)

        root.mainloop()
    else:
        while True:
            print(Fore.RESET + "Enter the name of folder or press" + Fore.BLUE + " RETURN" + Fore.RESET)
            directory = input(Fore.GREEN + "[SORTER] " + Fore.RESET + os.getcwd() + "> ")
            if directory == "":
                answer = input("Are you sure?\n" + Fore.RED + os.getcwd() + Fore.RESET + "\nType YES to continue: ").lower()
                if answer == "yes":
                    break
                else:
                    continue
            elif directory == "ls" or directory == "dir":
                for file in os.listdir():
                    if "." not in file:
                        print(Fore.YELLOW + file + Fore.RESET)
                    else:
                        print(Fore.GREEN + file + Fore.RESET)
            elif directory == "cd.." or directory == "cd ..":
                os.chdir("..")
            elif directory == "help":
                hello()
            elif directory in excluded_dirs:
                print("You really don't want to do this")
                break
            elif directory == "exit":
                print("\nHave a great day!")
                exit()
            else:
                try:
                    os.chdir(directory)
                except FileNotFoundError:
                    print("Directory not found. Please try again.")

        files = os.listdir()
        filesdict = {}
        #files.remove(__file__.rsplit("\\", 1)[1])
        #print(files)
        for file in files:
            if "." in file:
                ext = file.rsplit(".", 1)[1]
                if ext not in filesdict:
                    filesdict[file] = ext
                    
        for folder in filesdict.items():
            try:
                os.mkdir(folder[1])
            except FileExistsError:
                pass

        for file in filesdict:
            os.replace(directory + file, directory + filesdict[file] + "\\" + file)
        print("Done!")

except KeyboardInterrupt:
    print("\nHave a great day!")
    quit