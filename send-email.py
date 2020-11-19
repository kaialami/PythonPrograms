import smtplib, ssl, sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender = 'pizzahutofficial119@gmail.com'
receiver = 'pizzahutofficial119@gmail.com'

port = 465
password = str(input('Password: '))

msg = MIMEMultipart("alternative")
msg["Subject"] = "Multipart test"
msg["From"] = sender
msg["To"] = receiver

text = '''\
Yo whats up my doggie

Click this epic link: 
https://www.youtube.com/watch?v=4TnAKurylA8'''

html = '''\
<html>
    <body>
        <p>Yo whats up my doggie<br>
        <a href="https://www.youtube.com/watch?v=4TnAKurylA8">Click this epic link</a>
        </p>
    </body>
</html>
'''

part1 = MIMEText(text, "plain")
part2 = MIMEText(html, "html")

msg.attach(part1)
msg.attach(part2)

# Create secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    try:
        server.login(sender, password)
    except:
        print("That password is incorrect.")
        sys.exit(0)

    server.login(sender, password)
    # Send email here:
    server.sendmail(sender, receiver, msg.as_string())
    print(f"Email sent to {receiver}.")
