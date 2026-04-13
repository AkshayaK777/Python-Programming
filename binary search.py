def binary_search(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

arr.sort()  # Binary search needs sorted array
print("Sorted array:", arr)

target = int(input("Enter number to search: "))
result = binary_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result} (position {result+1})")
else:
    print(f"Element {target} not found in the list")