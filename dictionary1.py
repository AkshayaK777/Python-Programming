#create dictionery (name : marks)
students = { "akshaya" :92,
             "preethi": 79,
             "sneha":98,
             "teju":68}
#find topper
topper = max(students,key=students.get)
print("topper:",topper)
#pass and fail students
print("\npassed students:")
for name,marks in students.items():
    if marks >= 40:
        print(name)
        print("\nfailed students:")
