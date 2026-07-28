def generate_fibonacci_terms(n):
    """Return a list containing the first `n` terms of the Fibonacci sequence."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence
 
 
def is_fibonacci(number):
    """Return True if `number` appears in the Fibonacci sequence."""
    if number < 0:
        return False
 
    a, b = 0, 1
    while a < number:
        a, b = b, a + b
 
    return a == number
 

def run_part_a():
    n = int(input("How many terms? "))
 
    if n <= 0:
        print("Error: Number of terms must be a positive integer.")
        return
 
    sequence = generate_fibonacci_terms(n)
    print("Fibonacci sequence: " + " ".join(str(term) for term in sequence))
 
 
def run_part_b():
    number = int(input("Enter a number to check: "))
 
    if is_fibonacci(number):
        print(f"{number} is a Fibonacci number.")
    else:
        print(f"{number} is NOT a Fibonacci number.")
 
 
def main():
    run_part_a()
    print()
    run_part_b()
 
 
if __name__ == "__main__":
    main()
 