def all_thing_is_obj(object: any) -> int:
	obj_type = type(object)
	obj_type_name: str = obj_type.__name__
	
	if obj_type_name == 'str':
		print(f'{object} is in the kitchen : {obj_type}')
		return 42
	
	if obj_type_name in ['list', 'dict', 'set', 'tuple']:
		print(f'{obj_type_name.title()} : {obj_type}')
		return 42

	print('Type not found')
	return 42