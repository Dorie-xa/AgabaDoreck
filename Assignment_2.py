# Real-world application using control structures
# Assignment 2: E-commerce pricing calculator with login system

users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "customer": {"password": "cust123", "role": "Customer"},
    "cashier": {"password": "cash123", "role": "Cashier"}
}

coupon_rules = {
    "SAVE10": {"rate": 0.10, "min_subtotal": 0, "description": "10% off on any order"},
    "SAVE20": {"rate": 0.20, "min_subtotal": 100, "description": "20% off orders over $100"},
    "VIP30": {"rate": 0.30, "min_subtotal": 200, "description": "30% off orders over $200"}
}

tax_rates = {
    "NY": 0.08875,
    "CA": 0.0725,
    "TX": 0.0625,
    "OTHER": 0.05
}

def authenticate_user():
    print("Welcome to the e-commerce system")
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    user = users.get(username)
    if user and user["password"] == password:
        print(f"Login successful. Welcome, {username}! Role: {user['role']}")
        return username, user["role"]

    print("Invalid username or password. Access denied.")
    return None, None


def get_tax_rate(location_code):
    location_code = location_code.upper()
    return tax_rates.get(location_code, tax_rates["OTHER"])


def calculate_discount(subtotal, coupon_code):
    coupon_code = coupon_code.upper()
    coupon = coupon_rules.get(coupon_code)
    if coupon is None:
        return 0.0, f"Invalid coupon code '{coupon_code}'. No discount applied."

    if subtotal < coupon["min_subtotal"]:
        return 0.0, (
            f"Coupon '{coupon_code}' requires a minimum subtotal of ${coupon['min_subtotal']:.2f}. "
            "No coupon discount applied."
        )

    discount = subtotal * coupon["rate"]
    return discount, f"Coupon '{coupon_code}' applied: {int(coupon['rate'] * 100)}% off."


def get_subtotal():
    while True:
        try:
            subtotal = float(input("Enter product subtotal amount: $"))
            if subtotal < 0:
                print("Subtotal cannot be negative. Please enter a valid amount.")
                continue
            return subtotal
        except ValueError:
            print("Please enter a numeric amount.")


def get_coupon_code():
    code = input("Enter coupon code (SAVE10, SAVE20, VIP30) or leave blank: ").strip()
    return code if code else ""


def get_location():
    location = input("Enter location code (NY, CA, TX, OTHER): ").strip()
    return location if location else "OTHER"


def calculate_final_price(subtotal, discount, tax_rate):
    taxed_amount = (subtotal - discount) * tax_rate
    final_price = subtotal - discount + taxed_amount
    return taxed_amount, final_price


def show_user_menu(role):
    print("\nAvailable features based on your role:")
    if role == "Admin":
        print("- View user roles")
        print("- Process purchase orders")
        print("- Apply coupons and tax calculation")
    elif role == "Cashier":
        print("- Process purchase orders")
        print("- Apply coupons and tax calculation")
    elif role == "Customer":
        print("- Enter purchase details")
        print("- View final price with discounts and tax")
    else:
        print("- Basic checkout features")


def process_checkout(role):
    if role not in ["Admin", "Cashier", "Customer"]:
        print("Role does not have checkout access.")
        return

    subtotal = get_subtotal()
    coupon_code = get_coupon_code()
    location = get_location()
    tax_rate = get_tax_rate(location)

    discount, coupon_message = calculate_discount(subtotal, coupon_code)
    taxed_amount, final_price = calculate_final_price(subtotal, discount, tax_rate)

    print("\nCheckout summary")
    print("-----------------")
    print(f"Subtotal:          ${subtotal:.2f}")
    print(f"Discount:          -${discount:.2f}")
    print(f"Tax rate:          {tax_rate * 100:.2f}%")
    print(f"Tax amount:        +${taxed_amount:.2f}")
    print(f"Final price:       ${final_price:.2f}")
    print(coupon_message)


def show_all_users():
    print("\nSystem users and roles")
    print("----------------------")
    for username, info in users.items():
        print(f"{username}: {info['role']}")


def main():
    username, role = authenticate_user()
    if role is None:
        return

    show_user_menu(role)

    while True:
        if role == "Admin":
            print("\nOptions: [1] Checkout [2] View users [3] Quit")
        else:
            print("\nOptions: [1] Checkout [2] Quit")

        choice = input("Choose an option: ").strip()
        if choice == "1":
            process_checkout(role)
        elif choice == "2" and role == "Admin":
            show_all_users()
        elif (choice == "2" and role != "Admin") or (choice == "3" and role == "Admin"):
            print("Exiting the system. Thank you.")
            break
        else:
            print("Invalid selection. Please choose a valid option.")


if __name__ == "__main__":
    main()

