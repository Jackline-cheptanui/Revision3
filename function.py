
class Cat:
    def __init__(self,name):
       self.name=name

    def talk(self):
         print("woooof") 
    def printName(self):
        print("my name is:{}". format(self.name)) 
cat =Cat("Charlie")
cat.talk() 
cat.printName() 

# inheristance in python
class Person:
    def __init__(self,name) :
        self.name =name
    def sayName(self):
        print("my name is:{}" .format(self.name))
class Engineer(Person):
    def __init__(self,name):
        super().__init__(name)
        self.profession ="Engineer"

    def sayprofession(self):
        print(self.profession)


class Doctor(Person):
    def __init__(self,name):
        super().__init__(name)
        self.profession ="Doctor"

    def sayprofession(self):
        print(self.profession)

engineer =Engineer("timothy")
engineer.sayName()
engineer.sayprofession()
doctor=Doctor("faith")
doctor.sayName()
doctor.sayprofession()
# muiltible in heri
class M:
    def print(self): 
        print("from M")

class P:
    def print(self): 
        print("from P")
class R(M,P):
    def print(self): 
        print("from R")

object = R()

object.printM()
object.printP()
object.printR()


        





            

        
     


        