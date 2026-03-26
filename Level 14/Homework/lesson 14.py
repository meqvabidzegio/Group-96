# 3)
phrase = "Python Programming"
print(phrase[:6])        # Python
print(phrase[7:])        # Programming
print(phrase[::3])       # ყოველი მესამე სიმბოლო

# 4)
text = "PythonSlicing"
print(text[:6])          # პირველი 6 სიმბოლო
print(text[::-1])        # უკუღმა
print(text[::2])         # ყოველი მეორე სიმბოლო

# 5)
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print(letters[::2])      # ლუწ ინდექსები
print(letters[2:8:2])    # ინდექსი 2-დან 7-მდე ყოველ მეორე ნაბიჯზე
print(letters[:5][::-1]) # პირველი 5 ელემენტი უკუღმა

# 6)
sentence = "Slicing makes Python powerful"
print(sentence[14:20])     # Python
print(sentence[21:][::-1]) # powerful უკუღმა
print(sentence[::3])       # ყოველი მესამე სიმბოლო