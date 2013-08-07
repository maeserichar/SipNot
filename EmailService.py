import smtplib
from email.mime.text import MIMEText

def SendMail(fromAddress, toAddress, subject, body):
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = fromAddress
	msg['To'] = toAddress

	s = smtplib.SMTP('localhost')
	s.sendmail(fromAddress, toAddress, msg.as_string())
	s.quit()

if __name__ == '__main__':
	SendMail('test@youriphaschanged.com', 'rodriguezfernandezricardo@gmail.com', 'Test Email', 'This is a test email from MailService.py')
