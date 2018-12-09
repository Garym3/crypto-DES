import os
import re

def print_main_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    print("Choose if you want to encrypt or decrypt data:")
    print("1. Encrypt")
    print("2. Decrypt")
    print(67 * "-")

    choice = input("Enter your choice [1-2]: ")
     
    if choice == "1":     
        print("Encryption has been selected")
        print_encrypt_menu()

    elif choice == "2":
        print("Decryption has been selected")
        print_decrypt_menu()

    else:
        input("Wrong option selection. Enter any key to try again..")


def print_encrypt_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    choice = input("Enter the path to the file to encrypt: ")
    print(67 * "-")
    regex = re.compile('[^0-1]')
     
    if os.path.isdir(choice):     
        input("Target path is a directory. Enter any key to try again..")

    elif os.path.exists(choice) == False:
        input("Target path doesn't exist. Enter any key to try again..")

    elif os.path.exists(choice) and os.path.isdir(choice) == False:
        print_encrypt_menu()

    else:
        input("Wrong option selection or invalid DES message. Enter any key to try again..")


def print_decrypt_menu():                                             
    print(30 * "-" , "MENU" , 30 * "-")
    choice = input("Enter the path to the file to decrypt: ")
    print(67 * "-")
    regex = re.compile('[^0-1]')
     
    if os.path.isdir(choice):     
        input("Target path is a directory. Enter any key to try again..")

    elif os.path.exists(choice) == False:
        input("Target path doesn't exist. Enter any key to try again..")

    elif os.path.exists(choice) and os.path.isdir(choice) == False:
        print_fourth_menu()

    else:
        input("Wrong option selection or invalid DES message. Enter any key to try again..")


def print_key_encrypt_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    choice = input("Enter the path to the key: ")
    print(67 * "-")
    regex = re.compile('[^0-1]')
     
    if os.path.isdir(choice):     
        input("Target path is a directory. Enter any key to try again..")

    elif os.path.exists(choice) == False:
        input("Target path doesn't exist. Enter any key to try again..")

    elif os.path.exists(choice) and os.path.isdir(choice) == False:
        print_fourth_menu()

    else:
        input("Wrong option selection or invalid DES key. Enter any key to try again..")


def print_key_decrypt_menu():
    print(30 * "-" , "MENU" , 30 * "-")
    choice = input("Enter the path to the key: ")
    print(67 * "-")
    regex = re.compile('[^0-1]')
     
    if os.path.isdir(choice):     
        input("Target path is a directory. Enter any key to try again..")

    elif os.path.exists(choice) == False:
        input("Target path doesn't exist. Enter any key to try again..")

    elif os.path.exists(choice) and os.path.isdir(choice) == False:
        print_fourth_menu()

    else:
        input("Wrong option selection or invalid DES key. Enter any key to try again..")


#TODO Implémenter menus pour demander le type de retour du message chiffré/déchiffré
#TODO Implémenter la logique
 
    
loop=True      
  
while loop:
    print_main_menu()
    