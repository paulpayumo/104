#EE104 Project (Password Generator)

username = 0
password = 0

def createUsername():
    while(len(username) == 0):
        username = input("Please enter a username: ")

def createPassword():
    while(len(password) < 10):
        password = input("Please enter a 10 lettered password: ")
    
    return(password)

def main():
    open("./Vault.txt", "w")
    createUsername()
    createPassword()
    

main()
