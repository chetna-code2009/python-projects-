
# 🐍 Python Projects

A collection of Python projects built while learning and practicing Python programming.

These projects cover programming fundamentals such as functions, loops, conditional statements, user input, input validation, exception handling, lists, dictionaries, and basic program architecture.

---

## 📂 Projects

### 1. `Functions.ipynb` — Core Python Functions

A collection of Python programs designed to practice reusable functions, logical problem-solving, user interaction, and basic program structure.

#### 🔢 Greatest Number — `greatest_number(a, b, c)`

A function that determines the greatest value among three numbers.

**Concepts demonstrated:**

- Functions and parameters
- `if-elif-else`
- Comparison operators
- Logical conditions
- Handling equal values
- Returning results

---

#### 🪙 Coin Toss Game — `play_coin_toss()`

An interactive coin-toss game where the user plays against a computer-generated result and keeps track of the score.

**Concepts demonstrated:**

- `random.choice()`
- `while` loops
- User input
- Input validation
- `.strip()` and `.lower()`
- Conditional logic
- Score tracking
- `break`
- Function scope

---

#### 📊 Academic Percentage Calculator — `calculate_bciit_semester_percentage()`

A Python program designed to calculate semester performance using subject marks and academic evaluation rules.

**Concepts demonstrated:**

- Dictionaries
- Functions
- User input
- Input validation
- `try-except`
- Conditional statements
- Grade calculation
- Pass/fail checking
- Backlog detection
- Formatted output

This project demonstrates how Python can be used to automate real-world academic calculations.

---

### 2. `temperature_converter.ipynb` — Temperature Converter

An interactive program that converts temperatures between Celsius and Fahrenheit.

#### Features

- Accepts temperature values from the user
- Accepts the source temperature unit
- Validates user input
- Handles invalid entries
- Uses standard conversion formulas
- Displays formatted results

**Concepts demonstrated:**

- Functions
- User input
- Conditional logic
- Input validation
- Error handling
- Mathematical formulas
- Formatted strings

---

### 3. `calculator.ipynb` — Python Calculator

An interactive calculator designed to practice functions, loops, input validation, and basic program logic.

#### Features

- Continuous calculations
- Decimal number support
- Percentage calculations
- Previous-result functionality
- Input validation
- Division-by-zero protection
- Multiple arithmetic operations

#### 🛠️ Supported Operations

| Operator | Operation |
|----------|-----------|
| `+` | Addition |
| `-` | Subtraction |
| `*` | Multiplication |
| `/` | Division |
| `%` | Percentage |

**Concepts demonstrated:**

- Functions
- Loops
- Conditional statements
- User input
- Exception handling
- Arithmetic operations
- String formatting

---

### 4. `expense_tracker.py` — Expense Tracker

A terminal-based expense tracking application that allows users to add, view, and delete expenses.

The program uses Python data structures and a menu-driven interface to manage expense records.

#### 💰 Features

- Add new expenses
- Store expense categories
- Store expense amounts
- View recorded expenses
- Delete expenses by number
- Input validation
- Error handling
- Menu-driven interaction
- Formatted expense display

#### 🛠️ Concepts Demonstrated

- Functions
- Lists
- Dictionaries
- `while` loops
- `if-elif-else`
- User input
- `try-except`
- Input validation
- `enumerate()`
- String formatting
- Function scope
- Basic program architecture

#### 🚀 Future Improvements

- Save expense data permanently using JSON
- Load saved expenses when the program starts
- Calculate total expenses
- Calculate category-wise spending
- Find the highest expense
- Add search and filtering
- Add monthly expense summaries

---

### 5. `student_management.py` — Student Management System

A beginner-friendly **Python Student Management System** created to practice and strengthen Python fundamentals through a practical command-line application.

#### ✨ Features

- ➕ Add Student
- 👀 View All Students
- 🔍 Search Student by Roll Number
- ✏️ Update Student Details
- 🗑️ Delete Student
- 🚪 Exit Program
- ✅ Prevent Duplicate Roll Numbers
- 🛡️ Validate User Input
- ⚠️ Handle Invalid Input with Error Handling

#### 🧠 Concepts Demonstrated

- Variables
- Lists
- Dictionaries
- Functions
- `if`, `elif`, `else`
- `for` loops
- `while` loops
- `try` / `except`
- Input validation
- `append()`
- `enumerate()`
- `del`
- f-strings
- Dictionary access
- List manipulation
- Menu-driven programming

