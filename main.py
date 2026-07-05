try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    print("""
Press + for addition
Press - for subtraction
Press * for multiplication
Press / for division
""")

    o = input("Enter operation: ")

    match o:
        case "+":
            print(f"Result = {a + b}")
        case "-":
            print(f"Result = {a - b}")
        case "*":
            print(f"Result = {a * b}")
        case "/":
            print(f"Result = {a / b}")
        case _:
            print("Invalid operation!")

except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")


