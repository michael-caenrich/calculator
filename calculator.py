def calculator():
    """Interactive command-line calculator for basic operations"""
    while True:
        # Show meny options
        print("\n\033[96m=== Calculator ===\033[0m")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Choose category (number): ").strip()

        # Validate menu choice
        if not choice.isdigit() or not (1 <= int(choice) <= 5):
            print("\n⚠️Wrong value. Try again")
            continue

        choice = int(choice)

        # Exit the script
        if choice == 5:
            print("Goodbye! 👋")
            break

        # Ask for valid numerical input
        while True:
            try:
                a = float(input("\nEnter parameter \033[94ma\033[0m: "))
                b = float(input("Enter parameter \033[94mb\033[0m: "))
                break
            except ValueError:
                print("⚠️Wrong value. Enter numeric value.")

        # Perform calculation based on menu selection
        if choice == 1:
            print(f"Result: \033[92m{a + b:.2f}\033[0m")
        elif choice == 2:
            print(f"Result: \033[92m{a - b:.2f}\033[0m")
        elif choice == 3:
            print(f"Result: \033[92m{a * b:.2f}\033[0m")
        elif choice == 4:
            try:
                result = a / b
                print(f"Result: \033[92m{result:.2f}\033[0m")
            except ZeroDivisionError as e:
                print(f"⚠️Error: {e}")

if __name__ == "__main__":
    calculator()

