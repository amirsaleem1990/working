#!/usr/bin/python3

def send_email(MAIL_CUSTOMER, body, subject, filename=None):
	import smtplib
	from email.mime.text import MIMEText
	from email.mime.multipart import MIMEMultipart
	from email.mime.application import MIMEApplication

	MAIL_FROM = ""
	MAIL_HOST = "smtp.gmail.com"
	MAIL_PORT = 587
	MAIL_PASS = ""

    print(f"Sending Email to {MAIL_CUSTOMER} ................ ")

    s = smtplib.SMTP(f'{MAIL_HOST}:{MAIL_PORT}')
    s.starttls()
    s.login(MAIL_FROM, MAIL_PASS)

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = MAIL_FROM
    msg['To'] = MAIL_CUSTOMER

    txt = MIMEText(body)
    msg.attach(txt)

    if filename != None:
	    fo=open(filename,'rb')
	    attach = MIMEApplication(fo.read(),_subtype="pdf")
	    fo.close()
	    attach.add_header('Content-Disposition','attachment',filename=filename)
	    msg.attach(attach)

    s.send_message(msg)
    s.quit()


# # ye bilkul sahi h, bas is me attechment nahi h
# def send_email(MAIL_CUSTOMER, body):
# 	# message = MIMEText(email_html, 'html')
# 	# message['From'] = MAIL_FROM
# 	server = smtplib.SMTP(f'{MAIL_HOST}:{MAIL_PORT}')
# 	server.starttls()
# 	server.login(MAIL_FROM, MAIL_PASS)
# 	server.sendmail(from_addr=MAIL_FROM, to_addrs=MAIL_CUSTOMER, msg=body)
# 	server.quit()
# mail_options
# msg = f'''\
# From: LFD
# Subject: Salray slip for the month of {str(d.monthOfSalary) + " " +  str(d.yearofSalary)}'...

