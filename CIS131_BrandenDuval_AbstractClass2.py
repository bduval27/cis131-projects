'''
script: Software Engineering with Abstract Classes and Abstract Methods
action: TBD
author: Branden Duval
date: 03/24/2025
'''

# importing the necessary module
from abc import ABC, abstractmethod

# the abstract class
class Employee(ABC):
    def __init__(self, firstName = 'Null', lastName = 'Null', ssn = 0):
        self._firstName = firstName # private variable for first name
        self._lastName = lastName   # private variable for last name
        self._ssn = ssn             # private variable for social security number

    @abstractmethod # setting earnings to an abstract method
    def earnings(self):
        '''I have no idea what this is supposed to do in the program, but the instructions said to include it although it did not give any instruction on how to utilize it.'''
        raise NotImplementedError
        
    def __repr__(self): # this class' string representation that will be getting called in the other classes
        return(f'Employee: {self._firstName} {self._lastName}\nSocial Security Number: {self._ssn}')

# concrete subclass    
class SalariedEmployee(Employee):
    def __init__(self, weekly_salary = 0, firstName = 'Null', lastName = 'Null', ssn = 0):
        super().__init__(firstName, lastName, ssn) # calls the 'Employee' superclass' initialization
        self._weekly_salary = weekly_salary

    def earnings(self):
        return self._weekly_salary * 52 # takes the weekly salary and multiplies it by all the weeks within a year because I'm not too sure what else to do with this

    @property # weekly salary getter
    def weekly_salary(self):
            return self._weekly_salary
        
    @weekly_salary.setter # weekly salary setter
    def weekly_salary(self, weekly_salary):
        if weekly_salary < 0: # weekly salary has to be non-negative
            print('Salary cannot be negative.')
        elif type(weekly_salary) is not int: # weekly salary must be an integer
            raise TypeError('Salary must be in the form of an integer.')
            
        self._weekly_salary = weekly_salary
    
    def __repr__(self): # SalariedEmployee sublcass' string representation
        employee = super().__repr__() # stores the string representation from the superclass to be used in this subclass' representation
        return(f'SalariedEmployee: {self._weekly_salary}\n{employee}')

# concrete subclass    
class HourlyEmployee(Employee):
    def __init__(self, hours = 0, wages = 0, firstName = 'Null', lastName = 'Null', ssn = 0):
        super().__init__(firstName, lastName, ssn) # calls 'Employee' superclass' intialization
        self._hours = hours
        self._wages = wages

    def earnings(self):
        return self._wages * self._hours # multiplies the wages and the hours together 

    @property # hours getter
    def hours(self):
        return self._hours
    
    @hours.setter # hours setter
    def hours(self, hours):
        if hours > 168: # the max number of hours to be worked are 168
            print('Hours worked cannot be greater than 168.')
        elif hours < 0: # the minimum number of hours to be worked are 0
            print('Hours worked cannot be negative.')

        self._hours = hours

    @property # wages getter
    def wages(self):
        return self._wages

    @wages.setter # wages setter
    def wages(self, wages):
        if wages < 0: # employee can not have negative wage
            print('Wages entered cannot be negative.')
        elif wages / self._hours < 0: # employee can not have a negative wage per hour 
            print('Wages per hour cannot be negative.')

        self._wages = wages

    def __repr__(self): # string representation for the HourlyEmployee concrete subclass
        employee = super().__repr__() # stores the superclass' string representation to be used in this subclass' representation
        return(f'HourlyEmployee: {self._wages / self._hours:.2f}\n{employee}')
    
# '''debug nonesense'''
# employee1 = Employee('Barry', 'Bertie', 888904253)
employee2 = SalariedEmployee(50000)
employee3 = HourlyEmployee(120, 50000)
# # # print(employee)
# print(employee2)
# print(employee3)

employee_list = [employee2, employee3]
for employee in employee_list:
    print(employee)

try:
    employee1 = Employee('Barry', 'Bertie', 888904253)
except TypeError:
    print('A TypeError has occured.')