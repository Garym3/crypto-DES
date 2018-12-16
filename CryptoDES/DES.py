from Extract_ConstantesDES import recupConstantesDES
from ConvAlphaBin import *
from Utils import *


constDES = recupConstantesDES()

def cp1_conversion(cp1, key_64bits):
	""" Converts a 64 bits key into a 56 bits key """
	key_56bits = ""

	for i in cp1:
		for j in i:
			key_56bits += key_64bits[j]

	return key_56bits

def left_shifting(dictionary) :
	shifted_dict = dict()
	
	for i in range(0, len(dictionary)) :
		previous = i - 1
		if previous == -1 : previous = len(dictionary) - 1
		shifted_dict[previous] = dictionary[i]
		
	return shifted_dict

def cp2_conversion(cp2, key_56bits):
	""" Combines both half as input and returns a 48 bits string """
	key_48bits = ""

	for i in cp2:
		for j in i:
			key_48bits += key_56bits[j]

	return key_48bits

def get_keys(key) :
	dict_key = string_to_dict(key)
	permuted_key = permute_dicts(key, constDES["CP_1"][0])

	keys = dict()
	(left, right) = split_dict_in_half(permuted_key)
	
	for i in range(1, 17) :
		new_left = left_shifting(left)
		new_right = left_shifting(right)

		temp_matrix = merge_two_dicts(new_left, new_right)
		permuted_temp_key = permute_dicts(temp_matrix, constDES["CP_2"][0])
		keys[i] = permuted_temp_key
	
	return keys

def get_packets(bin_message) :
	packets = dict()
	index = -1
	
	for i in range(0, len(bin_message)) :
		if(i == 0 or i % 64 == 0) :
			index+=1
			packets[index] = dict()
		packets[index][i % 64] = bin_message[i]
	
	nb_packets = len(packets)
	length_last_packet = len(packets[nb_packets - 1])
	
	if(length_last_packet != 64) :
		for i in range (length_last_packet, 64) :
			packets[nb_packets - 1][i] = 0
		
	return packets

def expand(expansion_table, bits_32):
	""" Takes a 32-bits binary string as input and outputs a 48-bits binary string"""
	bits_48 = ""

	for i in expansion_table:
		bits_48 += bits_32[i]

	return bits_48

def XOR(bits1, bits2):
	""" XOR operation which returns the output """
	output = ""

	for i in range(len(bits1)):
		if bits1[i] == bits2[i]: 
			output += '0'
		else:
			output += '1'
	return output

def permute(permutation_table, S):
	""" Takes the S output and the permutation table and returns a 32 bits binary string """
	output_32bits = ""

	for i in permutation_table:
		output_32bits += S[i]

	return output_32bits

def start(expansion_table, permutation_table, key_32bits, key_48bits):	
	""" Main function """
	result = ""
	expanded_left_half = expand(expansion_table, key_32bits)
	xor_value = XOR(expanded_left_half, key_48bits)
	bits6_list = split_in_(6, xor_value)

	for S_count, bits6 in enumerate(bits6_list):
		first_last = bits6[0] + bits6[-1]
		middle4 = bits6[1:5]
		sboxvalue = S_search(S_count, first_last, middle4)
		result += sboxvalue

	return permute(permutation_table, result)

def circle(left, right, key) :
	new_right = XOR(permute_dicts(right, const["E"][0]), key)	
	blocks = get_blocks(new_right)
	
	for i in range(0, len(blocks)) :
		blocks[i] = handle_block(blocks[i], const["S"][i])

	index_right = 0		
	new_right = dict()
	
	for i in range(0, len(blocks)) :
		for j in range(0, len(blocks[i])) :
			new_right[index_right] = blocks[i][j]
			index_right += 1
			
	new_right = XOR(permute_dicts(new_right, const["PERM"][0]), key)
	
	return right, new_right

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
	blocks[pos]=dict()
	
	for i in range(0, len(matrix)) :
		if i != 0 and i % 6 == 0 :
			pos += 1
			blocks[pos] = dict()
			
		blocks[pos][i % 6] = matrix[i]

	return blocks

def S_search(nb_S, first_to_last, mid_4bits):  
	""" Takes three parameters, accesses the S matrix and returns the value """
	dec_first_to_last = binary_to_decimal(first_to_last)
	dec_mid_4bits = binary_to_decimal(mid_4bits)
	
	return decimal_to_binary(constDES[nb_S][dec_first_to_last][dec_mid_4bits])

def apply_initial_permutation(PI_I, text):
	cipher = ""

	for i in PI_I:
		cipher += text[int(i)]

	return cipher

def DES_encrypt(message, key):
	bin_message = conv_bin(message)

	keys = get_keys(key)
	packets = get_packets(bin_message)
	
	for i in range(0, len(packets)) :
		packets[i] = permute_dicts(packets[i], const["PI"][0])
		(left, right) = split_in_half(packets[i]) 
		
		for j in range(0, 16): (left, right) = circle(left, right, keys[j + 1])
		
		packets[i] = merge_bits(left, right)
		packets[i] = permute_dicts(packets[i], const["PI_I"][0])
		
		for j in range(0, len(packets[i])): s += str(packets[i][j])

	return s

path = "C:/Users/Olivier/source/repos/CryptoDES/CryptoDES/Input/"

f1 = open(path + "Clef1.txt", "r")
key = f1.read()
f1.close()

f2 = open(path + "MDES1.txt", "r")
mdes = f2.read()
f2.close()


print(DES_encrypt(mdes, key))


#key_56bits = cp1_conversion(constDES["CP_1"], key)
#print("key_56bits : " + key_56bits)

#left_half, right_half = split_key_in_half(key_56bits)
#print("left_half : " + left_half)
#print("right_half : " + right_half)

#key_48bits = cp2_conversion(constDES["CP_2"], key_56bits)

#print("key_48bits : " + key_48bits)
#print((left_half + right_half) == key_56bits)

##out_bits48 = expand(constDES["E"], bits32)
##print(out_bits48)

#bits1 = '1100'
#bits2 = '1010'
#print(XOR(bits1, bits2))

#print(split_in(6, "010101010101010101010101010101010101010101010101"))

#print(conv_bin("0123456789ABCDEF"))

#M = '0123456789ABCDEF' # plaintext in hexdecimal 16 digits so 64 bits 
#print(hex_String_to_binary_bits1(M))
## Output: 0000000100100011010001010110011110001001101010111100110111101111
#print(hexString_to_binary_bits2(M))
## Output: 0000000100100011010001010110011110001001101010111100110111101111