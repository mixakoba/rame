list1=["h","e","l","m","l","o"]
list2 = list1.copy()
n=0
m=len(list1)-1
while n<m/2:
    list1[n],list1[m-n]=list1[m-n],list1[n]
    n+=1
print(list1 == list2[::-1])