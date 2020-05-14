graus = int(input())

if (graus > 30):
  print("it’s hot")
  if (graus >= 100):
    print("water would boil")
elif (graus<10) :
  print("it’s cold")
  if (graus <= 0):
    print("water would freeze")
else:
  print("ok")