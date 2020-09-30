import smtplib
print("mail sender system")
sender=input("enter your mail id : ")
reciver=input("enter reciver's mail id : ")

message=input("enter the message here(without newline):")
try:
    passward=input("enter passward :")
    smtpObj=smtplib.SMTP('smtp.gmail.com' , 587)
    smtpObj.starttls()
    smtpObj.login(sender,passward)
    smtpObj.sendmail(sender,reciver,message)
    print("sucessfully mail sent")
    smtpObj.quit()
    
except Exception:
    print("Error !! unable to sent mail.")
    smtpObj.quit()
    
