import random

# Try to assign the same number of pages for each letter
alphabet = {'a': [],
			'b': [],
			'c': [],
			'd': [],
			'e': [],
			'f': [],
			'g': [],
			'h': [],
			'i': [],
			'j': [],
			'k': [],
			'l': [],
			'm': [],
			'n': [],
			'o': [],
			'p': [],
			'q': [],
			'r': [],
			's': [],
			't': [],
			'u': [],
			'v': [],
			'w': [],
			'x': [],
			'y': [],
			'z': [],
			}

input_message = raw_input('Input Message: ')

output_message = ''
for character in input_message:
	try:
		output_message += '%s ' % random.choice(alphabet[character])
	except:
		continue
print(output_message)
