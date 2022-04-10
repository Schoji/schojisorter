import os
import sys
import subprocess

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