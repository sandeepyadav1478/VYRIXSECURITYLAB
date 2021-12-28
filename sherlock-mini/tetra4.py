import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import utils
from datetime import datetime

#creds
# -------------------------------------------------
smtp_ser = 'smtp.gmail.com'
smtp_port = 587
receiver = #receiver's email 
sender = #sender's email
backup = #backup email address/secondary email address
password = #password
subj = "Taday's Report from Sherlock, "+ str(datetime.now())
# --------------------------------------------------


def mailer(dataarray):

  #message
  msg = MIMEMultipart('alternative')
  # Plain-text version of content
  plain_text = """\
      Hi there,
      This message is sent from Rob.
      Visit us here https://wakandacapital.net
      Have a good day!
  """
  s = "" 
  for data in dataarray:
        s += "<tr><td><a href= "+str(data)+">"+str(data)+"</a></td></tr>"

  # html version of content
  html_content = """\
  <!DOCTYPE html>
  <html lang="en">
    <body>
      <table>
        """+s+"""
      </table>
    </body>
  </html>
  """

  html_part = MIMEText(html_content, 'html')
  text_part = MIMEText(plain_text, 'text')

  msg.attach(text_part)
  msg.attach(html_part)

  msg['From'] = 'Reporter <tester14785@gmail.com>'
  msg['Subject'] = subj
  msg['Date'] = utils.formatdate(localtime = 1)
  msg['Message-ID'] = utils.make_msgid()


  # initialize connection to our email server, we will use Outlook here
  smtp = smtplib.SMTP(smtp_ser, port=smtp_port)

  smtp.ehlo()  # send the extended hello to our server
  r = smtp.starttls()  # tell server we want to communicate with TLS encryption
  if int(r[0]) == 220:
    print("--INFO: TLS Encryption stablished.")  # finally, don't forget to close the connection
  else:
    print("--ERROR: Some error occured during TLS Encryption stablishment.")
  r = smtp.login(sender, password)  # login to our email server
  if int(r[0]) == 235 or int(r[0]) == 334:
    print("--INFO: Login successful.")  # finally, don't forget to close the connection
  else:
    print("--ERROR: Invalid credentials for login.")
  # send our email message 'msg' to our boss
  smtp.sendmail(receiver,
                backup,
                msg.as_string())

  #closing connection
  r = smtp.quit()  
  if int(r[0]) == 221:
    print("--INFO: Connection colsed successfully.")  # finally, don't forget to close the connection
    return True
  else:
    print("--ERROR: Some error occured during connection closing.")
    return False
