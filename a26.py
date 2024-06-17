# class base:
#     def get_perimeter(self):
#         raise NotImplementedError("shvilobil klass ar gaachnia get_perimeter metodi")
# class Square(base):
#     def __init__(self,s):
#         self.s=s

#     def get_perimeter(self):
#         return (4*self.s)

# s1=Square(10)
# print(s1.get_perimeter())

# class Triangle(base):
#     def __init__(self,a,b,c):
#         self.a=a
#         self.b=b
#         self.c=c

#     def triangle_perimeter(self):
#         return (self.a+self.b+self.c)

# t1=Triangle(10,15,20)
# print(t1.triangle_perimeter())

# class Martkutxedi(base):
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
    
#     def get_perimeter(self):
#         return (2*self.a+2*self.b)
# m1=Martkutxedi(10,15)
# print(m1.get_perimeter())
# list1=[Square(10),Triangle(10,15,20),Martkutxedi(10,15),Martkutxedi(1,5),Martkutxedi(9,10),Martkutxedi(69,5)]
# print(list1)
# for i in list1:
#     try:
#         print(i.get_perimeter())
#     except AttributeError:
#         print("no perimetri")
class Parent:
    def move(self):
        raise NotImplementedError("ar modzraobs sheni transport")

class Car:
    def __init__(self,model,year,max):
        self.model=model
        self.year=year
        self.max=max
    def move(self):
        print("sheni transport modzraobs")
class Plaint