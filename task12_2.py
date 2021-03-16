class Car:
    def __init__(self,marka,speed):
        self.marka = marka
        self.speed = speed

    def moveB(self,b=5):
        return (f'Скорость: {self.marka} {self.speed + b} km/h')

    def moveM(self,a=5):
        if self.speed < 5:
            raise ValueError('NegativeSpeed')
        return(f'Скорость: {self.marka} {self.speed - a} km/h')

    def moveS(self):
        return(f'Скорость: {self.marka} {self.speed-self.speed} km/h')

    def moveO(self):
        return (f'Скорость: {self.marka} {self.speed} km/h')

    def moveZ(self):
        return (f'Скорость: {self.marka} {-self.speed} km/h')

car1 = Car("Audi",4)
try:
    car1.moveM()
except Exception:
    print('NegativeSpeed')



