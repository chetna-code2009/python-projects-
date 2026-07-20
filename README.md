# Python Projects

A collection of beginner-to-intermediate Python projects built in Google Colab, demonstrating core programming concepts including functions, user input handling, and conditional logic.

---

## Projects
### 1. Functions.ipynb — Utility & Core Logic Library
A modular collection of robust, production-ready Python functions focused on algorithmic problem solving, clean code architecture, and interactive control flows.

---

#### 🔢 Mathematical Logic: `greatest_number(a, b, c)`
A deterministic utility function designed to accurately identify and isolate the maximum value out of three integer inputs.

* **Architectural Purpose:** Handles multi-variable comparisons efficiently without relying on Python's built-in `max()` function, demonstrating custom algorithmic routing.
* **Core Engineering Concepts:** Multi-branch conditionals (`if-elif-else`), logical evaluation operators, and deterministic execution paths.
* **Interviewer Takeaway (Edge-Case Handling):** 
  * Designed to safely handle duplicate entries (e.g., if $a = b > c$).
  * Implements strict short-circuit evaluation logic to minimize CPU cycles during comparison checks.

---

#### 🪙 Interactive Simulation: `play_coin_toss()`
A stateful, terminal-based simulation engine that creates a live user-versus-computer gaming session.

* **Architectural Purpose:** Emulates real-world application cycles where the system must handle unpredictable user inputs while keeping track of score statistics in real time.
* **Core Engineering Concepts:** Pseudo-randomization via `random.choice()`, un-bounded iterative loops (`while True`), local mutation for score tracking, and explicit break state conditions.
* **Interviewer Takeaway (Clean Code Practices):**
  * **Defensive Input Sanitization:** Utilizes `.strip().lower()` to gracefully normalize human inputs, mitigating issues caused by trailing spaces or unexpected capitalization.
  * **Guard Clauses:** Includes explicit verification arrays (`if guess not in ["head", "tail"]`) to filter out invalid entries early, preventing corrupted runtime states without breaking the loop execution.
  * **Encapsulation:** Keeps score statistics locally scoped within the active frame, preventing global variable pollution and ensuring the function remains highly modular and easily testable.

---

#### 🛠️ High-Level Technical Summary
* **State Management:** Employs precise mutable counters to track and persist live application states (user vs. computer score) across asynchronous game iterations.
* **Resilience:** Built with zero external dependencies, leveraging native standard libraries to ensure lightweight execution and fast load times.

🚀 **Planned Enhancements:** Algorithmic optimizations including prime verification algorithms, recursive factorial tracking, and localized string palindrome checkers.


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
