# Function to count digits in a number
def count_digits(n):
    s = 0
    while n > 0:
        r = n % 10
        s += 1
        n = n // 10
    return s

# Function to reverse a number
def reverse(n):
    s = 0
    while n > 0:
        r = n % 10
        s = s * 10 + r
        n = n // 10
    return s

# Function to check if a number is a palindrome
def is_palindrome(n):
    s = 0
    a = n
    while a > 0:
        r = a % 10
        s = s * 10 + r
        a = a // 10
    return s == n

# Function to find the largest divisor of a number
def largest_divisor(n):
    big = 1
    for i in range(1, n + 1):
        if n % i == 0 and i > big:
            big = i
    return big

# Function to check if a number is prime
def is_prime(n):
    count = 0
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            count += 1
    if count == 2:
        return True
    elif count > 2:
        return False
    else:
        return 'Np Nc'  # Not prime and not composite

# Function to compute the GCD of two numbers using Euclidean algorithm
def gcd(n1, n2):
    while n1 > 0 and n2 > 0:
        if n1 > n2:
            n1 = n1 % n2
        else:
            n2 = n2 % n1
    return max(n1, n2)

# Main function calling the above functions
def main():
    # Count digits
    digits = count_digits(1234)
    print(f"Number of digits in 1234: {digits}")

    # Reverse a number
    reversed_number = reverse(1234)
    print(f"Reversed number of 1234: {reversed_number}")

    # Check if a number is a palindrome
    palindrome_check = is_palindrome(121)
    print(f"Is 121 a palindrome? {palindrome_check}")

    # Find the largest divisor of 18
    largest_div = largest_divisor(18)
    print(f"Largest divisor of 18: {largest_div}")

    # Check if a number is prime (example with n = 1)
    prime_check = is_prime(1)
    print(f"Is 1 prime? {prime_check}")

    # Compute the GCD of two numbers
    gcd_result = gcd(762, 15)
    print(f"GCD of 762 and 15: {gcd_result}")

# Call the main function
if __name__ == "__main__":
    main()
