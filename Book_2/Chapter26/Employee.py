class Employee:
    def computeSalary(self): print('compute salary')
    def giveRaise(self): print('give raise')
    def promote(self): print('promote')
    def retire(self): print('retire')

class Engineer(Employee):
    def computeSalary(self):
        print('compute salary engineer')
bob = Employee()
sue = Employee()
tom = Engineer()
bob.computeSalary()
sue.computeSalary()
tom.computeSalary()

