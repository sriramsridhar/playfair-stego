from playfair import *
def make_key(message):
	k = message
	key = []
	for char in k:
		if char in alpha and char not in key: 
			key.append(char)
		elif char is "J": 
			key.append("I")
	for char in alpha:
		if char not in key:
			key.append(char)
	return key
k = make_key("test_data")
print "\nKeyed PLAYFAIR matrix:\n"
m = gen_matrix(k)
print_matrix(m)
decision = ""
def get_message(message):
	m = message
	m2 = []
	for char in m.upper():
		if char in alpha: 
			m2.append(char)
		elif char == "J": 
			m2.append("I") 
		elif char == ".": 
			m2.append("X")
	return ''.join(m2)
def play_from(fire):
	print "\nEncrypt Message:"
	print "Enter the message you would like to encrypt. \nThe only valid characters are the letters A-Z. \nPeriods may be denoted with an X"
	message = get_message(fire)
	ciphertext = encrypt(message, m)
	cipher2_text=get_message(ciphertext)
	cipher2 = encrypt(cipher2_text, m)
	return cipher2
def play_to(stopfire):
	print "\nDecrypt Message:"
	print "Enter the message you would like to decrypt. \nThe only valid characters are the letters A-Z."
	message = get_message(stopfire)
	plaintext = decrypt(message, m)
	message2 =get_message(plaintext)
	plaintext2=decrypt(message2,m)
	return plaintext2
#t=play_from("helloguyz")
#print t
#t=play_to("HELXLOGUVW")
#print t