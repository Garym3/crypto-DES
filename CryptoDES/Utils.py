def get_first_and_last_bit(bits):
	""" Returns first and last bit from a binary string """
	return bits[0] + bits[-1]

def get_middle_four_bit(bits):
	""" Returns second to fifth bits """
	return bits[1:5]

def binary_to_decimal(binary_bits):
	""" Converts binary bits to decimal """
	return int(binary_bits,2)

def decimal_to_binary(decimal):
	""" Converts decimal to binary bits """
	return bin(decimal)[2:].zfill(4)

def string_to_dict(text):
	dictionary = dict()

	for i in range(0, len(text)): dictionary[i] = int(text[i])
	
	return dictionary

def permute_dicts(m1, m2) :
	m3 = dict()
	
	for i in range (0, len(m2)): m3[i] = m1[m2[i]]
		
	return m3

def split_dict_in_half(dictionary):
	length = len(dictionary)
	half_length = length / 2
	
	left_half = dict()
	right_half = dict()
	
	for i in dictionary :
		if(i < half_length) :
			left_half[i] = dictionary[i]
		else :
			right_half[i % half_length] = dictionary[i]
			
	return left_half, right_half

def split_in(nb_bits, XOR_48bits):
	return [XOR_48bits[i:i + nb_bits] for i in range(0, len(XOR_48bits), nb_bits)]

def split_in_half(bits):
	return bits[:32], bits[32:]

def merge_bits(first_bits, second_bits):
	return first_bits + second_bits

def merge_two_dicts(d1, d2):
	d3 = dict()
	pos = 0
	
	for i in range(0, len(d1)) :
		d3[pos] = d1[i]
		pos += 1
		
	for i in range(0, len(d2)) :
		d3[pos] = d2[i]
		pos += 1
		
	return d3