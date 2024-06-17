some_list=[1,2,3,4,5]
i=0
while True:
    some_list[i]=some_list[i]**2
    if some_list[i]==3:
        continue
    i+=1
    if i==len(some_list):
        break
print(some_list)