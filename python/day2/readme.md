# 🐍 Module 2 — Lesson 1: Strings and Numbers in Python

**📚 Course:** Python First  
**🎯 Level:** Beginner  
**📖 Module:** 2 — Strings and Numbers  
**📝 Lesson:** 1 — Working with Text and Numbers

---

## 🎯 Learning Objectives

In Module 1, we learned how to store information in variables.

Now we're going to learn how to work with that information.

We'll focus on two important concepts:

1. 📝 **Strings** — Working with text.
2. 🔢 **Numbers** — Performing mathematical operations.

By the end of this lesson, you will be able to:

- Create and manipulate strings.
- Combine strings using concatenation.
- Find the length of a string.
- Access individual characters using indexes.
- Use built-in string methods.
- Perform mathematical calculations.
- Update numerical values.
- Convert between strings and numbers.

---

# 📝 Part 1 — Strings in Python

## 1️⃣ What Is a String?

A **string** is a sequence of characters used to represent text.

```python
name = "Ahmed"
country = "Egypt"
message = "I am learning Python"
```

You can use either single or double quotation marks:

```python
first_name = 'Ahmed'
last_name = "Ali"
```

Both are valid.

**💡 Remember:** Strings must be surrounded by quotation marks.

---

## 2️⃣ Combining Strings (Concatenation)

We can combine two or more strings using the `+` operator.

```python
first_name = "Ahmed"
last_name = "Ali"

full_name = first_name + " " + last_name

print(full_name)
```

**Expected Output:**

```text
Ahmed Ali
```

**🔍 Notice:** We added `" "` to create a space between the names.

This process is called **String Concatenation**.

---

## 3️⃣ Finding the Length of a String

Python provides the `len()` function to count the number of characters in a string.

```python
name = "Ahmed"

print(len(name))
```

**Output:**

```text
5
```

Why 5?

Because Ahmed contains five characters.

**⚠️ Important:** Spaces also count as characters.

```python
message = "Hello World"

print(len(message))
```

**Output:**

```text
11
```

---

## 4️⃣ Accessing Individual Characters

We can access individual characters using their index (position).

**💡 Important:** Python indexing starts at `0`, not `1`.

```python
name = "Ahmed"

print(name[0])
print(name[1])
print(name[2])
```

**Expected Output:**

```text
A
h
m
```

### 🔙 Negative Indexing

We can also access characters from the end of a string using negative indexes.

```python
name = "Ahmed"

print(name[-1])
print(name[-2])
```

**Expected Output:**

```text
d
e
```

**🧠 Understanding String Indexing**

| Character | A | h | m | e | d |
|---|---|---|---|---|---|
| Positive Index | 0 | 1 | 2 | 3 | 4 |
| Negative Index | -5 | -4 | -3 | -2 | -1 |

---

## 5️⃣ Changing Uppercase and Lowercase

Python provides useful built-in string methods.

### 🔠 Uppercase — `.upper()`

Converts all letters to uppercase.

```python
name = "ahmed"

print(name.upper())
```

**Output:**

```text
AHMED
```

### 🔡 Lowercase — `.lower()`

Converts all letters to lowercase.

```python
name = "AHMED"

print(name.lower())
```

**Output:**

```text
ahmed
```

### 🔤 Capitalize — `.capitalize()`

Makes the first character uppercase and the remaining characters lowercase.

```python
name = "ahmed ali"

print(name.capitalize())
```

**Output:**

```text
Ahmed ali
```

### 🔄 Replace — `.replace()`

Replaces part of a string with another string.

```python
message = "I love JavaScript"

new_message = message.replace("JavaScript", "Python")

print(new_message)
```

**Output:**

```text
I love Python
```

### 📌 String Methods Summary

| Method | Purpose | Example |
|---|---|---|
| `.upper()` | Convert to uppercase | `"hello".upper()` |
| `.lower()` | Convert to lowercase | `"HELLO".lower()` |
| `.capitalize()` | Capitalize first character | `"hello".capitalize()` |
| `.replace()` | Replace text | `"Hi".replace("Hi", "Hello")` |

---

## 6️⃣ Removing Unnecessary Spaces

