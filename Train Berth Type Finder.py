a=int(input())
b=a%8
match b:
  case 1:
    print("LB")
  case 2:
    print("MB")
  case 3:
    print("UB")
  case 4:
    print("LB")
  case 5:
    print("MB")
  case 6:
    print("UB")
  case 7:
    print("SL")
  case _:
    print("SU")
