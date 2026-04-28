text = "hello world"
result = ""

for ch in text:
    if ch in "aeiou":
        result += "*"
    else:
        result += ch

print(result)