Sometimes text contains extra spaces.

We can use `.strip()` to remove spaces from the beginning and end of a string.

```python
name = "   Ahmed   "

print(name.strip())
```

**Output:**

```text
Ahmed
```

**💡 Remember:** `.strip()` removes spaces from both ends, not from the middle of the string.

---

## 7️⃣ F-Strings

Remember how we combined strings using `+`?

Python has a better way: **F-strings**.

F-strings make it easier to insert variables into text.

```python
name = "Ahmed"
age = 25

message = f"My name is {name} and I am {age} years old"

print(message)
```

**Expected Output:**

```text
My name is Ahmed and I am 25 years old
```

**🧠 How does it work?**

- Put the letter `f` before the quotation mark.
- Place variable names inside `{}`.
- Python automatically inserts their values.

---

# 🔢 Part 2 — Numbers in Python

## 8️⃣ Types of Numbers

We already learned two numerical data types.

| Data Type | Description | Examples |
|---|---|---|
| `int` | Integer (whole number) | `10`, `25`, `-5` |
| `float` | Decimal number | `10.5`, `3.14`, `-2.5` |

Example:

```python
age = 25
price = 99.99

print(type(age))
print(type(price))
```

**Output:**

```text
<class 'int'>
<class 'float'>
```

---

## 9️⃣ Mathematical Operators

Python can perform mathematical calculations using arithmetic operators.

### 📊 Arithmetic Operators Table

| Operator | Meaning | Example | Result |
|---|---|---|---:|
| `+` | Addition | `10 + 5` | 15 |
| `-` | Subtraction | `10 - 5` | 5 |
| `*` | Multiplication | `10 * 5` | 50 |
| `/` | Division | `10 / 5` | 2.0 |
| `//` | Floor Division | `11 // 5` | 2 |
| `%` | Modulo (Remainder) | `11 % 5` | 1 |
| `**` | Exponentiation | `2 ** 3` | 8 |

### 💻 Let's Try an Example

```python
a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
```

**Expected Output:**

```text
13
7
30
3.3333333333333335
3
1
1000
```

### 🔍 Understanding the Modulo Operator (`%`)

The `%` operator gives you the remainder after division.

For example:

```python
print(10 % 3)
```

**Output:**

```text
1
```

Why?

Because 3 goes into 10 three times, with 1 left over.

```text
10 ÷ 3 = 3 remainder 1
```

**💡 Real-world use cases:**

- Checking whether a number is even or odd.
- Calculating remainders.
- Dividing items into equal groups.

Example:

```python
number = 10

if number % 2 == 0:
    print("Even")
else:
    print("Odd")
```

---

## 🔟 Changing Number Values

You can update variables using shorthand assignment operators.

```python
score = 10

score += 5

print(score)
```

**Output:**

```text
15
```

### 📌 Other Assignment Operators

| Operator | Equivalent Expression |
|---|---|
| `x += 5` | `x = x + 5` |
| `x -= 2` | `x = x - 2` |
| `x *= 3` | `x = x * 3` |
| `x /= 2` | `x = x / 2` |

Example:

```python
x = 10

x += 5   # x = x + 5
x -= 2   # x = x - 2
x *= 3   # x = x * 3
x /= 2   # x = x / 2

print(x)
```

**Output:**

```text
19.5
```

---

## 1️⃣1️⃣ Converting Between Strings and Numbers

Sometimes we receive numbers as text.

For example:

```python
age = "25"

print(type(age))
```

**Output:**

```text
<class 'str'>
```

Although `"25"` looks like a number, Python treats it as a string.

### 🔢 Converting String to Integer — `int()`

```python
age = "25"

age = int(age)

print(age)
print(type(age))
```

**Output:**

```text
25
<class 'int'>
```

### 📌 Other Conversion Functions

| Function | Purpose | Example |
|---|---|---|
| `int()` | Convert to integer | `int("25")` |
| `float()` | Convert to decimal number | `float("25.5")` |
| `str()` | Convert to string | `str(25)` |

### 💻 Conversion Example

```python
price = 99

price = float(price)

print(price)
```

**Output:**

```text
99.0
```

**⚠️ Important:** Not every string can be converted into a number.

