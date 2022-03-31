import re
def valid_email(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False
#########################################################################################################
class Person:

    def __init__(self,name, money, mood, healthRate=1):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
            print(self.mood)
        elif hours<7:
            self.mood = "tired"
            print(self.mood)
        elif hours>7:
            self.mood = "lazy"
            print(self.mood)
        else:
            print("unkown hours")

    def eat(self, meals):
        if meals == 3:
            self.healthRate = "100%"
        elif meals == 2:
            self.healthRate = "75%"
        elif meals == 1:
            self.healthRate = "50%"
        else:
            print("Please enter values between 1 and 3")

    def buy(self, items):
        if items != 0:
            self.money = self.money - 10

##########################################################################################################
class Employee(Person):

    __mood = ["happy", "tired", "lazy"]
    empMood = ""

    def __init__(self, id, car, email, salary, distanceToWork, name, money, healthRate):
        self.id = id
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
        super().__init__(name, money, healthRate)
        is_valid = valid_email(self.email)
        if is_valid!=True:
            print("Please Enter a valid mail")
        if self.salary<1000:
            print("salary must be 1000 LE or more")
        if self.healthRate<0 and self.healthRate>100:
            print("Health Rate value must be between 0 and 100")


    def work(self, hours):
        if hours == 8:
            print(self.__mood[0])
        elif hours > 8:
            print(self.__mood[2])
        elif hours < 8:
            print(self.__mood[1])
        else:
            print("wrong hour format")

    def drive(self):
        distance = self.distanceToWork
        self.car.run(distance)

    def refuel(self, gas_amount=100):
        self.car.fuel_rate = self.car.fuel_rate + gas_amount

    def sendEmail(self):
        pass

##########################################################################################################
class Office:
    def __init__(self,officeName, employees):
        self.officeName = officeName
        self.employees = employees

    def get_all_employees(self):
        pass

    def get_employee(self):
        pass

    def hire(self):
        pass

    def fire(self):
        pass

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass

##########################################################################################################
class Car:
    def __init__(self,name, fuelRate, velocity):
        self.cName = name
        self.fuelRate = fuelRate
        self.velocity = velocity
        if self.velocity<0 and self.velocity>200:
            print("Please enter velocity between 0 and 200")
        if self.fuel_rate<0 and self.fuel_rate>100:
            print("Please enter fuel rate between 0 and 100")

    def run(self, distance):
        remianing_fuel = self.fuel_rate - distance
        if remianing_fuel <= 0:
            print(f"remaining distance is ", {remianing_fuel})
            self.stop()
        else:
            self.stop()
            print("you arrived")

    def stop(self):
        self.velocity=0
        print("you arrived")
