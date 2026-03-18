def check_temperature(temp_str: str) -> int | None:
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
