# epost-change-detector
This python application is designed to constantly check ePost for mark updates. It was designed for devices such as the Raspberry Pi.

## Usage
**Set up the required constants before running**

Type in terminal:
`python3 detector.py`

## Setup
If there is a \*, you must set up this constant to use the application.
In the file  `constants.py`:
- \*`PRISM_AUTH` allows you to select an authentication method (York Passport or PRISM account) depending on which one your course uses. `True` for PRISM account, `False` for York Passport.
- \*`USERNAME` is your York Passport or PRISM username.
- \*`PASSWORD`is your York Passport or PRISM password.
- \*`YEAR` is the year of the course you wish to track. Format `"FFFF-TT"` where `FFFF` is the 4 digit start year and `TT` is the 2 digit end year.
- \*`TERM` is the term of the course you wish to track. `F` for Fall term, `W` for Winter term or `S` for Summer term.
- \*`COURSE` is the course you wish to track, exactly as how it is written in the dropdown menu on the ePost website.
- \*`REFRESH_TIME` is the time interval the application will check for changes, in seconds.
- `NOTIFY_VIA_EMAIL` allows you to select if you wish to receive a change notification email sent to emails in `EMAILS_TO_NOTIFY`. `True` for yes or `False` for no. Set to `False` by default.
- `NOTIFY_VIA_TEXT` allows you to select if you wish to receive a change notification text sent to the phone number in `PHONE_NUMBER`. `True` for yes or `False` for no. Set to `False` by default.
- `EMAIL` is the email address you wish to send the emails from. **This must be set up for both Email and Text notification methods.**
- `EMAIL_PASSWORD` is the password of the email account you wish to send emails from.
- `EMAIL_SMTP_SERVER` is the **SMTP** email server address of email provider.
- `SMTP_PORT_NUMBER`is the STMP port your email provider uses.
- `PHONE_NUMBER` is the phone number you wish to send text notifications to.
- `CARRIER_GATEWAY` is the email to text gateway of your phone carrier.
- `EMAILS_TO_NOTIFY` are the email(s) you wish to send a email notification to. It must be in array format, even if it is just one email address. 
- `CHANGES_FILE_NAME` is the name of the file where changes are stored.
 
### Sending Emails/Texts
- It is recommended to use a burner email account to send these notification emails.
- The application uses email to send text messages. This requires your carrier to support the SMS gateway functionality. Most carriers support this feature free of charge. If the email notification feature does not work, then your text message notifications won't work as well.

### Note
- Your credentials are stored without encryption in  `constants.py`. Take care to protect your data.
