
def garden_operations() -> None:
    """
    Simulates various garden-related operations to demonstrate exception
    handling.

    This function intentionally triggers common Python exceptions (ValueError,
    ZeroDivisionError, FileNotFoundError, and KeyError) and catches them using
    try-except blocks. This ensures the execution flow is not interrupted by
    runtime errors.
    """
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError:
        # Adapted to a simpler message
        print("Caught ValueError: invalid literal for int()\n")

    print("Testing ZeroDivisionError...")
    try:
        # Used the dummy variable(it will keep information but won't use it)
        _ = 10/0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    file = "missing.txt"
    try:
        open(f"{file}")
    except FileNotFoundError:
        # Adapted to a simpler message
        print(f"Caught FileNotFoundError: No such file '{file}'\n")

    print("Testing KeyError...")
    dictionary = {"key": 26}
    try:
        dictionary["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        open("missing_plant.txt")
    except (ValueError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    """
    Main test runner for demonstrating garden error types.

    It initializes the demo and confirms the program's resilience after
    all operations are completed.
    """
    print("=== Garden Error Types Demo ===\n")
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
