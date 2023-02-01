lst = [26,20,13,11,1,3,15,20,26,4]
lst1 = set()
while(True):
    selected_number = int(input("Enter your number...\n"))
    if selected_number in lst:
        print("You choose a right number. Your selected number in a list")
        print(lst)
        break
    else:
        print("You entered a wrong number. Please try again!")
        lst1.add(selected_number)
        print(lst1)
        continue
