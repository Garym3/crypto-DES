from Extract_ConstantesDES import recupConstantesDES


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

def left_shifting(left_bits, right_bits):
	""" Left shifts the given bit string according to the number of bits """
	
	left_bits << 1
	right_bits << 1

	return left_bits[numberofbits:] + right_bits[:numberofbits]

def cp2_conversion(cp2, key_56bits):
	""" Combines both half as input and returns a 48 bits string """
	key_48bits = ""

	for i in cp2:
		for j in i:
			key_48bits += key_56bits[j]

	return key_48bits

path = "C:/Users/Olivier/source/repos/CryptoDES/CryptoDES/Input"

constDES = recupConstantesDES()

f1 = open(path + "/Clef1.txt", "r")
key = f1.read()
f1.close()

f2 = open(path + "/MDES1.txt", "r")
mdes = f2.read()
f2.close()

key_56bits = cp1_conversion(constDES["CP_1"], key)
print("key_56bits : " + key_56bits)

left_half, right_half = split_key_in_half(key_56bits)
print("left_half : " + left_half)
print("right_half : " + right_half)
  
shifted_bits = left_shifting(left_half, right_half)
print("shifted_bits : " + shifted_bits)

key_48bits = cp2_conversion(constDES["CP_2"], key_56bits)

print("key_48bits : " + key_48bits)
print((left_half + right_half) == key_56bits)