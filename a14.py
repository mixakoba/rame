# list1= [[1,2,3],[4,5,6],[7,8,9,]]
# for i in range(len(list1)):
#     for k in range(len(list1)):
#         print(list1[i][k])
list1=[[1,2,3],[4,5,6]]
ls=[]
result=[]
for i in range(len(list1)):
    ls.append(sum(list1[i]))
    print(ls)

for i in range(len(list1)):
    result+=list1[i]
print(result)

list1=[[1,2,3],[4,5,6]]
print(sum(result))