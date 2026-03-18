class GardenError(Exception):
    def __init__(self, message: str):
        Exception.__init__(self, message)


class PlantError(GardenError):
    def __init__(self, plant: str, message: str) -> None:
        message = f"{plant}: {message}"
        GardenError.__init__(self, message)


class WaterError(GardenError):
    def __init__(self):
        message = "Not enough water in the tank"
        GardenError.__init__(self, message)


class Plant:
    def __init__(self, name: str, water_level: int,
                 sunlight_hours: int):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours


class GardenManager:

    def __init__(self, owner: str, plants: list):
        self.gardens = []
        self.plants = []
        self.owner = owner

    def add_plant(self, plant: Plant) -> None:
        try:
            if plant.name == "":
                raise ValueError("Plant name cannot be empty!")
        except ValueError as e:
            print(f"Error adding plant: {e}")
        else:
            self.plants = self.plants + [plant]
            print(f"Added {plant.name} successfully")

    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant in self.plants:
                if plant is None:
                    raise ValueError("Cannot water None - invalid plant!")
                else:
                    print(f"Watering {plant.name} - success")
        except ValueError as e:
            print(f"Error: {e}")
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        for plant in self.plants:
            try:
                if plant.water_level > 10:
                    raise PlantError(plant.name, f"Water level "
                                     f"{plant.water_level} is too "
                                     "high (max 10)")
                if plant.water_level < 1:
                    raise PlantError(plant.name, f"Water level "
                                     f"{plant.water_level} is too low (min 1)")
                if plant.sunlight_hours > 12:
                    raise PlantError(plant.name, f"Sunlight hours"
                                     f" {plant.sunlight_hours} is too high"
                                     " (max 12)")
                if plant.sunlight_hours < 2:
                    raise PlantError(plant.name, f"Sunlight hours"
                                     f" {plant.sunlight_hours} "
                                     "is too low (min 2)")
                else:
                    print(f"{plant.name}: healthy (water: {plant.water_level},"
                          f" sun: {plant.sunlight_hours})")
            except Exception as e:
                print(f"Error checking {e}")


def errors_recovery(plants: list) -> None:
    for er in plants:
        try:
            raise er
        except GardenError as e:
            print(f"Caught a GardenError: {e}")
        finally:
            print("System recovered and continuing...")


def test_garden_management() -> None:
    print("=== Garden Management System ===\n")
    garden = GardenManager("Alice", [])
    print("Adding plants to garden...")
    garden.add_plant(Plant("tomato", 5, 8))
    garden.add_plant(Plant("lettuce", 15, 2))
    garden.add_plant(Plant("", 2, 2))
    print("\nWatering plants...")
    garden.water_plants()
    print("\nChecking plant health...")
    garden.check_plant_health()
    print("\nTesting error recovery...")
    errors_recovery([WaterError()])
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
