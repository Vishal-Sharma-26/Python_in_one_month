class add:
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    def printdetails(self):
        return f"Your name is {self.name} and the roll number is {self.roll_no}."

vishal = add("vishal", 23)
vishal.name = "vishal"
vishal.roll_no = 23
print(vishal.printdetails())            