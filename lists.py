# list = is used to store multiple items in single variables
food = ["Pizza","Burgers","Hot dogs","Spaghetti"]


food.append("Ice Cream")
# food.remove("Hot dogs")
# food.pop()
# food.insert(0,"cake")
# food.sort()

print(food[0])
print(food)

for x in food:
    print(x)

#TUPLES
student = ("Bro",21,"male")
print(student.count("Bro"))
print(student.index("male"))

for x in student:
    print(x)
if "Bro" in student:
    print("Bro is here")