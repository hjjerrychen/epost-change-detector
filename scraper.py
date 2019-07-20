import requests
import constants
import datetime
import time
import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from requests.models import PreparedRequest

def main():
    url = constants.PRISM_URL if constants.PRISM_AUTH else constants.YORK_PASSPORT_URL
    previous = get_grades(url)
    append_change_to_file(previous)
    while True:
        time.sleep(constants.REFRESH_TIME)
        current = get_grades(url)
        if current != previous:
            print("Change detected")
            append_change_to_file(current)
            if constants.NOTIFY_VIA_EMAIL or constants.NOTIFY_VIA_TEXT: send_email(url)
            previous = current

def get_grades(url):
    r = requests.get(url, auth = (constants.USERNAME, constants.PASSWORD), params = constants.PAYLOAD)
    return BeautifulSoup(r.text, "html.parser").html.find_all("table")[1].get_text()

def append_change_to_file(data):
    file = open(constants.CHANGES_FILE_NAME, "a")
    file.write("-----------------------------------------------------------------------------------------\n")
    file.write("page change for: " + constants.YEAR + " " + constants.TERM + " " + constants.COURSE +"\n")
    file.write("detected on: " + str(datetime.datetime.now().strftime("%a, %b %d, %Y  %l:%M:%S %p")) + "\n")
    file.write(data + "\n")
    file.close()

def send_email(url):
    req = PreparedRequest()
    req.prepare_url(url, constants.PAYLOAD)
    url = req.url
    recipients = []
    if constants.NOTIFY_VIA_EMAIL: recipients = constants.EMAILS_TO_NOTIFY
    if constants.NOTIFY_VIA_TEXT: recipients.append(constants.PHONE_NUMBER + constants.CARRIER_GATEWAY)
    email_body = f"change detected. link to marks:\n{url}"

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

if __name__== "__main__":
    main()