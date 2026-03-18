
def garden_operations() -> None:
    try:
        int("abc")
    except ValueError as e:
        print(e)
    try:
        10/0
    except ZeroDivisionError as e:
        print(e)
    try:
        open("folder/error")
    except FileNotFoundError as e:
        print(e)
    try:
        dictionary = {"key": 26}
        dictionary["not_found"]
    except KeyError as e:
        print(e)


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===\n")
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
    print("Testing ZeroDivisionError...")
    try:
        126/0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt")
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file or directory:"
              " 'missing.txt'\n")
    print("Testing KeyError...")
    try:
        dictionary = {"key": 26}
        dictionary["missing_plant"]
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")
    print("Testing multiple errors together...")
    try:
        open("not_a_file.txt")
    except (KeyError, FileNotFoundError):
        print("Caught an error, but program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
