char = input("Enter a letter: ").lower()
vowels = "aeiou"
if char in vowels:
    print(f"{char} is a vowel")
else:
    print(f"{char} is a consonant")