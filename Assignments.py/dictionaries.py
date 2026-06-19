Shoes = {
    "brand":"Nick",
    "color":"black",
    "size":40
}

print(Shoes["size"])

Shoes["brand"] = "Adidas"
Shoes["type"] = "sneakers"

print(Shoes.keys())
print(Shoes.values())

print("size" in Shoes)

for key, value in Shoes.items():
    print(key, value)

Shoes.pop("color")
print(Shoes)

Shoes.clear()
print(Shoes)

student = {"name":"Tom","age":20}
copy_student = student.copy()
print(copy_student)

school = {
    "student1":{"name":"Ann","age":20},
    "student2":{"name":"Ben","age":21}
}
print(school)