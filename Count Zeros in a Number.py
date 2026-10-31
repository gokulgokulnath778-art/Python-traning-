n=int(input())
count=0
if n==0:
  count=1
while n>0:
  r=n%10
  if r==0:
    count+=1
  n//=10
print(count)
