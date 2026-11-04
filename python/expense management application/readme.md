#expense management application

The application should allow users to:
1. Add expenses.
2. View all expenses.
3. Calculate total spending.
4. Calculate average spending.
5. Count expensive purchases.
6. Exit the application.
To build this, we'll need several concepts.
Which Python concept handles each task?
Lists and dictionaries

Store expense records.



If / else

Choose what the application should do.



Loops

Keep the application running and process records.



Functions

Organize each operation into reusable code.



Part 3 — Our final project: Expense Management System







dribbble.com


We'll build a small but functional expense management application.
Step 1: Store the expenses
First, we need a list to store all expense records.
expenses = [    {"name": "Food", "amount": 150},    {"name": "Transport", "amount": 80},    {"name": "Shopping", "amount": 300}]



Notice something important!

We're combining two data structures:
- A list stores multiple expenses.
- Each dictionary stores the name and amount of one expense.
This is a very common programming pattern.
Step 2: Create a function to add expenses
def add_expense(expenses):    name = input("Enter expense name: ")    amount = float(input("Enter expense amount: "))    if amount <= 0:        print("Invalid amount!")        return    expense = {        "name": name,        "amount": amount    }    expenses.append(expense)    print("Expense added successfully!")



New concept: input().

It allows the user to enter information while the program is running.

For example:
name = input("Enter your name: ")print(f"Hello, {name}!")



Remember that input() returns a string, so we use float() when we need a decimal number.
Step 3: Display all expenses
Let's create another function.
def show_expenses(expenses):    if len(expenses) == 0:        print("No expenses available.")        return    print("\n======= EXPENSES =======")    for index, expense in enumerate(expenses, start=1):        print(            f"{index}. {expense['name']}: "            f"{expense['amount']:.2f}"        )



Here we're combining:
- Functions.
- If conditions.
- Lists.
- Dictionaries.
- Loops.
- F-strings.
Notice this expression:
expense['amount']



We're accessing the value stored under the dictionary key "amount".
Step 4: Calculate total expenses
def calculate_total(expenses):    total = 0    for expense in expenses:        total += expense["amount"]    return total



Let's understand the logic:

Suppose our expenses are:
expenses = [150, 80, 300]



The loop calculates:
total = 0

total = 0 + 150
total = 150 + 80
total = 230 + 300

Final total = 530


Step 5: Calculate the summary
def show_summary(expenses):    if len(expenses) == 0:        print("No expenses to analyze.")        return    total = calculate_total(expenses)    average = total / len(expenses)    large_expenses = 0    for expense in expenses:        if expense["amount"] > 100:            large_expenses += 1    print("\n======= SUMMARY =======")    print(f"Total expenses: {total:.2f}")    print(f"Average expense: {average:.2f}")    print(f"Number of expenses: {len(expenses)}")    print(f"Expenses over 100: {large_expenses}")



This function uses another function:
total = calculate_total(expenses)



This is called function composition: using one function inside another.
Step 6: Create the application menu
Now we need to allow users to choose what they want to do.
while True:    print("\n===== EXPENSE MANAGER =====")    print("1. Add expense")    print("2. View expenses")    print("3. View summary")    print("4. Exit")    choice = input("Choose an option: ")    if choice == "1":        add_expense(expenses)    elif choice == "2":        show_expenses(expenses)    elif choice == "3":        show_summary(expenses)    elif choice == "4":        print("Goodbye!")        break    else:        print("Invalid choice!")



Notice the combination:
- while True keeps the application running.
- input() receives the user's choice.
- if / elif / else determines what happens.
- break exits the application.
- Functions perform the requested operations.

Part 4 — The complete application
Now let's put all six steps together.
Complete Python project
expenses = []# Add an expensedef add_expense(expenses):    name = input("Enter expense name: ")    amount = float(input("Enter expense amount: "))    if amount <= 0:        print("Invalid amount!")        return    expense = {        "name": name,        "amount": amount    }    expenses.append(expense)    print("Expense added successfully!")# Display expensesdef show_expenses(expenses):    if len(expenses) == 0:        print("No expenses available.")        return    print("\n======= EXPENSES =======")    for index, expense in enumerate(expenses, start=1):        print(



Important: This is a console-based application. Enter a valid numeric amount when prompted. Expenses are stored in memory, so they disappear when the program closes.
Part 5 — Test your application
Try the following interaction:
===== EXPENSE MANAGER =====

1. Add expense
2. View expenses
3. View summary
4. Exit

Choose an option: 1

Enter expense name: Food
Enter expense amount: 150

Expense added successfully!


Add two more expenses:
Transport: 80
Shopping: 300


Then choose option 3.

Expected result:
======= SUMMARY =======

Total expenses: 530.00
Average expense: 176.67
Number of expenses: 3
Expenses over 100: 2