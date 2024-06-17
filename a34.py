def abc(list1):
    i=0
    summ=0
    while i<len(list1):
        summ+=list1[i]
        i+=1
    if len(list1)//2:
        return summ
    else:
        print("kenti raodenobaa")
list1=[1,2,3,4,5,6,7,8,9,10]
print(abc(list1))