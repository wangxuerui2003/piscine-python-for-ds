from load_image import ft_load

print(ft_load("../landscape.jpg"))
print(ft_load("../animal.jpeg"))
print(ft_load("../mario.png"))
# print(ft_load("../doge.jpg"))
# print(ft_load("../haha.jpg"))
# print(ft_load("../cat-meme.jpg"))

""" Invalid path"""
print(ft_load("../notexist.png"))
print(ft_load("tester.py"))
print(ft_load(123))
