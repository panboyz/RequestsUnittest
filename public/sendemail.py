# -*- coding:utf-8 -*-

"""

@author:  zhoubaoyu
@create:  2018/8/16 22:31

"""

import smtplib
from public import getconfig
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr


cf = getconfig.ReadConfig()


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


def send_email(file_name, base_name):
    from_mail = cf.get_email('sender_default')
    to_mail = [cf.get_email('receiver')]
    auth_password = cf.get_email('mail_pass')

    message = MIMEMultipart()
    message.attach(MIMEText(cf.get_email('content'), 'plain', 'utf-8'))
    attach = MIMEText(open(file_name, 'rb').read(), 'base64', 'utf-8')
    attach['Content-Type'] = 'application/octet-stream'
    attach['Content-Disposition'] = 'attachment; filename="%s"' % base_name
    message.attach(attach)

    message['From'] = _format_addr('测试owner <%s>' % from_mail)
    message['To'] = _format_addr('测试组 <%s>' % (','.join(to_mail)))
    subject = cf.get_email('subject')
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtp_server = cf.get_email('mail_host')
        server = smtplib.SMTP(smtp_server, cf.get_email('mail_port_default'))
        server.login(from_mail, auth_password)
        server.sendmail(from_addr=from_mail, to_addrs=to_mail, msg=message.as_string())
        server.quit()
        print(u"邮件发送成功")
    except smtplib.SMTPException as e:
        print(u'邮件发送异常\n', e)
