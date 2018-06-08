

key = "abcdefghijklmnopqrstuvwxyz"


def encrypt(txt,shift):
	result = ''
	for char in txt.lower():
		i = (key.index(char) + shift) % 26
		result+= key[i]
	return result

def decrypt(ct,shift):
	result = ''
	for char in ct:
		i = (key.index(char) - shift) % 26
		result+= key[i]
	return result


txt = input("enter the string")
shift = 3


print("plain text is : ",txt)


ct = encrypt(txt,shift)
print("encrypted text is : ",ct)


print("decrypt text is ",decrypt(ct,shift))
