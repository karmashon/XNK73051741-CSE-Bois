import csv
import operator

def Sort(filename):
    li=[]
    with open(filename) as f:
        x=csv.reader(f,delimiter=',')
        for i in x:
            if len(i)!=0:
                li.append(i)
    li.sort()
    with open(filename,'w') as f:
        x=csv.writer(f,delimiter=',')
        for i in li:
            x.writerow(i)

def Separate():
    f1=open("namelist.csv")
    f2=open("nodose.csv",'w')
    x1=csv.reader(f1,delimiter=',')
    x2=csv.writer(f2,delimiter=',')
    for i in x1:
        if len(i)!=0:
            if int(i[4])==0:
                x2.writerow([i[0],i[1],i[2],i[3],i[4]])
    f2.close()
    f1.close()

    f1=open("namelist.csv")
    f2=open("onedose.csv",'w')
    x1=csv.reader(f1,delimiter=',')
    x2=csv.writer(f2,delimiter=',')
    for i in x1:
        if len(i)!=0:
            if int(i[4])==1:
                x2.writerow([i[0],i[1],i[2],i[3],i[4]])
    f2.close()
    f1.close()
    
    f1=open("namelist.csv")
    f2=open("twodose.csv",'w')
    x1=csv.reader(f1,delimiter=',')
    x2=csv.writer(f2,delimiter=',')
    for i in x1:
        if len(i)!=0:
            if int(i[4])==2:
                x2.writerow([i[0],i[1],i[2],i[3],i[4]])
    f2.close()
    f1.close()

def Delete(name):
    li=[]
    with open("namelist.csv") as f:
        x=csv.reader(f,delimiter=',')
        for i in x:
            if len(i)!=0:
                if i[0]!=name:
                    li.append(i)
    with open("namelist.csv",'w') as f:
        x=csv.writer(f,delimiter=',')
        for i in li:
            x.writerow(i)
    with open("nodose.csv") as f:
        x=csv.reader(f,delimiter=',')
        for i in x:
            if len(i)!=0:
                if i[0]!=name:
                    li.append(i)
    with open("nodose.csv",'w') as f:
        x=csv.writer(f,delimiter=',')
        for i in li:
            x.writerow(i)
    with open("onedose.csv") as f:
        x=csv.reader(f,delimiter=',')
        for i in x:
            if len(i)!=0:
                if i[0]!=name:
                    li.append(i)
    with open("onedose.csv",'w') as f:
        x=csv.writer(f,delimiter=',')
        for i in li:
            x.writerow(i)
    with open("twodose.csv") as f:
        x=csv.reader(f,delimiter=',')
        for i in x:
            if len(i)!=0:
                if i[0]!=name:
                    li.append(i)
    with open("twodose.csv",'w') as f:
        x=csv.writer(f,delimiter=',')
        for i in li:
            x.writerow(i)
        
# creating a list of entries
print('''MENU
       1. Add Entry
       2. Delete Entry
       3. Exit''')
print()
while True:
    ch=int(input("Enter choice: "))
    
    if ch==1:
        f=open("namelist.csv",'a')
        x=csv.writer(f,delimiter=',')
        name=input("Enter name: ")
        adhar=input("Enter aadhar no: ")
        email=input("Enter email address: ")
        dob=input("Enter date of birth dd-mm-yyyy: ")
        vacc=input("Enter vaccination count: ")
        print()
        x.writerow([name,adhar,email,dob,vacc])
        Sort("namelist.csv")
        Separate()
        print("Entry Added")
        print()

    elif ch==2:
        name=input("Enter name of entry to be deleted: ")
        Delete(name)
        print("Entry deleted")
        print()
        
    elif ch==3:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
        print()





'''def Set(column,new):
    li=[]
    found=False
    with open("namelist.csv") as f:
        x=csv.reader(f,delimiter=',')
        for i in x:
            if len(i)!=0:
                if i[0]==name:
                    found=True
                    li.append(i)
                    li[li.index(i)][column-1]=new
                else:
                    li.append(i)
    if found==True:
        with open("namelist.csv",'w') as f:
            x=csv.writer(f,delimiter=',')
            for i in li:
                x.writerow(i)
        with open("nodose.csv") as f:
            x=csv.reader(f,delimiter=',')
            for i in x:
                if len(i)!=0:
                    if i[0]==name:
                        li.append(i)
                        li[li.index(i)][column-1]=new
                    else:
                        li.append(i)
        with open("nodose.csv",'w') as f:
            x=csv.writer(f,delimiter=',')
            for i in li:
                x.writerow(i)
        with open("onedose.csv") as f:
            x=csv.reader(f,delimiter=',')
            for i in x:
                if len(i)!=0:
                    if i[0]==name:
                        li.append(i)
                        li[li.index(i)][column-1]=new
                    else:
                        li.append(i)
        with open("onedose.csv",'w') as f:
            x=csv.writer(f,delimiter=',')
            for i in li:
                x.writerow(i)
        with open("twodose.csv") as f:
            x=csv.reader(f,delimiter=',')
            for i in x:
                if len(i)!=0:
                    if i[0]==name:
                        li.append(i)
                        li[li.index(i)][column-1]=new
                    else:
                        li.append(i)
        with open("twodose.csv",'w') as f:
            x=csv.writer(f,delimiter=',')
            for i in li:
                x.writerow(i)

        print("Entry updated")
        print()
    else:
        print("Name not found")

def Update():
    column=int(input("Enter column number to update: "))
    if column==1:
        new=input("Enter new name: ")
        Set(column,new)
    elif column==2:
        new=input("Enter new aadhar no: ")
        Set(column,new)
    elif column==3:
        new=input("Enter new email id: ")
        Set(column,new)
    elif column==4:
        new=input("Enter new date of birth: ")
        Set(column,new)
    elif column==5:
        new=input("Enter new vaccination count status: ")
        Set(column,new)
    else:
        print("Invalid column number")'''
