def caesar_encrypt(str, n):
	enc_text = ""
	for ch in str:
		letter_as_num = ord(ch) + n
		if ch.islower():
			if letter_as_num > ord('z'):
				letter_as_num -= 26
			elif letter_as_num < ord('a'):
				letter_as_num += 26
			enc_text += chr(letter_as_num)
		elif ch.isupper():
			if letter_as_num > ord('Z'):
				letter_as_num -= 26
			elif letter_as_num < ord('A'):
				letter_as_num += 26
			enc_text += chr(letter_as_num)
		else:
			enc_text += ch
	return enc_text


print caesar_encrypt("abc", 1)
print caesar_encrypt("ABC", 1)
print caesar_encrypt("abc", 2)
print caesar_encrypt("aaa", 7)
print caesar_encrypt("xyz", 1)
print caesar_encrypt("abcd1ss4 45fA@A", 27)
print caesar_encrypt("abc", -3)