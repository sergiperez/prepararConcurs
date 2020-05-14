import fileinput
lines=[]
for line in fileinput.input():
    lines.append(line[:-1])
for l in lines:
    suma=0
    for i in l:
        suma = suma+ int(i)
    print("The sum of the digits of "+l+" is "+str(suma)+".")
