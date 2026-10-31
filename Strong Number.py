import math
n=int(input())
temp=n
r=0
res=0
while n>0:
  r=n%10
  res+=math.factorial(r)
  n//=10
if temp==res:
  print("Strong")
else:
  print("Not Strong")
