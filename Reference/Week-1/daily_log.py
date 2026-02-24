"""
Professional Growth Engine: Daily Log CLI (Week-1)
Description: A simple CLI tool to capture and echo daily integrator tasks.
Best Practice: Descriptive naming used for standalone utility scripts.
"""

def main():
    """
    Primary entry point for the Daily Log Engine.
    Handles user input and structured console output.
    """
    print("--- Apex Daily Log Engine: Initialized ---")
    print("Standard Operating Procedure: ACTIVE\n")

    # Capture Phase: Gathering data from the integrator
    # Real-World Note: We use input() for basic CLI interaction.
    user_name = input("Enter Integrator Name: ")
    current_task = input("Enter Current Task: ")
    status = input("Task Status (In-Progress/Complete): ")

    # Output Phase: Displaying structured results
    # Real-World Note: f-strings provide clean, readable string interpolation.
    print("\n" + "="*30)
    print("      DAILY LOG SUMMARY")
    print("="*30)
    print(f"INTEGRATOR : {user_name}")
    print(f"TASK       : {current_task}")
    print(f"STATUS     : {status}")
    print("="*30)

if __name__ == "__main__":
    # Ensure the script only runs when executed directly, not when imported.
    main()