# f=open("a1.py")
# print(f.read())
# contect=f.read()
# print("failis kontenti aris "+"\n",contect)
# f.seek(0)
# f=open("failis kontenti aris"+"\n",contect)
f=open("info.txt","r+")
with open("info.txt","r+"):
    f.write("nugo")
    f.write("kobakhidaze")
    f.write("14")
    f.write('gartymashi ar var')
print(f.read(a))