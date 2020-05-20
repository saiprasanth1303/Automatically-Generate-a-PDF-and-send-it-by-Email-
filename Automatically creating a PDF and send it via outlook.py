#! /usr/bin/env python3


from email.message import EmailMessage
import os.path
# label the attachment with a MIME type and subtype to tell them what sort of file you’re sending
import mimetypes
# create an object that will represent our mail server, and handle sending messages to that server
import smtplib
import ssl
# ask for invisible password
import getpass

# create empty email
message = EmailMessage()
print(type(message))

# add sender + recipient
sender = "yourmail@hotmail.fr"
recipient = "targetmail@hotmail.fr"
message['From'] = sender
message['To'] = recipient
print(message)

# add subject
message['Subject'] = f'Greetings from {sender} to {recipient}'
print(message)

# add message
body = "They're separate from the email's message body, which is the main content of the message."
message.set_content(body)
print(message)


# add an attachment
attachment_path = ""
attachment_filename = os.path.basename(attachment_path)
# get the MIME type and subtype
mime_type, _ = mimetypes.guess_type(attachment_path)
print(mime_type)
# EmailMessage type needs a MIME type and subtypes as separate strings
mime_type, mime_subtype = mime_type.split('/', 1)
print(mime_type)
print(mime_subtype)

# ADD attachment
with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

# HERE THE ADD LINES:


# create ssl protocol context
context = ssl.SSLContext(ssl.PROTOCOL_TLS)
# SMTP_SSL class will make a SMTP connection over SSL/TLS. Like this:
mail_server = smtplib.SMTP('smtp-mail.outlook.com', 587)

# email password => very bad habit
# better use the hash function for keeping the session login
mail_pass = getpass.getpass('Password? ')

# add the SSL context
mail_server.starttls(context=context)

# END OF THE ADDED LINES


# connect to the email server
# need to ADD a try/except
server_response = mail_server.login(sender, mail_pass)

print(server_response)
# send the message
server_response = mail_server.send_message(message)
print(server_response)

mail_server.quit()
