 
def print_multiplication_table(number):
    """Print the multiplication table for `number`, from 1 to 12."""
    print(f"Multiplication Table for {number}:")
    for i in range(1, 13):
        print(f"{number} x {i:<2} = {number * i}")
 
 
def print_tables_up_to(n):
    """Print the full multiplication table for every number from 1 to n."""
    separator = "-" * 30
    for number in range(1, n + 1):
        print_multiplication_table(number)
        if number != n:
            print(separator)
 
 
def run_part_a():
    number = int(input("Enter a number: "))
    print()
    print_multiplication_table(number)
 
 
def run_part_b():
    n = int(input("Enter N (print tables from 1 to N): "))
 
    if n <= 0:
        print("Error: N must be a positive integer.")
        return
 
    print()
    print_tables_up_to(n)
 
 
def main():
    print("Multiplication Table Generator")
    print("1. Single Table (Part A)")
    print("2. Tables from 1 to N (Part B - Bonus)")
    choice = input("Choose an option (1-2): ").strip()
 
    if choice == "1":
        run_part_a()
    elif choice == "2":
        run_part_b()
    else:
        print("Invalid choice. Please enter 1 or 2.")
 
 
if __name__ == "__main__":
    main()