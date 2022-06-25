class user():

    def __init__(self, name, age, salary, debts):
        
        self.name = name
        self.age = age #hey
        self.salary = salary #youh
        self.debts = debts

    # def user_data(name):    

    def verify(self):

        if self.age > 30 and self.salary > 2 and self.debts < (self.salary*0.3):

            print("Hi " + self.name + " we have verified your data and we are glad to say that you are elegible for a credit")

        else: print("Hi " + self.name + " we are sorry to say you can't get a credit here :(") 


name = input("Type your name here ---> ")
age = int(input("How old are you ---> "))
salary = int(input("How much do you earn per month ---> "))
debts = int(input("What's your debt ---> "))

person = user(name, age, salary, debts)

person.verify()

