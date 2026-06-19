names=["Peter","James","Doreck","Praise","Joseph"]
print(names)

new_name = "Sarah"
names[0] = new_name
print(names)

names.append("John")
print(names)

add_name="Bathel"
names[2] = add_name
print(names)

names.remove("Praise")
print(names)
print(names[-1])


new_list=["dad","mum","girl","boy","daughter","son","aunt"]
print(new_list[1:5])

# list of countries
countries=["Uganda", "Kenya", "Tanzania"]
new_countries = countries.copy()
print("Countries:", countries)
print("Copied countries:", new_countries)

for country in countries:
    print(country)

# list of animal names and sort them in ascending and descending order
animals = ["zebra", "lion", "elephant", "giraffe", "antelope", "cat", "dog"]
print("Animals ascending:", sorted(animals))
print("Animals descending:", sorted(animals, reverse=True))

#animal names containing the letter 'a'
for animal in animals:
    if "a" in animal:
        print(animal)

# join two lists 
first_name = ["Doreck"]
second_name = ["Agaba"]
full_name = first_name + second_name
print("Joined name list:", full_name)

