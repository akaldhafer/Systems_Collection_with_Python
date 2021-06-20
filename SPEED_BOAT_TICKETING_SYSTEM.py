#Name: Abdulmalek Aldhafer
#GitHub username: akaldhafer
#Email: Ak_aldhafer@hotmail.com
#System title: SPEED BOAT TICKETING  SYSTEM 

#import extra header files
import datetime
import os #to use pause and cls clean screen
import json
#my list for business class
BCS = ["B1", "B2", "B3", "B4"]
#my list for economy class
ECS = ["E1","E2","E3","E4","E5","E6","E7","E8"]
#my list for the avaiable time
Time = ["08:00am", "10:00am", "12:00noon", "14:00pm"]
#my list for the boat id
BoatID = ["B01", "B02", "B03", "B04", "B05", "B06", "B07", "B08", "B09", "B10"]
#my list for the ticket type
TicketType = ["BUSINESS CLASS", "ECONOMY CLASS"]

def MainMenu():
    create = open("TicketRecord.txt", "a+")
    create.close()
    print("\n\n============ WELCOME TO SPEED BOAT TICKETING  SYSTEM ============")
    print("         ========= PLEASE CHOOSE YOUR OPTION ========")
    print("P. PURCHASING SPEED BOAT TICKET")
    print("V. VIEW SEATING ARRANGEMENT")
    print("Q. QUIT SYSTEM")
    choice=input("PLEASE ENTER YOUR OPTION:")
    if choice=="P" or choice=="p":
        SelectSeat()       
    elif choice=="V" or choice=="v":
        print("PROCEED TO VIEW SEATING ARRANGEMENT PHRASE")
        ViewBoatRecord()
    elif choice=='Q' or choice=='q':
        print("========== EXIT FROM SYSTEM ==========")
        exit()
    else:
        print("ERROR:OPTION NOT FOUND")
    os.system("PAUSE")#waiting the user input 
    os.system("CLS")#clean screen 
    MainMenu()
