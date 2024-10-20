def brut(x, l):
    count = 0
    for i in l:
        if i == x:
            count += 1
    return count

def Hsh(arr, a):
    l = max(arr) + 1
    hsh = [0] * l
    for i in arr:
        hsh[i] += 1
    return hsh[a]

def sthsh(s, a):
    t = ord(a) - 97
    s = s.lower()
    hs = [0] * 27
    for i in s:
        x = ord(i) - 97
        hs[x] += 1
    return hs[t]

def countfreq(d):
    dic = {}
    for i in d:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic

# Main function
def main():
    # Call brut function
    result1 = brut(3, [1, 2, 1, 3, 2])
    print("Result of brut:", result1)

    # Call Hsh function
    result2 = Hsh([1, 2, 1, 3, 2], 1)
    print("Result of Hsh:", result2)

    # Call sthsh function
    result3 = sthsh('abcdabefc', 'c')
    print("Result of sthsh:", result3)

    # Call countfreq function
    result4 = countfreq('abcdabefc')
    print("Result of countfreq:", result4)

# Run the main function
if __name__ == "__main__":
    main()
