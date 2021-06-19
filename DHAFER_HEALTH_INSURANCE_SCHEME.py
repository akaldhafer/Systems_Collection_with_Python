#Name: Abdulmalek Aldhafer
#GitHub username: akaldhafer
#Email: Ak_aldhafer@hotmail.com
#System title: MEDILIFE HELATH INSURANCE SCHEME

from datetime import date
d = open('Patients.txt', "a")
d.close() 
d2 = open('HospitalRecord.txt', "a")
d2.close() 

def Welcome():
        print('_________________________________________________________________________________')
        print('-********************* DHAFER HEALTH INSURANCE SCHEME ************************-')
        print('1) Register new patient')
        print('2) Patient Claim Options')
        print('3) Search for Patients')
        print('4) View Hospital Records')
        print('0) Quit')
        CheckInput = str(input('Choose your Option: '))
        if(CheckInput == '1'):
                Registeration()
        elif(CheckInput == '2'):
                Hospitlization()
        elif(CheckInput == '3'):
                SearchPatients()
        elif(CheckInput == '4'):
                HospitalRecordsPrinting()
        elif(CheckInput == '0'):
                exit()
        else:
                input('Wrong input Try again (Click Enter)')
                Welcome()
def HospitalRecordsPrinting():
        
        print('*************************************************************************************************')
        print('1) Total amount claimed by Lifetime Claim Limit subscribers')
        print('2) Total number of Annual Claim Limit subscribers who have exhausted Their Balance')
        print('3) Print all Hospital records')
        print('0) Back')
        while True:                 
                try:
                        Pick = int(input('Choose your option: '))
                        if 0 > Pick or Pick > 3:
                            
                                print("Wrong Input!.")
                                continue
                except ValueError:
                        print("Wrong Input!.")
                        continue
                else:
                            
                        if(Pick == 1):
                                TotalAmount = 0
                                f = open('HospitalRecord.txt')
                                for line in f:
                                        if('Lifetime' in line):
                                                A,B,C,D,F,G,K,L,M,N,O,X,Fees,Z,J = line.split()
                                                TotalAmount = TotalAmount + int(Fees)
                                print('The total amount claimed by lifetime claim is: '+str(TotalAmount))
                                input('Click Enter to go back')
                                f.close()
                                HospitalRecordsPrinting()
                                
                        elif(Pick == 2):
                                Countexhausted =0
                                f = open('Patients.txt')
                                for line in f:
                                        if('Annual' in line):
                                                if('exhausted' in line):
                                                        Countexhausted = Countexhausted +1
                                print('The total exhausted Annual claims balance: '+str(Countexhausted))
                                input('Click Enter to go back')
                                f.close()
                                HospitalRecordsPrinting()
                                
                        elif(Pick == 3):
                                print('Record ID -PatientID -Name -PlanType -ClaimType -RoomDays -RoomFees -ICUDays -ICUFees -HospitalSuppliesandServices -SurgicalFees -OtherFees -TotalClaimed -BfrBalance -afterbalance')
                                f = open('HospitalRecord.txt')
                                for line in f:
                                        print(line)
                                f.close()
                                input('Click Enter to go back')
                                HospitalRecordsPrinting()
                        elif(Pick == 0):
                                Welcome()
                        break
