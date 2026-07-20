for i in range(5):
    print("Hello World")


for number in range(1,6):
    print(number)


subjects = [
    "Python",
    "AI",
    "C++"
]

for subject in subjects:
    print(subject)

# if we want to print subjects in 3 times
for _ in range(3):
    for subject in subjects:
        print(subject)


count = 1

while count <= 5:
    print(count)
    count += 1

