import os
import re
import sys
from DES import *

loop = True

def cls():
	os.system('cls' if os.name=='nt' else 'clear')

def print_main_menu():
	print(30 * "-" , "DES" , 30 * "-")
	print("Choose if you want to encrypt or decrypt data:")
	print("1. Encrypt")
	print("2. Decrypt")
	print(67 * "-")

	choice = input("Enter your choice [1 or 2]: ")

	cls()

	if choice == "1":
		print_message_menu(True)

	elif choice == "2":
		print_message_menu(False)

	else:
		input("Wrong option selection. Enter any key to try again.")

def print_message_menu(encrypt):
	print(30 * "-" , "MESSAGE" , 30 * "-")
	message_file_path = input("Enter the path to the message file: ")
	print(67 * "-")

	cls()

	if os.path.isdir(message_file_path):
		input("Target path is a directory. Enter any key to try again..")

	elif os.path.exists(message_file_path) == False:
		input("Target path doesn't exist. Enter any key to try again..")

	elif os.path.exists(message_file_path) and os.path.isdir(message_file_path) == False:
		print_key_menu(encrypt, message_file_path)

	else:
		input("Wrong option selection or invalid DES message. Enter any key to try again.")

def print_key_menu(encrypt, message_file_path):
	print(30 * "-" , "KEY" , 30 * "-")
	key_file_path = input("Enter the path to the key file: ")
	print(67 * "-")
	
	cls()

	if os.path.isdir(key_file_path):
		input("Target path is a directory. Enter any key to try again..")

	elif os.path.exists(key_file_path) == False:
		input("Target path doesn't exist. Enter any key to try again..")

	elif os.path.exists(key_file_path) and os.path.isdir(key_file_path) == False:
		print_output_menu(encrypt, message_file_path, key_file_path)

	else:
		input("Wrong option selection or invalid DES key. Enter any key to try again..")

def print_output_menu(encrypt, message_file_path, key_file_path):
	print(30 * "-" , "OUTPUT" , 30 * "-")
	output_file_path = input("Enter the path to the output directory: ")
	print(67 * "-")
	
	cls()

	if os.path.exists(output_file_path) == True and os.path.isdir(output_file_path):
		write_output(encrypt, key_file_path, message_file_path, output_file_path)

	else:
		input("Wrong path entered. Enter any key to try again..")

def write_output(encrypt, key_file_path, message_file_path, output_file_path):
	output_file = open(os.path.join(output_file_path, "Output.txt"), "w+")
	
	message_file = open(message_file_path, "r")
	
	key_file = open(key_file_path, "r")
	
	message = message_file.read()
	key = key_file.read()
	
	if(encrypt): output = DES_encrypt(message, key)
	else: output = DES_decrypt(message, key)
	
	output_file.write(output)
	
	message_file.close()
	
	key_file.close()
	
	output_file.close()

### MAIN LOOP ###
while loop:
	print_main_menu()