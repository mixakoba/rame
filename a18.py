# def returnMinimum(*args):
#     minimum = args[0]

#     for i in args:
#         if minimum > i:
#             minimum = i 
#     return minimum

# print(returnMinimum(1,2))

# def numberssum(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

# numberssum(name="nika",surname="dimitrich",age=14,salary="mona")

# def numberSum(**kwargs):
#     print(kwargs.keys())
#     print(kwargs.values())
#     summ=0
#     for value in kwargs.values():
#         summ+=value
#     print(summ)

# numberSum(elene=1000,giorgi=500,zangi=-4500,jumberi=3000)

# def numbers(*args,**kwargs):
#     print(args)
#     print(kwargs)

# numbers(10,12,123,51,464,64,name="levani",surname="bakhia",job="usaxlkaro")

# def abc(*args):
#     sashualo=sum(args)//len(args)
#     return sashualo
# print(abc(1,2,3,4,5,6,7,8,9))

# def sashualo(**kwa):
#     summ=0
#     for i in kwa.values():
#         summ+=i
#     sashualo=summ/len(kwa)
#     return sashualo
# print(sashualo(geografi=4,biologia=4,istoria=4))

# file=open('hello.txt','r',encoding='utf-8')
# print(file.readline())

# file=open('hello.txt','r+',encoding='utf-8')
# file.write(")
# file.read()

file=open("hello.txt",'a',encoding='utf-8')
file.write('hello \n')

with open("hello.txt",'r',encoding='utf-8') as file:
    print(file.read())

with open("hello.txt",'a',encoding='utf-8') as file:
    file.write("i hate niggers")   
    
    
    #rasist :/