import smtplib
import unittest
from email.message import EmailMessage
from variables import PASSWORD

class EmailTestCase(unittest.TestCase):
    def test_mailtrap(self):
        sender = "Private Person <from@example.com>"
        receiver = "A Test User <to@example.com>"
        subject = 'Test Email'
        body = 'This is a test email sent from SMTP server'
        msg = EmailMessage()
        msg.set_content(body)

        with smtplib.SMTP("sandbox.smtp.mailtrap.io", 2525) as server:
            server.login("a89c7e27877a63", PASSWORD)
            server.sendmail(sender, receiver, subject)


if __name__ == '__main__':
    unittest.main()