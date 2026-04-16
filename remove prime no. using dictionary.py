my_dict = {
    "a": 10,
    "b": 7,
    "c": 15,
    "d": 3,
    "e": 8
}

result = {}

for key, value in my_dict.items():
    is_prime = True

    if value < 2:
        is_prime = False
    else:
        for i in range(2, int(value**0.5) + 1):
            if value % i == 0:
                is_prime = False
                break

    if not is_prime:
        result[key] = value

print(result)