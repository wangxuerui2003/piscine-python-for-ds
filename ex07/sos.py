import sys

NESTED_MORSE = {
    ' ': '/ ',
    'A': '.- ',
    'B': '-... ',
    'C': '-.-. ',
    'D': '-.. ',
    'E': '. ',
    'F': '..-. ',
    'G': '--. ',
    'H': '.... ',
    'I': '.. ',
    'J': '.--- ',
    'K': '-.- ',
    'L': '.-.. ',
    'M': '-- ',
    'N': '-. ',
    'O': '--- ',
    'P': '.--. ',
    'Q': '--.- ',
    'R': '.-. ',
    'S': '... ',
    'T': '- ',
    'U': '..- ',
    'V': '...- ',
    'W': '.-- ',
    'X': '-..- ',
    'Y': '-.-- ',
    'Z': '--.. ',
    '0': '----- ',
    '1': '.---- ',
    '2': '..--- ',
    '3': '...-- ',
    '4': '....- ',
    '5': '..... ',
    '6': '-.... ',
    '7': '--... ',
    '8': '---.. ',
    '9': '----. '
}


def main():
    """
        Main function
    """

    try:
        assert len(sys.argv) == 2, "the arguments are bad"

        string = sys.argv[1]

        for c in string:
            assert c.isalnum() or c == ' ', "the arguments are bad"

        for i in range(len(string)):
            morse_code = NESTED_MORSE[string[i].upper()]
            if i == len(string) - 1:
                print(morse_code.strip())
            else:
                print(morse_code, end='')

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == '__main__':
    main()
