## 🛠️ Setup Instructions: The Python Development Sandbox

Welcome to the **Professional Growth Engine** development environment. In this lab, you are not just a student; you are a Systems Integrator. Following this **Standard Operating Procedure (SOP)** ensures your environment is stable and professional. 

You will not be "running" code provided to you—you will be building it from scratch in your own workspace.

Follow these steps to initialize your environment.

---

## Step 1: The Directory Structure
Before starting, ensure your local repository looks like this. You will notice the `/workspace` folder is where you will spend 90% of your time.

* `/reference`: Contains the complete code for verification.
* `/workspace`: This is your personal sandbox to write your code.
* `/PythonSandbox`: This will house your virtual Python environment and dependencies.

---

## Step 2: Initialize the PythonSandbox
We use a **Virtual Environment** to ensure our project is isolated from the rest of your computer. This prevents "version rot" and dependency conflicts.

**Execute the following commands in your terminal at the root of this repo:**

### For Windows:
```powershell
# Create the sandbox
python -m venv PythonSandbox

# Activate the sandbox
.\PythonSandbox\Scripts\activate
```

### For Mac/Linux:
```bash
# Create the sandbox
python3 -m venv PythonSandbox

# Activate the sandbox
source PythonSandbox/bin/activate
```
> [!TIP]
> **Note:** When activated, you should see (PythonSandbox) appearing at the start of your terminal prompt. This confirms you are now working inside your isolated environment.

---

## Step 3: Your First Task: Workspace Initialization
> [!TIP]
> Commands below are for Mac/Linux.

Do not copy files from the /reference folder. Instead, follow these steps to prove your environment is live:
1. **Navigate into the workspace/ directory:** cd workspace
2. **Create your first Python file:** touch app.py (or right-click in VS Code to create a new file).
3. Open app.py and write a single line of code to verify the environment:
```python
print("Professional Growth Engine: Sandbox Active.")
```
4. **Run your code:** `python3 app.py`

---

## Step 4: Best Practices
* **Never commit your Sandbox:** Your .gitignore is already configured to ignore the /PythonSandbox folder. We share logic on GitHub, not environments.
* **Type, Don't Paste:** To build muscle memory, type out every line of code from the weekly lessons.
* **Consult the Reference:** If your code fails and you cannot find the bug, compare your script to the version in /reference. This is how you learn to debug like a Pro.

---

**Next Step:** Proceed to the **Week 1 Lab Manual** to begin building your Daily Log Engine.