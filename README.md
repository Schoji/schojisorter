# Schoji's sorter
This is a simple python script that allows you to easily sort your files by file extensions. <br/> <br/>
![showcase](https://user-images.githubusercontent.com/96655599/160683306-92e56a97-2f10-4a38-99ec-fa5cdcfa79f3.gif)

# Usage
To launch the script you need to open command prompt or terminal (Assuming you already have python3 installed)
```
py schojisorter.py
```
Firstly, you need to specify the path to your desired directory by typing just the ***path*** or ***name*** of a folder (It can be a relative path or absolute path). For example:
```
D:/Data/SortingDirectory
```
you can also use:
* ls - to list a directory
* cd.. - to go back

When you are done, just press the RETURN or ENTER key on your keyboard. You will be prompted with a confirmation question. Type YES, and you're done! <br/> <br/>
![showcase1](https://user-images.githubusercontent.com/96655599/160690025-5f6d3088-e480-41b5-ab09-d86b21f0e114.gif)
# How it works
It uses os module to list all files in current directory and then makes one folder per file extension. After that, it moves files to their destination. It's very simple!
# ToDo
* Gui (Graphical User Interface)
* An user defined selection of files to be sorted
* An user defined exclusion of files to be NOT sorted
* An option to sort multiple directories at once
* An option to sort directories (I have no idea by what criterion will it sort
# Known bugs
* Directories containing a dot are interpreted as a file and sorted like regular files
* Files containing a lot of dots are confusing and incorrectly sorted