For example, `int("Ahmed")` causes a `ValueError` because the text doesn't represent a valid integer.

---

# 🧪 Part 3 — Practice

Let's test what you've learned!

## 🧠 Python Knowledge Check

<details>
<summary>❓ Question 1 — What does len('Python') return?</summary>

- A. `5`
- B. `6` ✅
- C. `7`
- D. Error

**Explanation:** Python contains six characters.

</details>

<details>
<summary>❓ Question 2 — What does 'Ahmed'[0] return?</summary>

- A. `h`
- B. `A` ✅
- C. `d`
- D. `Ahmed`

**Explanation:** String indexing starts at zero, so index 0 represents the first character.

</details>

<details>
<summary>❓ Question 3 — What does 'hello'.upper() return?</summary>

- A. `hello`
- B. `Hello`
- C. `HELLO` ✅
- D. `hello.upper`

**Explanation:** `.upper()` converts all letters to uppercase.

</details>

<details>
<summary>❓ Question 4 — What is the result of 17 % 5?</summary>

- A. `2` ✅
- B. `3`
- C. `3.4`
- D. `5`

**Explanation:** 17 divided by 5 gives a remainder of 2.

</details>

<details>
<summary>❓ Question 5 — What is the result of 2 ** 4?</summary>

- A. `6`
- B. `8`
- C. `16` ✅
- D. `24`

**Explanation:** `2 ** 4` means 2 multiplied by itself four times: 2 × 2 × 2 × 2 = 16.

</details>

<details>
<summary>❓ Question 6 — Which function converts text into an integer?</summary>

- A. `str()`
- B. `float()`
- C. `int()` ✅
- D. `len()`

**Explanation:** `int()` converts a valid numerical string into an integer.

</details>

---

# 💻 Part 4 — Your Coding Challenge

<badge color="success">Practical Exercise</badge>

## 🎯 Challenge: Personal Information & Calculator

Create a Python program that performs the following tasks:

### 📝 Requirements

**Part A — Strings**

1. Create a variable called `first_name` containing your first name.
2. Create a variable called `last_name` containing your last name.
3. Combine them into `full_name`.
4. Print the full name.
5. Print the number of characters in the full name.
6. Print the full name in uppercase.

**Part B — Numbers**

7. Create two numbers:

```python
num1 = 20
num2 = 6
```

8. Print their:
   - Addition.
   - Subtraction.
   - Multiplication.
   - Division.
   - Remainder.

### ✅ Expected Output Example

```text
Ahmed Ali
9
AHMED ALI

Addition: 26
Subtraction: 14
Multiplication: 120
Division: 3.3333333333333335
Remainder: 2
```

**💡 Hint:** Remember to use `len()`, `.upper()`, and the arithmetic operators.

<details>
<summary>🔑 Click here to reveal the solution</summary>

```python
# Part A: Strings

first_name = "Ahmed"
last_name = "Ali"

full_name = first_name + " " + last_name

print(full_name)
print(len(full_name))
print(full_name.upper())


# Part B: Numbers

num1 = 20
num2 = 6

print("\nAddition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)
print("Remainder:", num1 % num2)
```

</details>

---

# 📈 Part 5 — Module 2 Progress

## Python — Strings and Numbers

<badge color="success">Lesson Covered</badge>

You've now practiced:

- [x] 📝 String creation and concatenation.
- [x] 🔍 String length and indexing.
- [x] 🔠 String methods.
- [x] 💬 F-strings.
- [x] 🔢 Integer and float types.
- [x] ➕ Arithmetic operators.
- [x] 🔄 Assignment operators.
- [x] 🔁 Type conversion.

## 🌐 Next Lesson — JavaScript: Strings and Numbers

Coming next: We'll solve the same problems in JavaScript using:

- String methods.
- Template literals.
- `Math`.
- Arithmetic operators.
- Type conversion.

### 🎯 Your Turn!

Try the quiz and coding challenge. Then we'll learn how JavaScript handles strings and numbers and compare both languages side by side.

**Keep practicing. Keep building. Keep coding! 🐍💻**

⭐ If you found this lesson helpful, consider giving the repository a star!