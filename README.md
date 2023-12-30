# email-automation
This Python script automates the process of sending emails to multiple recipients using Gmail's SMTP server. It reads recipient email addresses from a file named `your_data.txt` and sends emails with attachments to those addresses. I created the program to do a freelance work - send automated emails for the customers. I researched and came up with a refined version that sends emails one by one and not including other recipients in the email. Also, added logs to see which emails were failed to send. Because of Gmail restrictions, added a timer to send the emails after some time not to be marked as spam.

### Prerequisites:
- Python environment
- Required Python libraries: `smtplib`

### Usage:
1. Set the working directory to the folder containing necessary files.
2. Configure SMTP server details: `smtp_server`, `port`, `sender_email`, and `password`.
3. Create a file with recipient email addresses (one email per line) and change the name of `your_data.txt`. 
4. Modify the email content, subject, and attachment path as needed.
5. Run the script in a Python environment.

### Script Overview:
- Reads recipient email addresses from `your_data.txt`.
- Sends emails with attachments to the listed recipients.
- Logs success or failure status in `log.txt`.

### Notes:
- Ensure the SMTP server and port are correctly set according to your email provider.
- Customize the email body, subject, and attachment path as required.
- Adjust the time delay between emails (in `time.sleep()`) based on your needs.

### Disclaimer:
- Use this script responsibly and comply with email regulations and policies.
