import smtplib

logf='/home/username/Desktop/asd.log'

f = open(logf,"r")
string = f.read()

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("mail1", "password")
 
# sending the mail
s.sendmail("mail1", "mail2", string)
 
# terminating the session
s.quit()
