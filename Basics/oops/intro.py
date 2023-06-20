class Sample:
    def display(self):
        print("This is sample class")
        
    def sum(self,a ,b):
        pass
        
        
# obj=Sample()
# obj.display()
# obj2=Sample()
# obj2.display()
# print(type(obj2))
# print(id(obj))
# print(id(obj2))
# print(dir(obj))

class Student:
    def __init__(self, name, roll_no):
        self.name=name
        self.roll_no= roll_no
        print(f"name of the student is {self.name} and roll no, is {self.roll_no}")
        
    def display_details(self):
        print("This is display method")
        
        
std=Student("vivek", 1)
# std.display_details()