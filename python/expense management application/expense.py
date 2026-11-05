
expenses = []


# Add an expense
def add_expense(expenses):

    name = input("Enter expense name: ")
    amount = float(input("Enter expense amount: "))

    if amount <= 0:
        print("Invalid amount!")
        return

    expense = {
        "name": name,
        "amount": amount
    }

    expenses.append(expense)

    print("Expense added successfully!")


# Display expenses
def show_expenses(expenses):

    if len(expenses) == 0:
        print("No expenses available.")
        return

    print("\n======= EXPENSES =======")

    for index, expense in enumerate(expenses, start=1):

        print(
            f"{index}. {expense['name']}: "
            f"{expense['amount']:.2f}"
        )


# Calculate total
def calculate_total(expenses):

    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# Display summary
def show_summary(expenses):

    if len(expenses) == 0:
        print("No expenses to analyze.")
        return

    total = calculate_total(expenses)
    average = total / len(expenses)

    large_expenses = 0

    for expense in expenses:

        if expense["amount"] > 100:
            large_expenses += 1

    print("\n======= SUMMARY =======")

    print(f"Total expenses: {total:.2f}")
    print(f"Average expense: {average:.2f}")
    print(f"Number of expenses: {len(expenses)}")
    print(f"Expenses over 100: {large_expenses}")


# Main application
while True:

    print("\n===== EXPENSE MANAGER =====")

    print("1. Add expense")
    print("2. View expenses")
    print("3. View summary")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense(expenses)

    elif choice == "2":
        show_expenses(expenses)

    elif choice == "3":
        show_summary(expenses)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
