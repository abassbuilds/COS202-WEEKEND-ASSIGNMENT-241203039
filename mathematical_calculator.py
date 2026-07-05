# ==============================
# COS202 MATHEMATICAL CALCULATOR
# Name: Abass Nurudeen
# ==============================

def calculator():
    print("=" * 40)
    print("     COS202 MATHEMATICAL CALCULATOR")
    print("=" * 40)

    while True:
        print("\nChoose an operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Clear Screen")
        print("7. OFF")

        choice = input("\nEnter your choice (1-7): ")

        if choice == "7":
            print("\nCalculator switched OFF.")
            break

        elif choice == "6":
            print("\n" * 40)
            continue

        elif choice in ["1", "2", "3", "4", "5"]:

            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    result = num1 + num2
                    print(f"Result = {result}")

                elif choice == "2":
                    result = num1 - num2
                    print(f"Result = {result}")

                elif choice == "3":
                    result = num1 * num2
                    print(f"Result = {result}")

                elif choice == "4":
                    if num2 == 0:
                        print("Error! Division by zero is not allowed.")
                    else:
                        result = num1 / num2
                        print(f"Result = {result}")

                elif choice == "5":
                    if num2 == 0:
                        print("Error! Cannot perform modulus by zero.")
                    else:
                        result = num1 % num2
                        print(f"Result = {result}")

            except ValueError:
                print("Invalid input! Please enter numbers only.")

        else:
            print("Invalid choice. Try again.")

calculator()