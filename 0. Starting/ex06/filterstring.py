import sys



def filterstring(string: str, integer: int):
	"""return a new array with words whose length is greater than integer

	Args:
		string (str): string with words
		integer (int): length to be compared with
	"""
	if string is None or integer is None:
		return None
	if not isinstance(string, str) or not isinstance(integer, int):
		return None
	string_array = string.split()
	filtered_string = [word for word in string_array if (lambda x: len(x) > integer)(word)]
	return filtered_string
	

def main():
	"""Main function to run and test the filterstring function
	"""
	try:
		if len(sys.argv) != 3:
			raise AssertionError("Assertion Error: The arguments are bad")
		string = str(sys.argv[1])
		integer = int(sys.argv[2])
		print(filterstring(string, integer))
	except Exception:
		print("AssertionError: the arguments are bad")
     
     
			
    







if __name__ == '__main__':
    main()