def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1
arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

target = int(input("Enter number to search: "))
result = linear_search(arr, target)
if result != -1:
    print(f"Element {target} found at index {result} (position {result+1})")
else:
    print(f"Element {target} not found in the list")