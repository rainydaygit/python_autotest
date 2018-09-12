# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from config import read_config

class sendEmail:

    def __init__(self, receiver):
        #邮件配置：发件人，收件人，服务器端口
        self.smtpserver = read_config.get_email_info('smtp_server')
        self.port = read_config.get_email_info('port')
        self.sender = read_config.get_email_info('sender')
        self.pwd = read_config.get_email_info('pwd')
        # 收件人接收多个
        self.receiver = ';'.join(receiver)

        # print(self.smtpserver,self.pwd,self.port,self.sender)

    def send_email_text(self, subject, content):

        #邮件内容：主题，正文
        # 发送文本邮件
        #self.subject = '测试邮件发送主题'
        # content = '<p>邮件正文哈哈哈哈</p>'
        msg = MIMEText(content, 'html', 'utf-8')

        msg['from'] = self.sender
        msg['to'] = self.receiver
        msg['subject'] = subject

        #发送邮件：实例化SMTP，链接服务器，登录服务器，发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.sender, self.pwd)
        except:
            smtp = smtplib.SMTP_SSL(self.smtpserver, self.port)
            smtp.login(self.sender, self.pwd)
        smtp.sendmail(self.sender, self.receiver, msg.as_string())
        smtp.quit()


    def send_email_multipart(self, subject, fpath):

        msg = MIMEMultipart()
        msg['from'] = self.sender
        msg['to'] = self.receiver
        msg['subject'] = subject

        # 发送带附件的邮件
        with open(fpath, 'rb') as f:
            mail_body = f.read()

        #正文
        #print(mail_body)
        content = MIMEText(mail_body, 'html', 'utf-8')
        # print(body)
        msg.attach(content)
        #附件
        att = MIMEText(mail_body, "base64", "utf-8")
        att["Content-Type"] = "application/octet-stream"
        att["Content-Disposition"] = 'attachment; filename="test_report.html"'
        msg.attach(att)

        #发送邮件：实例化SMTP，链接服务器，登录服务器，发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.smtpserver)
            smtp.login(self.sender, self.pwd)
        except:
            smtp = smtplib.SMTP_SSL(self.smtpserver, self.port)
            smtp.login(self.sender, self.pwd)
        smtp.sendmail(self.sender, self.receiver, msg.as_string())
        smtp.quit()


if __name__ == '__main__':
    se = sendEmail(['996807988@qq.com', 'zhujie@jianq.com'])
    #se.send_email_text('这是主题', '这是内容！！！！')
    se.send_email_multipart('带附件的主题', '../淘宝搜索Python的结果.xls')