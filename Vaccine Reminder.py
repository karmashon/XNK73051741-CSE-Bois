import csv
import datetime
import smtplib

# creating a mail server and sending the message
try:
    sender=input("Enter sender email address: ") #tname4513@gmail.com
    pswd=input("Enter password: " ) #vjay$2206
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login(sender,pswd)
    body="This is a reminder to undergo your vaccination as soon as possible!!"


    days={"Monday":0,"Tuesday":1,"Wednesday":2,"Thursday":3,"Friday":4,"Saturday":5,"Sunday":6}
    sendday1="Sunday"
    sendday2="Monday"
    if (datetime.date.today().weekday()==days[sendday1]):
        f1=open("nodose.csv")
        for i in csv.reader(f1,delimiter=','):
            if len(i)!=0:
                server.sendmail(sender,i[2],body)
        f1.close()

        print("Weekly Mail sent on",sendday1)
    else:
        print("No",sendday1,"mail sent")
        
    if (datetime.date.today().weekday()==days[sendday2]):
        f2=open("onedose.csv")
        for i in csv.reader(f2,delimiter=','):
            if len(i)!=0:
                server.sendmail(sender,i[2],body)
        f2.close()

        print("Weekly Mail sent on",sendday2)
    else:
        print("No",sendday2,"mail sent")
except Exception as e:
    print(e)
    
finally:
    server.quit()




