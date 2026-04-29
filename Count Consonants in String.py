text = "hello world"
count = 0

for ch in text:
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Consonants:", count)