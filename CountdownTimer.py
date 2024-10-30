import time

while True:
    my_time = int(input("Enter the time in seconds: "))
    for x in range(my_time, 0, -1):
        seconds = x % 60
        minutes = int(x / 60) % 60
        hours = int(x / 3600) % 24
        days = int(x / 86400)
        print(f"Days: {days:02} Hours:{hours:02} Minutes:{minutes:02} Seconds:{seconds:02}")
        time.sleep(1)

    print("Time's Up!")

    again = input("Would you like to set another Countdown? yes/no: ")
    if again.lower() != "yes":
        break
