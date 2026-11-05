# 💰 Expense Management System

A beginner-friendly **Python console-based Expense Management Application** that helps users record expenses, view spending history, and analyze their spending habits.

---

## 📌 Project Overview

The application allows users to:

- ➕ Add new expenses.
- 📋 View all recorded expenses.
- 💵 Calculate total spending.
- 📊 Calculate average spending.
- 🔍 Count expensive purchases.
- 🚪 Exit the application.

## 🧠 Part 1 — Python Concepts Used

To build this application, we'll combine several fundamental Python concepts.

| Python Concept | Purpose |
|---|---|
| 📦 Lists & Dictionaries | Store expense records. |
| 🔀 If / Else | Choose what the application should do. |
| 🔁 Loops | Keep the application running and process records. |
| ⚙️ Functions | Organize operations into reusable code. |

---

## 🚀 Part 2 — Building the Expense Management System

We'll build a small but functional expense management application.

### 📝 Step 1 — Store the Expenses

First, we need a list to store all expense records.

```python
expenses = [
    {"name": "Food", "amount": 150},
    {"name": "Transport", "amount": 80},
    {"name": "Shopping", "amount": 300}
]
```

**💡 Notice something important!**

We're combining two data structures:

- 📋 A **list** stores multiple expenses.
- 📖 Each **dictionary** stores the name and amount of one expense.

This is a very common programming pattern.

### ➕ Step 2 — Create a Function to Add Expenses

```python
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
```

**🆕 New Concept: `input()`**

It allows the user to enter information while the program is running.

For example:

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**⚠️ Important:** `input()` returns a string, so we use `float()` when we need a decimal number.

### 📋 Step 3 — Display All Expenses

Let's create another function.

```python
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
```

**🧠 Concepts used:**

- ⚙️ Functions
- 🔀 If conditions
- 📋 Lists
- 📖 Dictionaries
- 🔁 Loops
- 📝 F-strings

Notice this expression:

```python
expense['amount']
```

We're accessing the value stored under the dictionary key `"amount"`.

### 💵 Step 4 — Calculate Total Expenses

```python
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total
```

**🔍 Let's understand the logic:**

Suppose our expenses are:

```python
expenses = [150, 80, 300]
```

The loop calculates:

```python
total = 0

total = 0 + 150
total = 150 + 80
total = 230 + 300

# Final total = 530
```

<details>
<summary>💡 How does the loop work?</summary>

1. Start with `total = 0`.
2. Add the first expense (150).
3. Add the second expense (80).
4. Add the third expense (300).
5. Return the final total (530).

</details>

### 📊 Step 5 — Calculate the Summary

```python
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
```

**🧠 New Concept: Function Composition**

This function uses another function:

```python
total = calculate_total(expenses)
```

This is called **function composition**: using one function inside another.

The function calculates:

- 💰 Total spending.
- 📈 Average spending.
- 🔢 Number of expenses.
- 🔍 Number of expenses greater than 100.

### 🎛️ Step 6 — Create the Application Menu

Now we need to allow users to choose what they want to do.

```python
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
```

**🔍 Notice the combination:**

- 🔁 `while True` keeps the application running.
- ⌨️ `input()` receives the user's choice.
- 🔀 `if / elif / else` determines what happens.
- 🛑 `break` exits the application.
- ⚙️ Functions perform the requested operations.

---

## 🏗️ Part 3 — The Complete Application

Now let's put all six steps together into one Python program.

### 🐍 Complete Python Project

```python
# =====================================
#       EXPENSE MANAGEMENT SYSTEM
# =====================================

expenses = []


# 1. Add an expense
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


# 2. Display all expenses
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


# 3. Calculate total expenses
def calculate_total(expenses):
    total = 0

    for expense in expenses:
        total += expense["amount"]

    return total


# 4. Display spending summary
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


# 5. Main application menu
def main():

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


# 6. Run the application
if __name__ == "__main__":
    main()
```

---

## 🧪 Part 4 — Test Your Application

Let's test our application with some sample expenses.

### 1️⃣ Run the Application

```text
===== EXPENSE MANAGER =====

1. Add expense
2. View expenses
3. View summary
4. Exit

Choose an option:
```

### 2️⃣ Add Your First Expense

```text
Choose an option: 1

Enter expense name: Food
Enter expense amount: 150

Expense added successfully!
```

### 3️⃣ Add Two More Expenses

| Expense | Amount |
|---|---:|
| 🍔 Food | 150 |
| 🚌 Transport | 80 |
| 🛍️ Shopping | 300 |

### 4️⃣ View the Summary

Choose option `3`.

**Expected Result:**

```text
======= SUMMARY =======

Total expenses: 530.00
Average expense: 176.67
Number of expenses: 3
Expenses over 100: 2
```

---

## ⚠️ Important Notes

- This is a **console-based application**.
- Enter a valid numeric amount when prompted.
- Expenses are stored in memory.
- Expenses disappear when the program closes because we haven't implemented file or database storage yet.

---

## 🎯 Part 5 — What Have We Learned?

By completing this project, you've practiced several important Python concepts.

| Concept | What You Practiced |
|---|---|
| 📋 Lists | Storing multiple expenses |
| 📖 Dictionaries | Organizing expense information |
| 🔀 Conditions | Making decisions |
| 🔁 Loops | Repeating operations |
| ⚙️ Functions | Writing reusable code |
| ⌨️ User Input | Receiving user information |
| 🔢 Type Conversion | Converting strings to numbers |
| 📝 F-Strings | Formatting output |
| 🔙 Return | Returning calculated results |
| 🛑 Break | Exiting a loop |

## 🚀 Part 6 — Possible Future Improvements

Want to make this application more advanced? Try adding:

- [ ] 🗑️ Delete an expense.
- [ ] ✏️ Update an existing expense.
- [ ] 🔎 Search for expenses by name.
- [ ] 📅 Add dates to expenses.
- [ ] 💾 Save expenses in a JSON or CSV file.
- [ ] 📂 Load previous expenses when the application starts.
- [ ] 🏷️ Categorize expenses (Food, Transport, Shopping).
- [ ] 📊 Generate spending charts.
- [ ] 🛡️ Handle invalid user input using `try/except`.

---

## 👨‍💻 Final Thoughts

Congratulations! 🎉

You've built a simple Expense Management System using fundamental Python concepts.

The most important lesson is that **small Python concepts can work together to build real-world applications.**

Keep practicing, keep building, and keep improving! 🐍

⭐ If you found this project helpful, consider giving the repository a star!