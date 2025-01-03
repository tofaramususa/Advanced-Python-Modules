import math 

def NULL_not_found(object: any) -> int:
	"""Prints all types of null

	Args:
		object (any): takes in an object of any type

	Returns:
		int: either 0 or 1
	"""
	try:
		if object is None:
			print(f"Nothing: {object} {type(object)}")
		elif isinstance(object, float) and math.isnan(object):
			print(f"Cheese: {object} {type(object)}")
		elif isinstance(object, bool) and bool(object) is False:
			print(f"Fake: {object} {type(object)}")
		elif isinstance(object, int) and bool(object) is False:
			print(f"Zero: {object} {type(object)}")
		elif isinstance(object, str) and object == '':
			print(f"Empty: {object} {type(object)}")
		else:
			raise Exception("Type not Found")
	except Exception as e:
		print(e)
		return 1
	return 0

# //refactor
# def NULL_not_found(object: any) -> int:
# 	"""Prints all types of null

# 	Args:
# 		object (any): takes in an object of any type

# 	Returns:
# 		int: either 0 or 1
# 	"""
# 	null_cases = {
#             "Nothing": lambda x: x is None,
#             "Garlic": lambda x: isinstance(x, float) and math.isnan(x),
#             "Fake": lambda x: isinstance(x, bool) and not x,
#             "Zero": lambda x: isinstance(x, int) and not x,
#             "Empty": lambda x: isinstance(x, str) and x == '',
#         }
# 	try:
# 		for label, condition in null_cases.items():
# 			if condition(object):
# 				print(f"{label}: {object} {type(object)}")
# 				return 0
# 		raise Exception("Type not Found")
# 	except Exception as e:
# 		print(e)
# 		return 1
	# return 0