# ###### Sending Emails ######

# ==============================
# ### Simple way of sending emails ###

# ------------------------------
# ### Importing smtplib ###
import smtplib

# ------------------------------
# Inside SMTP class the first argument is the mail server that we want to use and second is the port number
# 587 is the default mail submission port

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    # ehlo method identifies ourselves to the mail server that we are using
    smtp.ehlo()
    # Unless we wish to use has_extn() before sending mail, it should not be necessary to call this method explicitly. It will be implicitly called by sendmail() when necessary.

    # Encrypting our traffic
    smtp.starttls()

    # After encrypting our traffic we have to re-run the ehlo method to re-identify ourselves as an encrypted connection
    smtp.ehlo()

    # Once we are encrypted now we can login to our main serve
    smtp.login('sender@gmail.com', 'password')

    subject = 'Grab dinner this weekend'
    body = 'How about dinner at 6pm this Saturday'

    # When we are constructing a plain text email from strach we need to add subject as a header and the have couple of blank lines and then we need to put the body
    msg = f'Subject: {subject}\n\n{body}'

    # smtp.sendmail(SENDER_ADDRESS, RECEIVER_ADDRESS, msg)
    smtp.sendmail('sender@gmail.com', 'receiver@gmail.com', msg)
# ==============================
# ### Using Local Debug Server ###

# Using the local dubug server for testing purposes
# ------------------------------
# Importing smtplib module
import smtplib

# ------------------------------
# Execute the line below in terminal to start local debug server
# python3 -m smtpd -c DebuggingServer -n localhost:1025
# ------------------------------
with smtplib.SMTP("localhost", 1025) as smtp:

    subject = "Grab dinner this weekend"
    body = "How about dinner at 6pm this Saturday"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail("sender@gmail.com", "receiver@gmail.com", msg)
# ------------------------------
# ### Output ###

# ---------- MESSAGE FOLLOWS ----------
# b'Subject: Grab dinner this weekend'
# b'X-Peer: 127.0.0.1'
# b''
# b'How about dinner at 6pm this Saturday'
# ------------ END MESSAGE ------------

# ==============================
# ### Sending messages uing SMTP_SSL class ###

# ------------------------------
# Importing smtplib module
import smtplib

# ------------------------------
# Using the SMTP_SLL class to have SSL connection for beginning only so we don't need to run ehlo and starttls method

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("sender@gmail.com", "password")

    subject = "Grab dinner this weekend"
    body = "How about dinner at 6pm this Saturday"

    msg = f"Subject: {subject}\n\n{body}"

    smtp.sendmail("sender@gmail.com", "receiver@gmail.com", msg)
# ==============================    
# ### Sending more complex messages ###

# ------------------------------
# Importing modules
import smtplib
from email.message import EmailMessage

# ------------------------------
msg = EmailMessage()

# Our Subject
msg["Subject"] = "Grab dinner this weekend"

# Sender and Reciver Addresses
msg["From"] = "sender@gmail.com"  # Sender
msg["To"] = "receiver@gmail.com"  # Reciver

# Message Content
msg.set_content('"How about dinner at 6pm this Saturday"')

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("sender@gmail.com", "password")

    # Since we are just sending the message so we will use send_message method instead of sendmail method
    smtp.send_message(msg)
# ==============================
# ### Attaching one image ###

# ------------------------------
# Importing modules
import smtplib
from email.message import EmailMessage

# ------------------------------
msg = EmailMessage()

msg["Subject"] = "Grab dinner this weekend"
msg["From"] = "sender@gmail.com"  # Sender
msg["To"] = "receiver@gmail.com"  # Reciver
msg.set_content("How about dinner at 6pm this Saturday")
# ------------------------------
with open("image1.jpeg", "rb") as f:
    file_data = f.read()
    file_type = imghdr.what(f.name)  #Passing file name
    file_name = f.name

msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)
# Since we are sending image as attachment therefore maintype='image'
# subtype take what type of image we are attaching

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("sender@gmail.com", "password")
    smtp.send_message(msg)
# ==============================
# ### Attaching multiple images ###

# ------------------------------
# Since while we are sending multiple images to get type images we are using the imghdr
import imghdr  

# Importing modules
import smtplib
from email.message import EmailMessage

# ------------------------------
msg = EmailMessage()

msg["Subject"] = "Grab dinner this weekend"
msg["From"] = "sender@gmail.com"  # Sender
msg["To"] = "receiver@gmail.com"  # Reciver
msg.set_content("How about dinner at 6pm this Saturday")
# ------------------------------
files = ["image1.jpeg", "image2.jpeg", "image3.jpeg"]

for _file in files:
    with open(_file, "rb") as f:
        file_data = f.read()
        file_type = imghdr.what(f.name)  # Passing file name
        file_name = f.name

    msg.add_attachment(
        file_data, maintype="image", subtype=file_type, filename=file_name
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("sender@gmail.com", "password")
    smtp.send_message(msg)
# ==============================
# ### Attaching multiple attachments ###

# For this we have to only change maintype and subtype
# ------------------------------
# Importing modules
import smtplib
from email.message import EmailMessage
import imghdr  

# ------------------------------
msg = EmailMessage()

msg["Subject"] = "Grab dinner this weekend"
msg["From"] = "sender@gmail.com"  # Sender
msg["To"] = "receiver@gmail.com"  # Reciver
msg.set_content("How about dinner at 6pm this Saturday")
# ------------------------------
files = ["resume.pdf"]

for _file in files:
    with open(_file, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data, maintype="application", subtype="octet-stream", filename=file_name
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("sender@gmail.com", "password")
    smtp.send_message(msg)    
# ==============================    
# ### Sending messages to multiple people ##

# ------------------------------
# Importing modules
import smtplib
from email.message import EmailMessage
import imghdr  

# ------------------------------
contacts = [
    "testing1@gmail.com",
    "testing2@gmail.com",
    "testing3@gmail.com",
    "testing4@gmail.com",
]

msg = EmailMessage()

msg["Subject"] = "Grab dinner this weekend"
msg["From"] = "sender@gmail.com"  # Sender
msg["To"] = ", ".join(contacts)  # Reciver (Do it this way)
msg.set_content("How about dinner at 6pm this Saturday")
# ------------------------------
files = ["resume.pdf"]

for _file in files:
    with open(_file, "rb") as f:
        file_data = f.read()
        file_name = f.name

    msg.add_attachment(
        file_data, maintype="application", subtype="octet-stream", filename=file_name
    )

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("sender@gmail.com", "password")
    smtp.send_message(msg)   
# ==============================    
# ### Having HTMl and Plain text as fallback ##

# ------------------------------
# Importing modules
import smtplib
from email.message import EmailMessage
import imghdr  

# ------------------------------
contacts = [
    "testing1@gmail.com",
    "testing2@gmail.com",
    "testing3@gmail.com",
    "testing4@gmail.com",
]

msg = EmailMessage()

msg["Subject"] = "Grab dinner this weekend"
msg["From"] = "sender@gmail.com"  # Sender
msg["To"] = ", ".join(contacts)  # Reciver (Do it this way)

# Fallback plain text message
msg.set_content("How about dinner at 6pm this Saturday")

# HTML message
msg.add_alternative(
    """\
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""",
    subtype="html",
)

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login("sender@gmail.com", "password")
    smtp.send_message(msg) 
