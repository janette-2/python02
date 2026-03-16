class TemperatureTooLow(Exception):
    def __init__(self, temp: int):
        super().__init__(f"Error: {temp}°C is too cold for plants (min 0°C)")


class TemperatureTooHot(Exception):
    def __init__(self, temp: int):
        super().__init__(f"Error: {temp}°C is too hot for plants (max 40°C)")


class NotANumber(Exception):
    def __init__(self, temp_str: str):
        super().__init__(f"Error: '{temp_str}' is not a valid number")


def check_temperature(temp_str: str) -> int:
    try:
        num = int(temp_str)
    except ValueError:
        raise NotANumber(temp_str)
    if num < 0:
        raise TemperatureTooLow(num)
    elif num > 40:
        raise TemperatureTooHot(num)
    else:
        print(f"Temperature {num}°C is perfect for plants!")
        return (num)


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    print("\nTesting temperature: 25")
    try:
        check_temperature("25")
    except (TemperatureTooHot, TemperatureTooLow, NotANumber) as e:
        print(e)
    print("\nTesting temperature: abc")
    try:
        check_temperature("abc")
    except (TemperatureTooHot, TemperatureTooLow, NotANumber) as e:
        print(e)
    print("\nTesting temperature: 100")
    try:
        check_temperature("100")
    except (TemperatureTooHot, TemperatureTooLow, NotANumber) as e:
        print(e)
    print("\nTesting temperature: -50")
    try:
        check_temperature("-50")
    except (TemperatureTooHot, TemperatureTooLow, NotANumber) as e:
        print(e)
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
