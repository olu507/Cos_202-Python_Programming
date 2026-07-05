# COS202 Mathematical Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def modulus(a, b):
    return a % b

def power(a, b):
    return a ** b

while True:
    print("\n====== MATHEMATICAL CALCULATOR ======")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Power (^)")
    print("7. Clear")
    print("8. Exit")

    choice = input("Select an option (1-8): ")

    if choice == "8":
        print("Calculator Closed.")
        break

    elif choice == "7":
        print("Screen Cleared!")
        continue

    elif choice in ['1','2','3','4','5','6']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Answer =", add(num1, num2))

        elif choice == "2":
            print("Answer =", subtract(num1, num2))

        elif choice == "3":
            print("Answer =", multiply(num1, num2))

        elif choice == "4":
            print("Answer =", divide(num1, num2))

        elif choice == "5":
            print("Answer =", modulus(num1, num2))

        elif choice == "6":
            print("Answer =", power(num1, num2))

    else:
        print("Invalid Choice!")