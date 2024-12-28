# Key-Logger
Designed to spread awareness about keylogging threats.

This project implements a Keylogger that captures keyboard inputs and sends the recorded logs via email for analysis or monitoring purposes.

**Features**

1.Keyboard Event Logging: Tracks all key presses, including special keys like Enter, Backspace, Tab, and Space.
2.Data Storage: Saves the recorded keystrokes in a keylogger.txt file.
3.Email Alerts: Sends the collected key logs to a specified email address using a secure SMTP connection.

**Requirements**
Python 3.6 or later.

**Required Libraries:**
1.pynput
2.smtplib
3.ssl

Install dependencies using:
pip install pynput

**How It Works**

1.Key Logging:
Captures all key press events, including alphanumeric and special keys.
Saves the data in a keylogger.txt file for record-keeping.

2.Email Notification:
Reads the logged data from keylogger.txt.
Sends the recorded data via email to a recipient using the Gmail SMTP server.

3.Termination:
The keylogger stops running when the ESC key is pressed.

4.Configuration
Before running the script, configure the email settings:
sender_email: Your Gmail address (used to send emails).
receiver_email: Recipient's email address.

5.password: Your Gmail account password (or app-specific password for enhanced security).
Example configuration:

python

sender_email = "your_email@gmail.com"
receiver_email = "recipient_email@gmail.com"
password = "your_password"

//Important: If using Gmail, enable "Allow less secure apps" or create an app-specific password.

Usage
Clone the repository or download the script.
Open the script and configure the email credentials as described above


Run the script using:
python keylogger.py

Press ESC to stop the keylogger.
File Description
keylogger.txt: Contains the logged keystrokes.
keylogger.py: Main Python script for logging and email notification.
Security and Legal Disclaimer
Authorization: Always obtain explicit consent before using a keylogger. Unauthorized usage is illegal and unethical.
Secure Configuration: Use app-specific passwords and avoid sharing your email credentials.
Educational Use Only: This project is intended for learning purposes. The author is not responsible for misuse.
Limitations
Requires an active internet connection to send email notifications.
Compatibility is limited to operating systems supported by the pynput library.

**License**
This project is licensed under the MIT License.

