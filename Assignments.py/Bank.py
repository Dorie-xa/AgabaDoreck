# Parent Class
class Transaction:
    def process_transaction(self, amount):
        print("Processing transaction of", amount)


# Child Class - Deposit
class Deposit(Transaction):
    def process_transaction(self, amount):
        print("Deposited:", amount)

    # Method Overloading (using default parameter)
    def deposit(self, amount, bonus=0):
        print("Total Deposited:", amount + bonus)


# Child Class - Withdrawal
class Withdrawal(Transaction):
    def process_transaction(self, amount):
        print("Withdrawn:", amount)


# Child Class - Transfer
class Transfer(Transaction):
    def process_transaction(self, amount):
        print("Transferred:", amount)


# Demonstration
employee_name = "John"

print("Employee:", employee_name)

d = Deposit()
w = Withdrawal()
t = Transfer()

# Overriding
d.process_transaction(500000)
w.process_transaction(100000)
t.process_transaction(200000)

# Overloading
d.deposit(500000)
d.deposit(500000, 50000)