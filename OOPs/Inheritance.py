class Employee:
    def __init__(self, name, course):
        self.name = name
        self.course = course

class student(Employee):
    def __init__(self, id, roll_no):
        Employee.__init__(self, name, course)
        self.id = id
        self.roll_no = roll_no
    def alldetails(self):
        return f"The name is {self.name}, Id no is {self.id}, roll number is {self.roll_no} and the course is {self.course}" 

vishal = student("vishal", 101, 2620, "B.tech")
vishal.name = "vishal"
vishal.id = 101
vishal.roll_no = 2620
vishal.course = "B.tech"
print(vishal.alldetails())           