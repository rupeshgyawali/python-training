'''Python OOP'''
# class Employee:
#     pass

# emp_1 = Employee()
# emp_2 = Employee()
# print(emp_1)
# print(emp_2)
# print(type(emp_2))

'''Manually creating instance variable'''
# emp_1.name = 'Ram'
# print(emp_1.name)

'''Init Method'''
# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = f'{self.first}.{self.last}@company.com'
#
#     def fullname(self):
#         return self.first + ' ' + self.last

# emp_1 = Employee('Ram', 'Chandra', 100)
# emp_2 = Employee('Hari', 'Shresth', 200)
# print(emp_1.email, emp_2.email)
# # object is passed authomatically as first argument
# print(emp_2.fullname(), Employee.fullname(emp_2))

'''Class variable'''
# class Employee:
#     raise_amount = 1.04
#     num_of_emps = 0

#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         Employee.num_of_emps += 1

#     def fullname(self):
#         return self.first + ' ' + self.last

#     def apply_raise(self):
#         self.pay = int(self.pay*self.raise_amount)  # or Employee.raise_amount

# emp_1 = Employee('Ram', 'Chandra', 100)
# emp_2 = Employee('Hari', 'Shresth', 200)
# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
# print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)
# Employee.raise_amount = 1.05
# print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)
# emp_1.raise_amount = 1.05
# print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)
# # print(emp_1.__dict__, Employee.__dict__)
# print(Employee.num_of_emps)

# # '''Class Method'''
# # class Employee:
# #     raise_amount = 1.04
# #     num_of_emps = 0
# #     def __init__(self, first, last, pay):
# #         self.first = first
# #         self.last = last
# #         self.pay = pay
# #         self.email = first + '.' + last + '@company.com'
# #         Employee.num_of_emps += 1
# #     def fullname(self):
# #         return self.first + ' ' + self.last
# #     def apply_raise(self):
# #         self.pay = int(self.pay*self.raise_amount)  # or Employee.raise_amount
# #     @classmethod
# #     def set_raise_amount(cls, amount):
# #         cls.raise_amount = amount
# #     # class method as a alternate constructor
# #     @classmethod
# #     def from_string(cls, emp_str):
# #         first, last, pay = emp_str.split('-')
# #         return cls(first, last, pay)
#
# # emp_1 = Employee('Ram', 'Chandra', 100)
# # emp_2 = Employee('Hari', 'Shresth', 200)
# # Employee.set_raise_amount(1.05)
# # print(Employee.raise_amount, emp_1.raise_amount, emp_2.raise_amount)
# # emp_str_1 = 'Ram-Chandra-100'
# # new_emp_1 = Employee.from_string(emp_str_1)
# # print(new_emp_1.pay)

# # '''Static Methods'''

'''Inheritance'''
# class Employee:
#     raise_amount = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#     def fullname(self):
#         return self.first + ' ' + self.last
#     def apply_raise(self):
#         self.pay = int(self.pay*self.raise_amount)
# class Developer(Employee):
#     pass

# dev_1 = Developer('Ram', 'Sharma', 1000)
# dev_2 = Developer('Shyam', 'Sharma', 2000)
# print(dev_1.email, dev_2.email, dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)

# class Developer(Employee):
#     raise_amount = 1.10

# emp_1 = Employee('Ram', 'Sharma', 1000)
# dev_1 = Developer('Shyam', 'Sharma', 2000)
# print(emp_1.raise_amount, dev_1.raise_amount)

# class Developer(Employee):
#     raise_amount = 1.10
#     def __init__(self, first, last, pay, prog_lang):
#         super().__init__(first, last, pay)  # Employee.__init__(self, first, last, pay)
#         self.prog_lang = prog_lang

# dev_1 = Developer('Ram', 'Sharma', 1000, 'Python')
# dev_2 = Developer('Shyam', 'Sharma', 2000, 'C')
# print(dev_1.email, dev_1.prog_lang)

# class Manager(Employee):
#     def __init__(self, first, last, pay, employees=None):
#         super().__init__(first, last, pay)
#         if employees is None:
#             self.employees = []
#         else:
#             self.employees = employees
#     def add_emp(self, emp):
#         if emp not in self.employee:
#             self.employees.append(emp)
#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)
#     def print_emps(self):
#         for emp in self.employees:
#             print('-->', emp.fullname())

# mgr_1 = Manager('Ram', 'Shrestha', 9000, [dev_1])
# print(mgr_1.email)
# mgr_1.print_emps()
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()

# # Buildin functions
# print(isinstance(mgr_1, Manager))
# print(isinstance(mgr_1, Employee))
# print(isinstance(mgr_1, Developer))

# print(issubclass(Developer, Employee))
# print(issubclass(Manager, Employee))
# print(issubclass(Manager, Developer))

'''Special(Magic/Dunder) Methods'''
# print(emp_1)

# class Employee:
#     # ....
#     def __repr__(self):
#         return f'Employee({self.first}, {self.last}, {self.pay})'
#     def __str__(self):
#         return f'{self.fullname()}-{self.email}'

# print(emp_1, str(emp_1), repr(emp_1), emp_1.__str__(), emp_1.__repr__())

# print(1+2, 'a'+'b', int.__add__(1, 2), str.__add__('a', 'b'))
# def __add__(self, other):
#     return self.pay + other.pay

# print(emp_1+emp_2)

# __sub__, __mul__, __mod__, ....
# print(len('hello'), 'hello'.__len__())
# def __len__(self):
#     return len(self.fullname())

# print(len(emp_1))

'''Property Decorators-Getters, Setters and Deleters'''
# class Employee:
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#     @property
#     def email(self):
#         return f'{self.first}.{self.last}@company.com'
#     @email.setter
#     def email(self, email):
#         self.first, self.last = email[:email.find('@')].split('.')
#     @email.deleter
#     def email(self):
#         print('**Delete Email!!**')
#         self.first = None
#         self.last = None
#     def fullname(self):
#         return self.first + ' ' + self.last

# emp_1 = Employee('Ram', 'Chandra', 100)
# emp_2 = Employee('Hari', 'Shresth', 200)
# print(emp_1.email, emp_2.email)
# emp_1.email = 'Ramesh.Chandra@gmail.com'
# print(emp_1.first, emp_1.last)
# del emp_1.email
# print(emp_1.first, emp_1.last)
