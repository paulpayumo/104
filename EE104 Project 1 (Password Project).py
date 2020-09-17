# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:23:07 2020
@author: Paul Payumo, Deric Abril, Mike Lin, Ryan Gallardo
"""

#EE104 Project (Password Project)
from random import randint
import linecache
import sys

class Global:
    count = 0
    vaultUsername = "default"
    vaultPassword = "default"
    myList = []

correct = False

def Login():
    if((Global.vaultUsername == "default") and (Global.vaultPassword == "default")):
        print("Default username and password for Vault is 'default'")
    f = open("./VaultCredentials.txt", "w")
    f.write(Global.vaultUsername + "\t" + Global.vaultPassword)
    f.close()
    inputUsername = input("Please input username: ")
    inputPassword = input("Please input password: ")
    if(inputUsername == Global.vaultUsername and inputPassword == Global.vaultPassword):
        Global.count = 0
        return(True)
    else:
        if(Global.count >= 5):
            print("Invalid attempt. Program will terminate.")
            return(False)
        print("\nIncorrect")
        Global.count += 1
        print("Attempt number ", Global.count)
        Login()
        
def changeVaultCredentials():
    Global.vaultUsername = input("Please input your new vault username: ")
    print("For security purposes, the program will create a vault password for you.\n")
    Global.vaultPassword = createPassword()
    f = open("./VaultCredentials.txt", "w")
    f.write(Global.vaultUsername)
    f.write("\t")
    f.write(Global.vaultPassword)
    f.close()
    Login()

def createUsername():
    username = ""
    username = input("Please enter a username: ")
    return username
        
def getWord(letter):
    word = "hi"
    while(len(word) < 10):
        word = linecache.getline(letter + "word.csv", randint(0,3000))
    return word

def createPassword():
    finalPass =""
    consonants = "bcdfghjklmnpqrstuvwxyz"
    password = getWord(input("Enter a letter: ")).strip()
    first = str(randint(10,99))
    second = str(randint(10,99))
    newPassword = first + password + second
    print("\n" + newPassword)
    newPassword = newPassword.replace("a", "@", 2)
    newPassword = newPassword.replace("e", "3", 2)
    newPassword = newPassword.replace("o", "0", 2)
    newPassword = newPassword.replace("i", "!", 2)
    for i in newPassword:
        num = randint(1,100)%2
        if(num != 0):
            if i in consonants:
                finalPass += i.upper()
            else:
                finalPass += i
        else:
            finalPass += i
    print("Generated Password: " + finalPass + "\n")
    return(finalPass)

def storeVaultIntoMatrix():
    Global.myList = []  #Including this here causes myList to be empty at the start of program
    f = open("./Vault.txt")
    with f as file:
        for line in file:
            Global.myList.append(line.split())
    f.close()
    
def search():
    username = input("Input the username you want to find the password for: ")
    for i in range(len(Global.myList)):
        if(username == Global.myList[i][0]):
            print("The password for that username is: " + Global.myList[i][1])
            return(Global.myList[i][1])
    print("Unable to find username")
    search()
        
def storeCredentialIntoVault():
    username = input("Please input username: ")
    password = input("Please input password: ")
    storeVaultIntoMatrix()
    concatenatedString = username + "\t" + password + "\n"
    f = open("./Vault.txt", "w")
    for i in range(len(Global.myList)):
        f.write(Global.myList[i][0] + "\t" + Global.myList[i][1] + "\n")
    f.write(concatenatedString)
    f.close()
    storeVaultIntoMatrix()

def whatToDo():
    print("\nInput '1' for Change Vault Credentials")
    print("Input '2' for Generate Password")
    print("Input '3' for Search for Password")
    print("Input '4' for Create New Credentials")
    print("Input '5' to logout")
    choice = input("What would you like to do? ")
    if(choice == "1"):
        changeVaultCredentials()
    elif(choice == "2"):
        createPassword()
    elif(choice == "3"):
        search()
    elif(choice == "4"):
        storeCredentialIntoVault()
    elif(choice == "5"):
        print("\nLogging out...\n")
        main()
    else:
        whatToDo()
    

def main():
    correct = False
    storeVaultIntoMatrix()
    while(correct == False):
        correct = Login()
        if(Global.count >= 5):
            sys.exit("Too many login attempts.")
    print("Would you like to change your vault username and password?")
    change = input("Input 'yes' or 'no': ")
    if(change == "yes"):
        changeVaultCredentials()
    while(1 == 1):
        whatToDo()
    
main()