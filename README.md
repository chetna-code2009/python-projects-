
# 🐍 Python Projects

A collection of Python programs and projects created while learning and practicing Python programming.

This repository documents my progression from Python fundamentals and problem-solving exercises toward building practical command-line applications.

The projects focus on writing programs independently, improving logical thinking, validating user input, handling errors, and applying Python concepts to practical problems.

---

## 📂 Projects

### 1. `Functions.ipynb` — Core Python Functions

A collection of Python programs created to practice reusable functions, logical problem-solving, user interaction, and basic program structure.

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

This project demonstrates how Python can be used to automate practical academic calculations.

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

An interactive calculator created to practice functions, loops, input validation, and program logic.

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

#### 🧠 Concepts Demonstrated

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

#### 🚀 Possible Improvements

- Save expense data permanently
- Load expenses when the program starts
- Calculate total expenses
- Calculate category-wise spending
- Find the highest expense
- Add search and filtering
- Add monthly expense summaries

---

### 5. `student_management.py` — Student Management System

A beginner-friendly command-line application created to strengthen Python fundamentals through a practical CRUD-style program.

#### ✨ Features

- ➕ Add Student
- 👀 View All Students
- 🔍 Search Student by Roll Number
- ✏️ Update Student Details
- 🗑️ Delete Student
- 🚪 Exit Program
- ✅ Prevent Duplicate Roll Numbers
- 🛡️ Validate User Input
- ⚠️ Handle Invalid Input

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
- Basic program organization

#### 📋 Student Information

Each student record contains:

- 👤 Name
- 🎂 Age
- 🔢 Roll Number

The **roll number is used as a unique identifier** for each student.

#### 🎮 Program Menu

