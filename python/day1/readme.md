# 🐍 Module 1 — Lesson 1: Variables and Data Types in Python

<text-placeholder />

**📚 Course:** Python First  
**🎯 Level:** Beginner  
**📖 Module:** 1 — Python Fundamentals  
**📝 Lesson:** 1 — Variables and Data Types

---

## 🎯 Learning Objectives

By the end of this lesson, you will be able to:

- Understand what variables are.
- Create and assign values to variables.
- Identify the four fundamental Python data types.
- Check data types using `type()`.
- Display variables using `print()`.
- Change variable values.

---

## 1️⃣ What Is a Variable?

A **variable** is a named place where we store information so we can use it later.

Think of it like a box with a label 📦.

For example:

```python
name = "Ahmed"
age = 25
```

Here:

- `name` is the variable name.
- `"Ahmed"` is the value.
- `age` is another variable.
- `25` is its value.

**💡 Important:** The `=` sign means *assign a value to a variable*.

---

## 2️⃣ The Four Fundamental Data Types

Python has different types of data. Let's learn the four important ones.

### 🅰️ A. String (`str`)

A **string** represents text. We write it inside quotation marks.

```python
name = "Ahmed"
country = "Egypt"
message = "Hello, world!"
```

**Output example:**

```text
Ahmed
Egypt
Hello, world!
```

### 🔢 B. Integer (`int`)

An **integer** is a whole number without a decimal point.

```python
age = 25
year = 2026
number_of_students = 30
```

**Examples:** `10`, `25`, `-5`, `100`

### 🔣 C. Float (`float`)

A **float** is a number with a decimal point.

```python
height = 1.75
price = 99.50
temperature = 36.5
```

**Examples:** `1.5`, `99.50`, `-3.14`

### ✅ D. Boolean (`bool`)

A **Boolean** has only two possible values:

- `True` — Yes / Correct
- `False` — No / Incorrect

```python
is_student = True
is_married = False
is_learning_python = True
```

**⚠️ Remember:** Python is case-sensitive. Write `True` and `False` with capital letters.

---

## 3️⃣ How Do We Check a Variable's Data Type?

Python provides a built-in function called `type()`.

It tells us the data type of a variable.

```python
name = "Ahmed"
age = 25
height = 1.75
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))
```

**Expected Output:**

```text
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```

**🧠 What did we learn?**

| Function | Purpose |
|---|---|
| `type()` | Checks the data type of a value. |
| `print()` | Displays information on the screen. |

---

## 4️⃣ Printing Variables

We use `print()` to display information.

```python
name = "Ahmed"
age = 25

print(name)
print(age)

print("My name is", name)
print("I am", age, "years old")
```

**Expected Output:**

```text
Ahmed
25
My name is Ahmed
I am 25 years old
```

**💡 Tip:** You can also use f-strings to make your output cleaner.

```python
name = "Ahmed"
age = 25

print(f"My name is {name}")
print(f"I am {age} years old")
```

---

## 5️⃣ Changing Variable Values

Variables can change their values.

For example:

```python
score = 10

print(score)

score = 20

print(score)
```

**Expected Output:**

```text
10
20
```

**🧠 Explanation:**

1. First, we assign `10` to the variable `score`.
2. We print the value.
3. Then, we assign `20` to the same variable.
4. We print the new value.

The latest assignment replaces the previous value.

---

## 📌 Lesson Summary

Let's review what we've learned.

| Concept | Description | Example |
|---|---|---|
| 📦 Variable | Stores information | `name = "Ahmed"` |
| 📝 String | Text | `"Hello"` |
| 🔢 Integer | Whole number | `25` |
| 🔣 Float | Decimal number | `1.75` |
| ✅ Boolean | True or False | `True` |
| 🔍 `type()` | Checks data type | `type(age)` |
| 🖨️ `print()` | Displays information | `print(name)` |
| 🔄 Assignment | Changes a variable's value | `score = 20` |

---

## 🧪 Practice Exercises

Time to test your understanding! 💪

### Exercise 1 — Create Variables

Create four variables:

- Your name.
- Your age.
- Your height.
- Whether you are a student.

Print all four variables.

### Exercise 2 — Check Data Types

Use `type()` to check the data type of each variable.

### Exercise 3 — Change Variable Values

Create a variable called `score` and assign it the value `50`.

Then:

1. Print the score.
2. Change the score to `100`.
3. Print the new score.

### Exercise 4 — Predict the Output

Before running this code, try to predict the output.

```python
x = 10
y = 5

print(x)
print(y)

x = 20

print(x)
print(type(y))
```

<details>
<summary>✅ Click to reveal the answer</summary>

```text
10
5
20
<class 'int'>
```

</details>

---

## 🎯 Mini Challenge

Create a small Python program that displays your personal information.

**Expected Output:**

```text
===== MY PROFILE =====

Name: Ahmed
Age: 25
Country: Egypt
Height: 1.75
Student: True
```

**Requirements:**

- Use at least five variables.
- Use all four fundamental data types.
- Use `print()` to display the information.
- Use f-strings for at least two output lines.

---

## 🚀 What's Next?

In the next lesson, we'll explore:

**Module 1 — Lesson 2: Operators in Python**

We'll learn how to perform mathematical calculations, compare values, and combine conditions.

Keep practicing and keep coding! 🐍💻

⭐ If you find this lesson helpful, don't forget to star the repository!