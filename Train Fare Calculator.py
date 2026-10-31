age = int(input())
distance = int(input())

fare = distance * 5

if age < 12:
    fare = fare * 0.5
elif age >= 60:
    fare = fare * 0.75

print(int(fare) if fare.is_integer() else fare)
