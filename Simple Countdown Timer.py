import time

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        
        time.sleep(1)
        seconds -= 1
    
    print("Time's up! 🚀")
try:
    user_time = int(input("Enter the time in seconds: "))
    countdown(user_time)
except ValueError:
    print("Please enter a valid number.")