class Employee:
    language = "py" #this is a  class attribute
    salary = 120000

harry = Employee()
harry.name = "Harry" # this is an intance attribute
print(harry.name,harry.language, harry.salary)

rohan = Employee()
rohan.name = "Rohan Roro"
print(rohan.name,rohan.salary, rohan.language)
#here name is intance attribute and salary and language are class atttributes as they directly belong to the class