
import random
import sys
import os
import time
from turtle import title
from re import T
os.system("color 2")

title("console")

input("hello")


target = input("pseudo : ")
print("Searching account")

input("searching...")
input("voulez vous démaré le CrAcKeR?")
print("                ")

input("Searching  " + target )

print("               ")

input("Searching all Servers for cracking")
input("voulez vous continuez ?")

def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()

for i in progressbar(range(35), "please wait... : ", 40):
    time.sleep(0.6)

caracteres = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

while True:
    nitrocode = ''

    for i in range(16):
        nitrocode = f"{nitrocode}{random.choice(caracteres)}"

    print(f"PassWord Cracker: [{nitrocode}] for : " + target)

    with open("client.txt", "a+") as nitroFile:

        nitroFile.write(f"PassWord Cracker : {nitrocode}\n for :" + target)

        nitroFile.close()