import smtplib

logf='/home/abhiven/Desktop/asd.log'

f = open(logf,"r")
string = f.read()

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("#Your Mail", "#Your Password")
 
# sending the mail
s.sendmail("#Your Mail", "#Your Mail", string)
 
# terminating the session
s.quit()
