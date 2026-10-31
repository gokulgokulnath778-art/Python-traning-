a=int(input())
even=0
while a>0:
  last=a%10
  if a%2==0:
    even+=last
  a=a//10
print(even)
  
