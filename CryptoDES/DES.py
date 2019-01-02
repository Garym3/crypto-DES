from Extract_ConstantesDES import recupConstantesDES
from ConvAlphaBin import *
from Utils import *


constDES = recupConstantesDES()

### Shifts a bit to the left ###
def left_shifting(dictionary) :
	shifted_dict = dict()
	
	for i in range(0, len(dictionary)) :
		j = i - 1
		if j == -1 : j = len(dictionary) - 1
		shifted_dict[j] = dictionary[i]
		
	return shifted_dict


### Permutes and splits the key into a subset of 16 keys then permutes them ###
def get_keys(key) :
	dict_key = string_to_dict(key)
	permuted_key = permute_dicts(dict_key, constDES["CP_1"][0])

	keys = dict()
	(left, right) = split_dict_in_half(permuted_key)
	
	for i in range(1, 17) :
		left = left_shifting(left)
		right = left_shifting(right)

		temp = merge_two_dicts(left, right)
		permuted_temp_key = permute_dicts(temp, constDES["CP_2"][0])
		keys[i] = permuted_temp_key
	
	return keys


### "Packages" the binary message into packets of 64 bits each. The ones that are not of 64 bits will be completed with zeros ###
def get_packets(bin_message) :
	packets = dict()
	index = -1
	
	for i in range(0, len(bin_message)) :
		if (i == 0 or i % 64 == 0) :
			index += 1
			packets[index] = dict()
		packets[index][i % 64] = bin_message[i]
	
	nb_packets = len(packets)
	length_last_packet = len(packets[nb_packets - 1])
	
	if (length_last_packet != 64) :
		for i in range (length_last_packet, 64) :
			packets[nb_packets - 1][i] = 0
		
	return packets


### XOR operation on two bits. Returns a dictionary representing the binary result of the XOR operation ###
def XOR(bits1, bits2):
	output = dict()
	
	for i in range(0, len(bits1)):
		sum = int(bits1[i]) + int(bits2[i])

		if (sum > 1): sum = 0

		output[i] = sum
	
	return output

### Processes the right part of the key and permutes it ###
def process_right(right, key) :
	new_right = XOR(permute_dicts(right, constDES["E"][0]), key)	
	blocks = get_blocks(new_right)
	
	for i in range(0, len(blocks)) :
		blocks[i] = handle_block(blocks[i], constDES["S"][i])

	index_right = 0		
	new_right = dict()
	
	for i in range(0, len(blocks)) :
		for j in range(0, len(blocks[i])) :
			new_right[index_right] = blocks[i][j]
			index_right += 1
			
	new_right = permute_dicts(new_right, constDES["PERM"][0])

	return new_right


###  ###
def circle(left, right, key) :
	new_right = process_right(right, key)
		
	new_right = XOR(new_right, left)
	
	return right, new_right


def uncircle(left, right, key) :
	old_right = process_right(left, key)
	
	old_left = XOR(right, old_right)
	
	return old_left, left


def handle_block(block, s_box) :
	temp = ""
	line = int(str(block[0]) + str(block[5]), 2)

	for i in range(1, 5): temp += str(block[i])

	column = int(temp, 2)	
	nb = decimal_to_binary(s_box[line][column])
	
	blocks = dict()
	
	for i in range(0, len(nb)): blocks[i] = nb[i]
	
	return blocks

def get_blocks(matrix) :
	blocks = dict()
	pos = 0
	blocks[pos] = dict()
	
	for i in range(0, len(matrix)) :
		if i != 0 and i % 6 == 0 :
			pos += 1
			blocks[pos] = dict()
			
		blocks[pos][i % 6] = matrix[i]

	return blocks

def DES_encrypt(message, key):
	bin_message = conv_bin(message)
	keys = get_keys(key)
	packets = get_packets(bin_message)
	enc = ""
	
	for i in range(0, len(packets)) :
		packets[i] = permute_dicts(packets[i], constDES["PI"][0])
		(left, right) = split_dict_in_half(packets[i]) 
		
		for j in range(0, 16): 
			(left, right) = circle(left, right, keys[j + 1])
		
		packets[i] = merge_two_dicts(left, right)
		packets[i] = permute_dicts(packets[i], constDES["PI_I"][0])
		
		for j in range(0, len(packets[i])): enc += str(packets[i][j])

	return nib_vnoc(enc)

def DES_decrypt(message, key):
	bin_message = conv_bin(message)
	keys = get_keys(key)
	packets = get_packets(bin_message)
	dec = ""
	
	for i in range(0, len(packets)) :
		packets[i] = permute_dicts(packets[i], constDES["PI"][0])
		(left, right) = split_dict_in_half(packets[i]) 
		
		for j in range(0, 16): 
			(left, right) = uncircle(left, right, keys[16 - j])
		
		packets[i] = merge_two_dicts(left, right)
		packets[i] = permute_dicts(packets[i], constDES["PI_I"][0])
		
		for j in range(0, len(packets[i])): dec += str(packets[i][j])

	return nib_vnoc(dec)

#path = "C:/Users/Olivier/source/repos/CryptoDES/CryptoDES/Input/"

#f1 = open(path + "Clef_de_Kaamelot.txt", "r")
#key = f1.read()
#f1.close()

#f2 = open(path + "Chiffrement_DES_de_Kaamelot.txt", "r")
#mdes = f2.read()
#f2.close()

#original = mdes
#decrypted = DES_decrypt(mdes, key)
#encrypted = DES_encrypt(decrypted, key)

#print(original == mdes)
#print(encrypted == original)