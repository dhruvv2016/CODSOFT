def calculator():
    print("\nSimple Calculator")
    print("----------------")
    
    try:
        # Get user input
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        # Perform calculation
        if choice == '1':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '2':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '3':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '4':
            if num2 == 0:
                print("\nError: Cannot divide by zero!")
            else:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
        else:
            print("\nInvalid input! Please select 1, 2, 3, or 4.")
    
    except ValueError:
        print("\nInvalid input! Please enter numbers only.")

# Run the calculator
calculator()

# Option to run again
while True:
    again = input("\nWould you like to perform another calculation? (yes/no): ").lower()
    if again == 'no':
        print("\nThank you for using the calculator!")
        break
    elif again == 'yes':
        calculator()
    else:
        print("Please enter 'yes' or 'no'.")
