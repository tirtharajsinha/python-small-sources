import smtplib
print("mail sender system")
# to use this snippet more efficient way save a mail gmail id as string in 'serderd' variable 
sender=input("enter your mail id (if default type only '1'): ").strip()
if sender=="1":
    senderd="tsinha098@gmail.com"
    sender=senderd
reciver=input("enter reciver's mail id : ")
sub="Subject:"+input("enter subject of the mail:")+"\n"
message=sub+input("enter the message here(without newline):")+"\n This message is auto-generated.sent by Tirtharaj_sinha-official.If you think this is mistake,ignore"
try: 
    passward=input("enter passward of your id:")
    smtpObj=smtplib.SMTP('smtp.gmail.com' , 587)
    smtpObj.starttls()
    smtpObj.login(sender,passward)
    try:
        smtpObj.sendmail(sender,reciver,message)
        print("sucessfully mail sent")
        smtpObj.quit()
    except Exception:
        print("Error !!  unable to send mail")
        smtpObj.quit()
    
    
except Exception:
    print("Error !! unable to login")
    
    smtpObj.quit()
    
