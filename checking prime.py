n = int(input("Enter number: "))
print("Prime" if all(n % i != 0 for i in range(2, n)) and n > 1 else "Not Prime")