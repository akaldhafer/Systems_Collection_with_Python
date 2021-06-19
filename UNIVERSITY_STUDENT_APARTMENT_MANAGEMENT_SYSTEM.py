#Name: Abdulmalek Aldhafer
#GitHub username: akaldhafer
#Email: Ak_aldhafer@hotmail.com
#System title: UNIVERSITY STUDENT APARTMENT MANAGEMENT SYSTEM

import math 
#recode variables
global sname
global stp
global sphone
global room
global Singal
global master
global paid
global unpaid
global TotalPayment
global sdate
global F1
global F2
global F3
global Netfee
global Deposit
global RoomFee
#database
F1 = "Laundry"
F2 = "Kitchen"
F3 = "Internet"
#list for block A single room
BlockA =[['A1R1 ','A1R2 ','A2R1 ','A2R2','A3R1 '], 
        ['A3R2 ','A4R1 ','A4R2 ','A5R1 ', 'A5R2'],
        ['A6R1 ','A6R2 ','A7R1 ','A7R2','A8R1 '],
        ['A8R2 ','A9R1 ','A9R2 ','A10R1 ', 'A10R2 '],
        ['A11R1 ','A11R2 ','A12R1 ','A12R2','A13R1 '],
        ['A13R2 ','A14R1 ','A14R2 ','A15R1 ', 'A15R2 '],
        ['A16R1 ','A16R2 ','A17R1 ','A17R2','A18R1 '],
        ['A18R2 ','A19R1 ','A19R2 ','A20R1 ', 'A20R2 ']]

Single = "Single"
master = "Master"
BlockBS =[['B1R2 ','B1R3 ','B2R2 ','B2R3 '], #list for block B single rooms
         ['B3R2 ','B3R3 ','B4R2 ','B4R3 '],
         ['B5R2 ','B5R3 ','B6R2 ','B6R3 '],
         ['B7R2 ','B7R3 ','B8R2 ','B8R3 '],
         ['B9R2 ','B9R3 ','B10R2 ','B10R3 '],
         ['B11R2 ','B11R3 ','B12R2 ','B12R3 '],
         ['B13R2 ','B13R3 ','B14R2 ','B14R3 '],
         ['B15R2 ','B15R3 ','B16R2 ','B16R3 '],
         ['B17R2 ','B17R3 ','B18R2 ','B18R3 '],
         ['B19R2 ','B19R3 ','B20R2 ','B20R3 ']]

BlockBM =[['B1RM ','B2RM '], #list for block B master rooms
         ['B3RM ','B4RM '],['B5RM ','B6RM '],['B7RM ','B8RM '],
         ['B9RM ','B10RM '],['B11RM ','B12RM '],['B13RM ','B14RM '],
         ['B15RM ','B16RM '],['B17RM ','B18RM '],['B19RM ','B20RM ']]


#***********************************************************
print("===========================================================")
print("Welcome to UNIVERSITY STUDENT APARTMENT MANAGEMENT SYSTEM =")
print("===========================================================")




