# Python Projects

A collection of beginner-to-intermediate Python projects built in Google Colab, demonstrating core programming concepts including functions, user input handling, and conditional logic.

---

## Projects

### 1. `functions.ipynb` — Utility Functions Library
A modular collection of reusable Python functions for common computational tasks.

| Function | Description | Concepts Used |
|----------|-------------|---------------|
| `greatest_number(a, b, c)` | Returns the largest of three input integers | Conditional statements (`if-elif-else`), comparison operators |
**Planned additions:**  prime number checker, factorial function, palindrome checker

# 2. `temperature_converter.ipynb` — Interactive Temperature Converter
A standalone utility application that provides an interactive interface for temperature conversion.

**Features:**
- Accepts user input for temperature value and source unit
- Validates input and handles invalid entries
- Converts between Celsius and Fahrenheit with precise formula application
- Displays formatted output with unit labels

**Concepts demonstrated:** User input handling, input validation, error handling, formatted string output.

## Tech Stack
- **Language:** Python 3
- **Environment:** Google Colab / Jupyter Notebook
- **Libraries:** Built-in functions only (no external dependencies)

## How to Run
1. Clone this repository
2. Open any `.ipynb` file in Google Colab or Jupyter Notebook
3. Run all cells sequentially (`Runtime` → `Run all` in Colab)

 ## What I'm Learning
**Current Focus:**
- Core Python programming (functions, conditionals, input handling) — practiced via Google Colab on Android
- Writing clean, reusable code with proper documentation
- Structuring small projects for clarity and scalability

**Academic Path:** Pursuing BCA (Bachelor of Computer Applications)

**Career Goal:** Building foundational skills toward a career in **Artificial Intelligence and Machine Learning**

**Why this matters:** Every function I write here — from a temperature converter to a calculator — is deliberate practice in problem decomposition, logic building, and code organization. These fundamentals scale directly to larger AI/ML systems where clean data pipelines and modular functions are critical.
# Advanced Python Calculator

A terminal-based Python calculator that supports continuous calculations, decimal inputs, percentage operations, and memory storage to chain equations together.

## 🚀 Features

*   **Continuous Loop**: Keep calculating without restarting the program.
*   **Memory Storage**: Option to use your last result as the starting number for the next math problem.
*   **Percentage Support (`%`)**: Easily calculate percentages (e.g., finding 10% of 200).
*   **Smart Input Validation**: Prevents crashes if a user accidentally types text instead of a number.
*   **Crash Protection**: Safeguards against math rule violations like dividing by zero.

## 🛠️ Supported Operations

*   `+` : Addition
*   `-` : Subtraction
*   `*` : Multiplication
*   `/` : Division
*   `%` : Percentage

## 💻 How To Run

1. Make sure you have **Python 3** installed on your computer.
2. Save the code into a file named `calculator.py`.
3. Open your terminal or command prompt.
4. Run the following command:

```bash
python calculator.py
```

## 📝 How It Works (Code Architecture)

*   **Modular Design**: Every math operation is assigned to its own dedicated function (`add`, `subtract`, etc.).
*   **Dictionary Mapping**: Instead of using long `if/elif` statements, the script uses a Python dictionary to map symbols (`+`, `-`) directly to functions for cleaner, faster execution.
*   **State Management**: Uses a global variable `previous_answer` to safely track your session history for chained calculations.


---
*More projects coming soon —  number guessing game, and data analysis tools.*
