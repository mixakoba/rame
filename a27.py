class Toy:
    def __init__(self,name):
        self.name=name
obj1=Toy("zangi")
obj2=Toy("levan")
obj3=Toy("nigga")
toy_list=[obj1,obj2,obj3]
x=0
while x<len(toy_list):
    print(toy_list[x].name)
    x+=1