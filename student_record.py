
#DB Connection Code

import smtp
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

import pymysql
mydb=pymysql.connect('localhost','root','root','python_usa')
cur=mydb.cursor()
def save_record():
    id=int(input("Enter the id::"))
    name=input("Enter your name:")
    age=int(input("Enter your age:"))
    query="insert into student values(%d,'%s',%d);" %(id,name,age)
    cur.execute(query)
    mydb.commit()

def show_all():
    query="select * from student;"
    cur.execute(query)
    data=cur.fetchall()
    print(data)

def search_record(id):
    query="select * from student where student.student_id=%d" % id
    cur.execute(query)
    data=cur.fetchall()
    print(data)

def delete_record(id):
    query="delete  student.* from student where student.student_id=%d" % id
    cur.execute(query)
    mydb.commit()

def export_to_excel():

    filename = open("test.csv", "wb")
    c = csv.writer(filename)

    query = "select * from student;"
    cur.execute(query)
    data = cur.fetchall()

    for item in data:
        c.writerow(item)

def send_email():
   fromaddr = "email address"
   toaddr = "Receveivers email addr"
   msg = MIMEMultipart()

   msg['From'] = #fromaddr
   msg['To'] = #toaddr
   msg['Subject'] = "SUBJECT OF THE EMAIL"

   body = "TEXT YOU WANT TO SEND"

   msg.attach(MIMEText(body, 'plain'))

   filename = #"NAME OF THE FILE WITH ITS EXTENSION"
   attachment = open("PATH OF THE FILE", "rb")  #location of the file

   part = MIMEBase('application', 'octet-stream')
   part.set_payload((attachment).read())
   encoders.encode_base64(part)
   part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

   msg.attach(part)

   # change gmail settings to allow less secure apps.
   server = smtplib.SMTP('smtp.gmail.com', 587)
   server.starttls()
   server.login(fromaddr, "YOUR PASSWORD")
   text = msg.as_string()
   server.sendmail(fromaddr, toaddr, text)
   server.quit()


def quit_db_excel():
    curr.close()
    mydb.close()
    filename.close()




while True:
   print("Enter option:")
   print("1. Add")
   print("2. Show All")
   print("3. Search")
   print("4. Delete")
   print("5. Export to excel")
   print("6. Quit")
   opt=int(input("Enter your option::"))
   if opt==1:
        save_record()
   elif opt==2:
        show_all()
   elif opt==3:
        id=int(input("Please enter a id to search::"))
        search_record(id)
   elif opt==4:
        id=int(input("Please enter a id to delete::"))
        delete_record(id)
   elif opt==5:
        export_to_excel()
   elif opt==6:
       quit_db_excel()
   else:
      print("Please Enter a Valid Option")

mydb.close()
