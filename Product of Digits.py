a=int(input())
digit=1
while a!=0:
  last=a%10
  digit=last*digit
  a=a//10
print(digit)
