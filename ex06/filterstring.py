from ft_filter import ft_filter
import sys


def main():
    """
        Main function
    """

    try:
        assert len(sys.argv) == 3, "the arguments are bad"

        try:
            length = int(sys.argv[2])

            words_list = sys.argv[1].split()
            for word in words_list:
                assert word.isalnum(), "the arguments are bad"
            print(ft_filter(lambda word: len(word) > length, words_list))
        except ValueError:
            raise AssertionError("the arguments are bad")

    except AssertionError as e:
        print("AssertionError:", e)


if __name__ == '__main__':
    main()
