def palindrome(num):
    rev = 0
    temp = num

    while temp != 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp //10

    return rev
num = int(input("Enter the number: "))

if num == palindrome(num):
    print("The number is a palindrome")
else:
    print("The number is not a palindrome")