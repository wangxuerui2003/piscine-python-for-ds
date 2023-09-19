import sys


if len(sys.argv) < 2:
    sys.exit()

try:
    assert len(sys.argv) <= 2, "more than one argument is provided"

    try:
        num = int(sys.argv[1])
        print("I'm Even" if num % 2 == 0 else "I'm Odd")
    except ValueError:
        raise AssertionError("argument is not an integer")
except AssertionError as e:
    print("AssertionError:", e)
