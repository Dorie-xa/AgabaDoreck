phones = ("samsung", "iphone", "tecno", "redmi")
print(phones[1])

print(phones[-2])

phones = list(phones)
phones[1] = "itel"
phones = tuple(phones)
print(phones)

phones = phones + ("Huawei",)
print(phones)

for phone in phones:
    print(phone)

phones = list(phones)
del phones[0]
phones = tuple(phones)
print(phones)

cities = tuple(("Kampala", "Mbarara", "Gulu", "Jinja"))
print(cities)

(a, b, c, d) = cities
print(a, b, c, d)

print(cities[1:4])

first = ("Agaba",)
second = ("Doreck",)
print(first + second)

colors = ("red", "blue")
print(colors * 3)

thistuple = (1,3,7,8,7,5,4,6,8,5)
print(thistuple.count(8))
