num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

match input("Enter operation (+, -, *, /): "):
    case "+":
        result = num1 + num2
        print(f"The result is {result}.")
    case "-":
        result = num1 - num2
        print(f"The result is {result}.")
    case "*":
        result = num1 * num2
        print(f"The result is {result}.")
    case "/":
        if num2 == 0:
            result = "Cannot divide by zero"
        else:
            result = num1 / num2
        print(f"The result is {result}.")
    case _:
        print("Invalid operation. Please enter +, -, *, or /.")
