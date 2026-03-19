def check_temperature(temp_str: str) -> int | None:
    """
    Validates and processes a string input as a plant-safe temperature.

    This function attempts to convert the input string into an integer and
    checks if it falls within the acceptable range (0°C to 40°C). It handles
    formatting errors and out-of-range values by printing a descriptive
    message instead of crashing the program.

    Args:
        temp_str (str): A string representing the temperature to be checked.

    Returns:
        int | None: The temperature as an integer if valid;
                    None if the input is non-numeric or out of range.
    """
    try:
        num = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return
    if num < 0:
        print(f"Error: {num}°C is too cold for plants (min 0°C)")
        return
    if num > 40:
        print(f"Error: {num}°C is too hot for plants (max 40°C)")
        return
    print(f"Temperature {num}°C is perfect for plants!")
    return (num)


def test_temperature_input() -> None:
    """
    Executes a series of test cases to demonstrate program robustness.

    Tests successful scenarios, type errors (non-numeric strings), and
    logical errors (out-of-range values) to ensure the program
    continues running despite invalid inputs.
    """
    print("=== Garden Temperature Checker ===")
    print("")
    print("Testing temperature: 25")
    check_temperature("25")
    print("")
    print("Testing temperature: abc")
    check_temperature("abc")
    print("")
    print("Testing temperature: 100")
    check_temperature("100")
    print("")
    print("Testing temperature: -50")
    check_temperature("-50")
    print("")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
