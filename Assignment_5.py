#Questuion 1: Square Numbers and Return Their Sum


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        print(x,y,z)
    def sqSum(self):
        return self.x**2+ self.y**2 + self.z**2
    
p = Point(2, 4, 5)
result = p.sqSum()
print(result)


#Question 2: Implement a Calculator Class



class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    def add(self):
        return self.num1 + self.num2
    def subtract(self):
        return self.num2 - self.num1
    def multiply(self):
        return self.num1 * self.num2
    def divide(self):
        return self.num2 / self.num1
pass
    
obj = Calculator(2, 4)
print(obj.add())       
print(obj.subtract())  
print(obj.multiply())  
print(obj.divide())  





#3. Implement the Complete Student Class

class Student:
    def __init__(self):
        self.name = None
        self.rollNumber = None
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setRollNumber(self, rollNumber):
        self.rollNumber = rollNumber
    def getRollNumber(self):
        return self.rollNumber


student = Student()
student.setName("Priyanka")
student.setRollNumber(79)
name = student.getName()
rollnumber = student.getRollNumber()
print("Name:", name)
print("Roll Number:", rollnumber)





#4: Implement a Banking Account

class Account:
    def __init__(self, account_holder_name, balance):
        self.account_holder = account_holder_name
        self.balance = balance

class SavingsAccount(Account):
    def __init__(self, account_holder_name, balance, interestRate):
        super().__init__(account_holder_name, balance)
        self.interestRate = interestRate

account1 = SavingsAccount("Priyanka Bhosle", 8000000, 5)
print("Account Holder     : ", account1.account_holder)  
print("Account Balance    : ", account1.balance)  
print("Interest Rate(%)   : ", account1.interestRate)  





# 5: Handling a Bank Account

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    def withdrawal(self, amount):
        self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def getBalance(self):
        return self.balance
    
class SavingsAccount(Account):
    def __init__(self, title, balance, interestRate):
        super().__init__(title, balance)
        self.interestRate = interestRate
    def interestAmount(self):
        return (self.balance * self.interestRate)/100

demo1 = SavingsAccount("Priyanka", 3000, 5)
demo1.deposit(200)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Priyanka", 2000, 5)
demo1.withdrawal(1000)
print(demo1.getBalance()) 

demo1 = SavingsAccount("Priyanka", 2000, 5)
print(demo1.interestAmount()) 

