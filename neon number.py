n = int(input("Enter number: "))
sq = n * n
s = 0

while sq > 0:
    s += sq % 10
    sq //= 10

print("Neon" if s == n else "Not Neon")