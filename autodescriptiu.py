numeroAutoDescriptiu = 0
for i in range(999999999,10000000000):
  print(str(i))
  for x in str(i):
    cops = 0
    numero=0
    index = 0
    while (str(i).index(x,index)>0):
      cops = cops + 1;
    if (cops == int(x)):
      if (numero == 9):
       numeroAutoDescriptiu = str(i)
       break
      numero = numero + 1;
    else:
       break
  if (numeroAutoDescriptiu > 0):
    break
print(numeroAutoDescriptiu)