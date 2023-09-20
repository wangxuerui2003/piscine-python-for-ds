from load_image import ft_load

print(ft_load("../landscape.jpg"))
print(ft_load("../animal.jpeg"))
print(ft_load("../mario.png"))
# print(ft_load("../doge.jpg"))
# print(ft_load("../cat-meme.jpg"))

print('""" Invalid path"""')
print(ft_load("../notexist.png"))  # not exist
print(ft_load("tester.py"))  # invalid format/extension
print(ft_load(123))  # invalid path datatype
