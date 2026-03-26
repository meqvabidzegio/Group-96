# 3) ლუწი თუ კენტი
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# 4) ტემპერატურა
temp = int(input("Enter temperature: "))
if temp > 30:
    print("It's Hot")
elif 15 <= temp <= 30:
    print("It's Warm")
else:
    print("It's Cold")

# 5) დადებითი/უარყოფითი
num2 = int(input("Enter a number: "))
if num2 > 0:
    if num2 % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Negative")

# 6) Even / Odd 0-დან N-მდე
n = int(input("Enter a number: "))
for i in range(n + 1):
    if i % 2 == 0:
        print(i, "Even")
    else:
        print(i, "Odd")

# 7) 10 რიცხვი
positive = 0
negative = 0
zero = 0

for i in range(10):
    x = int(input("Enter number: "))
    if x > 0:
        positive += 1
    elif x < 0:
        negative += 1
    else:
        zero += 1

print("Positive:", positive)
print("Negative:", negative)
print("Zero:", zero)

# 8) fruits
fruits = ["apple", "banana", "orange", "grape"]
fruits[1] = "kiwi"
print(fruits)

# 9) nums
nums = [4, 8, 12, 16, 20]
print(nums[0] + nums[-1])

# 10) სიის თითოეული წევრი
my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)

# 11) მხოლოდ ლუწი რიცხვები
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    if num % 2 == 0:
        print(num)

# 12) ლუწების ჯამი
sum_even = 0
for num in numbers:
    if num % 2 == 0:
        sum_even += num
print("Sum of evens:", sum_even)

# 13) > 6 რიცხვები
for num in numbers:
    if num > 6:
        print(num)

# 14) სიტყვის ასოები
word = "Python"
for letter in word:
    print(letter)

# 15) პირველი 3 წევრი
my_list2 = [10, 20, 30, 40, 50]
print(my_list2[:3])