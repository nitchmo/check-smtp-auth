import smtplib

host = 'smtp.hostname.tld'
port = 587
user = 'user_name'
pwd = 'password'

try:
    s = smtplib.SMTP(host, port)
    print "Connected ", host, ":", port

    code, msg = s.ehlo()
    print "> EHLO: [", code, "]\n", msg

    code, msg = s.starttls()
    print "> STARTTLS: [", code, "]\n", msg

    code, msg = s.ehlo()
    print "> EHLO: [", code, "]\n", msg

    code, msg = s.login(user, pwd)
    print "> LOGIN: [", code, "]\n", msg

except Exception, e:
    print "\nError:"
    print e

finally:
    s.close()
