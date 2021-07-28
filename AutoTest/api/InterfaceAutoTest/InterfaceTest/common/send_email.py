# -*- coding:utf8 -*- #
# -----------------------------------------------------------------------------------
# ProjectName:   python20
# FileName:     python_lb.py
# Author:      liuyeyu
# Datetime:    2020/9/7 11:09
# Description:
#------------------------------------------------------------------------------------
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SendEmail:
    def send_emali(self, report_path):
        try:
                #配置邮箱服务器
                smtpserver = "smtp.163.com"
                #设置端口号
                port = "25"
                #设置发送人和登录密码（此密码是邮箱授权码，不是登录邮箱的密码）
                sender = "liu_ye_yu@163.com"
                pwd = "FONSQKJPKDWSDZVC"
                #设置收件人
                receiver = "liu_ye_yu@163.com"
                #创建邮件对象
                msg = MIMEMultipart()
                #发件人
                msg["from"] = sender
                #收件人
                msg["to"] = receiver
                #主题
                msg['subject'] ="测试报告"
                #
                with open(report_path,mode="rb") as fp:
                    body = fp.read()

                #写正文
                mime_text = MIMEText(body,"html","utf8")
                msg.attach(mime_text)
                #添加附件
                att = MIMEText(body,"base64","utf8")
                att["Content-Type"] = "application/octet-stream"
                att["Content-Disposition"] = "appchment;filename = %s"%report_path
                msg.attach(att)
                #发送邮件
                smtp= smtplib.SMTP()
                #连接服务器
                smtp.connect(smtpserver,port)
                #登录
                smtp.login(sender,pwd)
                #发送
                smtp.sendmail(sender,receiver.split(","),msg.as_string() )
                print("邮件发送成功")
        except:
            print("邮件发送失败")