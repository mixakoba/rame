# tuple1=(1,2,3,4,5)
# for i in tuple1:
#     print(i)
# set1=set()

# for i in range(1,6):
#     set1.add(i)
#     print(i)    
employees = {
    "001001":"zangi jumberi",
    "001002":"qurdi jumberi",
    "001003":"rasisti jumberi",
    "001004":"jumberi"
}
print(employees)

print(employees["001001"])
print(employees["001002"])
print(employees["001003"])
print(employees["001004"])

employees["001001"]="shavkaniani jumberi"
print(employees["001001"])

print("001001" in employees) #true
print("0010013" not in employees)
print("001004" in employees)
print("00100121" in employees)

for i in employees:
    print(i)

for n in employees:
    print(employees[n])

dedaqalaqebi={
    "saqartvelo":"tbilisi",   #keyshi shevinaxet qveqnebi da valueshi dedaqalaqebi
    "germania":"berlin",
    "ukraina":"kievi",
    "niger":"abudja"
}

for i in dedaqalaqebi:  #gamovitaet qveqnebi
    print(i)

for n in dedaqalaqebi:  #gamovitanet dedaqalaqebi
    print(dedaqalaqebi[n])

print(dedaqalaqebi.keys())
for i in dedaqalaqebi.keys():
    print(i)


employees={"01":"nigger niggerovich","02":"george floyd"}

print(employees.items())
for item in employees.items():
    print(item)

dictonery1={
    "001":"mikheil",
    "002":"kobakhidze",
    "003":14
}
for i in dictonery1:
    print(dictonery1[i])


dictonery2={
    "001":"mikheil",
    "002":"kobakhidze",
    "003":14
}

for i in dictonery2.values():
    print(i)