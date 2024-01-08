import pywhatkit as kit
import pyautogui
import time

# Recipient's WhatsApp number (including country code)
phone_numbers = ["",""]  #"+9194*****3"

# Message to be sent
message = "!...."

# Ensure WhatsApp Web is logged in and focused
for phone_number in phone_numbers:
    kit.sendwhatmsg_instantly(phone_number, message, wait_time=30)  # Allow ample time for loading
    time.sleep(20)  # Wait for message box to appear
    pyautogui.press('enter')


print("Message sent successfully!")
