
def add(a, b):
    return a + b
 
 
def subtract(a, b):
    return a - b
 
 
def multiply(a, b):
    return a * b
 
 
def divide(a, b):
    """Return a / b rounded to 2 decimal places, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)
 
 
def modulus(a, b):
    """Return a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b
 

def power(a, b):
    return a ** b
 
 
def get_number(prompt):
    """Read a number from the user, preserving int type when possible."""
    value = input(prompt)
    try:
        return int(value)
    except ValueError:
        return float(value)
 
 
def display_menu():
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")
 
 
def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", power),
    }
 
    while True:
        display_menu()
        choice = input("Select an operation (1-7): ").strip()
        print()
 
        if choice == "7":
            print("Goodbye!")
            break
 
        if choice not in operations:
            print("Error: Invalid choice. Please select a number from 1 to 7.")
            print()
            continue
 
        symbol, operation = operations[choice]
        a = get_number("Enter first number : ")
        b = get_number("Enter second number: ")
 
        if choice in ("4", "5") and b == 0:
            if choice == "4":
                print("Error: Cannot divide by zero.")
            else:
                print("Error: Cannot perform modulus by zero.")
            print()
            continue
 
        result = operation(a, b)
        print(f"Result: {a} {symbol} {b} = {result}")
        print()
 
 
if __name__ == "__main__":
    main()