# Python Basics for Beginners 🐍

A beginner-friendly guide to learning Python programming fundamentals with simple explanations and practical examples.

## 📚 Table of Contents

1. [Variables](#1-variables)
2. [Data Types](#2-data-types)
3. [Conditionals](#3-conditionals)
4. [Loops](#4-loops)
5. [Exception Handling](#5-exception-handling)
6. [Lists, Tuples, Sets, and Dictionaries](#6-lists-tuples-sets-and-dictionaries)
7. [Functions](#7-functions)
8. [How to Run Python Code](#8-how-to-run-python-code)

---

## 1. Variables

Variables are used to store data values. In Python, a variable is created by assigning a value to a name using the `=` operator.

### Example

```python
x = 10
name = "Alice"
pi = 3.14
is_active = True

print(x)
print(name)
print(pi)
print(is_active)
```

### Output

```text
10
Alice
3.14
True
```

### Key Points

- Variables store data values.
- Python does not require explicit variable type declarations.
- Variable names are case-sensitive.
- Use meaningful names such as `user_name` and `total_price`.

---

## 2. Data Types

Python provides different data types to represent different kinds of values.

### 2.1 Numeric Types

**Integer (`int`)** — Whole numbers without decimal points.

```python
x = 5
y = -42

print(x)
print(y)
print(type(x))
```

**Float (`float`)** — Numbers containing decimal points.

```python
price = 3.14
temperature = -0.99

print(price)
print(type(price))
```

### 2.2 Text Type

**String (`str`)** — A sequence of characters enclosed in single or double quotes.

```python
name = "Alice"
greeting = "Hello, World!"

print(name)
print(greeting)
print(type(name))
```

### 2.3 Boolean Type

**Boolean (`bool`)** — Represents either `True` or `False`.

```python
is_active = True
has_permission = False

print(is_active)
print(has_permission)
print(type(is_active))
```

### Summary

| Data Type | Example | Description |
|---|---|---|
| `int` | `10` | Whole numbers |
| `float` | `3.14` | Decimal numbers |
| `str` | `"Python"` | Text |
| `bool` | `True` | Logical values |

---

## 3. Conditionals

Conditional statements execute different blocks of code depending on whether a condition is true or false.

Python uses `if`, `elif`, and `else`.

### Example

```python
age = 20

if age >= 18:
    print("You are an adult.")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
```

### Output

```text
You are an adult.
```

### Key Points

- `if` checks the first condition.
- `elif` checks another condition if previous conditions are false.
- `else` executes when none of the preceding conditions are true.
- Python uses indentation to define code blocks.

---

## 4. Loops

Loops are used to execute a block of code repeatedly.

Python provides two commonly used loops: `for` and `while`.

### 4.1 For Loop

A `for` loop iterates over a sequence, such as a list, tuple, string, or range.

```python
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)
```

### Output

```text
apple
banana
cherry
```

**Using `range()`**

```python
for i in range(1, 6):
    print(i)
```

Output:

```text
1
2
3
4
5
```

### 4.2 While Loop

A `while` loop repeats as long as its condition is true.

```python
i = 0

while i <= 10:
    print(i)
    i += 1
```

This prints numbers from `0` to `10`.

**Important:** Update the loop variable when necessary to avoid an infinite loop.

---

## 5. Exception Handling

Exceptions are errors or unexpected events that occur while a program is running. Python uses `try` and `except` to handle exceptions gracefully.

### Example

```python
try:
    x = 1 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

### Output

```text
Cannot divide by zero!
```

### Handling Multiple Exceptions

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)

except ValueError:
    print("Please enter a valid integer.")

except ZeroDivisionError:
    print("Number cannot be zero.")
```

### Key Points

- `try`: Contains code that might raise an exception.
- `except`: Handles a matching exception.
- `else`: Runs when no exception occurs.
- `finally`: Runs whether an exception occurs or not.

---

## 6. Lists, Tuples, Sets, and Dictionaries

Python provides built-in collection types for storing multiple values.

### 6.1 List

A list is an ordered, mutable collection that allows duplicate values and different data types.

```python
my_list = [1, 2, 3, "apple", 4.5]

print(my_list)
print(my_list[0])

my_list.append("banana")
my_list[1] = 20

print(my_list)
```

**Key Points:**
- Ordered collection.
- Mutable (can be modified).
- Allows duplicate values.
- Uses square brackets `[]`.

### 6.2 Tuple

A tuple is an ordered, immutable collection that allows duplicate values.

```python
my_tuple = (1, 2, 3, "banana", 4.5)

print(my_tuple)
print(my_tuple[0])
print(type(my_tuple))
```

**Key Points:**
- Ordered collection.
- Immutable after creation.
- Allows duplicate values.
- Uses parentheses `()`.

### 6.3 Set

A set is a mutable collection of unique elements. It does not guarantee a specific iteration order.

```python
my_set = {1, 2, 3, "orange"}

my_set.add(4)
my_set.add(2)

print(my_set)
```

The duplicate value `2` is stored only once.

**Key Points:**
- Stores unique values.
- Does not support indexing.
- Supports adding and removing elements.
- Uses curly braces `{}` or `set()`.

To create an empty set, use:

```python
my_set = set()
```

### 6.4 Dictionary

A dictionary stores data as key-value pairs. Keys must be unique, and dictionaries are mutable.

```python
my_dict = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

print(my_dict["name"])

my_dict["age"] = 26
my_dict["country"] = "USA"

print(my_dict)
```

**Key Points:**
- Stores key-value pairs.
- Accesses values using keys.
- Supports adding, updating, and deleting entries.
- Uses curly braces `{key: value}`.

### Collection Comparison

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Syntax | `[]` | `()` | `{}` | `{key: value}` |
| Ordered | Yes | Yes | No guaranteed order | Yes |
| Mutable | Yes | No | Yes | Yes |
| Duplicates | Yes | Yes | No | Keys are unique |
| Access | Index | Index | Membership | Key |

---

## 7. Functions

Functions are reusable blocks of code that perform a specific task. They help reduce repetition and make programs easier to maintain.

Python functions are defined using the `def` keyword.

### 7.1 Basic Function

```python
def greet():
    print("Hello, World!")

greet()
```

Output:

```text
Hello, World!
```

### 7.2 Function with Parameters

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")
greet_user("John")
```

### Output

```text
Hello, Alice!
Hello, John!
```

### 7.3 Function with a Return Value

```python
def add(a, b):
    return a + b

result = add(10, 20)

print(result)
```

Output:

```text
30
```

### Key Points

- `def` defines a function.
- Parameters receive input values.
- `return` sends a result back to the caller.
- A function runs when it is called.

---

## 8. How to Run Python Code

### Prerequisites

- Install Python 3 from [python.org](https://www.python.org/downloads/).
- Install a code editor such as Visual Studio Code, or use a terminal.

### Step 1: Verify Python Installation

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Step 2: Create a Python File

Create a file named `main.py`.

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Python Learner")
```

### Step 3: Run the Program

On Windows:

```bash
python main.py
```

On Linux or macOS:

```bash
python3 main.py
```

### Expected Output

```text
Hello, Python Learner!
```

---

## 🎯 Learning Goals

After completing these examples, you should understand:

- How to declare and use variables.
- How to identify basic Python data types.
- How to make decisions using conditional statements.
- How to repeat tasks using loops.
- How to handle common exceptions.
- How to work with Python collections.
- How to create reusable functions.

## 🚀 Next Topics to Learn

1. Operators and expressions
2. String methods
3. List and dictionary methods
4. List comprehensions
5. File handling
6. Modules and packages
7. Object-oriented programming (OOP)
8. Virtual environments and `pip`
9. Unit testing with `pytest`

## 📖 Official Documentation

- [Python Tutorial](https://docs.python.org/3/tutorial/)
- [Python Built-in Types](https://docs.python.org/3/library/stdtypes.html)
- [Python Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)

---

**Happy Learning! 🐍**

Practice each example, modify the values, and experiment with the code to strengthen your Python programming skills.