def SelectSeat():
    while True:
        #selecting the ticket type
        print("\n\n========= PURCHASING PHRASE =========")
        print("1. PURCHASE BUSINESS CLASS TICKET\n2. PURCHASE ECONOMY CLASS TICKET\n3. RETURN MAIN MENU")
        choice1=input("ENTER ONE OPTION: ")
        if choice1=="1":
            myTicketType = TicketType[0]
            print("\n  BUSINESS CLASS SELECTED\n")
            print("1. ", BCS[0], "2. ", BCS[1])
            print("3. ", BCS[2], "4. ", BCS[3])
            Seat = input("\nChoose your seat: ")
            if Seat == "1":
                Myseat = BCS[0]
            elif Seat == "2":
                Myseat = BCS[1]
            elif Seat == "3":
                Myseat = BCS[2]
            elif Seat == "4":
                Myseat = BCS[3]
            else:
                print("Wrong option")
                os.system("PAUSE")#waiting the user input 
                os.system("CLS")#clean screen 
                SelectSeat()
            #selecting the Boat ID
            print("\n SELECT THE BOAT ID")
            print("1. ", BoatID[0], "\t2. ", BoatID[1])
            MyBID = input("Select the Boat ID: ")
            if MyBID == "1":
                BID = BoatID[0]
            elif MyBID == "2":
                BID = BoatID[1]
            else:
                print("ERROR: OPTION NOT FOUND")
                os.system("PAUSE")#waiting the user input 
                os.system("CLS")#clean screen 
                SelectSeat()
        elif choice1=="2":
            myTicketType = TicketType[1]
            print("\n  ECONOMY CLASS SELECTED\n")
            print("1. ", ECS[0], "\t2. ", ECS[1], "\t3. ", ECS[2], "\t4. ", ECS[3])
            print("5. ", ECS[4], "\t6. ", ECS[5], "\t7. ", ECS[6], "\t8. ", ECS[7])
            Seat = input("\nChoose your seat: ")
            if Seat == "1":
                Myseat = ECS[0]
            elif Seat == "2":
                Myseat = ECS[1]
            elif Seat == "3":
                Myseat = ECS[2]
            elif Seat == "4":
                Myseat = ECS[3]
            elif Seat == "5":
                Myseat = ECS[4]
            elif Seat == "6":
                Myseat = ECS[5]
            elif Seat == "7":
                Myseat = ECS[6]
            elif Seat == "8":
                Myseat = ECS[7]
            else:
                print("\n  Wrong option  !!\n")
                os.system("PAUSE")#waiting the user input 
                os.system("CLS")#clean screen 
                SelectSeat()
            #selecting the Boat ID
            print("\n SELECT THE BOAT ID")
            print("1. ", BoatID[2], "\t2. ", BoatID[3], "3. ", BoatID[4], "4. ", BoatID[5])
            print("5. ", BoatID[6], "\t6. ", BoatID[7], "7. ", BoatID[8], "8. ", BoatID[9])
            MyBID = input("Select the Boat ID: ")
            if MyBID == "1":
                BID = BoatID[2]
            elif MyBID == "2":
                BID = BoatID[3]
            elif MyBID == "3":
                BID = BoatID[4]
            elif MyBID == "4":
                BID = BoatID[5]
            elif MyBID == "5":
                BID = BoatID[6]
            elif MyBID == "6":
                BID = BoatID[7]
            elif MyBID == "7":
                BID = BoatID[8]
            elif MyBID == "8":
                BID = BoatID[9]
            else:
                print("ERROR: OPTION NOT FOUND")
                os.system("PAUSE")#waiting the user input 
                os.system("CLS")#clean screen 
                SelectSeat()
        elif choice1=="3":
            print("RETURN TO MAIN INTERFACE\n")
            os.system("PAUSE")#waiting the user input 
            os.system("CLS")#clean screen 
            MainMenu()
        else:
            print("ERROR: OPTION NOT FOUND")
            os.system("PAUSE")#waiting the user input 
            os.system("CLS")#clean screen 
            SelectSeat()
        #selecting the time
        print("\n SELECT THE TIME")
        print("1. ", Time[0], "\t\t2. ", Time[1], "\n3. ", Time[2],"\t\t4. ", Time[3])
        time = input("\nSelect the wanted time: ")
        if time == "1":
            Mytime = Time[0]
        elif time == "2":
            Mytime = Time[1]
        elif time == "3":
            Mytime = Time[2]
        elif time == "4":
            Mytime = Time[3]
        else:
            print("Wrong option !!")
            os.system("PAUSE")#waiting the user input 
            os.system("CLS")#clean screen 
            SelectSeat()
        #defining the date
        Mydate = str(datetime.date.today())
        #getting the customer info
        print("\nPlease fill up the customer details: ")
        Myname = input("\nEnter customer name: ")
        ensure = input("\nDo you want to ensure the purchase(1.Yes 2. NO):  ")
        if ensure == "2":
            SelectSeat()
        else:
            #the record details to be stored
            myRecord= [BID, myTicketType, Myseat, Mytime, Mydate, Myname]
            #checking weather the seat still avaiable or not
            myf = open("TicketRecord.txt", "r")
            lines = myf.readlines()
            #Check each line by line from the text file
            back = 0
            for line in lines:
                my = json.loads(line)
                if (my[0] == BID and my[2] == Myseat and my[3] == Mytime and my[4] == Mydate): #comparing the seat to define weather the seat if avaiable in the file or not
                    back = 1
                    break
            myf.close() 
            if back == 1:
                print('\033[91m' + " The seat is not avaiable, please choose new one !" + '\033[0m')
                SelectSeat()

            #The list is converted to json for easier reading
            TicketRecord = json.dumps(myRecord)
            f = open("TicketRecord.txt", "a")
            f.writelines(TicketRecord)
            f.writelines("\n")
            f.close()
            #printing the ticket detials
            print("""\n\n                                 <><>  THE TICKET DETAILS  <><>
            ****************************************************************************
            * Boat ID: """, BID, """        Date: """,Mydate, """ \t\t\tTime: """,Mytime, """     
            ****************************************************************************
            *""", myTicketType,"""                                                     
            ****************************************************************************
            * Seat ID""", Myseat,"""                                                    
            ****************************************************************************
            * Customer Name: """, Myname, """                                           
            ****************************************************************************
            * Note: Please keep the ticket with you                                    *\n\n""")
def ViewBoatRecord():
    view = input("""              The Avaiable Boats 
    B01 , B02 , E03 , E04, E05 , E06, E07, E08 , E09 ,E10
    Enter Which Boat you want to view(Ex: B01): """)
    f2 = open("TicketRecord.txt", "r+")
    lines = f2.readlines()
    if (not len(lines)):
        print("No records found...")
        MainMenu()
    print("BID\t\tTicket Type\t\tSeat ID\t\tTime\t\tDate\t\tCustomer Name")
    #Check each line by line from the text file
    for line in lines:
        myRecord = json.loads(line)
        if (myRecord[0] == view):          #If the entered BID matches the BID of a line, it prints the result
            print(str(myRecord[0]) + "\t\t" + str(myRecord[1]) + "\t\t" + str(myRecord[2]) + "\t\t" + str(myRecord[3]) + "\t\t" + str(myRecord[4])+ "\t\t" + str(myRecord[5]))
    f2.close() 

#calling the main menu to run
MainMenu()
