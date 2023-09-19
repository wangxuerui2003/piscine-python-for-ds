import sys


def count_upper(string: str) -> int:
    """
        return the number of upper letters in a string
    """

    return sum(1 for c in string if c.isupper())


def count_lower(string: str) -> int:
    """ return the number of lower letters in a string """

    return sum(1 for c in string if c.islower())


def count_spaces(string: str) -> int:
    """
        return the number of spaces in a string
    """

    return sum(1 for c in string if c.isspace())


def count_digits(string: str) -> int:
    """
        return the number of digits in a string
    """

    return sum(1 for c in string if c.isdigit())


def count_punctuations(string: str) -> int:
    """
        return the number of punctuations in a string
    """

    punctuation_chars = '''!()-[]{};:'"\\,<>./?@#$%^&*_~'''
    return sum(1 for c in string if c in punctuation_chars)


def main():
    """
        Main function
    """

    try:
        assert len(sys.argv) <= 2, "more than one argument is provided"
    except AssertionError as e:
        print("AssertionError:", e)
        sys.exit()

    string = ''
    if len(sys.argv) < 2:
        try:
            print("What is the text to count?")
            string = sys.stdin.readline()
        except EOFError:
            pass
    else:
        string = sys.argv[1]

    print(f"The text contains {len(string)} characters!")
    print(count_upper(string), "upper letters")
    print(count_lower(string), "lower letters")
    print(count_punctuations(string), "punctuation marks")
    print(count_spaces(string), "spaces")
    print(count_digits(string), "digits")


if __name__ == '__main__':
    main()
