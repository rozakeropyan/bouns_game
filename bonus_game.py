import time

def countdown(total_seconds):
    while total_seconds > 0:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        print(f"{hours}:{minutes}:{seconds}")
        time.sleep(1)
        total_seconds -= 1

try:
    user_input = input("Insert time to count down ")
    hours, minutes, seconds = map(int, user_input.split(":"))
    total_seconds = hours * 3600 + minutes * 60 + seconds
    countdown(total_seconds)
except ValueError:
    print("Erroe...Please enter time in the format 'hh:mm:ss' with integer values.")
