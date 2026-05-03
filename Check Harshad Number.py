num = 18
temp = num
sum = 0
while temp > 0:
    digit = temp % 10
    sum += digit
    temp = temp 
if num % sum == 0:
    print("Harshad Number")
else:
    print("Not Harshad Number")