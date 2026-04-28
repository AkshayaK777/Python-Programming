text = "Hello world from python, my name is python"
count = 0

for ch in text:
    if ch == " ":
        count += 1

print("Spaces:", count)