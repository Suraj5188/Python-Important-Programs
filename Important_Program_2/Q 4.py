class vehicle:
    
    def __init__(self):
        self.seating_capacity = 100
        self.total_fares=0

class Bus(vehicle):
    def __init__(self):
        super.__init__()

    def calculate_fares(self,passenger_count,full_fare):
        self.total_fares=passenger_count *full_fare

        if isinstance(self,Bus):
            self.total_fares*=1.10

        return self.total_fares
    
obj1=vehicle()
obj2=Bus()

print(obj1)
print(obj2)