n=int(input())
temp=n
s=len(str(n))
res=0
while n>0:
  r=n%10
  res+=pow(r,s)
  n//=10
if res==temp:
  print("Armstrong")
else:
  print("Not Armstrong")
