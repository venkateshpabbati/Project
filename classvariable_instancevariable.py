class car:

    wheels = 4

    def __init__(self):
        self.brand = "BMW"
        self.mil = 10
    
c1 = car()
c2 = car()

c1.brand = 'TATA'
c1.mil = 24

car.wheels = 5

print(c1.brand, c1.mil, c1.wheels)
print(c2.brand, c2.mil, c2.wheels)

