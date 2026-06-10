# BILL SPLIT CALCULATOR
print("Welcome to Dee Restaurant!!!!")

total_amount = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))

print("Choose a tip percentage:")
print("1. 10%")
print("2. 15%")
print("3. 20%")
print("4. Custom percentage")

choice = input("Enter option 1, 2, 3 or 4: ")

if choice == "1":
    tip_percent = 10
elif choice == "2":
    tip_percent = 15
elif choice == "3":
    tip_percent = 20
elif choice == "4":
    tip_percent = float(input("Enter custom tip percentage: "))
else:
    print("Invalid option. Defaulting to 15% tip.")
    tip_percent = 15

tip_amount = total_amount * tip_percent / 100
total_with_tip = total_amount + tip_amount
amount_per_person = total_with_tip / num_people

print("\n==============================")
print("DEE RESTAURANT")
print("Receipt")
print("==============================")
print(f"{'Bill amount:':<20}Shs.{total_amount:>8.2f}")
print(f"{'Tip percentage:':<20}{tip_percent:>7.2f}%")
print(f"{'Tip amount:':<20}Shs.{tip_amount:>8.2f}")
print(f"{'Total with tip:':<20}Shs{total_with_tip:>8.2f}")
print(f"{'Number of people:':<20}{num_people:>8}")
print(f"{'Per person share:':<20}Shs.{amount_per_person:>8.2f}")
print("==============================")
print("Thank you for dining with us!")
print("==============================")
