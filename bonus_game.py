import time

# Function to perform countdown
def countdown(total_seconds):
    while total_seconds > 0:
        # Convert total seconds into hours, minutes, and seconds
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60
        
        # Print formatted time
        print(f"{hours}:{minutes}:{seconds}")

        # Wait for 1 second
        time.sleep(1)

        # Decrement total seconds by 1
        total_seconds -= 1
        
# Main program
try:
    # Take user input for time to count down
    user_input = input("Insert time to count down ")

    # Split user input into hours, minutes, and seconds
    hours, minutes, seconds = map(int, user_input.split(":"))

    # Calculate total seconds
    total_seconds = hours * 3600 + minutes * 60 + seconds

    # Start the countdown
    countdown(total_seconds)
except ValueError:
    # Handle invalid input format
    print("Error...Please enter time in the format 'hh:mm:ss' with integer values.")
