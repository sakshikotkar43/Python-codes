class Employee:
    language = "python" # this is  a class attribute
    salary = 12000

harry = Employee()
harry.language = "javascript" # this is an instance attribute
print(harry.language, harry.salary)
