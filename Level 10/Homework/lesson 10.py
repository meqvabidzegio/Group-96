#3) რიცხვები 50-დან 200-მდე (for loop)
for num in range(50, 201):
    print(num)


#4) ყველა ლუწი რიცხვი 1-დან 100-მდე
for num in range(1, 101):
    if num % 2 == 0:
        print(num)


#5) ყველა კენტი რიცხვი 100-დან 150-მდე
for num in range(100, 151):
    if num % 2 != 0:
        print(num)


#6) რიცხვები 1-დან 50-მდე (while loop)
num = 1
while num <= 50:
    print(num)
    num = num + 1


#7) რიცხვები 20-დან 60-მდე 5-ის გამოტოვებით
num = 20
while num <= 60:
    print(num)
    num = num + 5


#8) მომხმარებლის გვარის თითოეული ასო
surname = input("Enter your surname: ")

for letter in surname:
    print(letter)


#9) წვენის გაყიდვის პროგრამა
drinks = 300

while drinks > 0:
    drinks = drinks - 2
    print("You have bought the drink")
    print("Left in stock:", drinks)

print("Out of stock")


#10) 50-დან 20-მდე (3-ით კლებადი)
for num in range(50, 19, -3):
    print(num)


#11) 150-დან 0-მდე (while loop)
num = 150

while num >= 0:
    print(num)
    num = num - 1


    #12) For loop გამოიყენება მაშინ როცა ვიცით რამდენჯერ უნდა შესრულდეს გარკვეული კოდი ის გადის კონკრეტულ რიცხვებზე ან სიმბოლოებზე და ყოველ ჯერზე ასრულებს ციკლში დაწერილ კოდს.


    #13) While loop მუშაობს მანამდე სანამ მოცემული პირობა არის True (მართალი) პირველ რიგში ვქმნით counter ცვლადს შემდეგ ვწერთ while და პირობას. თუ პირობა მართალია კოდი შესრულდება.