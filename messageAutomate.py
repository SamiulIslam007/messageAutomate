import pyautogui
import time

# Wait for a few seconds before starting to allow you to focus on the input field
time.sleep(5)

# Specify the line to be typed
line_to_type = "Tmi onk besi sundor ree."


# Number of iterations
num_iterations = 100  # Adjust this as needed

# Time delay between iterations in seconds
delay_seconds = 0.0001

# Loop with a delay of 0.3 seconds
for _ in range(num_iterations):

    # Type the line
    pyautogui.typewrite(line_to_type)

    # Press Enter
    pyautogui.press('enter')

    time.sleep(delay_seconds)
    

# The run script is " python messageAutomate.py "



