#type() ფუნქცია ამოწმებს თუ რა სახის მონაცემი გვაქს მოცემული.
print(type("gio"))
print(type(5.0))
print(type(555))
print(type(True))
print(type(False))

name = "Gio"
surname = "Meqvabidze"
age = 17

print("I am " + name + " " + surname + " and I am " + str(age) + " years old")

num1 = float(input("First number: "))
num2 = float(input("Second number: "))

addition = num1 + num2
substraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print(addition)
print(substraction)
print(multiplication)
print(division)

number1 = float(input("Enter number 1: "))
number2 = float(input("Enter number 2: "))
number3 = float(input("Enter number 3: "))
number4 = float(input("Enter number 4: "))
number5 = float(input("Enter number 5: "))

average = (number1 + number2 + number3 + number4 + number5) / 5
print(average)

celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("Temperature in fahrenheit")

