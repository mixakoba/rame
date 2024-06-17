# # x=5
# # print(type(x))
# # x="hello,World"
# # print(type(x))
# # class Dog:
# #     name="Doggo"
# #     age=2
# #     weight=20
# # dog2=Dog()
# # dog2.name="richi"
# # dog2.age=10
# # dog2.weight=50

# # dog3=Dog()
# # dog3.name="jumberi"
# # dog3.age=9
# # dog3.weight=30

# # class Dog:
# #     def __init__(self,name,age,weight):
# #         self.name=name
# #         self.age=age
# #         self.weight=weight

# # dog1=Dog("doggo",2,40)
# # dog2=Dog("richi",10,30)
# # dog3=Dog("umberto",9,35)
# class Dog:
#     def __init__(self,name,age,weight):
#         self.name=name
#         self.age=age
#         self.weight=weight
# dog1=Dog("doggo",2,40)
# dog2=Dog("richi",10,30)
# dog3=Dog("umberto",9,35)

# print(dog1.age)
# print(dog1.name)
# print(dog1.weight)

# print(dog2.age)
# print(dog2.name)
# print(dog3.weight)

# class employee:
#     salary_raise=1.1
#     def __init__(self,name,surname,age,salary):
#         self.name=name
#         self.surname=surname
#         self.age=age
#         self.salary=salary
#         self.raised_salary=self.salary=self.salary_raise
    
# employee1=employee("geogre","fload",47,5000)
# print(employee1.name)
# print(employee1.salary)
# print(employee1.raised_salary)
# print(employee1.salary_raise)
# employee2=employee("tetri","zangi",12,0)
# print(employee2.name)
# print(employee2.age)
# print(employee2.surname)
# print(employee2.salary)
# print(employee2.raised_salary)
# print(employee2.salary_raise)

# class Employee:
#     salary_raise = 1.1
#     def __init__(self, name, surname, age, salary):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.raised_salary=self.salary=self.salary_raise
#         self.surname = surname
#     def print_full_name(self):
#         print(f"{self.name} {self.surname}")

#     def print_sallary(self): 
#         print(f"{self.salary}")

#     def print_raised_sallary(self):
#         print(f"{self.raised_salary}")
# nigga1=Employee("Nigga", "Floyd", "19", 88)
# nigga1.print_full_name()
# nigga1.print_sallary()
# nigga1.print_raised_sallary()
class Director:
    def __init__(self,name,surname,age,kanisferi):
        self.name=name
        self.age=age
        self.surname = surname
        self.kanisferi=kanisferi
# print(f"directoris saxelia {Director.name},is aris {Director.age},misi gvaria{Director.surname}is {Director.kanisferi}")
    def print_name(self):
        print(f"{self.name} {self.surname}")
    def print_age(self):
        print(f"{self.age}")
    
a = Director("Giorgi", "Baxia", 40, "tetri")
a.print_name()