# Pattern 1
def pattern1():
    for i in range(5):
        for j in range(5):
            print("*", end="")
        print()

# Pattern 2
def pattern2():
    for i in range(6):
        for j in range(i):
            print('*', end='')
        print()

# Pattern 3
def pattern3():
    for i in range(1, 7):
        for j in range(1, i):
            print(j, end='')
        print()

# Pattern 4
def pattern4():
    for i in range(6, 0, -1):
        for j in range(1, i):
            print(j, end='')
        print()

# Pattern 5
def pattern5():
    for a in range(5):
        for b in range(5 - a - 1):
            print(' ', end='')
        for b in range(2 * a + 1):
            print('*', end='')
        for b in range(5 - a - 1):
            print(' ', end='')
        print()

# Pattern 6
def pattern6():
    for i in range(5, 0, -1):
        for j in range(5 - i):
            print(' ', end='')
        for j in range(2 * i - 1):
            print("*", end='')
        print()

# Pattern 7
def pattern7():
    for i in range(5):
        for j in range(i):
            print('*', end='')
        print()
    for a in range(5, 0, -1):
        for b in range(a):
            print("*", end='')
        print()

# Pattern 8
def pattern8():
    start = 0
    for i in range(6):
        if i % 2 == 0:
            start = 0
        else:
            start = 1
        for j in range(i):
            print(start, end='')
            start = 1 - start
        print()

# Pattern 9
def pattern9():
    k = 4
    for i in range(1, 5):
        for j in range(1, i + 1):
            print(j, end=' ')
        for j in range(2 * (k - i)):
            print(' ', end=' ')
        for j in range(1, i + 1):
            print(j, end=' ')
        print()

# Pattern 10
def pattern10():
    for i in range(6):
        for j in range(i):
            x = chr(j + 65)
            print(x, end='')
        print()

# Pattern 11
def pattern11():
    for i in range(4, 0, -1):
        for j in range(i, 5):
            print(chr(j + 65), end=' ')
        print()

# Main function to run patterns
def main():
    pattern1()
    print("\n")
    pattern2()
    print("\n")
    pattern3()
    print("\n")
    pattern4()
    print("\n")
    pattern5()
    print("\n")
    pattern6()
    print("\n")
    pattern7()
    print("\n")
    pattern8()
    print("\n")
    pattern9()
    print("\n")
    pattern10()
    print("\n")
    pattern11()

if __name__ == "__main__":
    main()