```text
📚 Student Management System

1. ➕ Add Student
2. 👀 View Students
3. 🔍 Search Student
4. 🗑️ Delete Student
5. ✏️ Update Student
6. 🚪 Exit
````

#### ➕ Add Student

Allows the user to enter a student's name, age, and roll number.

The program validates the input and prevents duplicate roll numbers.

#### 👀 View Students

Displays all students currently stored in the program.

#### 🔍 Search Student

Searches for a student using their unique roll number.

#### ✏️ Update Student

Allows the user to update the student's name and age.

The roll number remains unchanged because it acts as the student's unique identifier.

#### 🗑️ Delete Student

Removes a student from the system using their roll number.

#### 🚪 Exit

Allows the user to safely exit the program.

---

## 🛡️ Validation & Error Handling

The Student Management System validates user input to reduce invalid data and prevent unexpected program crashes.

### Name Validation

Handles:

* Empty student names
* Names containing only spaces

### Age Validation

Checks:

* Invalid non-numeric input
* Negative age
* Zero age

Only valid positive age values are accepted.

### Roll Number Validation

Checks:

* Invalid non-numeric input
* Negative roll numbers
* Zero roll numbers
* Duplicate roll numbers

Each student must have a unique positive roll number.

### Search Validation

Handles:

* Invalid roll number input
* Searching for a student who does not exist

### Update Validation

Handles:

* Invalid roll number input
* Updating a non-existent student
* Invalid age input
* Empty fields

The user can leave a field blank to keep the existing value.

### Delete Validation

Handles:

* Invalid roll number input
* Attempting to delete a student who does not exist

### Menu Validation

Handles:

* Non-numeric menu input
* Numbers outside the available menu options

### Exception Handling

`try-except` is used where appropriate to handle invalid numeric input and prevent the program from terminating unexpectedly.

---

# 📚 Python Concepts Studied



### 🐍 Python Fundamentals

* Variables and assignments
* Data types
* Operators
* Expressions
* Input and output
* Type conversion
* Conditional statements
* Loops
* `break`
* `continue`
* Nested loops

### 🔤 Strings

* String operations
* String traversal
* String slicing
* String methods
* String formatting

### 📦 Python Data Structures

* Lists
* Tuples
* Dictionaries
* List operations
* Dictionary operations
* Searching and sorting concepts

### 🔧 Functions

* Defining functions
* Calling functions
* Parameters and arguments
* Positional arguments
* Default arguments
* Keyword arguments
* Multiple arguments
* Returning values
* Multiple return values
* Function composition
* Variable scope
* Mutability and immutability

### 📚 Python Libraries

* Importing modules
* Importing specific objects
* Standard Python libraries
* Using built-in and standard-library functions

### 📁 File Handling

Studied and practiced:

* Text files
* Opening and closing files
* Reading from files
* Writing to files
* File pointers
* Binary files
* Pickling and unpickling
* Searching in files
* Updating binary files
* CSV files
* Reading and writing CSV data

### ⚠️ Exception Handling

Studied:

* Exceptions
* `try`
* `except`
* `finally`
* Handling different types of errors
* Raising exceptions

### 🧱 Data Structures

Studied:

* Linear lists / arrays
* Stacks
* Queues
* Linked lists
* Trees
* Basic operations on data structures
* Stack implementation and applications

### 🗄️ SQL & Relational Databases

Studied:

* Relational database concepts
* DBMS fundamentals
* MySQL
* SQL commands
* `SELECT`
* `WHERE`
* `ORDER BY`
* `DISTINCT`
* `NULL` handling
* SQL operators
* SQL functions
* String functions
* Numeric functions
* Date and time functions
* Aggregate functions
* `GROUP BY`
* `HAVING`
* Table aliases
* Joins
* Creating databases
* Creating tables
* Constraints
* `INSERT`
* `UPDATE`
* `DELETE`
* `ALTER TABLE`
* `DROP TABLE`

### 🔗 Python with MySQL

Studied the fundamentals of connecting Python programs with MySQL databases, including:

* Database connectivity
* Creating database connections
* Executing SQL commands from Python
* Parameterised queries
* Performing insert and update operations

---

# 🧠 Current Skill Level

My current Python experience is focused on **fundamentals, problem-solving, command-line applications, data structures, file handling, SQL, and database concepts**.

I am now moving from learning individual concepts toward combining them into larger and more practical programs.

### Current Position

```text
Python Fundamentals       🟢
Functions                 🟢
Lists / Tuples / Dicts    🟢
Input & Validation        🟢
Exception Handling        🟢
File Handling             🟢
CSV                       🟢
Basic Data Structures     🟢
SQL                       🟢
Relational Databases      🟢
Python + MySQL            🟢
Git / GitHub              🟢
Practical Projects        🟢
OOP                       🔵
Advanced DSA              🔵
Web Development           🔵
APIs                      🔵
Backend Development       🔵
```

> 🟢 = Studied / Practiced
> 🔵 = Future Learning

---

# 🎯 Next Learning Goals

The next stage of my Python learning will focus on applying the concepts I have already studied and developing stronger software development skills.

### Planned Topics

* Object-Oriented Programming (OOP)
* Classes and objects
* Constructors
* Encapsulation
* Inheritance
* Polymorphism
* JSON
* More database-driven applications
* Advanced SQL
* Data Structures and Algorithms
* APIs
* Web development
* Backend development
* Larger software projects

---

# 🚀 Future Project Improvements

The existing projects can be extended as my skills improve.

### Student Management System

Possible improvements:

* MySQL database integration
* Persistent data storage
* Student marks and grades
* Attendance management
* Search and filtering
* CSV export
* Performance reports
* OOP-based architecture
* GUI or web interface

### Expense Tracker

Possible improvements:

* JSON or database storage
* Expense analytics
* Category summaries
* Monthly reports
* Search and filtering
* CSV export

---

# 🛠️ Tech Stack

* **Language:** Python 3
* **Editors:** Visual Studio Code / Google Colab / Jupyter Notebook
* **Database:** MySQL
* **Version Control:** Git
* **Repository:** GitHub
* **Libraries:** Python Standard Library

---

# ▶️ How to Run

## Google Colab / Jupyter Notebook

1. Open the `.ipynb` file in Google Colab or Jupyter Notebook.
2. Run the cells sequentially.
3. In Google Colab, use **Runtime → Run all**.

## Python Script

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

# 📈 Learning Progress

These projects represent my progression from basic Python exercises toward practical command-line applications.

### Skills Practiced

* 🐍 Python programming
* 🔧 Functions
* 🔁 Loops
* 🧠 Conditional logic
* 📚 Lists, tuples, and dictionaries
* ⌨️ User input
* 🛡️ Input validation
* ⚠️ Exception handling
* 📁 File handling
* 🗄️ SQL and databases
* 🔗 Python-MySQL concepts
* ✨ String formatting
* 💻 Command-line applications
* 🏗️ Basic program architecture
* 🔀 Git and GitHub

---

# 🌱 What's Next?

The goal is to move from small standalone programs toward applications that combine multiple concepts.

The next projects will focus on:

```text
Python
   ↓
OOP
   ↓
SQL + MySQL
   ↓
Data Structures & Algorithms
   ↓
APIs
   ↓
Backend Development
   ↓
Larger Software Projects
```

---

# 👩‍💻 Author

**Chetna**

BCA student learning Python, C++, problem-solving, databases, and software development through practical projects.

---

⭐ This repository documents my programming journey from Python fundamentals toward building larger, more practical software applications.

```

