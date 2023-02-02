class A:
    No_of_role = 10

class B(A):
    No_of_code = 20

class C(B):
    def __init__(self,name,sets):
        self.name = name
        self.sets = sets
    def details(self):
        return f"The name is: {self.name} and the sets is: {self.sets}"

Emp = C("carry", 5)
Emp.name = "carry"
Emp.sets = 5
print(Emp.No_of_code)       