def SearchPatients():
        print('******************************************************************')
        print('Search for patients')
        print('1) Search with ID.')
        print('2) Search with Age.')
        print('3) Search with Plan.')
        print('4) Search with Claim limit Type.')
        print('0) Back')
        print('__________________________________________________________________')
        while True:         
                    try:
                            Searching = int(input('Choose your option: '))
                            if 0 > Searching or Searching > 4:
                                    print("Wrong Input!.")
                                    continue
                    except ValueError:
                            print("Wrong Input!.")
                            continue
                    else:
                            global Patient
                            global Searchingg
                            if(Searching == 1 ):
                                    Patient = int(input('Enter patient ID : '))
                                    Searchingg = 0
                            if(Searching ==2):
                                    Patient= int(input('Enter Patient Age : '))
                                    Searchingg = 1
                            if(Searching ==3):
                                    print('1) Plan150 ')
                                    print('2) Plan200 ')
                                    print('3) Plan300 ')
                                    Plan = int(input('Choose the plan: '))
                                    Searchingg = 3
                                    if(Plan == 1):
                                        
                                            Patient= 'Plan150'
                                    elif(Plan == 2):      
                                            Patient= 'Plan200'
                                    elif(Plan == 3):      
                                            Patient= 'Plan300'
                            if(Searching ==4):
                                    print('1) Annual Claim Limit ')
                                    print('2) Lifetime  Claim Limit ')
                                    Plan = int(input('Choose the plan: '))
                                    Searchingg = 2
                                    if(Plan == 1):      
                                            Patient= 'Annual'
                                    elif(Plan == 2):
                                          
                                            Patient= 'Lifetime'
                            if(Searching == 0):
                                    Welcome()
                            break
       
        SearchingForPatient() 
def SearchingForPatient():
        print('*************************************************************************************************')
        f = open('Patients.txt')
        Count =1
        for line in f:
                FindIDD,FindnameE,FindAddressS,FindPhoneE,FindAgeE,FindChoosenPlanN,FindChoosenClaimM,FindBalanceE = line.split()
                if(str(Patient)== FindIDD and Searchingg == 0):
                        
                        print(line)
                        Count = 0
                if(str(Patient) == FindAgeE and Searchingg == 1):
                        print(line)
                        Count = 0
                        input('Click Enter to go back')
                        SearchPatients()
                if(Searchingg == 2 and str(Patient)== FindChoosenClaimM):
                        print(line)
                        Count = 0
                        input('Click Enter to go back')
                        SearchPatients()
                if(Searchingg == 3 and str(Patient)== FindChoosenPlanN):
                        print(line)
                        Count = 0
                        input('Click Enter to go back')
                        SearchPatients()
                elif(Count == 1):
                        print('Sorry There is no records')
                        input('Click Enter to try again')
                        SearchPatients()
        f.close()
