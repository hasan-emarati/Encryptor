# # Created by SHemarati
# from colorama import Fore
# from tkinter.filedialog import askopenfile
# from tkinter import *

# class choice:
#     def UI():
#         try:
#             path = askopenfile(initialdir="/", title="Select file",
#                         filetypes=(("key files", "*.key"),("text files", "*.safe"),("all files", "*.*")))
#             File = path.read()
#             print (Fore.GREEN + "File selected" + Fore.RESET)
#             print(Fore.CYAN + "\n File detected")
#             return str(File)
#         except:
#             print (Fore.RED + "UI Error" + Fore.RESET)
#             choice()

#     def Prompt():
#         try:        
#             print (Fore.MAGENTA + "\n\t\tType File \"*.txt\" , \"*.key\"\n")
#             Path = input("Enter Your Directory ==>  " + Fore.RESET)
#             if Path[-3:] == 'key' or Path[-3:] == 'txt':
#                 Open = open(Path , "r")
#                 File = Open.read()
#                 print (Fore.GREEN + "File selected" + Fore.RESET)
#                 print(Fore.CYAN + "\n File detected")
#                 return str(File)
#             else :
#                 print (Fore.RED + "Invalid File" + Fore.RESET)
#                 choice()
#         except:
#             print (Fore.RED + "Prompt Error" + Fore.RESET)
#             choice()

#     def Option():
#         while True :
#             print(Fore.CYAN + "\t\t[1] UI Select File")
#             print(Fore.CYAN + "\t\t[2] Prompt Select File")
#             Option = input(Fore.BLUE + 'Please select > ' + Fore.RESET)
#             if Option == '1':
#                 choice.UI()
#                 break
#             elif choice == '2':
#                 choice.Prompt()
#                 break
#             else:
#                 print(Fore.RED + 'Invalid choice, please try again' + Fore.RESET)

# if __name__ == '__main__':
#     Run = choice
#     Run.Option()
# # Created by SHemarati







from colorama import Fore
from tkinter import filedialog, Tk

class Choice:
    
    def ui_select_file(self):
        try:
            path = filedialog.askopenfilename(
                initialdir="/",
                title="Select file",
                filetypes=(("key files", "*.key"), ("text files", "*.safe"), ("all files", "*.*"))
            )
            if path:
                with open(path, "r") as file:
                    content = file.read()
                print(Fore.GREEN + "File selected" + Fore.RESET)
                print(Fore.CYAN + "\nFile detected")
                return content
            else:
                print(Fore.RED + "No file selected." + Fore.RESET)
                return None  # Indicate no file chosen
        except FileNotFoundError:
            print(Fore.RED + "File not found." + Fore.RESET)
            return None

    def prompt_select_file(self):
        while True:
            try:
                print(Fore.MAGENTA + "\n\t\tType File \"*.txt\" , \"*.key\"\n")
                path = input("Enter Your Directory ==> " + Fore.RESET)
                if path[-3:] in ("key", "txt"):  # Check for valid extensions efficiently
                    with open(path, "r") as file:
                        content = file.read()
                    print(Fore.GREEN + "File selected" + Fore.RESET)
                    print(Fore.CYAN + "\nFile detected")
                    return content
                else:
                    print(Fore.RED + "Invalid File Extension." + Fore.RESET)
            except FileNotFoundError:
                print(Fore.RED + "File not found." + Fore.RESET)

    def option(self):
        while True:
            print(Fore.CYAN + "\t\t[1] UI Select File\n")
            print(Fore.CYAN + "\t\t[2] Prompt Select File\n")
            option = input(Fore.BLUE + 'Please select > ' + Fore.RESET)
            if option == '1':
                return self.ui_select_file()
            elif option == '2':
                return self.prompt_select_file()
            else:
                print(Fore.RED + 'Invalid choice, please try again' + Fore.RESET)

if __name__ == '__main__':
    choice = Choice()
    content = choice.option()
