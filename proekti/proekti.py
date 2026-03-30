age = int(input("ასაკი :"))

if age >= 18 and age <=60:
    print("სრულ წლოვანი ხართ, მიღებულია")
elif age < 18:
    print("არასრულწლოვანი ხართ, შეიყვანეთ მშობლის ინფორმაცია")
    name = input("მშობლის სახელი :")
    surname = input("მშობლის გვარი :")
    phone = input("მშობლის ნომერი :")
    facebook = input("მშობლის Facebook ლინკი :")
    email = input("მშობლის Email :")

    print("მშობლის ინფორმაცია :")
    print("სახელი :",name)
    print("გვარი :",surname)
    print("ნომერი :",phone)
    print("Facebook :",facebook)
    print("Email :", email)
    print("მიღებულია")
    
else:
    print("მიუღებელია")
