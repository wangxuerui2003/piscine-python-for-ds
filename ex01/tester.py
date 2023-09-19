from array2D import slice_me

""" Basic tests """
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))


""" Not a list test """
print()
family = 123
print(slice_me(family, 0, 1))


""" Lists not same size test """
print()
family = [[1, 2],
          [1, 2, 3]]
print(slice_me(family, 0, 1))


""" family not 2d list test """
print()
family = [1, 2, 3]
print(slice_me(family, 0, 1))


""" invalid slicing index """
print()
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 'a', 'b'))