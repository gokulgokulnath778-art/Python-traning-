f=0
f1=0
a=input()
for i in a:
  if i.isdigit():
    f=1
  elif i.isalpha():
    f1=1
if f!=0 and f1!=0:
  print("true")
else:
  print("false")
