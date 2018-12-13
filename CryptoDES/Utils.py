def get_first_and_last_bit(bits):
	""" Returns first and last bit from a binary string """
	return bits[0] + bits[-1]

def get_middle_four_bit(bits):
	""" Returns first and last bit from a binary string """
	return bits[1:5]

def binary_to_decimal(binary_bits):
	""" Converts binary bits to decimal """
	return int(binary_bits,2)

def decimal_to_binary(decimal):
	""" Converts decimal to binary bits """
	return bin(decimal)[2:].zfill(4)

def hex_Digit_to_binary_bits(hex_digit):
	return HEX_to_Binary[hex_digit]

def hex_String_to_binary_bits1(hex_string):
	binary_bits = ""

	for hex_digit in hex_string:
		binary_bits += hex_Digit_to_binary_bits(hex_digit)

	return binary_bits

def hex_String_to_binary_bits2(hex_digits):
	binary_digits = ""

	for hex_digit in hex_digits:
		binary_digits += bin(int(hex_digit,16))[2:].zfill(4)

	return binary_digits
