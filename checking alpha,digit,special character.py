a="abc1233xyz*345"
digits = ""
alphabets = ""
special = ""
for ch in a:  
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        alphabets += ch
    else:
        special += ch
print("digits:", digits)
print("alphabets:", alphabets)
print("special:",special)