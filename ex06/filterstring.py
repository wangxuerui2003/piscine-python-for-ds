from ft_filter import ft_filter
import sys

try:
    assert len(sys.argv) == 3, "the arguments are bad"

    try:
        length = int(sys.argv[2])
        print(ft_filter(lambda word: len(word) > length, sys.argv[1].split()))
    except ValueError:
        raise AssertionError("the arguments are bad")

except AssertionError as e:
    print("AssertionError:", e)