def Book(): #book room function
    with open("student.txt", "a") as studentf: #opening file as appending mode
                print("***********************************************************")
                print("*Booking Menu                                             *")
                print("1. Book single room in Block A.                           *")
                print("2. Book single room in Block B.                           *")
                print("3. Book master room in Block B.                           *")
                print("4. Return to the main menu.                               *")                                    
                print("***********************************************************")
                optionb = input("Enter your option: ")#Read user input
                if(optionb == '1'):
                            print("These are all the available single rooms in block A")
                            print(BlockA) #display block A list
                            room = input("Enter your room number(Ex.A1R1): ")
                            print("Wuold you to add internet service (50Rm monthly)")
                            print("1. Yes \n2. No")
                            netoption = input("Enter your option: ")
                            if(netoption == '1'):
                                    Netfee = 50
                            else:
                                Netfee = 0
                            print("Please fill up the student details: ")
                            #get student details
                            sname = input("Enter student name: ")
                            stp = input("Enter student TP No: ")
                            sphone = input("Enter student Phone No: ")
                            sdate = input("Enter starting date: ")
                            Deposit = 100
                            RoomFee = 400
                            TotalPayment = (Netfee*5)+(RoomFee*5)+Deposit
                            print("*****         The receipt           ****")
                            print("Room type           : ", Single)
                            print("Room No             : ", room)
                            print("student TP(e:012345): ", stp)
                            print("student name        : ",sname)
                            print("student phone No    : ", sphone)
                            print("Starting date       : ", sdate)
                            print("available facility 1: ", F1)
                            print("available facility 2: ", F2)
                            print("available facility 3: ", F3)
                            print("Internet fees       : ", Netfee)
                            print("Facility Deposit fee: ", Deposit)
                            print("Room monthly rent   : ", RoomFee)
                            print("The total payment   : ", TotalPayment)
                            unpaid = TotalPayment
                            print("What type of payment you prefer: ")
                            print("1. Pay partial amount(at least 50%).\n2. Pay full amount.")
                            payoption = input("Enter one choice: ")
                            if(payoption == '1'):
                                 cost = TotalPayment/2
                                 paid = int(input("Enter your payment: "))
                                 while(paid < cost):
                                      paid = int(input("Enter your payment: "))                                        
                            else:
                                paid = int(input("Enter your payment: "))
                            unpaid = paid-unpaid
                            print("The paid amount     : ", paid)
                            print("The unpaid amount   : ", unpaid)        
                            studentf.write(stp)
                            studentf.write('  RoomType: %s ' %Single)            
                            studentf.write('RoomNo: %s ' %room)
                            studentf.write('Name: %s ' %sname)
                            studentf.write('PhoneNO: %s ' %sphone)
                            studentf.write('Date: %s ' %sdate)
                            studentf.write('F1: %s ' % F1)
                            studentf.write('F2: %s ' % F2)
                            studentf.write('F3: %s ' % F3)
                            studentf.write('Deposit: %d ' % Deposit)
                            studentf.write('RoomFee: %d  ' % RoomFee)
                            studentf.write('NetFee: %d  ' % Netfee)
                            studentf.write('TotalPayment: %d  ' % TotalPayment)
                            studentf.write('paid: %d  ' % paid)
                            studentf.write('unpaid: %d  ' % unpaid)
                            studentf.write(" \n")
                            studentf.close()
                            print(" !!! The recode has been saved successfully!!!")
                            
                elif(optionb == '2'):
                            print("These are all the available Master and single rooms in block B")
                            print(BlockBS)
                            room = input("Enter your the room number(Ex.B1R2): ")
                            print("Wuold you to add internet service (40Rm monthly)")
                            print("1. Yes \n2. No")
                            netoption = input("Enter your option: ")
                            if(netoption == '1'):
                                    Netfee = 40
                            else:
                                Netfee = 0
                            print("Please fill up the student details: ")
                            sname = input("Enter student name: ")
                            stp = input("Enter student TP No: ")
                            sphone = input("Enter student Phone No: ")
                            sdate = input("Enter starting date: ")
                            
                            Deposit = 100
                            RoomFee = 300
                            TotalPayment = (Netfee*5)+(RoomFee*5)+Deposit
                            print("*****         The receipt           ****")
                            print("Room type           : ", Single)
                            print("Room No             : ", room)
                            print("student Tp          : ", stp)
                            print("student name        : ",sname)
                            print("student phone No    : ", sphone)
                            print("Starting date       : ", sdate)
                            print("available facility 1: ", F1)
                            print("available facility 2: ", F2)
                            print("available facility 3: ", F3)
                            print("Internet fees       : ", Netfee)
                            print("Facility Deposit fee: ", Deposit)
                            print("Room monthly rent   : ", RoomFee)
                            print("The total payment   : ", TotalPayment)
                            unpaid = TotalPayment
                            print("What type of payment you prefer: ")
                            print("1. Pay partial amount(at least 50%).\n2. Pay full amount.")
                            payoption = input("Enter one choice: ")
                            if(payoption == '1'):
                                 cost = TotalPayment/2
                                 paid = int(input("Enter your payment: "))
                                 while(paid < cost):
                                      paid = int(input("Enter your payment: "))                                        
                            else:
                                paid = int(input("Enter your payment: "))
                            unpaid = paid-unpaid
                            print("The paid amount     : ", paid)
                            print("The unpaid amount   : ", unpaid)        
                            studentf.write(stp)
                            studentf.write('  RoomType: %s ' %Single)            
                            studentf.write('RoomNo: %s ' %room)
                            studentf.write('Name: %s ' %sname)
                            studentf.write('PhoneNO: %s ' %sphone)
                            studentf.write('Date: %s ' %sdate)
                            studentf.write('F1: %s ' % F1)
                            studentf.write('F2: %s ' % F2)
                            studentf.write('F3: %s ' % F3)
                            studentf.write('Deposit: %d ' % Deposit)
                            studentf.write('RoomFee: %d  ' % RoomFee)
                            studentf.write('NetFee: %d  ' % Netfee)
                            studentf.write('TotalPayment: %d  ' % TotalPayment)
                            studentf.write('paid: %d  ' % paid)
                            studentf.write('unpaid: %d  ' % unpaid)
                            studentf.write(" \n")
                            studentf.close()
                            print(" !!! The recode has been saved successfully!!!")
                elif(optionb == '3'):
                            print("These are all the available Master and single rooms in block B")
                            print(BlockBM)
                            room = input("Enter your the room number(Ex.B1R2): ")
                            print("Wuold you to add internet service (40Rm monthly)")
                            print("1. Yes \n2. No")
                            netoption = input("Enter your option: ")
                            if(netoption == '1'):
                                    Netfee = 40
                            else:
                                Netfee = 0
                            print("Please fill up the student details: ")
                            sname = input("Enter student name: ")
                            stp = input("Enter student TP No: ")
                            sphone = input("Enter student Phone No: ")
                            sdate = input("Enter starting date: ")
                            
                            Deposit = 100
                            RoomFee = 500
                            TotalPayment = (Netfee*5)+(RoomFee*5)+Deposit
                            print("*****         The receipt           ****")
                            print("Room type           : ", master)
                            print("Room No             : ", room)
                            print("student Tp          : ", stp)
                            print("student name        : ",sname)
                            print("student phone No    : ", sphone)
                            print("Starting date       : ", sdate)
                            print("available facility 1: ", F1)
                            print("available facility 3: ", F3)
                            print("Internet fees       : ", Netfee)
                            print("Facility Deposit fee: ", Deposit)
                            print("Room monthly rent   : ", RoomFee)
                            print("The total payment   : ", TotalPayment)
                            unpaid = TotalPayment
                            print("What type of payment you prefer: ")
                            print("1. Pay partial amount(at least 50%).\n2. Pay full amount.")
                            payoption = input("Enter one choice: ")
                            if(payoption == '1'):
                                 cost = TotalPayment/2
                                 paid = int(input("Enter your payment: "))
                                 while(paid < cost):
                                      paid = int(input("Enter your payment: "))                                        
                            else:
                                paid = int(input("Enter your payment: "))
                            unpaid = paid-unpaid
                            print("The paid amount     : ", paid)#saving the data
                            print("The unpaid amount   : ", unpaid)        
                            studentf.write(stp)
                            studentf.write('  RoomType: %s ' %master)            
                            studentf.write('RoomNo: %s ' %room)
                            studentf.write('Name: %s ' %sname)
                            studentf.write('PhoneNO: %s ' %sphone)
                            studentf.write('Date: %s ' %sdate)
                            studentf.write('F1: %s ' % F1)
                            studentf.write('F3: %s ' % F3)
                            studentf.write('Deposit: %d ' % Deposit)
                            studentf.write('RoomFee: %d  ' % RoomFee)
                            studentf.write('NetFee: %d  ' % Netfee)
                            studentf.write('TotalPayment: %d  ' % TotalPayment)
                            studentf.write('paid: %d  ' % paid)
                            studentf.write('unpaid: %d  ' % unpaid)
                            studentf.write("\n")
                            studentf.close()
                            print(" !!! The recode has been saved successfully!!!")
                            
                else:
                    print("-----------------------------------------------------------")
                f = open("Totalpaid.txt","a") #opening as appending mode
                Tpaid = paid-Deposit #calculate the paid amount without the deposit
                f.write('%d\n' % Tpaid) #writing the paid amount into the file
                f.close()#close the file
                
                f2 = open("Deposit.txt","a")#opening as appending mode
                f2.write('%d\n' % Deposit)#writing the deposit amount into the file
                f2.close()#close the file
                
                f3 = open("TotalUnpaid.txt","a")#opening as appending mode
                f3.write('%d\n' % unpaid)#writing the unpaid amount into the file
                f3.close()#close the file
                
                