def Hospitlization():
        print('-*********************************************************************************************-')
        print('Hospitalisation and Surgical Benefits ')
        print('Plans>                                                  Plan150         Plan200         Plan300')
        print('_______________________________________________________________________________________________')
        print('Room Charges >                                          150/Day         200/Day         300/Day')
        print('_______________________________________________________________________________________________')
        print('Intensive Care Unit (ICU) Charges >                     300/Day         500/Day         900/Day')
        print('_______________________________________________________________________________________________')
        print('Hospital Supplies and Services                                                                 ')
        print('Surgical Fees                         As charged. Subject to approval by EZMediLife            ')
        print('Other Fees                                                                                     ')
        print('_______________________________________________________________________________________________')
        print('-*********************************************************************************************-')
        global SearchID
        SearchID= int(input('Enter Patient ID: '))
        FindData()
        print('Name: '+Findname+'_ Age: '+FindAge)
        print('Plan: '+FindChoosenPlan+'_ Plan Type: '+FindChoosenClaim)
        print('Balance: '+FindBalance)
        if(FindBalance == 'exhausted'):
                print('Your balance is exhausted or it has been fully claimed')
                input('Click enter to go back to the main menu')
                Welcome()
        global RoomFees
        CheckRoom = input('Would you like to have a room?(Yes/No): ')
        if CheckRoom == 'Yes' or CheckRoom == 'yes':
                global RoomDays
                while True:         
                    try:
                            RoomDays = int(input('For how many days would like to claim? '))
                            if 1 > RoomDays :
                                    
                                    print("Wrong Input!.")
                                    continue
                    except ValueError:
                            print("Wrong Input!.")
                            continue
                    else:
                            
                            if(FindChoosenPlan == 'Plan150'):
                                    RoomFees=RoomDays * 150
                            if(FindChoosenPlan == 'Plan200'):
                                    RoomFees=RoomDays * 200
                            if(FindChoosenPlan == 'Plan300'):
                                    RoomFees= RoomDays * 300
                            if(RoomFees > int(FindBalance)):
                                    print('You have exceed your balance!')
                                    continue
                            break
                
        else:
                RoomFees = 0
                RoomDays = 0
        
        CheckICU = input('Would you like to have a Intensive Care Unit (ICU)?(Yes/No): ')
        global ICUFees
        ICUFees = 0
        global ICUDays
        ICUDays = 0
        if CheckICU == 'Yes' or CheckICU == 'yes':
                while True:         
                    try:
                            ICUDays = int(input('For how many days would like to claim?: '))
                            if 1 > ICUDays :
                                    
                                    print("Wrong Input!.")
                                    continue
                    except ValueError:
                            print("Wrong Input!.")
                            continue
                    else:
                            
                            if(FindChoosenPlan == 'Plan150'):
                                    ICUFees= ICUDays * 300
                            if(FindChoosenPlan == 'Plan200'):
                                    ICUFees= ICUDays * 500
                            if(FindChoosenPlan == 'Plan300'):
                                    ICUFees= ICUDays * 900
                            Total = RoomFees + ICUFees    
                            if(Total > int(FindBalance)):
                                    print('You have exceed your balance!')
                                    
                                    continue     
                            break
                                
                    
        else:
                ICUFees = 0
                ICUDays = 0
        global HSSF,SF,Others,TotalFees 
        global Change
        while True:         
                    try:
                            
                            HSSF = int(input('Hospital Supplies and Services Fees (RM): '))
                            if 0 > HSSF :
                                    
                                    print("Wrong Input!.")
                                    continue
                    except ValueError:
                            
                            print("Wrong Input!.")
                            continue
                    else:
                            break
        while True:         
                    try:
                            SF = int(input('Surgical Fees  (RM): '))
                            if 0 > SF :
                                    print("Wrong Input!.")
                                    continue
                    except ValueError:
                            print("Wrong Input!.")
                            continue
                    else:
                            break
        while True:         
                    try:
                            Others = int(input('Others(RM): '))
                            if 0 > Others :
                                    print("Wrong Input!.")
                                    continue
                    except ValueError:
                            print("Wrong Input!.")
                            continue
                    else: 
                            break
        print('-*********************************************************************************************-')
        print('Room Charges (Days = '+str(RoomDays)+') Fees('+str(RoomFees)+').')
        print('Intensive Care Unit (ICU) Charges (Days = '+str(ICUDays)+') Fees('+str(ICUFees)+').')
        print('Surgical Fees  (RM):'+str(SF))
        print('Others (RM): '+str(Others))
        print('________________________________________________________________________________________________')
        TotalFees= RoomFees+ICUFees+HSSF+SF+Others
        print('Total Charged RM: ' + str(TotalFees))            
        print('Your balance is '+FindBalance)
        Change = int(FindBalance) - TotalFees
        print('Balance after claim RM: '+ str(Change))
        print()
        CheckPayment= input('Would like to confirm your claim?(Yes/No): ')
        if CheckPayment == 'yes' or CheckPayment == 'Yes':
                if(int(FindBalance) < int(TotalFees)):
                        print('No enough Balance!!')
                        input('Try again!!(Click Enter)')
                        Hospitlization()
                else:
                        WriteBackData()
                        HopitalFile()
                print
        elif(CheckPayment == 'no' or CheckPayment == 'No'):
                print('ok')
                Welcome()
        else:
                print('Wrong input! Try Again(Click Enter)')
                input()
def Register():
        with open('Patients.txt', 'a') as the_file:
            ID=0
            with open('Patients.txt', 'r') as f:                
                for line in f:
                    
                    ID += 1
            ID = ID+ 1
            the_file.write(str(ID)+' '+name+' '+Address+' '+str(Phone)+' '+str(Age)+' '+ChoosenPlan+' '+ChoosenClaim+' '+Balance+'\n')
            print('Success!!')
            print('Thanks '+name+' For registering in ""')
            print('Your ID is: '+str(ID))
            print('Your is plan is :'+ChoosenPlan+' And your Claim type is: '+ChoosenClaim)
            input('Click Enter to go back to main menu')
            the_file.close()
            Welcome()
