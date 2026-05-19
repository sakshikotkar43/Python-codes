class Employee:
    language = "python" # this is  a class attribute
    salary = 12000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

harry = Employee()
harry.language = "javascript" # this is an instance attribute
harry.getInfo()
# Employee.getInfo(harry)