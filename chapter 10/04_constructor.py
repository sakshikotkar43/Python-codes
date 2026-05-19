class Employee:
    language = "python" # this is  a class attribute
    salary = 12000


    def _init_(self, name, salary, language): #dunder method which is automatically called
        self.name = name
        self.salary = salary
        self.language = language
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    
    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee("Harry", 13300, "Javascript")
#harry.name = "Harry"
#harry.language = "javascript" # this is an instance attribute
harry.getInfo()
# Employee.getInfo(harry)
print(harry.name, harry.salary, harry.language)