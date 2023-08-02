"""
Method Overriding

Two - Parent And Child Class Both Have Same Name Methods With Same No. Of Arguments


"""

class Vehicle:
    def speed(self):
        print("Max Speed Limit : 80Kmh")
        
class Car(Vehicle):
    def speed(self):
        print("Max Speed Limit : 120kmh")
        return super().speed
    
obj = Car()
obj.speed()            