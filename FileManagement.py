import os
import shutil
import tkinter as tk
import math
money = 0
size = 0
import datetime
def directory_show():
    cwd = os.getcwd()
    print("Current Directory:", cwd)
    begin()

def show_files():
    ls = os.listdir()
    print("All Files:", ls)

def delete_file():
    print("Which file would you like to delete:")
    delfile = input()
    if os.path.exists(delfile):
        os.remove(delfile)
        print(f"{delfile} has been deleted.")
    else:
        print("File doesn't exist.")
    begin()

def create_file():
    print("Type name for file to create:")
    file = input()
    with open(file, "w") as f:
        pass  # Create an empty file
    print(f"{file} has been created.")
    begin()

def read_file():
    print("What file do you want to read:")
    readfile = input()
    if os.path.exists(readfile):
        with open(readfile, "r") as read:
            print(read.read())
    else:
        print("File doesn't exist.")
    begin()


def deleteall():
    e = os.listdir()
    i = 0
    while i < len(e):
        # Check if the path is a file before attempting to delete it
        if os.path.isfile(e[i]) and e[i] != "FileManager.py":
            os.remove(e[i])
            print(f"{e[i]} has been deleted.")
        elif e[i] == "FileManager.py":
            print("Can't Delete Main Source")
        else:
            print(f"{e[i]} is not a file and cannot be deleted.")
        i += 1
    print("All files have been deleted.")
    begin()
def new_directory():
    print("Name Your Directory")
    directory_name = input()
    os.mkdir(directory_name)
    print("Directory created", directory_name)
    begin()

def delete_directory():
    print("Which Directory")
    rm = input()
    if os.path.exists(rm):
        shutil.rmtree(rm)
        print("Deleted Directory", rm)
    else:
        print("Doesn't Exist")
    begin()

def change_directory():
    print("What Directory")
    cd = input()
    if os.path.exists(cd):
        os.chdir(cd)
    else:
        print("Directory Doesn't Exist")

def backtolast_directory():
    os.chdir("..")
    begin()

def make_window():
    print("Look at your window")
    window = tk.Tk()
    window.title("Close Me")
    w = tk.Label(window, text='Whoever moves first is GAY!!!', font =("Comic Sans", 20))
    w.pack()
    window.geometry("400x400")
    window.mainloop()

def delete_all_directories():
    t = os.listdir()
    for item in t:
        if os.path.isdir(item):  # Check if item is a directory
            shutil.rmtree(item)
            print("Directories Deleted")
def fun_game():
    global moneyl
    print("Fun Game")

    # Set up the main window
    r = tk.Tk()
    r.title("Fun Game")
    r.geometry("400x400")
    r.configure(bg='#90ee90')
    # Create a label, button, and money display label
    we = tk.Label(r, text='Click The Button', font=("Comic Sans", 20),bg = "#90ee90")
    we.pack()

    fein = tk.Button(r, text="Click Me", padx=20, pady=10, command=increase_money,bg = "#8DFFCD")
    fein.pack(expand=True)

    moneyl = tk.Label(r, text=money, font=("Comic Sans", 15),bg = "#90ee90")
    moneyl.pack()

    # Run the main loop
    r.mainloop()
def increase_money():
    global money
    money += 1
    moneyl.config(text=money)  # Update label text

def write_file():
    print("Which file would you like to overwrite?")
    write = input().strip()

    # Check if file exists
    if os.path.exists(write):
        with open(write, "w") as file:
            print("Type something to write into the file:")
            content = input()  # Avoid using 'type' as variable name
            file.write(content)
    else:
        print("File doesn't exist.")

    # Assuming `begin()` is a function defined elsewhere
    begin()

def square():
    print("Type A Number")
    num = int(input())
    result = num **2
    print("Result:",result)
    begin()


def squareroot():
    print("Type A Number")
    number = int(input())
    result = math.sqrt(number)
    print("Result:",result)
    begin()

def rename():
    print("Which File")
    current_file = input()
    if os.path.exists(current_file):
        print("What Would You Like To Rename")
        new_name = input()
        os.rename(current_file,new_name)
        print("Renamed File To",new_name)
        begin()
    else:
        print("File Doesn't Exist")

def cubed():
    print("Which Number")
    number = int(input())
    result = number **3
    print("Result:",result)
    begin()

def copy_file():
    print("Which File To Copy")
    file = input()
    if os.path.exists(file):
        print("New Name For Copy Can't Be Same Name")
        new = input()
        copied = shutil.copyfile(file,new)
        print("Copied New File Named",copied)

    else:
        print("File Doesn't Exist")
    begin()
def move_files():
    print("Which File")
    fil = input()
    if os.path.exists(fil):
        print("Which Directory To Move")
        dir = input()
        if os.path.isdir(dir):
            shutil.move(fil,dir)
            print(f"{fil} moved into {dir}")

        else:
            print("Directory Doesn't Exist")
    else:
        print("No File Exists")
    begin()

def zip_file():
    print("Which Directory")
    zip = input()
    if os.path.exists(zip):
        shutil.make_archive(zip,'zip')
        print(f"{zip} Directory Archived")
    else:
        print("Directory Doesn't Exist")


