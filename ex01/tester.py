from array2D import slice_me

print('""" Basic tests """')
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]

print(slice_me(family, 0, 2))
print(slice_me(family, 1, -2))


print()
print('""" Not a list test """')
family = 123
print(slice_me(family, 0, 1))


print()
print('""" Lists not same size test """')
family = [[1, 2],
          [1, 2, 3]]
print(slice_me(family, 0, 1))


print()
print('""" family not 2d list test """')
family = [1, 2, 3]
print(slice_me(family, 0, 1))
family = [[[1, 2, 3], [4, 5, 6]]]
print(slice_me(family, 0, 1))


print()
print('""" invalid slicing index """')
family = [[1.80, 78.4],
          [2.15, 102.7],
          [2.10, 98.5],
          [1.88, 75.2]]
print(slice_me(family, 'a', 'b'))
