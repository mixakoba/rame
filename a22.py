# A=int(input("enter the first number:"))
# B=int(input("enter the second number:"))

# try:
#     print(A/B)
# except ZeroDivisionError:
#     print("ver moxvda a/b ze gayofa,radgan b=0")
# print("GAMARJOBA!!!")
# try:
#     a=int(input("sheiyvane ricxvi"))
# except ValueError:
#     print("ricxvi da ara sxva simbolo")
# try:
#     a=int(input("sheiyvanet pirveli ricxvi:"))
#     b=int(input("sheiyvanet meore ricxvi:"))
#     print(a/b)
# except ValueError:
#     print("shen unda sheiyvano ricxvi")
# except ZeroDivisionError:
#     print("b ar unda iyos 0")
# try:
#     print(y)
# except NameError:
#     print("y ar arsebobs")
# try:
#     file=open("example.txt","r")

# except FileNotFoundError:
#     print("faili ar arsebobs")
# finally:
#     file.close()
# list1=[1,2,3,4,5,6,7,8,9,10]
# i=0
# while len(list1)>i:
#     print(list1[i])
#     i+=1
while True:
    try:    
        a = int(input("Sheiyvane Pirveli Ricxvi: "))
        print(a ** 2)
        break
    except ValueError:
        print("Araswori Ricxvia!")