def check_plant_health(plant_name: str, water_level: int, sunlight_hours: int):
    """
    Validates plant environmental conditions and raises errors if invalid.

    This function checks if the plant name is provided and if the water
    and sunlight levels are within the safe operational range.

    Args:
        plant_name (str): The name of the plant to check.
        water_level (int): Current water level (must be between 1 and 10).
        sunlight_hours (int): Daily sunlight hours (must be between 2 and 12).

    Raises:
        ValueError: If the plant name is empty or if levels are out of range.
    """
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    if water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too high"
                         " (max 12)")
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low"
                         " (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    """
    Executes a suite of test cases for plant health validation.

    Tests successful validation as well as multiple error scenarios
    to ensure the exception handling logic correctly catches and
    reports specific ValueErrors.
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("tomato", 1, 2)
    except ValueError as e:
        print(f"Error: {e}")
    print("")

    print("Testing empty plant name...")
    try:
        check_plant_health("", 1, 2)
    except ValueError as e:
        print(f"Error: {e}")
    print("")

    print("Testing bad water level...")
    try:
        check_plant_health("plant", 15, 2)
    except ValueError as e:
        print(f"Error: {e}")
    print("")

    print("Testing bad sunlight hours...")
    try:
        check_plant_health("plant", 2, 0)
    except ValueError as e:
        print(f"Error: {e}")
    print("")

    print("All error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
