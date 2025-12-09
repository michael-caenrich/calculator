# 🧮 Simple CLI Calculator

A lightweight and beginner-friendly command-line calculator built with Python.  
Supports basic operations: **addition, subtraction, multiplication, division** 
All commands run from the terminal, with color-coded input prompts.

---

## Features
- Simple CLI interface
- Handles numeric input validation
- Supports:
    - ➕ Addition
    - ➖ Subtraction
    - ✖️ Multiplication
    - ➗ Division (with zero-division handling)
- Clean exit option
- ANSI-colored prompts for clarity (no external libraries)

---

## How to Run
```bash
python calculator.py
```
---

## Example Output
### === Choose calculation category ===
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose category: 2
Enter parameter 'a': 15
Enter parameter 'b': 5
Result: 10.0
Note: 'a' and 'b' appear in cyan using ANSI escape codes (\033[96m...\033[0m)

---

## Folder Structure
```text
calculator/
├── calculator.py     # main CLI script
├── README.md         # this file
└── .gitignore        # optional
```

---

## Future Ideas
- Support operator input (+, -, etc.) instead of menu
- Store history of operations
- Add scientific calculator mode
- Add unit tests for core operations

---

## .gitignore
```text
__pycache__/
*.pyc
.DS_Store
```

---

## License
This project is for learning and practice — feel free to use or modify it however you like.

