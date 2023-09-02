temp = int(input("What is the temperature outside"))

if temp >= 0 and temp <= 30:
    print("The temperatur is good today")
    print("Go Outside")
elif temp < 0 or temp > 30:
    print("The temperatur is bad")


#---------- IF ELSE NOT CONDITION ---------------- ###
if not (temp >= 0 and temp <= 30):
    print('The temperatures isnt good today')
    print('stay inside')
elif not (temp < 0 or temp > 30):
    print("The temperatur is good today")
    print("Go Outside")