class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        return f"Employee ID: {self.id}, Name: {self.name}"
    
class Manager(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
        self.employees = []

    def display(self):
        print(f"Manager - {super().display()}, Salary: {self.salary}, Employees:")
        for e in self.employees:
            print(e.display())

    def add_employee(self, employee):
        self.employees.append(employee)

class Engineer(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id)
        self.salary = salary
        self.engineer = "I am an engineer\n"

e1 = Employee("Emp1", 1)
e2 = Employee("Emp2", 2) 
m1 = Manager("M1", 1, 500)
m1.add_employee(e1)
m1.add_employee(e2)
m1.display()
