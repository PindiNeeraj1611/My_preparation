# Selection sort function
def selecn(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# Bubble sort function
def bubble(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-1):
            if arr[j+1] < arr[j]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# Insertion sort function
def insertionsort(arr):
    for i in range(len(arr)):
        for j in range(i+1):
            if arr[j] > arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

# Main function to test sorting algorithms
def main():
    arr1 = [5, 4, 3, 2, 1]
    arr2 = [5, 4, 3, 2, 1]
    arr3 = [14, 9, 15, 12, 6, 8, 13]
    
    print("Original array 1:", arr1)
    print("Selection Sort:", selecn(arr1.copy()))  # Copy to avoid modifying the original array
    print()

    print("Original array 2:", arr2)
    print("Bubble Sort:", bubble(arr2.copy()))  # Copy to avoid modifying the original array
    print()

    print("Original array 3:", arr3)
    print("Insertion Sort:", insertionsort(arr3.copy()))  # Copy to avoid modifying the original array
    print()

# Calling the main function
if __name__ == "__main__":
    main()
