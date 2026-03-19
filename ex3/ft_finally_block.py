def water_plants(plant_list: list) -> None:
    """
    Simulates the process of watering a list of plants.

    This function demonstrates the use of a try-except-finally block.
    It iterates through the plant list and raises a ValueError if a
    None value is encountered. Regardless of whether an error occurs,
    the 'finally' block ensures the watering system is closed.

    Args:
        plant_list (list): A list of strings representing plant names.
                           May contain None to simulate an error.
    """
    print("Opening watering system")

    try:
        for plant in plant_list:
            if plant is None:
                raise ValueError("Cannot water None - invalid plant!")
            print(f"Watering {plant}")
    except ValueError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Test suite for the watering system's resilience.

    Executes a normal watering scenario and an error scenario involving
    a None value to prove that cleanup operations in the 'finally'
    block are always executed.
    """
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!")

    print("")
    print("Testing with error...")
    water_plants(["tomato", None, "carrots"])
    print("")

    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
