from give_bmi import give_bmi, apply_limit


print('""" Basic test """')
height = [2.71, 1.15]
weight = [165.3, 38.4]

bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print()
print('""" give_bmi different size test """')
height = [1.75, 1.80, 1.85]
weight = [123, 123]
give_bmi(height, weight)

print()
print('""" Invalid data type test """')
height = [1.75, 1.80, 'abc']
weight = [123, 123, 123]
give_bmi(height, weight)
apply_limit(['a', 'b'], 26)

print()
print('""" Dimension too high test """')
height = [[1.75, 1.80], [1.70, 1.85]]
weight = [123, 123]
give_bmi(height, weight)
apply_limit([[1, 2], [3, 4]], 26)

print()
print('""" Not same size lists test """')
height = [[1.75, 1.80, 1], [1.70, 1.85]]
weight = [123, 123]
give_bmi(height, weight)
apply_limit([[1, 2], [3, 4]], 26)

print()
print('""" Not a list test """')
height = 'a'
weight = [123, 123]
give_bmi(height, weight)
apply_limit(123, 26)
