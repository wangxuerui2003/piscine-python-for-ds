from give_bmi import give_bmi, apply_limit


def main():
    """ Basic test """
    height = [2.71, 1.15]
    weight = [165.3, 38.4]

    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))

    """ Different size test """
    print()
    height = [1.75, 1.80, 1.85]
    weight = [123, 123]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)

    """ Invalid data type test """
    print()
    height = [1.75, 1.80, 'abc']
    weight = [123, 123, 123]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)

    """ Dimension too high test """
    print()
    height = [[1.75, 1.80], [1.70, 1.85]]
    weight = [123, 123]
    try:
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(e)


if __name__ == '__main__':
    main()
