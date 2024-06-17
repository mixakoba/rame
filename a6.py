# num=17
# while True:
#     user_input = int(input("enter num :"))

#     if user_input==num:
#         print(user_input)
# password="shavitoma123"

# while True:
#     entered_password= input("enter your password :")
#     if entered_password==password:
#         print("thats correct password")
#         break
# paroli="shavikaci123"
# x=3
# while x>0:
#     x-=1
#     entered_paroli=(input("sheiyanet paroli tqven gaqvt 3 cda :"))
#     if entered_paroli==paroli:
#         print("thats correct password")
#         break

# if entered_paroli!=paroli and x==0:
#     print("you dont have anymore tries")
# while True:
#     num1=float(input("sheiyvanet ricxvi 1:")) #sheviyvanet 1 ricxvi
#     operator=input("seiyvanet operatori (+,-,*,/): ") #sheviyvanet operatori
#     num2=float(input("sheiyvanet ricxvi 2: ")) #sheviyvanet meore ricxvi 

#     if operator=="+":
#         result=num1 + num2 #tu operatori mimateba aghmochnda mivumatet
#     elif operator=="-":
#         result=num1 - num2 #tu gamokleba gamovakelit
#     elif operator=="*":
#         result=num1 * num2 #tu gamravleba gavamravlet
#     elif operator=="/":
#         result=num1 / num2 # tu gayofa gavyavit
#     else:
#         print("shecdomaa araswori operatori sheyvanet")

#     print("shedegia: ",result) #gamovitanet shedegi

#     choice=input("ginda gamotvlis gagrdzheleba :") #vkitxet unda tu ara gagrdzeleba
#     if choice!="yes":
#         break
x=0
maximum=0
while True:
    num=int(input("sheiyvanet ricxvi :"))
    maximum+=num
    x+=1
    kitxva=input("gnebavs gagrdzheleba :")
    if kitxva=="ara":
        break
print(maximum/x)