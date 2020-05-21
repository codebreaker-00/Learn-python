'''
class person:
    def __init__(personal,gender,age):  
        personal.gender = gender
        personal.age = age
'''        

class car:
    def __init__(self,company,model,year) :
        self.company = company
        self.model = model
        self.year = year

    def info_of_car(self) :
        print(f"{self.year} {self.company} {self.model}")

new_car = car('audi','a4',2019)
new_car.info_of_car()

# Now suppose we need to make a child of the class say-- for car we have Sports_car
#Parent must be there in the same file 
class Sports_car(car): #Note the Parenthesis must include parent
    def __init__(self,company,model,year) :
        super().__init__(company,model,year) 
        #super() is a special function to check the __init__() of parent super-class for child sub-class

My_sports_car = Sports_car('Jaguar','A46',2020)
My_sports_car.info_of_car()

# NOw the Question Arrises that can we have some extra facilities in the child which is not present in the parent
# The answer is Yes of course!!! Check the following part for it

class electric_car(car):
    def __init__(self,company,model,year) :
        super().__init__(company,model,year) 
        self.battery_size = 100

    def battery_query(self):
        print(f"The battery is of size : {self.battery_size}")

new_electric_car = electric_car('tesla','Elkra',2023)
new_electric_car.battery_query()

$ python3 -m pip install --user pygame