class car:
    def __init__(self,windows,doors,enginetype):
        self.windows = windows
        self.doors = doors
        self.enginetype = enginetype
    def drive(self):
        print(f"The person will drive the {self.enginetype} car")
obj = car(5,2,"electric")
obj.drive()
### Single inheritence
class tesla(car):
    def __init__(self,windows,doors,enginetype,is_selfdriving):
        super().__init__(windows,doors,enginetype)
        self.is_selfdriving = is_selfdriving
    def dive(self):
        print(f"Tesla supports self driving : {self.is_selfdriving}")
obj = tesla(4,5,"petrol",True)
obj.dive()

##Multiple Inheritence
class Animal:
    def __init__(self,name):
        self.name = name
    def speak(self):
        print("Subclass must implement this method")

class Pet:
    def __init__(self,owner):
        self.owner = owner
            
class dog(Animal,Pet):
    def __init__(self,name,owner):
        Animal.__init__(self,name)
        Pet.__init__(self,owner)
    def speak(self):
        print(f"{self.name} say woof")
        
obj = dog("Kitty","Dhana")
obj.speak()
       
           