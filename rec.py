def main():
    # Calling the 'rec' function to print "Hello world" 5 times
    print("Function rec:")
    def rec(x, count):
        if count == 5:
            return 0
        print(x)
        count += 1
        rec(x, count)
    rec('Hello world', 0)

    # Calling the 'incc' function to print numbers from 1 to 10
    print("\nFunction incc:")
    def incc(x):
        if x == 11:
            return 0
        print(x)
        x += 1
        incc(x)
    incc(1)

    # Calling the 'fac' function to calculate the factorial of 5
    print("\nFunction fac:")
    def fac(x):
        if x == 1:
            return 1
        else:
            return x * fac(x - 1)
    b = fac(5)
    print(b)

    # Calling the 'dec' function to print numbers from 10 down to 1
    print("\nFunction dec:")
    def dec(x):
        if x == 0:
            return 0
        else:
            print(x)
            dec(x - 1)
    dec(10)

    # Calling the 'fib' function to print the first 10 Fibonacci numbers
    print("\nFunction fib:")
    def fib(a, b, i):
        if i == 10:
            return 0
        s = a + b
        print(s)
        a = b
        b = s
        fib(a, b, i + 1)
    print(0)
    print(1)
    fib(0, 1, 0)

    # Calling the 'rev' function to reverse an array
    print("\nFunction rev:")
    def rev(arr, i, j):
        if j < i:
            print(arr)
            return 0
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        rev(arr, i + 1, j - 1)
    a = [1, 2, 3, 4]
    n = len(a) - 1
    rev(a, 0, n)

    # Calling the 'pal' function to check if the string "RACECAR" is a palindrome
    print("\nFunction pal:")
    def pal(arr, i, j):
        if j <= i:
            print(True)
            return
        if arr[i] != arr[j]:
            print(False)
            return
        pal(arr, i + 1, j - 1)
    a = "RACECAR"
    n = len(a) - 1
    pal(a, 0, n)

# Run the main function
main()
