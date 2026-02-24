## 📑 Week-1: Building the Input Layer
Welcome to your first build. Now that your sandbox is active per the Standard Operating Procedure (SOP) in the root directory, you will begin engineering the Daily Log Engine. This week focuses on the Input Layer: a CLI script that captures user input and echoes it back in a structured format.

---

## Step 1: Initialize your Week-1 Workspace
Before writing logic, you must prepare your environment for this specific module.

1. Ensure you are in the `/Week-1` directory at the root of the repository.
2. Create a new file named `daily_log.py`.
3. Open the file in your preferred editor (e.g., VS Code).

---

## Step 2: Engineering the Entry Point
Every professional script requires a clean entry point. We will use the if __name__ == "__main__": block to ensure our script runs only when executed directly.

Type the following into daily_log.py:

```python
def main():
    print("--- Apex Daily Log Engine: Initialized ---")
    
if __name__ == "__main__":
    main()
```

---

## Step 3: Capturing User Input
A Systems Integrator builds tools that interact with users. Your task is to capture three data points: the User's Name, the Current Task, and the Completion Status.

Update your main() function with this logic:

```python
def main():
    print("--- Apex Daily Log Engine: Initialized ---")
    
    # Capturing Data
    user_name = input("Enter Integrator Name: ")
    current_task = input("Enter Current Task: ")
    status = input("Task Status (In-Progress/Complete): ")

    # Structuring Output
    print("\n--- Log Entry Summary ---")
    print(f"Integrator: {user_name}")
    print(f"Task: {current_task}")
    print(f"Status: {status}")
```

---

## Step 4: Verification (The Apex Standard)
To complete this lab, you must verify your script against the Gold Standard.

Run your script: Execute python daily_log.py in your terminal.

Test the input: Enter your data and ensure the summary prints correctly.

Compare: Open /reference/Week-1/daily_log.py and compare your logic. Even if yours works, check the reference for formatting differences.

---

## 🛡️ Pro-Tip: Muscle Memory
Do not copy and paste the code above. The physical act of typing these characters is what builds the neurological pathways required for rapid debugging later.