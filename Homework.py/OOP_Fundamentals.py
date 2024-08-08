class Vehicle():
    def __init__(self, reg_num, model, owner):
        self.reg_num = reg_num
        self.model = model
        self.owner = owner
   
    def update_owner(self, new_owner):
        self.owner = new_owner

    def vehicle_info(self):
        return (f'Registration Number: {self.reg_num}\n'
                f'Model: {self.model}\n'
                f'Owner: {self.owner}') 

Car = Vehicle('1111321321331', 'Tesla', 'Gamel')
Car2 = Vehicle('TBITB2132' , 'Jeep' , 'Travis')

print("Vehicle information")
print(Car.vehicle_info())
print(Car2.vehicle_info())

Car.update_owner('Homelander')
Car2.update_owner('Hughie')

print("\nUpdated vehicle information")
print(Car.vehicle_info())
print(Car2.vehicle_info())