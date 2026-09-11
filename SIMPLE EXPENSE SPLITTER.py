print("===== EXPENSE SPLITTER =====")
                         
people = int(input("How many people? "))

names = []
amounts = []

for i in range(people):
    name = input("Enter name: ")
    amount = int(input("Enter amount: "))

    names.append(name)
    amounts.append(amount)

total = sum(amounts)

print("\nTotal Expense:", total)

average = total / people

print("Average Expense:", average)

print("\n===== EXPENSE DETAILS =====")

for name, amount in zip(names, amounts):
    print(name, "-", amount)

print("\n===== BALANCE DETAILS =====")

for name, amount in zip(names, amounts):

    if amount > average:
        print(name, "paid", amount - average, "extra")

    elif amount < average:
        print(name, "needs to pay", average - amount)

    else:
        print(name, "is settled")