def FindData():    
    f = open('Patients.txt', "r")
    finput=''
    inte = SearchID - 1
    finput = f.readlines()
    the_string = finput[inte]
    global FindID,Findname,FindAddress,FindPhone,FindAge,FindChoosenPlan,FindChoosenClaim,FindBalance
    FindID,Findname,FindAddress,FindPhone,FindAge,FindChoosenPlan,FindChoosenClaim,FindBalance = the_string.split()
def WriteBackData():
    with open('Patients.txt', 'w') as the_file:
        
        global Change
        if(Change == 0):
            Change = 'exhausted'
        the_file.seek(int(FindID))
        the_file.write(FindID+' '+Findname+' '+FindAddress+' '+FindPhone+' '+FindAge+' '+FindChoosenPlan+' '+FindChoosenClaim+' '+str(Change)+'\n')
def HopitalFile():
        with open('HospitalRecord.txt', 'a') as the_file:
            RecordID=0
            with open('HospitalRecord.txt', 'r') as f:                
                for line in f:
                    
                    RecordID += 1
            RecordID = RecordID+ 1
            the_file.write(str(RecordID)+' '+FindID+' '+Findname+' '+FindChoosenPlan+' '+FindChoosenClaim+' '+str(RoomDays)+' '+str(RoomFees)+' '+str(ICUDays)+' '+str(ICUFees)+' '+str(HSSF)+' '+str(SF)+' '+str(Others)+' '+str(TotalFees)+' '+FindBalance+' '+str(Change)+'\n')
            print('Claim Success!!')
            print('Thanks '+Findname+'!')
            print('Your Recipt is: '+str(RecordID))
            input('Click Enter to go back to main menu')
            Welcome()
            #Read()            
