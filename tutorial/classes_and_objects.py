class Car:
    def __init__(self, brand, name, fuel_type, owner):
        self.brand = brand
        self.name = name
        self.fuel_type = fuel_type
        self.owner = owner

class Owner:
    def __init__(self, Oname, contact, address):
        self.Oname = Oname
        self.contact = contact
        self.address = address

o1 = Owner('Yash', '123', 'patna')
c1 = Car('Toyota', 'Supraa GT', 'Petrol',o1)
print(c1.brand)
print(c1.fuel_type)
print(c1.owner.Oname)

