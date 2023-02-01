# Write a program for you can drive or not!

def find_your_age(age):
    if age > 18:
        print("You can drive")
    elif age == 18:
        print("We will think!")
    else:
        print("You can't drive")

age = int(input("Enter your age\n"))
find_your_age(age)

