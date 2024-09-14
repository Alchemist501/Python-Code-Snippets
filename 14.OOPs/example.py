class RoyalEnfield:
    vehicle = "Bike"
    company = "Royal Enfield"

    def __init__(self):
        pass

    def __init__(self, fullname):
        self.name = fullname
        print(self)
        print("New one is adding.......")

    @staticmethod
    def welcome():
        print("Welcome!!!")


Himalayan = RoyalEnfield("Himalayan")
print(Himalayan)
print(Himalayan.name)
print(Himalayan.vehicle)
print(Himalayan.company)
Himalayan.welcome()

ContinentalGT = RoyalEnfield("ContinentalGT")
print(ContinentalGT)
print(ContinentalGT.name)
print(ContinentalGT.vehicle)
print(ContinentalGT.company)
ContinentalGT.welcome()