#### 📋 Student Information

Each student record contains:

- 👤 Name
- 🎂 Age
- 🔢 Roll Number

The **roll number is used as a unique ID** for each student.

#### 🎮 How to Use

After running the program, the following menu will appear:

```text
📚 Student Management System
1. ➕ Add Student
2. 👀 View Students
3. 🔍 Search Student
4. 🗑️ Delete Student
5. ✏️ Update Student
6. 🚪 Exit
````

Enter the number corresponding to the action you want to perform.

#### ➕ Add Student

Enter the student's name, age, and roll number.

The program validates the information and prevents duplicate roll numbers.

#### 👀 View Students

Displays all students currently stored in the program.

#### 🔍 Search Student

Searches for a student using their unique roll number.

#### ✏️ Update Student

Allows the user to update the student's name and age.

Leave a field blank if you want to keep the existing value.

The roll number remains unchanged because it acts as the student's unique identifier.

#### 🗑️ Delete Student

Removes a student from the system using their roll number.

#### 🚪 Exit

Select option `6` to safely exit the program.

---

## 🛡️ Validation & Error Handling

The Student Management System validates user input to prevent invalid data and unexpected program crashes.

### Name Validation

The program handles:

* Empty student names
* Names containing only spaces

### Age Validation

The program checks:

* Invalid non-numeric input
* Negative age
* Zero age

Only valid positive age values are accepted.

### Roll Number Validation

The program checks:

* Invalid non-numeric input
* Negative roll numbers
* Zero roll numbers
* Duplicate roll numbers

Each student must have a unique positive roll number.

### Search Validation

The program handles:

* Invalid roll number input
* Searching for a student who does not exist

### Update Validation

The program handles:

* Invalid roll number input
* Updating a non-existent student
* Invalid age input
* Empty fields

The user can leave the name or age field blank to keep the existing information.

### Delete Validation

The program handles:

* Invalid roll number input
* Attempting to delete a student who does not exist

### Menu Validation

The program handles:

* Non-numeric menu input
* Numbers outside the available menu options

### Exception Handling

`try-except` is used to safely handle invalid numeric input and prevent the program from crashing.

---

## 🚀 Future Improvements

The Student Management System can be extended with:

* 💾 Permanent data storage using JSON
* 🗄️ SQLite database integration
* 📊 Marks and grade management
* 📈 Student performance reports
* 🔐 User authentication
* 📅 Attendance management
* 🔎 Advanced search and filtering
* 🖥️ Graphical User Interface (GUI)
* 📤 Export student data to CSV

---

## 📌 Current Status

**Completed ✅**

The current version stores student data temporarily in memory.

Therefore, all student data is lost when the program is closed.

Permanent data storage using JSON is planned as a future improvement.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Environment:** Google Colab / Jupyter Notebook / VS Code
* **Libraries:** Python Standard Library
* **External Dependencies:** None

---

## ▶️ How to Run

### Google Colab / Jupyter Notebook

1. Open the `.ipynb` file in Google Colab or Jupyter Notebook.
2. Run the cells sequentially.
3. In Google Colab, use **Runtime → Run all**.

### Python Script

1. Install Python 3.
2. Open the project folder in VS Code or a terminal.
3. Run the Python file:

```bash
python filename.py
```

For the Student Management System:

```bash
python student_management.py
```

For the Expense Tracker:

```bash
python expense_tracker.py
```

---

## 🎯 Learning Progress

These projects represent my progression from Python fundamentals to building interactive command-line applications.

### Skills Practiced

* 🐍 Python fundamentals
* 🔧 Functions
* 🔁 Loops
* 🧠 Conditional logic
* 📚 Lists and dictionaries
* ⌨️ User input
* 🛡️ Input validation
* ⚠️ Exception handling
* ✨ String formatting
* 💻 Interactive programs
* 🏗️ Basic program architecture
* 🔗 Git and GitHub workflow

---

## 📈 Future Learning Goals

As I continue my BCA journey, I plan to expand my programming and software development skills.

### Planned Topics

* Object-Oriented Programming (OOP)
* File handling
* JSON
* SQL and databases
* Data Structures and Algorithms
* C++
* APIs
* Web development
* Backend development
* Larger software projects

---

## 👩‍💻 Author

**Chetna**

BCA student learning Python, problem-solving, and software development through practical projects.

---

⭐ This repository documents my learning journey from Python fundamentals toward building larger and more practical software projects.

```
```
