import smtplib
from email.mime.text import MIMEText

# Group3123456


def send_mail(receivers,info):
    mail_host = 'smtp.163.com'
    mail_user = 'g3_test'
    mail_pass = 'ZCILNXRKZLVSPKBD'
    # mail_pass = 'Group3123456'
    sender = 'g3_test@163.com'
    # receivers = ['1632259373@qq.com']
    txt = '您好，您乘坐的'+info+'班次列车上有感染人员，请及时居家隔离，谢谢合作。'
    message = MIMEText(txt, 'plain', 'utf-8')
    message['Subject'] = '同乘交通系统居家隔离提醒'
    message['From'] = sender
    message['To'] = receivers
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 587)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)


# send_mail('z1632259373@gmail.com','K3301')
