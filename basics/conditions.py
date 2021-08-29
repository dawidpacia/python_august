flight_dict = {
    "Krakow-Nicosia": 1980,
    "Krakow-Reykjavik": 2900,
    "Krakow-Chartum": 'not exist'
}

direction = "Krakow-Nicosia"
distance = flight_dict[direction]


if distance >= 2000:
    cost = 2 * distance
    print(f"total cost is {cost}")
elif 0 < distance < 2000:
    cost = 2 * distance + 100
    print(f"total cost is {cost}")
else:
    print("No such flight")
