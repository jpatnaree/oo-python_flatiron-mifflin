

class Employee:
    
    all = []

    def __init__(self,name ,salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        Employee.all.append(self)
    
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
    def salary(self):
         return self._salary
    
    @salary.setter
    def salary(self, new_salary):
        if isinstance(new_salary, float):
            self._salary = new_salary
        else:
            raise Exception('salary must be a float number')
    
    def manager_name(self):
        for e in Employee.all:
            return e.manager.name

    @classmethod
    def paid_over(self, salary):
        return [e for e in Employee.all if e.salary > salary]
    
    @classmethod
    def find_by_department(self, department):
        for e in Employee.all: 
            if e.manager.department == department:
                return e[0]

    def tax_bracket(self):
        return [e for e in Employee.all if e.name != self and ((self.salary - 1000) <= e.salary <= (self.salary + 1000))] 
    
