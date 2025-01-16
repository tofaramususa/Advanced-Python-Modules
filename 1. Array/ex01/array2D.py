






def slice_me(family: list, start: int, end: int) -> list: #your code here
	

	try:
		if isinstance(family, list) is False:
			raise ValueError("The parameter is not a list")
		if len(family) == 0:
			raise ValueError("The list is empty")
		if not all(len(row) == len(family[0]) for row in family):
			raise ValueError("The list items are not the same size")
		if not all(isinstance(row, list) for row in family):
			raise ValueError("One of the list items are not a list ")
		
		print(f"My shape is : ({len(family )}, {len(family[0])})");
		new_shape = family[start:end]
		print(f"My new shape is : ({len(new_shape) if new_shape else 0}, {len(new_shape[0]) if new_shape else 0})");
		return(new_shape if new_shape else [])
	except Exception as e:
		print(e)
		return([])









