

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
	"""takes in weight and height and returns the bmi values as a list

	Args:
		height (list[int  |  float]): list of heights
		weight (list[int  |  float]): list of weights
  
	Note: BMI is weight divided by (height squared)
 
	Returns:
		list[int | float]: list of bmi values
	"""
	bmi_values = []
	try:
		if len(height) != len(weight):
			raise ValueError("the height and weight do not match")
		if isinstance(height, list) is False or isinstance(weight, list) is False:
			raise TypeError("The parameters should be lists") 
		for h_value, w_value in zip(height, weight):
			item = w_value / (h_value * h_value)
			bmi_values.append(item)
	except Exception as e:
		print(f"Error occurred {e}")
	return bmi_values

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
	"""_summary_

	Args:
		bmi (list[int  |  float]): _description_
		limit (int): _description_

	Returns:
		list[bool]: _description_
	"""
	try:
		if len(bmi) == 0:
			raise ValueError("the bmi values are empty")
		new_list = [True if item > limit else False for item in bmi]
		return new_list
	except Exception as e:
		print(f"Error occurred {e}")