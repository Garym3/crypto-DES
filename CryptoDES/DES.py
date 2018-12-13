from Extract_ConstantesDES import recupConstantesDES
from ConvAlphaBin import *
from Utils import *

constDES = recupConstantesDES()

############ SUBKEY GENERATION ############

def cp1_conversion(cp1, key_64bits):
	""" Converts a 64 bits key into a 56 bits key """
	key_56bits = ""

	for i in cp1:
		for j in i:
			key_56bits += key_64bits[j]

	return key_56bits

def split_key_in_half(key):
	""" Splits the key in half """
	left_key = key[:28]
	right_key = key[28:]
	return left_key, right_key

def left_shifting(bits, nb_bits):
	""" Left shifts the given bit string according to the number of bits """
	return bits[nb_bits:] + bits[:nb_bits]

def cp2_conversion(cp2, key_56bits):
	""" Combines both half as input and returns a 48 bits string """
	key_48bits = ""

	for i in cp2:
		for j in i:
			key_48bits += key_56bits[j]

	return key_48bits

def generate_keys(key_64bits):
	round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

	rounded_keys = list() 
	converted_cp1 = cp1_conversion(constDES["CP_1"], key_64bits) 
	left, right = split_in_half(converted_cp1)

	for round in range(16):
		new_left = left_shifting(left, round_shifts[round])
		new_right = left_shifting(right, round_shifts[round])
		rounded_key = cp2_conversion(constDES["CP_2"], new_left + new_right)
		rounded_keys.append(rounded_key)
		left = new_left
		right = new_right

	return rounded_keys

############ END SUBKEY GENERATION ############

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

def split_in(nb_bits, XOR_48bits):
	return [XOR_48bits[i:i + nb_bits] for i in range(0, len(XOR_48bits), nb_bits)]

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

def S_search(nb_S, first_to_last, mid_4bits):  
	""" Takes three parameters, accesses the S matrix and returns the value """
	dec_first_to_last = binary_to_decimal(first_to_last)
	dec_mid_4bits = binary_to_decimal(mid_4bits)
	
	return decimal_to_binary(constDES[nb_S][dec_first_to_last][dec_mid_4bits])

def apply_initial_p(PI_I, text):
	cipher = ""
	for i in PI_I:
		cipher += text[int(i)]
		print(cipher)

	return cipher

def split_in_half(binary_bits):
	return binary_bits[:32],binary_bits[32:]

def DES_encrypt(message, key):
	subKeys = getSubKeys(key)
	packets = getPacketsFromBinaryString(binaryString)
	
	for i in range(0, len(packets)) :
		packets[i] = permuteTwoMatrix(packets[i], const["PI"][0])
		(left, right) = splitDict(packets[i]) 
		
		for j in range(0, 16) :
			(left, right) = ronde(left, right, subKeys[j+1])
		
		packets[i] = concatenateDicts(left, right)
		packets[i] = permuteTwoMatrix(packets[i], const["PI_I"][0])
		
		for j in range(0, len(packets[i])) :
			s+=str(packets[i][j])
	return s


	#cipher = ""
	## Convert hex digits to binary
	#plaintext_bits = conv_bin(message)
	#key_bits = conv_bin(key)
	## Generate rounds key
	#round_keys = generate_keys(key_bits)
	##### DES steps
	
	### initial permutation
	#p_plaintext = apply_initial_p(constDES["PI_I"][0], plaintext_bits)
	### split in two half
	#L, R = split_in_half(p_plaintext)
	### start rounds
	#for round in range(16):
	#	newR = XOR(L, start(R, round_keys[round]))
	#	newL = R
	#	R = newR
	#	L = newL
	#return apply_initial_p(INVERSE_PERMUTATION_TABLE, R+L)



path = "C:/Users/Olivier/source/repos/CryptoDES/CryptoDES/Input/"

f1 = open(path + "Clef1.txt", "r")
key = f1.read()
f1.close()

f2 = open(path + "MDES1.txt", "r")
mdes = f2.read()
f2.close()

#print(constDES["PI_I"][0])

print(DES_encrypt("0123456789ABCDEF", "12345678ABCEDFF9"))


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