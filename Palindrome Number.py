n=int(input())
temp=n
res=0
while n>0:
  r=n%10
  res=res*10+r
  n//=10
if res==temp:
  print("Palindrome")
else:
  print("Not Palindrome")
