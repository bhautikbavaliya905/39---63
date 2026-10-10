import smtplib

sender = "bhautikbavaliya905@gmail.com"
password = "lrvftudyynedbwmv"
receiver = "b1204gamer@gmail.com"

message = "Hello, this is a test email sent using Python."

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender, password)
server.sendmail(sender, receiver, message)

server.quit()

print("Email sent successfully!")

