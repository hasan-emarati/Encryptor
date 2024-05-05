from cryptography.fernet import Fernet
from time import sleep
from colorama import Fore, Back, Style, init

class Encryptor:
    def Key_Generator(Filename):
        key = Fernet.generate_key()
        with open(f'{Filename}.key', 'wb') as mykey:
            mykey.write(key)

    def File_Encryptor(Key , File):
        # print (File)
        # print (Key)
        sleep(2)
        if Key is None:  # Added check for Key
            print("Key invalid")
        Encrypted = Fernet(Key).encrypt(File)
        print(Fore.RESET + Encrypted.decode('utf-8'))
        Save_File_Option = input(Fore.BLUE + "\nDo you want to save the file? [Y] [N]") 
        if Save_File_Option == 'y' or Save_File_Option == 'Y':
            File_Name = input("Please enter your File Name : ")
            with open (f'{File_Name}.safe', 'wb') as Encrypted_File:
                Encrypted_File.write(Encrypted)
                print("safe File is created")
        else:
            print("Good bye")

    def File_Decryptor(Key , File):
        sleep(2)
        if Key is None:  # Added check for Key
            print("Key invalid")
        Decrypted = Fernet(Key).decrypt(File)
        print(Fore.RESET + Decrypted.decode('utf-8'))
        Save_File_Option = input(Fore.BLUE + "\nDo you want to save the file? [Y] [N]") 
        if Save_File_Option == 'y' or Save_File_Option == 'Y':
            File_Name = input("Please enter your File Name : ")
            with open(f'{File_Name}.txt', 'wb') as Decrypted_File:
              Decrypted_File.write(Decrypted)
              print (f'{File_Name}.txt' + Fore.GREEN + 'Saved')
        else:
            print("Good bye")
            
    

              
if __name__ == '__main__':
    Run = Encryptor()