class Car:
    
    def __init__(self,brand,color,top_speed):
        self.brand = brand 
        self.color = color
        self.top_speed = top_speed
        self.current_speed = top_speed
        
#create a function on behavior/methods
    def acceletrte(self):
            
            self.current_speed+= 20
            print(f"the {self.color} {self.brand} is now moving at {self.current_speed} km/h")
#function calling or {creating a object from the class}

car1 = Car("ferrari","Red",400)
car2 = Car("bmw","black",500)
#using the actions(method)
car1.acceletrte()
car2.acceletrte()