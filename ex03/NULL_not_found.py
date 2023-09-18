def NULL_not_found(object: any) -> int:
	obj_type = type(object)

	if object is None:
		print(f"Nothing: {object} {obj_type}")
		return 0
	elif obj_type == float and str(object) == 'nan':
		print(f"Cheese: {object} {obj_type}")
		return 0
	elif obj_type == int and object == 0:
		print(f"Zero: {object} {obj_type}")
		return 0
	elif obj_type == str and object == '':
		print(f"Empty: {object} {obj_type}")
		return 0
	elif obj_type == bool and not object:
		print(f"Fake: {object} {obj_type}")
		return 0
	
	print("Type not found")
	return 1