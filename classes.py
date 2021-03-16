class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

class Figure:
    pass

class Circle(Figure):
    def __init__(self,x,y,dl_r):
        self.point = Point(x=x,y=y)
        self.dl_r = dl_r
    def res_p(self):
        res_p = (2*3.14*(self.dl_r**2))
        return res_p
    def res_s(self):
        res_s = (3.14 * (self.dl_r ** 2))
        return res_s

class Triagle(Figure):
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def res_p(self):
        res_p = (self.a + self.b + self.c)
        return res_p
    def res_s(self):
        res_s = ((self.a * self.b)/2)
        return res_s
class Square(Figure):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def res_p(self):
        res_p = (4*self.a)
        return res_p
    def res_s(self):
        res_s = (self.a**2)
        return res_s
