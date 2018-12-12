from Extract_ConstantesDES import recupConstantesDES

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

def generate_keys(key_64bits, cp1, cp2):
	round_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

	rounded_keys = list() 
	converted_cp1 = cp1_conversion(cp1, key_64bits) 
	left, right = split_in_half(converted_cp1)

	for round in range(16):
		new_left = circular_left_shift(left, round_shifts[round])
		new_right = circular_left_shift(right, round_shifts[round])
		rounded_key = cp2_conversion(cp2, new_left + new_right)
		rounded_keys.append(rounded_key)
		left = new_left
		right = new_right

	return rounded_keys

############ END SUBKEY GENERATION ############

def expand(expansion_table, bits32):
	""" Takes a 32-bits binary string as input and outputs a 48-bits binary string"""
	bits48 = ""

	for index in expansion_table:
		bits48 += bits32[index-1]

	return bits48

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

def functionF(expansion_table, permutation_table, pre_32bits, key_48bits):	
	""" Main function """
	result = ""
	expanded_left_half = expand(expansion_table,pre_32bits)
	xor_value = XOR(expanded_left_half, key_48bits)
	bits6_list = split_in_(6, xor_value)

	for S_count, bits6 in enumerate(bits6_list):
		first_last = bits6[0] + bits6[-1]
		middle4 = bits6[1:5]
		sboxvalue = S_search(S_count,first_last,middle4)
		result += sboxvalue

	return permute(permutation_table, result)

def S_search(nb_S, first_last, middle4):  
	""" Takes three parameters, accesses the S matrix and returns the value """
	d_first_last = binary_to_decimal(first_last)
	d_middle = binary_to_decimal(middle4)
	
	sbox_value = SBOX[nb_S][d_first_last][d_middle]
	return decimal_to_binary(sbox_value)
	##############TODO

path = "C:/Users/Olivier/source/repos/CryptoDES/CryptoDES/Input/"

constDES = recupConstantesDES()

f1 = open(path + "Clef1.txt", "r")
key = f1.read()
f1.close()

f2 = open(path + "MDES1.txt", "r")
mdes = f2.read()
f2.close()

key_56bits = cp1_conversion(constDES["CP_1"], key)
print("key_56bits : " + key_56bits)

left_half, right_half = split_key_in_half(key_56bits)
print("left_half : " + left_half)
print("right_half : " + right_half)

key_48bits = cp2_conversion(constDES["CP_2"], key_56bits)

print("key_48bits : " + key_48bits)
print((left_half + right_half) == key_56bits)

#out_bits48 = expand(constDES["E"], bits32)
#print(out_bits48)

bits1 = '1100'
bits2 = '1010'
print(XOR(bits1, bits2))

print(split_in(6, "010101010101010101010101010101010101010101010101"))