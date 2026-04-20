L1= []
n=int(input("enter how many numbers:"))
for i in range(n):
    num = int(input("enter the numbers:"))
L1.append(num)
print("the list of elemnts are:",L1)
L=[]
for j in L1:
    L.append(j**2)
    print("the square of the list are:",L)