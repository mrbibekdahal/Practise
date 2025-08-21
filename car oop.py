class Car:
    def __init__(self,brand,year):
        self.brand = brand
        self.year = year
    
    def drive(self):
        print(f"{self.brand} is driving")
        
    
carharu = Car("Toyota",2025)
carharu.drive()