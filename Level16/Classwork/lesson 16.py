word = input("შეიყვანე სიტყვა :")
letter = input("შეიყვანე ერთი ასო :")
index = word.find(letter)

if index!= -1:

 print("ასოს მდებარეობა:", index)
else:
  print("ეს ასო სიტყვაში არ არის")

  #3

fruits = ["apple", "banana","peach","pinapple",]

fruits.append("orange")
fruits.append("mango")
fruits.append("kiwi")
print("სიის სოგრძეა : ",len(fruits))
