import smtplib
from email.mime.text import MIMEText

def send_email(to, subject, body, smtp_server, smtp_port, username, password):
    body = body.encode('utf-8')
    msg = MIMEText(body, 'plain', 'utf-8')
    msg['To'] = ', '.join(to)
    msg['From'] = username
    msg['Subject'] = subject
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    server.sendmail(username, to, msg.as_string())
    server.quit()