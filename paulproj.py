# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 19:23:07 2020

@author: Paul
"""
#1123724

#EE104 Project (Password Generator)
import csv
from random import randint
import linecache
import string


def createUsername():
    username = ""
    while(len(username) == 0):
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
    password = getWord(input("Enter a letter:")).strip()
    first = str(randint(10,99))
    second = str(randint(10,99))
    newPassword = first + password + second
    newPassword = newPassword.replace("a", "@", 2)
    newPassword = newPassword.replace("e", "3", 2)
    newPassword = newPassword.replace("o", "0", 1)
    newPassword = newPassword.replace("i", "!", 2)
    for i in newPassword:
        num = randint(1,100)%2
        if(num != 0):
            if i in consonants:
                finalPass += i.upper()
        else:
            finalPass += i
    print("Generated Password: " + finalPass)


def main():
    open("./Vault.txt", "w")
    createUsername()
    createPassword()
    
createPassword()
