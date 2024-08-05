import csv
def main():

    f=open("player.csv","r",newline='')
    while True:
        choice=int(input("Enter your choice: 1) Show details 2) Write data 3) Append data 4) Update data"))
        if choice==1:
            display_csv()
        elif choice==2:
            write_csv()
        elif choice==3:
            append_csv()
        elif choice==4:
            update_csv()
        else:
            print("Enter valid number!")
        con=input("Do you want to continue?? (y/n)")
        if con.lower()=='n':
            break
    f.close()

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
    writer.writerow(["S.No","Name","Team","Age","PPG","RPG","APG",""])
    record=[]
    while True:
        sno=int(input("Enter serial number: "))
        name=input("Enter name: ")
        team=input("Enter team: ")
        age=input("Enter age: ")
        ppg=int(input("Enter points per game: "))
        rpg=int(input("Enter rebounds per game: "))
        apg=int(input("Enter assists per game: "))
        bpg=int(input("Enter blocks per game: "))
        spg=int(input("Enter steals per game: "))
        a=ppg+rpg+apg+bpg+spg
        per=a/5
        data=[sno,name,team,age,ppg,rpg,apg,bpg,spg,per]
        record.append(data)
        con=input("Do you want to continue? (y/n)")
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
        ppg=int(input("Enter points per game: "))
        rpg=int(input("Enter rebounds per game: "))
        apg=int(input("Enter assists per game: "))
        bpg=int(input("Enter blocks per game: "))
        spg=int(input("Enter steals per game: "))
        a=ppg+rpg+apg+bpg+spg
        per=a/5
        data=[sno,name,team,age,ppg,rpg,apg,bpg,spg,per]
        record.append(data)
        con=input("Do you want to continue? (y/n)")
        if con.lower()=='n':
            break
    f.seek(0,0)
    for i in record:
        writer.writerow(i)
    f.close()

def update_csv():
    f=open("player.csv","r+",newline='')
    reader=csv.reader(f)
    chk=input("Enter name to be searched: ")
    found=0
    for i in reader:
        if i[1].lower()==chk.lower():
            found+=1
            print("Record found")
            print(i[0],i[1],i[2],i[3],i[4])
            while True:
                x=int(input("What should be changed? 1) S.No 2) Name 3) Team 4) Age 5) PPG 6) RPG 7) APG 8) BPG 9)SPG "))
                if x==1:
                    y=int(input("Enter new serial number: "))
                    i[0]=y

                elif x==2:
                    y=input("Enter new name: ")
                    i[1]==y

                elif x==3:
                    y=int(input("Enter new team: "))
                    i[2]=y

                elif x==4:
                    y=int(input("Enter new age: "))
                    i[3]=y

                elif x==5:
                    y=input("Enter new points per game: ")
                    i[4]=y

                elif x==6:
                    y=input("Enter new rebounds per game: ")
                    i[5]==y

                elif x==7:
                    y=int(input("Enter new assists per game: "))
                    i[6]=y

                elif x==8:
                    y=int(input("Enter new blocks per game : "))
                    i[7]=y

                elif x==9:
                    y=input("Enter new steals per game : ")
                    i[8]=y

                else:
                    print("Enter valid number")

                ch=input("Do you want to continue?? (y/n)")
                if ch.lower()=='n':
                    break
    if found==0:
        print("Record not found")       
    f.close()

main()