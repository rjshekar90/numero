
#DB Connection Code

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
