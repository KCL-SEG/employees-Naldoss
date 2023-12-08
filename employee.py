"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, salary, hours=1, commission = False, money =0, numOfCom =1):
        self.name = name
        self.contract = contract
        self.salary = salary
        self.hours = hours
        self.commission = commission
        self.money = money
        self.numOfCom = numOfCom


    def get_pay(self):
        if self.contract == "monthly":
            if self.commission :
                return self.salary + ( self.money * self.numOfCom)
            else:
                return self.salary
        if self.contract == "hourly":
            if self.commission :
                return (self.salary * self.hours) + (self.money * self.numOfCom)
            else:
                return self.salary * self.hours
        

    def __str__(self):
        if self.contract == "monthly":
            if self.commission :
                if self.numOfCom > 1:
                    return f"{self.name} works on a monthly salary of {self.salary} and receives a commission for {self.numOfCom} contract(s) at {self.money}/contract. \nTheir total pay is {self.get_pay()}."
                else:
                    return f"{self.name} works on a monthly salary of {self.salary} and receives a bonus commission of {self.money}. \nTheir total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a monthly salary of {self.salary}. \nTheir total pay is {self.get_pay()}."
        if self.contract == "hourly":
            if self.commission :
                if self.numOfCom > 1:
                    return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a commission for {self.numOfCom} contract(s) at {self.money}/contract. \nTheir total pay is {self.get_pay()}."
                else:
                    return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour and receives a bonus commission of {self.money}. \nTheir total pay is {self.get_pay()}."
            else:
                return f"{self.name} works on a contract of {self.hours} hours at {self.salary}/hour. \nTheir total pay is {self.get_pay()}."



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 'monthly', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 'hourly', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee','monthly', 3000, 1, True, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 'hourly', 25, 150, True, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 'monthly', 2000 , 1, True, 1500, 1)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 'hourly', 30, 120, True, 600, 1)
