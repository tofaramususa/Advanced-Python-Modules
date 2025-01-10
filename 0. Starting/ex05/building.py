import sys


def count_characters(string: str) -> dict:
	"""Counts the number of characters
	Args:
		string (str): the string to count characters
		characterDict (dict): dict holding information about the characters counted
	"""
	characterDict = {
		"Upper letters": 0,
		"Lower letters": 0,
		"Punctuation Marks": 0,
		"Spaces": 0,
		"Digits": 0,
	}
	for char in string:
		if char.isupper():
			characterDict["Upper letters"] += 1
		if char.islower():
			characterDict["Lower letters"] += 1
		if char in "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~":
			characterDict["Punctuation Marks"] += 1
		if char.isspace():
			characterDict["Spaces"] += 1
		if char.isdigit():
			characterDict["Digits"] += 1
	return characterDict


def main() -> None:
    """Main function to count the number and type of characters in a string

    Raises:
            AssertionError: There is no string inputted or passed in
    """
    try:
        string = None
        if len(sys.argv) < 2 or sys.argv[1] == "":
            string = input("Enter a string to count: ") + " "
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        string = sys.argv[1] if string is None else string
        characterDict = count_characters(string)
        print(f"The text contains {len(string)} characters")
        for key, value in characterDict.items():
            print(f"{value} {key}")
    except Exception as e:
        if isinstance(e, AssertionError):
            print("AssertionError: {e}")
        elif isinstance(e, EOFError):
            string = string.rstrip()

if __name__ == "__main__":
    main()
