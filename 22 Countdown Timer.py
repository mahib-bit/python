import time

countdown = int(input("Enter the countdown time in seconds:"))

for t in reversed(range(1, countdown+1)): #(countdown,0,-1)
    seconds = t % 60
    minutes = int(t/60)
    hours = int(t/3600)
    time.sleep(1)
    print(f"{hours:02}:{minutes:02}:{seconds:02}")

print("TIME'S UP!")