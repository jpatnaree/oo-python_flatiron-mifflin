from employee import Employee
from statistics import mean

class Manager:
    
    all = []

    def __init__(self, name, department,age):
        self.name = name
        self.department = department
        self.age = age
        Manager.all.append(self)

    @property
    def name(self):
         return self._name
    
    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise Exception('name must be a string')
    
    @property
    def department(self):
         return self._department
    
    @department.setter
    def department(self, new_department):
        if isinstance(new_department, str):
            self._department = new_department
        else:
            raise Exception('name must be a string')
        
    @property
    def age(self):
         return self._age
    
    @age.setter
    def age(self, new_age):
        if isinstance(new_age, int):
            self._age = new_age
        else:
            raise Exception('age must be an integer')

    def employess(self):
        return [e for e in Employee.all if e.manager == self]
    
    def hire_employee(self,employees_name, salary):
            if isinstance(employees_name, Employee.all.name) and isinstance(salary, int):
                Employee(self, employees_name)
            else:
                raise Exception('Cannot hire this employee, invalid employee or salary')
            
    @classmethod
    def all_departments(cls):
        return [m.department for m in Manager.all]
    
    @classmethod
    def average_age(cls):
        return round(mean([m.age for m in Manager.all]),2)


            
            