def SearchByTP(): #search student recode by tp
    print("***********************************************************")
    print("*Search by TP NO                                          *")
    data = str(input("Enter Student TP(e:12345): "))# get student TP
    flag = 0
    myfile = open("student.txt", "r")# open as reading mode
    for line in myfile: #read line by line
            line = line.rstrip()
            if(line.startswith(data)): #if the line start the the TP
                        flag = 1
                        print("Recode found !!")
                        print(line)#displaying the student recode
    if(flag == 1):
                print("-------------------------------------------------")
    else:
                print("TP Not Found!")
    myfile.close()#close the file
                                                                       
      
def Display(): #display payment function
    print("***********************************************************")
    print("*Display Payment Menu                                     *")
    print("1. Total deposit collecte.                                *")
    print("2. Total amount collected excluding the deposit.          *")
    print("3. Total amount receivable from the students.             *")
    print("4. return to the main menu.                               *")
    op = input("Enter your option: ") #get user input
    if(op == '1'):
                dep = 0
                f1 = open("Deposit.txt","r")#opening as reading mode
                for line in f1:#to go through all lines inside the file
                            num =  int(line)#assign the value in the line to num
                            dep += num #add the assigned value to the total
                print("Total deposit: ", dep)
                f1.close()#close the file 
                
    elif(op == '2'):
                Tmade = 0
                f2 = open("Totalpaid.txt","r")#opening as reading mode
                for line in f2:#to go through all lines inside the file
                            num =  int(line)#assign the value in the line to num
                            Tmade += num #add the assigned value to the total
                print("Total paid: ", Tmade)
                f2.close() #close the file               

    elif(op == '3'):
                Tunmade = 0 #create variable to store the unpaid payment
                f3 = open("TotalUnpaid.txt","r") #opening as reading mode
                for line in f3: #to go through all lines inside the file
                            num =  int(line) #assign the value in the line to num
                            Tunmade += num #add the assigned value to the total
                print("Total unpaid: ", Tunmade) #display the total unpaid
                f3.close()#close the file 
    else:
        print("***********************************************************")

                
