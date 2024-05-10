# Project 2
from datetime import datetime
import datetime
#import pandas as pd
#from spire.doc import 
#from spire.doc.common import
#pip install Spire.Doc 

class Employee:
    #Constructor
    def __init__(self, name, job_title, department, salary, hire_year):
         self.name = str(name)
         self.job_title = str(job_title)
         self.department = str(department)
         self.salary = float(salary)
         self.hire_year = int(hire_year) 

    #return a string representation         
    def __str__(self):
        return f'{self.name} works as {self.job_title} in {self.department} department from {self.hire_year} year, with monthly salary of ${self.salary}'
        
    #Adding data on an employee (for example, if an employee works in two departments at the same time) 
    def __add__(self,other):
        return Employee(self.name + other.name, self.job.title + other.job_title, self.department + other.department, self.salary + other.salary, self.hire_year + other.hire_year)
       
    #return the total years employee has worked here, based on the hire year
    def years_worked(self):
        today = datetime.datetime.now()
        year = today.year
        return f'{self.name} has been working for {year-self.hire_year} year(s). '
    
    
    #calculate the total salary expense for this employee, which is the salary multiplied by the years worked 
    def total_expenses(self):
        today = datetime.datetime.now()
        year = today.year
        return f'{self.name} earned for the entire period of work at the enterprise ${self.salary*12*(today.year - self.hire_year)  } '
    
    #Write  employee information to a text file.
    def write_employees(self):
        f = open('list_employees.txt', 'w')
        f.write(f'{self.name} works as {self.job_title} in {self.department} department from {self.hire_year} year, with monthly salary of ${self.salary} and {self.total_expenses()}')
        f.close()
        
    #def total_expenses_short(self):
    #    return 12*self.salary * self.years_worked()

    #Changing employee information        
    def set_name(self, other):
        self.name = other
        
    def set_job_title(self, other):
        self.job_title = other
        
    def set_department(self, other):
        self.department = other
        
    def set_salary(self, other):
        self.salary = other
        
    def set_hire_year(self, other):
        self.hire_year = other

    #Receiving any data on an employee    
    def get_name(self):
        return self.name
        
    def get_job_title(self):
        return self.job_title
        
    def get_department(self):
        return self.department
        
    def get_salary(self):
        return self.salary
        
    def get_hire_year(self):
        return self.hire_year
    
    #def Employee_table(self):
    #    return f'{Emp1,Emp2,Emp3,Emp4}'
    
    #with open('Employee.csv', 'w') as file:
    #writer = csv.writer(file)
    #writer.writerows(Employee_table)

    #Emp1.clear()
    #Emp4.append()
    #for name in Employee_table:
    #    if self.name == 'Oleg':
    #        print(Emp1)
        
        
         
         
Emp1 = Employee('Kozachenko', 'CEO', 'Administration', '10000', '2010')
Emp2 = Employee('Bezkrovnyi', 'CFO', 'Accounting', '3500', '2013')
Emp3 = Employee('Zadorognyi', 'CTO', 'Engineering', '2500', '2011')
Emp4 = Employee(input('Enter name ' ), input('Enter position '), input('Enter department ' ), input('Enter salary '), input('Enter hire year '))

#Employee_table = {Emp1(self.name,self.job_title,self.department,self.salary,self.hire_year),Emp2(),Emp3(),Emp4()}
#print(Employee_table)

    

#Employee_table = {Emp1,Emp2,Emp3,Emp4}
#print(Employee_table)

print(Emp1)
print(Emp2)
print(Emp3) 
print(Emp4)
print(Emp1.total_expenses())
print(Emp2.total_expenses()) 
print(Emp3.total_expenses())
#print(Emp3.set_hire_year('2012'))
print(Emp2.get_name())
print(Emp2.set_name('Oleg'))
print(Emp2)
Emp2.set_salary(float(3700))
print(Emp2)
Emp2.set_hire_year(2014)
print(Emp1.years_worked())
#print(Emp2.total_expenses_short())
#print(Employee.__dict__)
#print(Emp1.__str__)
#print(Emp2.__str__)
#print(Emp3.__str__) 

Emp1.write_employees()
Emp2.write_employees()
Emp3.write_employees()
Emp4.write_employees()

#Emp3.__add__(self.name('Grig'))
#print(Emp3)
#print([Emp1.write_employees()] + [Emp2.write_employees()] + [Emp3.write_employees()] + [Emp4.write_employees()])

