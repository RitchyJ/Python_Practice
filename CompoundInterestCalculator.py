# Instead of using while principle <= 0, if you would like to incorperate the number 0, just use while True. Do not do while principle = 0
#       while True will prompt the code to run nomatter the value of the principle

principle = 0
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero")
    else:
        break
while True:
    rate = float(input("Enter the rate amount: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero")
    else:
        break
while True:
    time = int(input("Enter the time in years amount: "))
    if time < 0:
        print("Time can't be less than or equal to zero")
    else:
        break
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ${total:.2f}")