def Echeck():
    print("***********************************************************")
    print("*Early check out")
    Sname = input("Enter student TP: ")
    flag = 0
    myfile = open("student.txt", "r") #open on reading mode
    for line in myfile:
            line = line.rstrip()
            if(line.startswith(Sname)):# if the line srart with the given TP
                        flag = 1
                        print("Recode found !!")
                        print(line)
    if(flag == 1):
                print("-------------------------------------------------")
    else:
                print("TP Not Found!")
                main()
    myfile.close()
    Smonths = int(input("Enter staying months: "))
    SroomPrice = int(input("Enter room price: "))
    Snet = int(input("Enter net price(zero if the student does use Net): "))
    Total = 0
    Total = (Snet*Smonths)+(SroomPrice*Smonths)
    print("The total payment without the deposit: ", Total)
    made = int(input("Enter the paid payment: "))
    unpaid = Total -(made-100)
    print("The unpaid amount: ", unpaid)  
    while(unpaid != 0):# while the unpaid is not equal to zero
                paid = int(input("Enter the payment: "))
                unpaid = unpaid-paid
                print("The unpaid amount: ", unpaid)
    print("You have checked-out successfully!!! ") 
    f = open("Totalpaid.txt","a") #saving the paid amount 
    Tpaid = paid
    f.write('%d\n' % Tpaid)
    f.close()
    #deleting the recode from the orginal file
    fn = 'student.txt' 
    f = open(fn)
    output = [] #list to store the line data
    for line in f:
        if not line.startswith(Sname):
            output.append(line)#store all the data into the list except the
    f.close()                  #needed recode to be deleted 
    f = open(fn, 'w')
    f.writelines(output) #rewriting the saved data from the list
    f.close()
    


def menu():       
    print("***********************************************************")
    print("*Main Menu                                                *")
    print("1. Book a room.                                           *")
    print("2. Display total payment.                                 *")
    print("3. Search student's recode.                               *")
    print("4. Early Check-Out.                                       *")
    print("5. Quit the system.                                       *")
    print("***********************************************************")
    
#starting the program
def main():  #declaring the text files
    f1 = open("student.txt","a") #opening as appending mode
    f1.close()#close the file 
    f = open("Totalpaid.txt","a") #opening as appending mode
    f.close()#close the file  
    f2 = open("Deposit.txt","a")#opening as appending mode
    f2.close()#close the file
    f3 = open("TotalUnpaid.txt","a")#opening as appending mode
    f3.close()#close the file
    while True:#the while true will stay repeating the menu 
      menu()#calling the system menu         
      m=input("Enter your chocie: ") # for menu options
      if(m == '1'):
            Book()#calling register menu 
      elif(m == '2'):
            Display()#calling display menu     
      elif(m == '3'):
            SearchByTP()#calling search function 
      elif(m == '4'):
            Echeck() #calling check out function
      elif(m == '5'):
            exit() #exit from the program
      else:
          print("!!! You have chosen a wrong option  !!!")
main()
