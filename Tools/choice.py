from colorama import Fore
from tkinter import filedialog, Tk

class Choice:
    
    def ui_select_file(self):
        try:
            path = filedialog.askopenfilename(
                initialdir="/",
                title="Select file",
                filetypes=(("key files", "*.key;*.safe;*.txt"), ("all files", "*.*"))
            )
            if path:
                with open(path, "rb") as file:
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
                    with open(path, "rb") as file:
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
