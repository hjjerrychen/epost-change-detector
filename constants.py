# TODO: FILL IN THE FOLLOWING BEFORE RUNNING scraper.py

# Put 'True' if course uses PRSIM account authentication, otherwise put 'False' for York Passport authentication
PRISM_AUTH = True
# York Passport or PRISM account username
USERNAME = "USERNAME"
# York Passport or PRISM account password
PASSWORD = "PASSWORD"
# Put the school year, 4 digit 'from' year, 2 digit 'to' year(FFFF-TT) 
YEAR = "2018-19"
# Fall: 'F', Winter: 'W', Summer: 'S'
TERM = "S"
# Course as it is displayed in the dropdown
COURSE = "2021"
# Refresh time in seconds
REFRESH_TIME = 60.0

# Notify changes via email and text?
NOTIFY_VIA_EMAIL = False
NOTIFY_VIA_TEXT = False
# Gmail Address
EMAIL = 'EMAIL@EMAIL.COM'
# Gmail Password
EMAIL_PASSWORD = 'PASSWORD'
# Email SMTP server address 
EMAIL_SMTP_SERVER = 'smtp.gmail.com'
# Email SMTP port number
SMTP_PORT_NUMBER = 465
# Send texts to these addresses when change detected...
PHONE_NUMBER = "1234567890"
CARRIER_GATEWAY = "@GATEWAY.COM"
# Send emails to these addresses when change detected...
EMAILS_TO_NOTIFY = ["EMAIL@EMAIL.COM"]
# File name to store change log
CHANGES_FILE_NAME = "changes.txt"

# DO NOT CHANGE ANYTHING AFTER THIS LINE
PRISM_URL = "https://www.eecs.yorku.ca/~roumani/ePost/server/ep.cgi"
YORK_PASSPORT_URL = "https://www.eecs.yorku.ca/~roumani/ePost/ppy/ep.cgi"
PAYLOAD = {
    "year": YEAR,
    "term": TERM,
    "course": COURSE
}