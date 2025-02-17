def safe_division():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 =float(input("Enter the second number: "))
            result=num1/num2
            print(f"Result: {result:.2f}")
            break
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed. Try again.")
        except ValueError:
            print("Error: Please enter valid numeric values.")
        except KeyboardInterrupt:
            print("\nOperation interrupted by user. Exiting...")
            break  # Exit on Ctrl+C
        except Exception as e:
            print(f"Unexpected Error: {e}")

        print("Let's try again!\n")



safe_division()