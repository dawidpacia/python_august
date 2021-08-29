def calculate_fuel(mass):

    if type(mass) != int:
        return False

    if mass <= 0:
        return False
    elif 9 > mass > 0:
        return 1

    fuel = mass // 3 - 2
    return fuel




















def print_something(text):
    print(text)

def add_one(value):
    result = value + 1
    return result


if __name__ == "__main__":

    print_something("test")
    result = add_one(10)
    print(result)

    fuel_needed = calculate_fuel(12)
    print(fuel_needed)

    assert fuel_needed == 2, f"Calculated fuel -> {fuel_needed}"
