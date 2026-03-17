def check_plant_health(plant_name: str, water_level: int , sunlight_hours: int) -> None:
    try:
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
    except ValueError as e:
        print(f"Error: {e}")
    


if __name__ == "__main__":
    print("=== Garden Plant Health Checker ===\n")
    print("Testing good values...")
    check_plant_health("tomato", 1, 2)
    print("")
    print("Testing empty plant name...")
    check_plant_health("", 1, 2)
    print("")
    print("Testing bad water level...")
    check_plant_health("plant", 15, 2)
    print("")
    print("Testing bad sunlight hours...")
    check_plant_health("plant", 2, 0)
    print("")
    print("All error raising tests completed!")