import sys

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    if len(sys.argv) < 2:
        sys.exit()

    is_num = True
    try:
        num = int(sys.argv[1])
        print("I'm Even" if num % 2 == 0 else "I'm Odd")
    except ValueError:
        is_num = False

    assert is_num, "argument is not an integer"

except AssertionError as e:
    print("AssertionError:", e)
