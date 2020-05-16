numero = input()
n1 = int(numero[0])
n2 = int(numero[1])
n3 = int(numero[2])

s1 = ""
s2 = ""
s3 = ""

if n1 <= n2 and n1 <= n3:
  s1 = n1
  if (n2 <= n3):
    s2 = n2
    s3 = n3
  else:
    s2 = n3
    s3 = n2
elif n2 <= n1 and n2 <= n3:
  s1 = n2
  if (n1 <= n3):
    s2 = n1
    s3 = n3
  else:
    s2 = n3
    s3 = n1
elif n3 <= n1 and n3 <= n2:    
  s1 = n3
  if (n1 <= n2):
    s2 = n1
    s3 = n2
  else:
    s2 = n2
    s3 = n1
print(str(s1)+str(s2)+str(s3))