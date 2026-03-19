class GardenError(Exception):
    """ The GardenError is the father of all the exceptions,
    it gives a common structure so the others can fit their
    behaviour, in this case, by being able to portray messages
    """
    def __init__(self, message: str):
        Exception.__init__(self, message)


class PlantError(GardenError):
    """
    Specific error for plant health issues.
    Raised when a specific plant species requires attention.
    """
    def __init__(self, plant: str) -> None:
        message = f"The {plant} plant is wilting!"
        GardenError.__init__(self, message)


class WaterError(GardenError):
    """
    Specific error for irrigation system failures.
    Raised when water levels are below the required threshold.
    """
    def __init__(self):
        message = "Not enough water in the tank!"
        GardenError.__init__(self, message)


def ft_custom_errors() -> None:
    """
    Demonstrates the handling of custom garden-related exceptions.

    This function performs three main tasks to validate the error system:
    1. Triggers and catches 'PlantError' to show specific exception handling.
    2. Triggers and catches 'WaterError' to show resource-specific handling.
    3. Iterates through a list of different custom errors and catches them
       using the base 'GardenError' class, demonstrating that a parent
       exception can manage all its subclasses.

    The function ensures the program remains stable by using try-except
    blocks for every raised exception.
    """
    print("=== Custom Garden Errors Demo ===\n")

    print("Testing PlantError...")
    try:
        plant = "tomato"
        raise PlantError(plant)
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    print("Testing WaterError...")
    try:
        raise WaterError()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")
    errors = [PlantError("tomato"), WaterError()]
    for er in errors:
        try:
            raise er
        except GardenError as e:
            print(f"Caught a garden error: {e}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
