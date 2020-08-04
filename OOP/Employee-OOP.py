# ###### Employee OOP ######

# =================================
class Employee:
    
    raise_amount = 2.3
    no_of_emp = 0
    day = ["Sat", "Sun"]
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        
        Employee.no_of_emp += 1
        
    @property    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)   
    
    def apply_rasie(self):
        self.pay = int(self.pay * Employee.raise_amount)
        
    @property
    def email(self):
        return "{}{}.@gmail.com".format(self.first, self.last)
        
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
        
    @fullname.deleter
    def fullname(self):
        print('Delete Name!')
        self.first = None
        self.last = None 
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
    
    @staticmethod
    def holidays_in_week(day):
        day = day
        return "{} is/are holidays".format(day)
        
    def __repr__(self):
        return "Employee({} {} - {})".format(self.first, self.last, self.pay)
        
    def __str__(self):
        return '{} - {}'.format(self.fullname, self.email)
        
    def __add__(self, other):
        return self.pay + other.pay
        
    def __len__(self):
        return len(self.fullname)

emp_1 = Employee("Brock", "Lesnar", 1000000)
emp_2 = Employee("John", "Cena", 9000000)

class Developer(Employee):
    raise_amount = 19999
    
    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

dev_1 = Developer("CM", "Punk", 199870, "Python")
dev_2 = Developer("Randy", "Ortan", 94211, "JavaScript")

class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            employees = []
        else:
            self.employees = employees
            
        def add_emp(self, emp):
            if emp in self.employees:
                self.employees.append(emp)
                
        def remove_emp(self, emp):
            if emp in self.employees:
                self.employees.remove(emp)
                
        def print_emp(self):
            print("--> {}".format(self.fullname()))
            
            
mgr_1 = Manager('Paul', 'Heyman', 90000, [dev_1])
