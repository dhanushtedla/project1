# 1. Variables and printing
name = "Dhanush"
age = 25
print("Hello,", name)
print("Age next year:", age + 1)

# 2. User input
city = input("Which city do you live in? ")
print(f"{city} is a nice place!")

# 3. Condition
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# 4. Loop
for i in range(1, 6):
    print("Count:", i)

# 5. List
fruits = ["apple", "banana", "mango"]
fruits.append("orange")
for fruit in fruits:
    print(fruit)

# 6. Function
def add(a, b):
    return a + b

print("5 + 3 =", add(5, 3))