def RegisterPlan():
    global Balance 
    global ChoosenPlan 
    global ChoosenClaim
    if 14 < Check and Check < 9133:
        print('-*********************************************************************************************-')
        print('EZMediLife Health Insurance Plan ')
        print('-*********************************************************************************************-')
        print('Plans>                                      |            Plan150         Plan200        Plan300')
        print('_______________________________________________________________________________________________')
        print('15 days old – 25 Years Old Avaialbalilty >  |	          ✔ 	          ✔	         ✔   ')
        print('_______________________________________________________________________________________________')
        print('Annual Claim Limit Amount > 	           |           100,000 	       200,000 	      300,000 ')
        print('_______________________________________________________________________________________________')
        print('Lifetime Claim Limit Amount > 	           |           500,000 	      1,000,000      2,000,000')
        print('-*********************************************************************************************-')
        print('Hospitalisation and Surgical Benefits ')
        print('_______________________________________________________________________________________________')
        print('Room Charges >                                         150/Day          200/Day         300/Day')
        print('_______________________________________________________________________________________________')
        print('Intensive Care Unit (ICU) Charges >                    300/Day          500/Day         900/Day')
        print('_______________________________________________________________________________________________')
        print('Hospital Supplies and Services                                                                 ')
        print('Surgical Fees                         As charged. Subject to approval by EZMediLife            ')
        print('Other Fees                                                                                     ')
        print('_______________________________________________________________________________________________')
        print('-*********************************************************************************************-')
        
        print('Your age is ',Age,'.')
        
        while True:         
            try:
                print('You can choose any of these plans : ')
                print('1) Plan 150')
                print('2) Plan 200')
                print('3) Plan 300')
                Plan = int(input('Choose the Plan Number(EG: 1,2,3) : '))
                if 1 > Plan or  Plan > 3:
                    print("Wrong Input!.")
                    continue
            except ValueError:
                print("Wrong Input!.")
                continue
            else:
                if Plan == 1:
                    ChoosenPlan = 'Plan150'
                if Plan == 2:
                    ChoosenPlan = 'Plan200'
                if Plan == 3:
                    ChoosenPlan = 'Plan300'
                break
        while True:
            try:
                print('There is two types of claim limit: ')
                print('1) Annual Claim Limit')
                print('2) Lifetime Claim Limit')
                Claim = int(input('Choose the Claim Limit type: '))
                if 1 > Claim or  Claim > 2:
                    print("Wrong Input!.")
                    continue
            except ValueError:
                print("Wrong Input!.")
                continue
            else:
                if Claim == 1:
                    ChoosenClaim = 'Annual'
                if Claim == 2:
                    ChoosenClaim = 'Lifetime'
                break
    elif 9132 < Check and Check < 1275 :
        print('-*********************************************************************************************-')
        print('EZMediLife Health Insurance Plan ')
        print('-*********************************************************************************************-')
        print('Plans>                                      |            Plan150         Plan200        Plan300')
        print('_______________________________________________________________________________________________')
        print('15 days old – 25 Years Old Avaialbalilty >  |	          🛇 	          ✔	         ✔   ')
        print('_______________________________________________________________________________________________')
        print('Annual Claim Limit Amount > 	           |           100,000 	       200,000 	      300,000 ')
        print('_______________________________________________________________________________________________')
        print('Lifetime Claim Limit Amount > 	           |           500,000 	      1,000,000      2,000,000')
        print('-*********************************************************************************************-')
        print('Hospitalisation and Surgical Benefits ')
        print('_______________________________________________________________________________________________')
        print('Room Charges >                                         150/Day          200/Day         300/Day')
        print('_______________________________________________________________________________________________')
        print('Intensive Care Unit (ICU) Charges >                    300/Day          500/Day         900/Day')
        print('_______________________________________________________________________________________________')
        print('Hospital Supplies and Services                                                                 ')
        print('Surgical Fees                         As charged. Subject to approval by EZMediLife            ')
        print('Other Fees                                                                                     ')
        print('_______________________________________________________________________________________________')
        print('-*********************************************************************************************-')
        print('You is age is ',Age,'.')
        
        while True:
            try:
                print('You can choose any of these plans : ')
                print('1) Plan 200')
                print('2) Plan 300')
                Plan = int(input('Choose the Plan Number(EG: 1,2) : '))
                if 1 > Plan or  Plan > 2:
                    print("Wrong Input!.")
                    continue
            except ValueError:
                print("Wrong Input!.")
                continue
            else:
                if Plan == 1:
                    ChoosenPlan = 'Plan200'
                if Plan == 2:
                    ChoosenPlan = 'Plan300'
                break
        while True:
            try:
                print('There is two types of claim limit: ')
                print('1) Annual Claim Limit')
                print('2) Lifetime Claim Limit')
                Claim = int(input('Choose the Claim Limit type: '))
                if 1 > Claim or  Claim > 2:
                    print("Wrong Input!.")
                    continue
            except ValueError:
                print("Wrong Input!.")
                continue
            
            else:
                if Claim == 1:
                    ChoosenClaim = 'Annual'
                if Claim == 2:
                    ChoosenClaim = 'Lifetime'
                break
    elif 12784 < Check and Check < 18263:    
        print('-*********************************************************************************************-')
        print('EZMediLife Health Insurance Plan ')
        print('-*********************************************************************************************-')
        print('Plans>                                      |            Plan150         Plan200        Plan300')
        print('_______________________________________________________________________________________________')
        print('15 days old – 25 Years Old Avaialbalilty >  |	          🛇 	          🛇              ✔   ')
        print('_______________________________________________________________________________________________')
        print('Annual Claim Limit Amount > 	           |           100,000 	       200,000 	      300,000 ')
        print('_______________________________________________________________________________________________')
        print('Lifetime Claim Limit Amount > 	           |           500,000 	      1,000,000      2,000,000')
        print('-*********************************************************************************************-')
        print('Hospitalisation and Surgical Benefits ')
        print('_______________________________________________________________________________________________')
        print('Room Charges >                                         150/Day          200/Day         300/Day')
        print('_______________________________________________________________________________________________')
        print('Intensive Care Unit (ICU) Charges >                    300/Day          500/Day         900/Day')
        print('_______________________________________________________________________________________________')
        print('Hospital Supplies and Services                                                                 ')
        print('Surgical Fees                         As charged. Subject to approval by EZMediLife            ')
        print('Other Fees                                                                                     ')
        print('_______________________________________________________________________________________________')
        print('-*********************************************************************************************-')
        print('You is age is ',Age,'.')
        
        while True:
            try:
                print('You can choose only this plan : ')
                print('1) Plan 300')
                Plan = int(input('Choose the Plan Number(EG: 1,2,3) : '))
                
                if 1 > Plan or  Plan > 3:
                    print("Wrong Input!.")
                    continue
            except ValueError:
                print("Wrong Input!.")
                continue
            else:
                ChoosenPlan = 'Plan300'
                break
        while True:
            try:
                print('There is two types of claim limit: ')
                print('1) Annual Claim Limit')
                print('2) Lifetime Claim Limit')
                Claim = int(input('Choose the Claim Limit type: '))
                if 1 > Claim or  Claim > 2:
                    print("Wrong Input!.")
                    continue
            except ValueError:
                print("Wrong Input!.")
                continue
            else:
                if Claim == 1:
                    ChoosenClaim = 'Annual'
                if Claim == 2:
                    ChoosenClaim = 'Lifetime'
                break

    
     
    if ChoosenClaim == 'Annual':
        if ChoosenPlan == 'Plan150':
            Balance = '100000'
        if ChoosenPlan == 'Plan200':            
            Balance = '200000'
        if ChoosenPlan == 'Plan300':
            Balance = '300000'
    if ChoosenClaim == 'Lifetime':     
        if ChoosenPlan == 'Plan150':
            Balance = '500000'
        if ChoosenPlan == 'Plan200':            
            Balance = '1000000'
        if ChoosenPlan == 'Plan300':
            Balance = '2000000'
    Register()
    Hospitlization()
    
