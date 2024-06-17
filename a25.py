# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("person created")

#     def say_hello(self):
#         print(f"{self.name} says hello")

# class Student(Person):
#     def __init__(self,name,surname,age):
#         self.name=name
#         self.surname=surname
#         self.age=age

#     def __str__(self):
#         return f"{self.name} {self.name} {self.age}"
# class Teacher(Person):
#     def teach(self):
#         print(f"a teacher named {self.name} is teaching")

# student1=Student("luka",20)
# student2=Student("mikheil",14)
# teacher=Teacher("nika",12)

# student1.say_hello()
# student2.say_hello()
# teacher.say_hello()

# student1.study()
# student2.study()
# teacher.teach()

# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("person created")

#     def say_hello(self):
#         print(f"{self.name} says hello")


# class Student(Person):
#     def __init__(self,name,age,surname):
#         super().__init__(name,age)
#         self.surname=surname

#     def study(self):
#         print(f"student named {self.name} is studying")

#     def say_hello(self):
#         super().say_hello()
#         print(f"{self.name} mogesalmebit dzhmebo da debo")

class Car:
    def __init__(self,year,model,engine):
        self.year=year
        self.model=model
        self.engine=engine
    def car_drive(self):
        print(f"{self.model} modzraobs")

class Bmw(Car):
    def __init__(self,year,model,engine,horsepower,maxspeed):
        super().__init__(year,model,engine)
        self.horsepower=horsepower
        self.maxspeed=maxspeed
    def max_speed(self):
        print(f"{self.maxspeed} aris am modelis maximaluri siswrafe")
    def horse_power(self):
        print(f"am models aqvs {self.horsepower} cxenis dzhala")

class Mercedes(Car):
    def __init__(self,year,model,engine,horsepower,maxspeed):
        super().__init__(year,model,engine)
        self.horsepower=horsepower
        self.maxspeed=maxspeed
    def max_speed(self):
        print(f"{self.maxspeed} aris am modelis maximaluri siswrafe")
    def horse_power(self):
        print(f"am models aqvs {self.horsepower} cxenis dzhala")
bmw1=Bmw(2001,"m4","v3",500,170)
bmw2=Bmw(2023,"m5","v10",500,350)

print(bmw1.max_speed)