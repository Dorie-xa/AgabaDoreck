#Write a custom exception for a Ugandan to drive a car (>=18)
class UnderAgeException(Exception):
    pass
class Driver:  
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def check_eligibility(self):
        if self.age < 18:
            raise UnderAgeException("Must be 18 years or older to drive in Uganda.")
        else:
            print(f"{self.name} is eligible to drive in Uganda.")

try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    driver = Driver(name, age)
    driver.check_eligibility()

except UnderAgeException as e:
    print("Error:", e)

except ValueError:
    print("Please enter a valid age.")