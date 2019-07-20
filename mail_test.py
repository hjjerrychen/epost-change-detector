import smtplib
import constants
from email.mime.text import MIMEText
from requests.models import PreparedRequest

req = PreparedRequest()
req.prepare_url(constants.PRISM_URL, constants.PAYLOAD)
url = req.url
print(url)
recipients = []
if constants.NOTIFY_VIA_EMAIL: recipients = constants.EMAILS_TO_NOTIFY
if constants.NOTIFY_VIA_TEXT: recipients.append(constants.PHONE_NUMBER + constants.CARRIER_GATEWAY)
email_body = f"change detected. click on link to view marks:\n{url}"

message = MIMEText(email_body)
message["Subject"] = f"MARKS UPDATED {constants.YEAR} {constants.TERM} {constants.COURSE}"
message["From"] = constants.EMAIL
message["To"] = ", ".join(recipients)

try:
    server = smtplib.SMTP_SSL(constants.EMAIL_SMTP_SERVER, constants.SMTP_PORT_NUMBER)
    server.ehlo()
    server.login(constants.EMAIL, constants.EMAIL_PASSWORD)
    server.sendmail(constants.EMAIL, recipients, message.as_string())
    server.close()

except Exception as exception:
    print ("Email cannot be sent:")
    print(exception)