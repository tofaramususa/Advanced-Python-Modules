import sys


def main():
    try:
        if len(sys.argv) < 2:
            return print()
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        number = 0
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        result = "Even" if number % 2 == 0 else "Odd"
        print(f"l'm {result}")
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
