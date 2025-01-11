

    # Decorate an iterable object, returning an iterator which acts exactly
    # like the original iterable, but prints a dynamically updating
    # progressbar every time a value is requested.

def ft_tqdm(lst: range) -> None:
	"""Decorate an iterable object, returning an iterator which acts exactly
	 like the original iterable, but prints a dynamically updating
     progressbar every time a value is requested.

	Args:
		lst (range): A range object
	"""
	start = "["
	end = "]"
	bar_length = 50
	WHITE_BG = "\033[47m"  # White background
	RESET = "\033[0m"      # Reset formatting
	try:
		for item in lst:
			percentage = round((item / (lst.stop)) * 100)
			complete = round(percentage/ 100 * bar_length)
			uncomplete = bar_length - complete
			colored_part = WHITE_BG + " " * complete + RESET
			uncolored_part = " " * uncomplete
			bar = colored_part + uncolored_part
			yield(print(f"\r{percentage}%|{start}{bar}{end}| {item + 1}/{lst.stop}",end=""))
	except Exception as e:
		print(e)
     
