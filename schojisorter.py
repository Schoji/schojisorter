import os
from colorama import Fore, init

init(convert=True)
os.system("mode 360")
os.system("cls")

def hello():
    print("Choose your directory")
    print("You can change directories by typing names of subsequent folders OR")
    print("You can also enter an absolute path to a directory like 'D:/Data/File'")
    print("Confirm by typing " + Fore.BLUE + "RETURN" + Fore.RESET)
    print("If you want to view contents of directory type " + Fore.BLUE + "ls" + Fore.RESET)
    print("If you want to go back type " + Fore.BLUE + "cd.." + Fore.RESET)
    print("If you have any trouble, type " + Fore.BLUE + "HELP" + Fore.RESET)

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
        elif directory == "ls":
            for file in os.listdir():
                if "." not in file:
                    print(Fore.YELLOW + file + Fore.RESET)
        elif directory == "cd..":
            os.chdir("..")
        elif directory == "help":
            hello()
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
    print("\nBye!")
    quit