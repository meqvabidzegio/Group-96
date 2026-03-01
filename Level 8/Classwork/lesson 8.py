print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(True and False or False or True and True and False or True) #True გამოვა.

family = 4
motion_detected = True
alarm_on = True
thief_detected = family >= 4 and motion_detected and alarm_on
print(thief_detected)