# import necessary packages
 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import keyring
 
# create message object instance
msg = MIMEMultipart()

message = "This is a test message:\n"
 
# setup the parameters of the message
password = keyring.get_password("new_keyring", "nas@escolaarrels.com")
msg['From'] = "nas@escolaarrels.com"
msg['To'] = "josep.garriga@escolaarrels.com"
msg['Subject'] = "Automatic mail"
attachment=open("body.txt",'r')
 
# add in the message body and attachments
msg.attach(MIMEText(message, 'plain'))
msg.attach(MIMEText(attachment.read()))
 
#create server
server = smtplib.SMTP('smtp.gmail.com: 587')
 
server.starttls()
 
# Login Credentials for sending the mail
server.login(msg['From'], password)
 
 
# send the message via the server.
server.sendmail(msg['From'], msg['To'], msg.as_string())
 
server.quit()