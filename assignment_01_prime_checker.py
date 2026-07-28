
 
def is_prime(number):
    # Numbers less than 2 (0, 1, negatives) are never prime.
    if number < 2:
        return False
 
    # Check for divisors from 2 up to sqrt(number).
    # If any of them divides evenly, the number is not prime.
    divisor = 2
    while divisor * divisor <= number:
        if number % divisor == 0:
            return False
        divisor += 1
 
    return True
 
 
def main():
    user_input = input("Enter a number: ")
    number = int(user_input)
 
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is NOT a prime number.")
 
 
if __name__ == "__main__":
    main()
 