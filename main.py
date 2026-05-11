cars = [
    {"brand": "BMW", "year": 2020},
    {"brand": "Audi", "year": 2018},
    {"brand": "Tesla", "year": 2023},
    {"brand": "Kia", "year": 2019}
]

new_cars = []
old_cars = []

for car in cars:
    if car["year"] >= 2020:
        new_cars.append(car["brand"])
    else:
        old_cars.append(car["brand"])

print("Yangi mashinalar:")

for car in new_cars:
    print(car)

print("Eski mashinalar:")

for car in old_cars:
    print(car)

count = len(cars)
print("Jami mashina:", count)
