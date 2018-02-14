import smtplib

logf='/home/abhiven/Desktop/asd.log'

f = open(logf,"r")
string = f.read()

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
 
# start TLS for security
s.starttls()
 
# Authentication
s.login("abkven@gmail.com", "Sriram*247")
 
# sending the mail
s.sendmail("abkven@gmail.com", "abkven@gmail.com", string)
 
# terminating the session
s.quit()
