import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class WorkEmail():

    def __init__(self, login, password, host_output='smtp.gmail.com', host_input='imap.gmail.com'):
        self.login = login
        self.password = password
        self.host_output = host_output
        self.host_input = host_input

    def send_message(self, message, subject=None, recipients=None): 
        messager = MIMEMultipart()
        messager['From'] = self.login
        messager['To'] = ', '.join(recipients)
        messager['Subject'] = subject
        messager.attach(MIMEText(message))
        
        smtp_server = smtplib.SMTP(self.host_output, 587)
        smtp_server.ehlo()
        smtp_server.starttls()
        smtp_server.ehlo()

        smtp_server.login(self.login, self.password)
        smtp_server.sendmail(self.login, recipients, messager.as_string())
        smtp_server.quit()

    def recieve_massage(self, header=None):
        imap_server = imaplib.IMAP4_SSL(self.host_input)
        imap_server.login(self.login, self.password)
        imap_server.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, list_email_uid = imap_server.uid('search', None, criterion)
        assert list_email_uid[0], 'There are no letters with current header'
        last_email_uid = list_email_uid[0].split()[-1]
        result, msg = imap_server.uid('fetch', last_email_uid, '(RFC822)')
        raw_email = msg[0][1]
        email_message = email.message_from_string(raw_email)
        imap_server.logout()


if __name__ == '__main__':
    igmail = WorkEmail(...)
    igmail.send_message(...)
    igmail.recieve_massage(...)