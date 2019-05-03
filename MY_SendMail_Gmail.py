
import smtplib

fromaddr = '@gmail.com'
toaddrs  = '@gmail.com'
msg = ''


# Credentials (if needed)
username = '@gmail.com'
password = 'irjlpglqfujcdomq'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
