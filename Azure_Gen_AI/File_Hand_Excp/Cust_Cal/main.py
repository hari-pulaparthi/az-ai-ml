def calculator():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            operation = input("Enter the operation (+, -, *, /): ")
            num2 = float(input("Enter the second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2
            else:
                raise Exception("Invalid operation. Please enter one of +, -, *, /.")
                
            print(f"The result is: {result}")
            
        except ValueError:
            print("Invalid input. Please enter a number.")
        except ZeroDivisionError:
            print("Cannot divide by zero. Please enter a non-zero number.")
        except Exception as e:
            print(f"Error occurred: {e}")
    
        cont = input("Do you want to perform another calculation? (y/n): ")
        if cont.lower() != 'y':
            print("Exiting the calculator. Goodbye!")
            break

if __name__ == "__main__":
    calculator()

            