def unzip():
    print("Enter the path to the archive file:")
    file_path = input()

    if os.path.exists(file_path):
        # Define the extraction directory (optional)
        extract_to = os.path.splitext(file_path)[0]  # Default extraction folder
        shutil.unpack_archive(file_path, extract_to)
        print(f"Archive extracted to: {extract_to}")
    else:
        print("File doesn't exist")

def calculator():
    print("Which Operation Mul,Add,Sub,Div")
    oper = input()
    if oper == "Mul":
        fn = float(input("First Integer:"))
        sn = float(input("Second Integer:"))
        result = fn * sn
        print("Result:",result)
    elif oper == "Add":
        fn = float(input("First Integer:"))
        sn = float(input("Second Integer:"))
        result = fn + sn
        print("Result:",result)
    elif oper == "Sub":
        fn = float(input("First Integer:"))
        sn = float(input("Second Integer:"))
        result = fn - sn
        print("Result:",result)
    elif oper == "Div":
        fn = float(input("First Integer:"))
        sn = float(input("Second Integer:"))
        result = fn / sn
        print("Result:",result)
    else:
        print("Non Valid Operation")
    begin()

def directory_size():
    global size
    size_mb =  size / (1024 * 1024)  # Convert bytes to megabytes
    dir = os.getcwd()
    for ele in os.scandir(dir):
        size += os.path.getsize(ele)
        print("Size Of Directory Bytes:",size)
        print("Size Of Directory Megabytes:",size_mb)
        size = 0
    begin()

def move_file():
    print("Which File")
    file = input()
    if os.path.exists(file):
        print("Which Directory To Move")
        dir = input()
        if os.path.exists(dir):
            shutil.move(file,dir)
            print(f"{file} moved to {dir}")
        else:
            print("Directory Doesn' Exist")
    else:
        print("File Doesn't Exist")
    begin()


def backup():
    backup_dir = "Backup"

    if os.path.exists(backup_dir):
        print("Backup directory already exists.")
    else:
        os.mkdir(backup_dir)  # Create the directory if it doesn't exist.
        print("Backup directory created.")

    dir = os.getcwd()

    # Loop through all items in the current directory
    for item in os.listdir(dir):
        source = os.path.join(dir, item)
        destination = os.path.join(backup_dir, item)

        # Only copy files, not directories
        if os.path.isfile(source):  # If it's a file, copy it
            shutil.copy(source, destination)

    print("Backup created successfully.")
    begin()

def current_datetime():
    x = datetime.datetime.now()
    print("Current Date And Time:",x)
    begin()

def search_file():
    search_term = input("Enter file name to search for: ")
    for root, dirs, files in os.walk(os.getcwd()):
        if search_term in files:
            print(f"Found {search_term} at {root}")
            return
    print(f"{search_term} not found.")
    begin()

def area_of_circle():
    print("Type In Radius")
    radius = float(input())
    equation = radius**2 * math.pi
    print("Area Of Circle:",equation)
    begin()

def pytheorem():
    fn = float(input("First Number:"))
    sn = float(input("Second Number:"))
    c = fn**2 + sn**2
    print("C Squared:",c)
    cleng = math.sqrt(c)
    print("Length Of C:",cleng)
    begin()

def begin():
    while True:
        print(" 1. Show Directory\n 2. Show Files\n 3. Delete Files\n 4. Create Files\n 5. Read Files\n 6. Quit\n 7. Delete All Files\n 8. Create Directory\n 9. Delete Directory\n 10. Change Directory\n 11. Back To Last Directory\n 12. Create Window\n 13. Delete All Directories\n 14. Fun Game\n 15. Overwrite File\n 16. Square Calculator\n 17. Square Root\n 18. Rename File\n 19. Cubed Calculator\n 20. Copy File\n 21. Move File\n 22. Zip File\n 23. Unzip File\n 24. Basic Calculator\n 25. Directory Size\n 26. Move Files\n 27. Backup -Only Backups Files\n 28. Current DateTime\n 29. Find Files Or Directories\n 30. Area Of Circle Calculator\n 31. Pythagorean Theorem\n")
        choice = input("Choose an option: ")
        if choice == "1":
            directory_show()
        elif choice == "2":
            show_files()
        elif choice == "3":
            delete_file()
        elif choice == "4":
            create_file()
        elif choice == "5":
            read_file()
        if choice == "6":
            print("Exiting the program.")
            break
        elif choice == "7":
            deleteall()
        elif choice == "8":
            new_directory()
        elif choice == "9":
            delete_directory()
        elif choice == "10":
            change_directory()
        elif choice == "11":
            backtolast_directory()
        elif choice == "12":
            make_window()
        elif choice == "13":
            delete_all_directories()
        elif choice == "14":
            fun_game()
        elif choice == "15":
            write_file()
        elif choice == "16":
            square()
        elif choice == "17":
            squareroot()
        elif choice == "18":
            rename()
        elif choice == "19":
            cubed()
        elif choice == "20":
            copy_file()
        elif choice == "21":
            move_files()
        elif choice == "22":
            zip_file()
        elif choice == "23":
            unzip()
        elif choice == "24":
            calculator()
        elif choice == "25":
            directory_size()
        elif choice == "26":
            move_file()
        elif choice == "27":
            backup()
        elif choice == "28":
            current_datetime()
        elif choice == "29":
            search_file()
        elif choice == "30":
            area_of_circle()
        elif choice == "31":
            pytheorem()
        else:
            print("Invalid option. Please type a number.")

begin()
