import string 
s="Hello world!"
result=""
for ch in s:
    if ch not in string.punctuation:
        result+=ch
        print(result)