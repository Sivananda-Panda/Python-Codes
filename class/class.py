'''class circle:    
    def __init__(self):
        self.rad = int(input('enter here: '))
    
    def area(self):
        area=3.14*(self.rad)**2
        return area

    def diameter(self):
        diameter=2*self.rad
        return diameter

    def circumference(self):
        circumference=2*3.14*self.rad
        return circumference

siva=circle()
print(siva.area())

class student():
    def __init__(self,sci,math,oriya):
        self.sci=sci
        self.math=math
        self.oriya=oriya
    def total(self):
        totalmarks=self.sci+self.math+self.oriya
        return totalmarks
    def per(self):
        percent=(self.sci+self.math+self.oriya)/3
        return percent

siva=student(98,100,99)
print(siva.total())
print(siva.per())'''
        


class student():
    totalmarks=0

    def __init__(self, *subjects):
        self.subjects = subjects

    def total(self):
        
        for i in self.subjects:
            self.totalmarks = self.totalmarks+i
        return self.totalmarks
    def per(self):
        
        percent=(self.totalmarks)/len(self.subjects)
        return percent

siva=student(98,100,99,99,98)
        
#siva=student(map(int, input('Give the marks: ').split()))
print(siva.total())
print(siva.per())



