n = int(input("Enter number: "))
temp = n
s = 0

while temp > 0:
    d = temp % 10
    s += d**3
    temp //= 10

print("Armstrong" if n == s else "Not Armstrong")