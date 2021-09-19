import os 
import platform

if platform.system() == "Windows":
    print (os.system("cls"))
else:
    print (os.system("clear"))