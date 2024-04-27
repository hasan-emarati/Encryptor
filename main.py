from colorama import Fore, Back, Style, init
from tkinter.filedialog import askopenfile
from Tools.Code import Encryptor
from Tools.choice import Choice


class main:
    def __init__(self):
        self.Encryptor = Encryptor
        self.Input = Choice()
        print (Fore.GREEN + '''

                                   ,--~~~````~---,
                                 _i       `   `--,`i_
                                _i,`~i~-,  ;      i i_
                                i``~``~`    i      i i_
                      _,,---~~``~~~~'----,,i__   __i_i
                     ,`  `~-,           _,--';;iiiiiii
                     i_,,--'~i_,,--~~~``    `;;;``~ii
                               .`  _         ';   _i
                               ;    `"~~`         '`
                               i                  ;
                               `~i~          `    i_
                                 `i        ,~      i_
                                   `-,_.,-`         i`-,,_
                                     _,,-i__      _,`     `i-,_
                                _,i~`      ```~~``        SHe
                                  `                

    Created by SHemarati 
    __________________________________________________________________________\n'''+ Fore.RESET)

    def Selector(self):
        while True:
                print(Fore.YELLOW + "Place Select Your Option You Have a Some Option :\n" + '''
[1] > Create Key     Create Key For Encryption Files
[2] > Decrypt File     Decrypt File
[3] > Encrypt File     Encrypt File
''' + Fore.RESET)
                Option = input(Fore.LIGHTBLUE_EX + "Enter Your Option Number >>> ")
                if Option == '1' :
                    FileName = input(Fore.YELLOW + "Enter Your File Name : ")
                    self.Encryptor.Key_Generator(str(FileName))
                    print (Fore.GREEN + "\nYour is Complete")
                    break
                
                elif Option == '2' :
                    print("Plase Enter your key file (.key)")
                    Key = self.Input.option()
                    print(Fore.RED + f"Key <{Key}> is selected"+Fore.RESET)
                    print("Plase Enter your encrypted File (.self)")
                    File = self.Input.option()
                    OutPut = self.Encryptor.File_Decryptor(Key , File)
                    print (OutPut)
                    break
                elif Option == '3' :
                    print("Plase Enter your key file (.key)")
                    Key = self.Input.option()
                    print(Fore.RED + f"Key <{Key}> is selected"+Fore.RESET)
                    print("Plase Enter your File")
                    File = self.Input.option()
                    OutPut = self.Encryptor.File_Encryptor(Key , File)
                    print (OutPut)
                    break
                else :
                    print(Fore.RED + "Invalid Option: " + Option + "\nPlease Enter the new Value" + Fore.RESET)