def Registeration():
    global name 
    global Address 
    global Phone 
    while True:
        try:
            name = input('Name: ')
            if ' ' in name:
                print("Wrong Input(Space not allowed)!.")
                continue            
        except ValueError:
            print("Wrong Input.")
            continue
        else:
            break
    while True:
        try:
            Phone = int(input('Phone Number(EG:0112345678): '))
            if ' ' in str(Phone):
                print("Wrong Input(Space not allowed)!.")
                continue
            if len(str(Phone)) != 10:
                print(len(str(Phone)))
                print("Wrong Input(Phone has 10 min&max)!.")
                continue 
        except ValueError:
            print("Wrong Input(Only integer)!.")
            continue
        else:
            break
    while True:
        try:
            Address = input('Address: ')
            if ' ' in Address:
                print("Wrong Input(Space not allowed(You can use ',' to seperate words))!.")
                continue 
        except ValueError:
            print("Wrong Input!.")
            continue
        else:
            break
    while True:
        try:
            Year = int(input('Year of Birth: '))
            if Year < 1920 or Year > 2020:
                print("Wrong Input(Year out of ranged)!.")
                continue
            if ' ' in str(Year):
                print("Wrong Input(Space is not Allowed)!.")
                continue
        except ValueError:
            print("Wrong Input(Only integer)!.")
            continue
        else:
            break
    while True:
        try:
            Month = int(input('Month of Birth(In numbers): '))
            if 1 > Month or Month > 12:
                print("Wrong Input!.")
                continue
            if ' ' in str(Month):
                print("Wrong Input(Space is not allowed)!.")
                continue
        except ValueError:
            print("Wrong Input(Only Integer)!.")
            continue
        else:
            break
    while True:
        try:
            Day = int(input('Day Of Birth: '))
            if 1 > Day or Day > 31:
                print("Wrong Input(Out of range)!.")
                continue
            if ' ' in str(Day):
                print("Wrong Input(Space is not allowed)!.")
                continue
        except ValueError:
            print("Wrong Input(Only integer)!.")
            continue
        else:
            break 
    from datetime import datetime
    global f_date
    f_date = date(Year, Month, Day)  
    now = datetime.now()
    string = now.strftime("%d %m %Y %H:%M:%S")
    import datetime
    date1 = datetime.datetime.strptime(string, "%d %m %Y %H:%M:%S")
    l_date = date(int(date1.year), int(date1.month), int(date1.day))
    delta = l_date - f_date
    global Age
    Age = round(delta.days / 365)
    global Check
    Check = delta.days 
    RegisterPlan()

Welcome()
