from cryptography.fernet import Fernet

master_pwd = input("Master Password?: ")
phone_num = input("What is your phone number?: ")

def load_key():
    file = open("Password + Image Manipulation\key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key() + master_pwd.encode()
fer = Fernet(key)

def view():
    with open('Password + Image Manipulation\passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User: " + user + " | Password: " + fer.decrypt(passw.encode()).decode())

def add():
    name = input("Username: ")
    pwd= input("Password: ")

    with open('Password + Image Manipulation\passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("\nAdd new password or view existing passwords? (A = Add, V = View, Q = Quit): ").upper()
    if mode == "Q":
        print("Good bye")
        break
    if mode == "V":
        view()
    elif mode == "A":
        add()
    else:
        print("Invalid mode")