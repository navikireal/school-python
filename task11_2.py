class Car:
    def __init__(self,marka,speed):
        self.marka = marka
        self.speed = speed

    def moveB(self,b=5):
        return (f'Скорость: {self.marka} {self.speed + b} km/h')

    def moveM(self,a=5):
        return(f'Скорость: {self.marka} {self.speed - a} km/h')

    def moveS(self):
        return(f'Скорость: {self.marka} {self.speed-self.speed} km/h')

    def moveO(self):
        return (f'Скорость: {self.marka} {self.speed} km/h')

    def moveZ(self):
        return (f'Скорость: {self.marka} {-self.speed} km/h')

car1 = Car("Audi",45)
print(car1.moveM())



