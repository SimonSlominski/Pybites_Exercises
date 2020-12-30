import smtplib

from_addr = ''
to_addr = ''

body = 'E-mail text'

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

# Beep to server
smtp_server.ehlo()

smtp_server.starttls()
smtp_server.login('')
smtp_server.sendmail(from_addr, to_addr, body)
smtp_server.quit()

print('Email sent successfully')
