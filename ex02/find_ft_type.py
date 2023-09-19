def all_thing_is_obj(object: any) -> int:
	obj_type = type(object)
	obj_type_name: str = obj_type.__name__
	
	if obj_type == str:
		print(f'{object} is in the kitchen : {obj_type}')
	elif isinstance(object, (list, dict, tuple, set)):
		print(f'{obj_type_name.title()} : {obj_type}')
	else:
		print('Type not found')
	return 42
