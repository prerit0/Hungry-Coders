# Copilot Instructions for basics-again

## Project Overview
This repository appears to be a beginner-friendly Python learning workspace. The codebase currently contains a single script (`1-pyt.py`) that demonstrates basic input/output and arithmetic operations. The project is likely used for educational or experimentation purposes, with a focus on simple, self-contained Python scripts.

## Key Patterns and Conventions
- Each script is standalone and does not import from other files.
- User input is collected using `input()` and converted to integers with `int()`.
- Output is printed directly using `print()`.
- Variable names are short and descriptive (e.g., `a`, `b`, `sum`).
- There is no use of functions, classes, or modules at this stage.

## Developer Workflows
- To run a script, use:
  ```powershell
  python 1-pyt.py
  ```
- No build, test, or dependency management tools are present or required.
- No external libraries are used; only the Python standard library is expected.

## Project Structure
- All code is in the root directory. There are no subfolders or package structures.
- Each file is intended to be run independently.

## Recommendations for AI Agents
- When adding new scripts, follow the pattern of simple, self-contained files.
- Use clear prompts for user input and print outputs for results.
- Avoid introducing unnecessary complexity (e.g., advanced Python features) unless the project evolves.
- If expanding, consider naming new files descriptively (e.g., `2-strings.py`, `3-loops.py`).

## Example
```python
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
sum = a + b
print(sum)
```

## No Special Integration Points
- There are no external APIs, services, or integrations.
- No configuration files or environment variables are required.

---
If the project structure or goals change, update these instructions to reflect new patterns or workflows.
