import json
print("==========STUDENT REPORT==========")
students=[]


def add():
    no =int(input("enter no. of student to add: "))
    for i in range(no):
        name = input("enter student's name:")
        rollno = int(input("enter  student's roll no. : "))
        marks=[]
        for i in range(1,4):
            mark = int(input("enter marks"))
            if mark>100 or mark<0:
                print("marks shoud be positive or less then 100")
            if i ==1 :
                 marks.append(mark)
            if i ==1:
                marks.append(mark)
            if i == 3:
                 marks.append(mark)

        student={
           "name":name,
           "rollno":rollno,
           "marks":marks
        }
        students.append(student)
    with open("student.json", "w") as file:
           json.dump(students,file,indent=3)
    print("STUDENT ADDED SUCCESSFULLY")
def display():
       print("====list of student====")
       with open("student.json","r") as file:
          studentdata = json.load(file)      
       for student in studentdata:
                
            print("name:",student["name"])
            print("Roll No.: ",student["rollno"])
            for i in range(0,len(student["marks"])):
                if i==0:
                      print("PYTHON: ",student["marks"][i])
                if i==1:
                      print("DBMS:    ",student["marks"][i])
                if i==2:
                      print("OS:      ",student["marks"][i])
                

       

def search():

    searchrollno=int(input("enter roll no of student to search: "))
    with open("student.json", "r") as file:
            data = json.load(file)
    for student in data:
          if searchrollno == student["rollno"]:
                print("name:",student["name"])
                print("Roll No.: ",student["rollno"])
                for i in range(0,len(student["marks"])):
                    if i==0:
                        print("PYTHON: ",student["marks"][i])
                    if i==1:
                        print("DBMS:    ",student["marks"][i])
                    if i==2:
                        print("OS:      ",student["marks"][i])
                    
def result():

    searchrollno=int(input("enter roll no of student to search: "))
    with open("student.json", "r") as file:
            data = json.load(file)
    for student in data:
          if searchrollno == student["rollno"]:
                print("name:",student["name"])
                print("Roll No.: ",student["rollno"])
                total = 0
                for i in range(0,len(student["marks"])):
                    total = total + student["marks"][i]

                    if i==0:
                        print("PYTHON: ",student["marks"][i])
                    if i==1:
                        print("DBMS:    ",student["marks"][i])
                    if i==2:
                        print("OS:      ",student["marks"][i])

                    

                print("TOTAL: ", total)
                percent=total/3
                print("PERCENTAGE: ",percent,"%")
                if percent>=75:
                  print("distinction")
                elif percent>=60:
                     print("first division")
                elif percent>=40:
                     print("pass")
                else:
                     print("FAIL")

def topper():
    with open("student.json", "r") as file:
            data = json.load(file)
    highest= 0
    toppername = "none"
    for student in data:
         if sum(student["marks"])> highest:
              highest=sum(student["marks"])
              toppername  = student["name"]
    print("TOPPER IS: ", toppername)
    print("TOTAL MARKS IS; ",highest)
    
def classst():
    with open("student.json", "r") as file:
        data = json.load(file)
    total = 0
    for i in data:
        total   += 1
    print("total student",total)
    totalmark=0
    highest =0
    lowest =100
    passed =0
    fail=0

    for mark in data:
        
        if highest<(sum(mark["marks"])):
            highest = (sum(mark["marks"]))
        if lowest>(sum(mark["marks"])):
             lowest=  sum(mark["marks"])

         
        totalmark += sum(mark["marks"])
        if sum(mark["marks"])>40:
             
             passed+=1
        else:
             fail+=1
             
    print( "class average" ,totalmark/len(data))
    print("highest: ",highest,"%")
    print("lowest",lowest,"%")
    topper()
    print("student passed",passed)
    print("student fail",fail)
    

while True:
    print(
          "1.Add student\n" 
          "2.Display student\n" 
          "3.Search student\n" 
          "4.Student result\n" 
          "5.Find topper\n" 
          "6.Class statistic\n" 
          "7.Exit"
     )
    ch = int(input("enter your choice: "))
    if ch==1:
          add()
    elif ch==2:
         display()
    elif ch == 3:
         search()
    elif ch == 4:
         result()
    elif ch == 5:
         topper()
    elif ch ==6:
         classst()
    elif ch==7:
        print("===thank you===")
        break
    else:
         print("invalid choice")