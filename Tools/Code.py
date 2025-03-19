from cryptography.fernet import Fernet
from time import sleep
from colorama import Fore, Back, Style, init
import os  # اضافه شده برای مدیریت مسیرها

class Encryptor:
    @staticmethod
    def Key_Generator(Filename):
        key = Fernet.generate_key()
        # ایجاد مسیر برای پوشه‌ی والد
        parent_dir = os.path.dirname(os.getcwd())  # پوشه‌ی والد
        target_dir = os.path.join(parent_dir, "EncryptedFiles")  # مسیر دایرکتوری جدید
        os.makedirs(target_dir, exist_ok=True)  # ایجاد دایرکتوری اگر وجود نداشته باشد
        
        # ذخیره فایل کلید در دایرکتوری جدید
        key_path = os.path.join(target_dir, f'{Filename}.key')
        with open(key_path, 'wb') as mykey:
            mykey.write(key)
        print(Fore.GREEN + f"Key file created at: {key_path}")

    @staticmethod
    def File_Encryptor(Key, File):
        sleep(2)
        if Key is None:  # بررسی معتبر بودن کلید
            print(Fore.RED + "Key invalid")
            return

        Encrypted = Fernet(Key).encrypt(File)
        print(Fore.RESET + "Encrypted Data:\n" + Encrypted.decode('utf-8'))
        
        Save_File_Option = input(Fore.BLUE + "\nDo you want to save the file? [Y] [N]: ")
        if Save_File_Option.lower() == 'y':
            File_Name = input("Please enter your File Name: ")
            # ایجاد مسیر برای پوشه‌ی والد
            parent_dir = os.path.dirname(os.getcwd())  # پوشه‌ی والد
            target_dir = os.path.join(parent_dir, "EncryptedFiles")  # مسیر دایرکتوری جدید
            os.makedirs(target_dir, exist_ok=True)  # ایجاد دایرکتوری اگر وجود نداشته باشد
            
            # ذخیره فایل رمزگذاری شده در دایرکتوری جدید
            file_path = os.path.join(target_dir, f'{File_Name}.safe')
            with open(file_path, 'wb') as Encrypted_File:
                Encrypted_File.write(Encrypted)
                print(Fore.GREEN + f"Safe file created at: {file_path}")
        else:
            print(Fore.YELLOW + "Goodbye")

    @staticmethod
    def File_Decryptor(Key, File):
        sleep(2)
        if Key is None:  # بررسی معتبر بودن کلید
            print(Fore.RED + "Key invalid")
            return

        Decrypted = Fernet(Key).decrypt(File)
        print(Fore.RESET + "Decrypted Data:\n" + Decrypted.decode('utf-8'))
        
        Save_File_Option = input(Fore.BLUE + "\nDo you want to save the file? [Y] [N]: ")
        if Save_File_Option.lower() == 'y':
            File_Name = input("Please enter your File Name: ")
            # ایجاد مسیر برای پوشه‌ی والد
            parent_dir = os.path.dirname(os.getcwd())  # پوشه‌ی والد
            target_dir = os.path.join(parent_dir, "EncryptedFiles")  # مسیر دایرکتوری جدید
            os.makedirs(target_dir, exist_ok=True)  # ایجاد دایرکتوری اگر وجود نداشته باشد
            
            # ذخیره فایل رمزگشایی شده در دایرکتوری جدید
            file_path = os.path.join(target_dir, f'{File_Name}.txt')
            with open(file_path, 'wb') as Decrypted_File:
                Decrypted_File.write(Decrypted)
                print(Fore.GREEN + f"File saved at: {file_path}")
        else:
            print(Fore.YELLOW + "Goodbye")

if __name__ == '__main__':
    init(autoreset=True)  # Initialize colorama
    Run = Encryptor()

    # مثال استفاده از توابع
    # Run.Key_Generator("my_key")  # ساخت کلید
    # Run.File_Encryptor(key, b"Hello, World!")  # رمزگذاری
    # Run.File_Decryptor(key, encrypted_data)  # رمزگشایی