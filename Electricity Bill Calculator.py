units = float(input())

if units <= 50:
    bill = units * 1
elif units>=51 and units <= 150:
    bill = 50 + (units - 50) * 2
elif units>=151 and units <= 250:
    bill = 50 + 200 + (units - 150) * 3
else:
    bill = 50 + 200 + 300 + (units - 250) * 4

if bill > 150:
    bill = bill + bill * 0.20

print(int(bill) if bill.is_integer() else bill)
