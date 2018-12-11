import os
import re
from DES import *

loop=True
encrypt=False

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def print_main_menu():
	print(30 * "-" , "DES" , 30 * "-")
	print("Choose if you want to encrypt or decrypt data:")
	print("1. Encrypt")
	print("2. Decrypt")
	print(67 * "-")

	choice = input("Enter your choice [1-2]: ")
	 
	if choice == "1":
		cls()
		encrypt=True
		print_encrypt_menu()

	elif choice == "2":
		cls()
		encrypt=False
		print_decrypt_menu()

	else:
		cls()
		input("Wrong option selection. Enter any key to try again..")


def print_encrypt_menu():
	print(30 * "-" , "ENCRYPTION" , 30 * "-")
	choice = input("Enter the path to the file to encrypt: ")
	print(67 * "-")
	regex = re.compile('[^0-1]')
	 
	if os.path.isdir(choice):
		cls()
		input("Target path is a directory. Enter any key to try again..")

	elif os.path.exists(choice) == False:
		cls()
		input("Target path doesn't exist. Enter any key to try again..")

	elif os.path.exists(choice) and os.path.isdir(choice) == False:
		cls()
		print_key_encrypt_menu()

	else:
		cls()
		input("Wrong option selection or invalid DES message. Enter any key to try again..")


def print_decrypt_menu():											 
	print(30 * "-" , "DECRYPTION" , 30 * "-")
	choice = input("Enter the path to the file to decrypt: ")
	print(67 * "-")
	regex = re.compile('[^0-1]')
	 
	if os.path.isdir(choice):
		cls()
		input("Target path is a directory. Enter any key to try again..")

	elif os.path.exists(choice) == False:
		cls()
		input("Target path doesn't exist. Enter any key to try again..")

	elif os.path.exists(choice) and os.path.isdir(choice) == False:
		cls()
		print_key_decrypt_menu()

	else:
		cls()
		input("Wrong option selection or invalid DES message. Enter any key to try again..")


def print_key_encrypt_menu():
	print(30 * "-" , "ENCRYPTION" , 30 * "-")
	choice = input("Enter the path to the key: ")
	print(67 * "-")
	regex = re.compile('[^0-1]')
	 
	if os.path.isdir(choice):
		cls()
		input("Target path is a directory. Enter any key to try again..")

	elif os.path.exists(choice) == False:
		cls()
		input("Target path doesn't exist. Enter any key to try again..")

	elif os.path.exists(choice) and os.path.isdir(choice) == False:
		cls()
		print_return_option_menu()

	else:
		cls()
		input("Wrong option selection or invalid DES key. Enter any key to try again..")


def print_key_decrypt_menu():
	print(30 * "-" , "DECRYPTION" , 30 * "-")
	choice = input("Enter the path to the key: ")
	print(67 * "-")
	regex = re.compile('[^0-1]')
	 
	if os.path.isdir(choice):
		cls()
		input("Target path is a directory. Enter any key to try again..")

	elif os.path.exists(choice) == False:
		cls()
		input("Target path doesn't exist. Enter any key to try again..")

	elif os.path.exists(choice) and os.path.isdir(choice) == False:
		cls()
		print_return_option_menu()

	else:
		cls()
		input("Wrong option selection or invalid DES key. Enter any key to try again..")

def print_return_option_menu():
	print(30 * "-" , "MENU" , 30 * "-")
	choice = input("Enter the path to the output file: ")
	print(67 * "-")
	regex = re.compile('[^0-1]')
	 
	if os.path.isdir(choice):
		cls()
		input("Target path is a directory. Enter any key to try again..")

	elif os.path.exists(choice) == False:
		cls()
		name = "Output.txt"

		print("Path does not exist. " + name + " file created in the Output directory.")
		f = open("Output/" + name, "w+")
		f.close()



		loop = False

	elif os.path.exists(choice) and os.path.isdir(choice) == False:
		cls()
		
		loop = False

	else:
		cls()
		input("Wrong path entered. Enter any key to try again..")


while loop:
	print_main_menu()