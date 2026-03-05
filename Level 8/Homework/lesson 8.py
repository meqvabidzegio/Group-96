#პითონში გვაქვს 6 შედარების ოპერატორები: ==, !=, >, <, <=, >=.
#მაგალითები: 5<10, 10>5.
#name = "Gio"
#print(name != "Nika")
#print(name == "Gio")
#num1 = 5
#print(num1 >= 10)
#print(num1 <= 15)
#3)
#ჩვენ ვიცით 2 ლოგიკური ოპერატორები or და and.
#and ოპერატორს გამოაქვს True როდესაც ორივე True არის.
#or ოპერატორს გამოაქვს True როცა ერთრთი მაინც არის True.
#4)
user_height = int(input("Enter your height in cm: " ))
my_height = 175
print(user_height > my_height)
#5)
#num1 = "21"
#num2 = 21
#print(num1 == num2) ეს კოდი False-ს გამოიტანს იმიტომ რომ integer ტიპის 21 არ უდრის string ტიპის 21-ს
#6)
my_surname = "Meqvabidze"
user_surname = str(input("Enter your surname: " ))
print(my_surname == user_surname)
#7)
print(False or True and True and False) #გამოიტანს False-ს
print(True and False or False or True) #გამოიტანს True-ს
print(True or True and False or True or False and True or False) #გამოიტანს True-ს
#8)
temperature = int(input("Enter temperature: " ))
print(temperature > 30)
#9)
celsius = float(input("Enter your home temperature: " ))
fahrenhet = celsius * 9/5 + 32
print(fahrenhet > 89.6)
