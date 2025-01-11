import sys

def sos(string: str):
	"""Takes in a string and translates it to morse code

	Args:
		string (str): A string to be translated to morse code
	"""
	NESTED_MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
    '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/' }

	morse_code = ""
	for char in string:
		if char.upper() in NESTED_MORSE:
			morse_code += NESTED_MORSE[char.upper()] + " "
 
	return morse_code

def main():
	
	try:
		if len(sys.argv) != 2:
			raise AssertionError("Assertion Error: The arguments are bad")
		if not sys.argv[1].replace(" ", "").isalpha():
			raise AssertionError("Assertion Error: The arguments are bad")
		print(sos(sys.argv[1]))
	except Exception:
		print("AssertionError: the arguments are bad")






if __name__ == '__main__':
	main()