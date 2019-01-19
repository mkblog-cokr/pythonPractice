import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class mkSendEmail:
    def __init__(self, sentTo, subject, content):
        emailAddr = "sender@mail.com"   #MK: sender email address
        emailPass = "*********"         #MK: password for sender email
        smtpAddr = "smtp.mail.com"      #MK: smtp server. in case of gmail, smtp.gmail.com
        smtpPort = 465
        emailMsg = MIMEMultipart()
        #MK: isinstance는 Variable Type을 파악하기 위해 사용
        if isinstance(sentTo, list):
            emailMsg["To"] = ", ".join(sentTo)
            #MK: STR.join(list): List에 있는 String 사이에 STR을 추가하여서 한 String으로 변경함
            #MK: """ STRING """ (3개)를 사용하면 새로운 줄도 STRING에 포함
            #MK: " STRING %s " % STR_VARIABLE을 사용하면 %s에 STR_VARIABLE이 들어감
        elif isinstance(sentTo, str):
            emailMsg["To"] = sentTo
        else:
            print("MK:First parameter is unknown type")
            return
        emailMsg["From"] = emailAddr
        emailMsg["Subject"] = subject
        content = content + "\n\n by MKBlog"
        tmp = MIMEText(content, "plain")
        emailMsg.attach(tmp)
        try:
            emailServer = smtplib.SMTP_SSL(smtpAddr, smtpPort)
            emailServer.ehlo()
            emailServer.login(emailAddr, emailPass)
            emailServer.sendmail(emailAddr, sentTo, emailMsg.as_string())
            emailServer.close()
            print("MK: Email is sent")
        except:
            print("Error: Could not semd email")

if __name__ == "__main__":
    #MK: List or String, Subject String, Contect String
    sendMail=mkSendEmail(["test@mail.com", "test1@mail.com"], "Test Subject", "Test Content")

#출처
#https://stackabuse.com/how-to-send-emails-with-gmail-using-python/
#https://docs.python.org/2/library/email-examples.html#id5