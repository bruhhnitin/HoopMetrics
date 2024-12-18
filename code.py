import csv

def main():
    while True:
        choice=int(input("Enter your choice: \n1) Show details \n2) Write \n3) Append \n4) Update \n5) Delete \n6) Search \n: "))
        if choice==1:
            display_csv()
        elif choice==2:
            write_csv()
        elif choice==3:
            append_csv()
        elif choice==4:
            update_csv()
        elif choice==5:    
            delete_csv()
        elif  choice==6:
            search_csv()
        else:
            print("Enter valid number!")
        con=input("Do you want to continue operations?? (y/n): ")
        if con.lower()=='n':
            break

def display_csv():
    f=open("player.csv","r")
    reader=csv.reader(f)
    print("Player details are: ")
    for i in reader:
        print(i)
    f.close()


def write_csv():
    f=open("player.csv","w",newline='')
    writer=csv.writer(f)
    writer.writerow(["S.No","Name","Team","Age","PPG","RPG","APG","BPG","SPG","Player Efficiency Rating"])
    record=[]
    while True:
        sno=int(input("Enter serial number: "))
        name=input("Enter name: ")
        team=input("Enter team: ")
        age=input("Enter age: ")
        ppg=float(input("Enter points per game: "))
        rpg=float(input("Enter rebounds per game: "))
        apg=float(input("Enter assists per game: "))
        bpg=float(input("Enter blocks per game: "))
        spg=float(input("Enter steals per game: "))
        a=ppg+rpg+apg+bpg+spg
        x=a/5
        per=round(x,2)
        data=[sno,name,team,age,ppg,rpg,apg,bpg,spg,per]
        record.append(data)
        con=input("Do you want to continue writing data? (y/n): ")
        if con.lower()=='n':
            break
    for i in record:
        writer.writerow(i)
    f.close()

def append_csv():
    f=open("player.csv","a",newline='')
    writer=csv.writer(f)
    record=[]
    while True:
        sno=int(input("Enter serial number: "))
        name=input("Enter name: ")
        team=input("Enter team: ")
        age=input("Enter age: ")
        ppg=float(input("Enter points per game: "))
        rpg=float(input("Enter rebounds per game: "))
        apg=float(input("Enter assists per game: "))
        bpg=float(input("Enter blocks per game: "))
        spg=float(input("Enter steals per game: "))
        a=ppg+rpg+apg+bpg+spg
        per=a/5
        data=[sno,name,team,age,ppg,rpg,apg,bpg,spg,per]
        record.append(data)
        con=input("Do you want to continue appending data? (y/n): ")
        if con.lower()=='n':
            break
    f.seek(0,0)
    for i in record:
        writer.writerow(i)
    f.close()

def update_csv():

    with open("player.csv", "r") as fr:
        reader = csv.reader(fr)
        lines = list(reader)

   
    found = False

    
    with open("player.csv", "w", newline='') as fw:
        writer = csv.writer(fw)
        writer.writerow(lines[0]) 

        
        check_name = input("Enter the name of the person to be updated: ")
        search = int(input("Enter what should be updated: \n1) S.No \n2) Name \n3) Team \n4) Age \n5) PPG \n6) RPG \n7) APG \n8) BPG \n9) SPG \n: "))

        for i in lines[1:]:
            if i[1] == check_name:
                found = True
                if search == 1:
                    new_sno = int(input("Enter new serial number: "))
                    i[0] = new_sno

                elif search == 2:
                    new_name = input("Enter new name: ")
                    i[1] = new_name

                elif search == 3:
                    new_team = input("Enter new team: ")
                    i[2] = new_team

                elif search == 4:
                    new_age = input("Enter new age: ")
                    i[3] = new_age

                elif search == 5:
                    new_ppg = float(input("Enter new points per game: "))
                    i[4] = new_ppg
                    a=float(i[5])+float(i[6])+float(i[4])+float(i[7])+float(i[8])
                    per=a/5
                    i[9]=per

                elif search == 6:
                    new_rpg = float(input("Enter new rebounds per game: "))
                    i[5] = new_rpg
                    a=float(i[5])+float(i[6])+float(i[4])+float(i[7])+float(i[8])
                    per=a/5
                    i[9]=per

                elif search == 7:
                    new_apg = float(input("Enter new assists per game: "))
                    i[6] = new_apg
                    a=float(i[5])+float(i[6])+float(i[4])+float(i[7])+float(i[8])
                    per=a/5
                    i[9]=per

                elif search == 8:
                    new_bpg = float(input("Enter new blocks per game: "))
                    i[7] = new_bpg
                    a=float(i[5])+float(i[6])+float(i[4])+float(i[7])+float(i[8])
                    per=a/5
                    i[9]=per

                elif search == 9:
                    new_spg = float(input("Enter new steals per game: "))
                    i[8] = new_spg
                    a=float(i[5])+float(i[6])+float(i[4])+float(i[7])+float(i[8])
                    per=a/5
                    i[9]=per
                    
                else:
                    print("Enter valid number.")
                writer.writerow(i) 
  
            else:
                writer.writerow(i)  

    if not found: 
        print("Record not found.")
    else:
        print("Data has been updated in the CSV file.") 

def delete_csv():
    with open("player.csv", "r", newline='') as fr:
        reader = csv.reader(fr)
        lines = list(reader)
    found = False
    with open("player.csv", "w", newline='') as fw:
        writer = csv.writer(fw)
        writer.writerow(lines[0])
        choice = input("Enter name of person to be deleted: ")
        for i in lines[1:]:
            if i[1].lower() == choice.lower():
                found = True
                continue
            else:
                writer.writerow(i)
        if not found:
            print("Name not found.")
        else:
            print("Deleted data from the CSV File.")

        
def search_csv():
    fr=open("player.csv","r")
    reader=csv.reader(fr)
    print("Searching data from CSV file....")
    choice=int(input("How do you want to search? \n1) Serial Number \n2) Name \n3) Team \n4) Age \n5) Player Efficiency Rating \n: "))
    found=0
    next(reader)
    if choice==1:
        sno=int(input("Enter serial number to be searched: "))
        for i in reader:
            if int(i[0])==sno:
                print(i)
                found+=1
                  
    if choice==2:
        name=input("Enter name to be searched: ").lower()
        for i in reader:
            if name in i[1].lower():
                print(i)
                found+=1
                  
    if choice==3:
        team=input("Enter team to be searched : ").lower()
        for i in reader:
            if team in i[2].lower():
                print(i)
                found+=1
                  
    if choice==4:
        age=int(input("Enter age to be searched : "))
        for i in reader:
            if int(i[3])==age:
                print(i)
                found+=1

    if choice==5:
        per=float(input("Enter PER to be searched: "))
        for i in reader:
            if float(i[9])==per:
                print(i)
                found+=1
    
    if found==0:
            print("Search not found")
            fr.close()      
main()
