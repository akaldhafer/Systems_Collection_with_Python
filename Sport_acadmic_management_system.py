#Name: Abdulmalek Aldhafer
#GitHub username: akaldhafer
#Email: Ak_aldhafer@hotmail.com
#System title: REAL CHAMPIONS SPORT ACADEMY SYSTEM


#import json for list implementation
import json
import os #to use pause and cls clrean screen 


#Sport center list
SportCenterName = ["RCSAS(KL)", "RCSAS(Cyberjaya)", "RCSAS(Ampang)"]
SportCenterCode = ["RCSASKL", "RCSASCJ", "RCSASA"]
#main menu of the system *************************************
def MainMenu():
    
    #Decalre the files
    DeclareFile1 = open('SportRecords.txt', 'a+')
    DeclareFile2 = open('CoachRecords.txt', 'a+')
    DeclareFile3 = open('SecheduleSportRecords.txt', 'a+')
    DeclareFile4 = open('StudentRecords.txt', 'a+')
    DeclareFile5 = open('RegisteredLesson.txt', 'a+')
    DeclareFile1.close()
    DeclareFile2.close()
    DeclareFile3.close()
    DeclareFile4.close()
    DeclareFile5.close()
    
    #System menu
    print('\n********    ALDHAFER SPORT ACADEMY SYSTEM   ********')
    print('__________________________________________________________')
    print('1. Login as admin')
    print('2. Login as customer')
    print('3. Customer Page')
    print('4. Exit')
    
    menuOption = int(input("Enter one option: "))
    if(menuOption == 1):
        #login as admin
        LoginAsAdmin()
    elif(menuOption == 2):
        #login as student
        LoginAsStudent()
    elif(menuOption == 3):
        #student page
        StudentPage()
    elif(menuOption == 4):
        #exit from the system
        exit()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")#waiting the user input 
    os.system("CLS")#clean screen 
    MainMenu()
    
#Main menu functions ------------------------------------------   
#login as admin
def LoginAsAdmin():
    print("\nEnter Admin Details To Access the Admin Menu\nNote: (UserName and Password: admin, pass by Default)\n\n")
    for i in range(5):
        Username = input("Enter admin username: ")
        Password = input("Enter admin password: ")
        if(Username == "admin" and Password == "pass"):
            print("\n  Welcome to Admin Menu \n")
            AdminMenu()
        else:
            print("\nWrong username or password, try again\n")
    print("\n You have reached the maximum attempt allowed, the system will terminate\n")
    exit()
    
#login as student
def LoginAsStudent():
    print("\nEnter Student Details To Access the Student Menu\nNote:\n\n")
    OpenFile = open('StudentRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('StudentRecords.txt') == 0:
        print('No Records')
    
    for i in range(5):
        StudentId = int(input("Enter Student ID: "))
        StudentPassword = input("Enter Student password: ")
        for r in Record:
            Coachs = json.loads(r)
            if StudentId == Coachs[0] and StudentPassword == Coachs[4]:
                print(" Welcome back, ", Coachs[1])
                StdID = StudentId
                StdName = Coachs[1]
                os.system("PAUSE")
                os.system("CLS")
                OpenFile.close() 
                StudentMenu(StdID, StdName)
        print("\n Wrong Student ID or password, please retry again")
    print("\n You have reached the maximum attempt allowed, the system will terminate\n")
    exit()
    
#Sign up as student
def SignUpStudent():
    print("\n  Welcome to sign up page for student ")
    print("\nPlease enter the wanted requirements: ")
    StudentID = GetNumberOfRecords('StudentRecords.txt')+1
    print("Student ID is: ", StudentID)
    StudentName = input("Enter Student Name: ")
    StudentPhone = input("Enter Student Phone No: ")
    StudentAddress = input("Enter Student Address: ")
    StudentPassword = input("Enter Student Password: ")
    StudentRecord = [StudentID, StudentName, StudentPhone, StudentAddress, StudentPassword]
    listIntoJson = json.dumps(StudentRecord)
    OpenFile = open('StudentRecords.txt', 'a+')
    OpenFile.writelines(listIntoJson)
    OpenFile.writelines('\n')
    OpenFile.close()
    print("\nRecord has been added successfully..\n")
    
#student page
def StudentPage():
    #student page
    print('\n********          Customer Page                ********')
    print('__________________________________________________________')
    print('1. View avaiable sports')
    print('2. View avaiable sport schedules')
    print('3. Sign up')
    print('4. Back')
    
    StudentOption = int(input("Enter one option: "))
    if(StudentOption == 1):
        #Display sport
        DisplaySportRecord()
    elif(StudentOption == 2):
        #Display Sport Secheduled Record
        DisplaySportSecheduledRecord()
    elif(StudentOption == 3):
        #Sign up as student
        SignUpStudent()
    elif(StudentOption == 4):
        #back
        MainMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    StudentPage()
#------------------------------------------------------------

#admin menu**************************************************
def AdminMenu():
    
    #Admin menu
    print('\n********             Admin Menu               ********')
    print('__________________________________________________________')
    print('1. Add Record')
    print('2. Display Records')
    print('3. Search Specific Record')
    print('4. Sort and Display Record')
    print('5. Modify Record')
    print('6. Log out')
    AdminOption = int(input("Enter one option: "))
    if(AdminOption == 1):
        #Add Record menu
        AddRecordMenu()
    elif(AdminOption == 2):
        #display record menu
        DisplayRecordMenu()
    elif(AdminOption == 3):
        #search record menu
        SearchRecordMenu()
    elif(AdminOption == 4):
        #sort and display record
        SortRecordMenu()
    elif(AdminOption == 5):
        #Modify record menu
        ModifyRecordMenu()
    elif(AdminOption == 6):
        #log out
        MainMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    AdminMenu()
    
#Add Record menu
def AddRecordMenu():    
    #add record menu
    print('\n********          Add Record Menu             ********')
    print('__________________________________________________________')
    print('1. Add Coach Record')
    print('2. Add Sport Record')
    print('3. Add Sport Sechedule Record')
    print('4. Back')
    
    AddOption = int(input("Enter one option: "))
    if(AddOption == 1):
        #Add coach
        AddCoachRecord()
    elif(AddOption == 2):
        #add sport
        AddSportRecord()
    elif(AddOption == 3):
        #add sport sechedule
        AddSportSecheduleRecord()
    elif(AddOption == 4):
        #back
        AdminMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    AddRecordMenu()
#add record functions --------------------------------
#Add coach
def AddCoachRecord():
    print("\nPlease enter the wanted requirements: \n")
    CoachID = GetNumberOfRecords('CoachRecords.txt')+1
    CoachName = input("Enter Coach Name: ")
    CoachPhone = input("Enter Coach Phone: ")
    CoachAddress = input("Enter Coach Address: ")
    CJoinDate = input("Enter Join in Date: ")
    CTerminated = input("Enter Terminated Date: ")
    HourlyRate = int(input("Enter Hourly Rate: "))
    #choose sport
    print("\nChoose sport from the avaiable sport down: ")
    DisplaySportRecord()
    SCode = int(input("Enter Sport Code: "))
    SName = ""
    Openfile = open('SportRecords.txt', 'r')
    Records = Openfile.readlines()
    availableSports = False
    #sport= [code(0), name(1)]
    for r in Records:
        Sports = json.loads(r)
        if SCode == Sports[0]:
            availableSports = True
            SName = Sports[1]
            break
    if not availableSports:
        print('Sports not available...')
        os.system("PAUSE")
        AddRecordMenu()
    Openfile.close()
    #choose sport center 
    print("\nThe avaiable Sport Center: \n")
    print("1. Code: ",SportCenterCode[0],"\tName: ",SportCenterName[0])
    print("2. Code: ",SportCenterCode[1],"\tName: ",SportCenterName[1])
    print("3. Code: ",SportCenterCode[2],"\tName: ",SportCenterName[2])
    sportcenter = int(input("Choose sport center: "))
    if sportcenter == 1:
        SCCode = SportCenterCode[0]
        SCName = SportCenterName[0]
    elif sportcenter == 2:
        SCCode = SportCenterCode[1]
        SCName = SportCenterName[2]
    elif sportcenter == 3:
        SCCode = SportCenterCode[2]
        SCName = SportCenterName[2]
    else:
        print("\nWrong option, retry again !!\n")
        AddRecordMenu()
    
    CoachRating = int(input("Enter Coach overall performaance(1-5): "))
    CoachRecord = [CoachID, CoachName, CoachPhone, CoachAddress, CJoinDate, CTerminated, HourlyRate, SCode, SName, CoachRating, SCCode, SCName]
    listIntoJson = json.dumps(CoachRecord)
    OpenF = open('CoachRecords.txt', 'a+')
    OpenF.writelines(listIntoJson)
    OpenF.writelines('\n')
    OpenF.close()
    print("\nRecord has been added successfully..\n")

#add sport
def AddSportRecord():
    print("\nPlease enter the wanted requirements: \n")
    SportCode = GetNumberOfRecords('SportRecords.txt') + 1
    print("Sport Code is: ", SportCode)
    SportName = input("Enter Sport Name(ex:Swimming,Badminton,\n Football,Archery,Gymnastics): ")
    SportRecord = [SportCode, SportName]
    listIntoJson = json.dumps(SportRecord)
    OpenFile = open('SportRecords.txt', 'a+')
    OpenFile.writelines(listIntoJson)
    OpenFile.writelines('\n')
    OpenFile.close()
    print("\nRecord has been added successfully..\n")


#add sport sechedule
def AddSportSecheduleRecord():  
    print("\nPlease enter the wanted requirements: \n")
    SportSecheduleID = GetNumberOfRecords('SecheduleSportRecords.txt')+1
    print("Lesson ID is: ", SportSecheduleID)
    LessonDate = input("Enter lesson Date(yyyy/mn/dd): ")
    LessonTime = input("Enter lesson Time: ")
    LessonPeriod = input("Enter lesson period: ")
    #choose coach
    print("\nChoose Coach from the avaiable Coach down: ")
    DisplayCoachRecord()
    CoachID = int(input("Enter Coach ID: "))
    CoachName = input("Enter Coach Name: ")
    Ofile = open('CoachRecords.txt', 'r')
    Records = Ofile.readlines()
    availableCoach = False
    for r in Records:
        Coachs = json.loads(r)
        if CoachID == Coachs[0] and CoachName == Coachs[1]:
            availableCoach = True
            break
    if not availableCoach:
        print('Coach not available...')
        AddRecordMenu()
    Ofile.close()
    #choose sport
    print("\nChoose sport from the avaiable sport down: ")
    DisplaySportRecord()
    SCode = int(input("Enter Sport Code: "))
    SName = input("Enter Sport Name: ")
    Openfile = open('SportRecords.txt', 'r')
    Records = Openfile.readlines()
    availableSports = False
    for r in Records:
        Sports = json.loads(r)
        if SCode == Sports[0] and SName == Sports[1]:
            availableSports = True
            break
    if not availableSports:
        print('Sports not available...')
        os.system("PAUSE")
        AddRecordMenu()
    Openfile.close()
    #choose sport center 
    print("\nThe avaiable Sport Center: \n")
    print("1. Code: ",SportCenterCode[0],"\tName: ",SportCenterName[0])
    print("2. Code: ",SportCenterCode[1],"\tName: ",SportCenterName[1])
    print("3. Code: ",SportCenterCode[2],"\tName: ",SportCenterName[2])
    sportcenter = int(input("Choose sport center: "))
    if sportcenter == 1:
        SCCode = SportCenterCode[0]
        SCName = SportCenterName[0]
    elif sportcenter == 2:
        SCCode = SportCenterCode[1]
        SCName = SportCenterName[2]
    elif sportcenter == 3:
        SCCode = SportCenterCode[2]
        SCName = SportCenterName[2]
    else:
        print("\nWrong option, retry again !!\n")
        AddRecordMenu()
    
    CoachRecord = [SportSecheduleID,CoachID, CoachName,LessonDate,LessonTime,LessonPeriod, SCode, SName, SCCode, SCName]
    listIntoJson = json.dumps(CoachRecord)
    OpenF = open('SecheduleSportRecords.txt', 'a+')
    OpenF.writelines(listIntoJson)
    OpenF.writelines('\n')
    OpenF.close()
    print("\nRecord has been added successfully..\n")
#----------------------------------------------------- 
#display record menu
def DisplayRecordMenu():
    #display record menu
    print('\n********        Display Record Menu           ********')
    print('__________________________________________________________')
    print('1. Display Coach Record')
    print('2. Display Sport Record')
    print('3. Display Registered student')
    print('4. Display Sport Secheduled Record ')
    print('5. Display Registered lesson')
    print('6. Back')
    
    DisplayOption = int(input("Enter one option: "))
    if(DisplayOption == 1):
        #Display coach
        DisplayCoachRecord()
    elif(DisplayOption == 2):
        #Display sport
        DisplaySportRecord()
    elif(DisplayOption == 3):
        #Display student record
        DisplayStudentRecord()
    elif(DisplayOption == 4):
        #Display Sport Secheduled Record
        DisplaySportSecheduledRecord()
    elif(DisplayOption == 5):
        #Display Registered lesson
        DisplayRegisteredlesson()
    elif(DisplayOption == 6):
        #back
        AdminMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    DisplayRecordMenu()
#display record functions -------------------------------
#Display coach
def DisplayCoachRecord():
    OpenFile = open('CoachRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('CoachRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Coachs = json.loads(r)
        print('CoachID     : '+ str(Coachs[0]) 
              + '\n' + 'Name        : '+str(Coachs[1]) 
              + '\n' + 'Phone       : '+str(Coachs[2]) 
              + '\n' + 'Address     : '+str(Coachs[3]) 
              + '\n' + 'Join in Date: '+str(Coachs[4]) 
              + '\n' + 'Leave Date  : '+str(Coachs[5]) 
              + '\n' + 'Hourly Rate : '+str(Coachs[6]) 
              + '\n' + 'Sport Code  : '+str(Coachs[7]) 
              + '\n' + 'Sport Name  : '+str(Coachs[8]) 
              + '\n' + 'Rating      : '+str(Coachs[9]) 
              + '\n' + 'Center Code : '+str(Coachs[10]) 
              + '\n' + 'Center Name : '+str(Coachs[11])+'\n------------------------------------------------\n')
    OpenFile.close()
    
#Display sport
def DisplaySportRecord():
    OpenFile = open('SportRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('SportRecords.txt') == 0:
        print('No Records')
    print('Sport Code\t\tSport Name')
    for r in Record:
        Sports = json.loads(r)
        print(str(Sports[0]) + '\t' + str(Sports[1])+'\n')
    OpenFile.close()
#Display student record
def DisplayStudentRecord():
    print("\nStudent records:  ")
    OpenFile = open('StudentRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('StudentRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Student = json.loads(r)
        print('StudentID     : '+ str(Student[0]) 
              + '\n' + 'Name        : '+str(Student[1]) 
              + '\n' + 'Phone       : '+str(Student[2]) 
              + '\n' + 'Address     : '+str(Student[3]) 
              + '\n------------------------------------------------\n')          
    OpenFile.close()  

#Display Sport Secheduled Record
def DisplaySportSecheduledRecord():
    OpenFile = open('SecheduleSportRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('SecheduleSportRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Lesson = json.loads(r)
        print('LessonID    : '+ str(Lesson[0]) 
              + '\n' + 'Coach ID    : '+str(Lesson[1]) 
              + '\n' + 'Coach Name  : '+str(Lesson[2]) 
              + '\n' + 'Date        : '+str(Lesson[3]) 
              + '\n' + 'Time        : '+str(Lesson[4]) 
              + '\n' + 'Period      : '+str(Lesson[5]) 
              + '\n' + 'Sport Code  : '+str(Lesson[6]) 
              + '\n' + 'Sport Name  : '+str(Lesson[7]) 
              + '\n' + 'Center Code : '+str(Lesson[8]) 
              + '\n' + 'Center Name : '+str(Lesson[9])+'\n------------------------------------------------\n')
    OpenFile.close()
      
#Display Registered lesson
def DisplayRegisteredlesson():  
    OpenFile = open('RegisteredLesson.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('RegisteredLesson.txt') == 0:
        print('No Records')
    for r in Record:
        Lesson = json.loads(r)
        print('Registered Lesson ID: '+ str(Lesson[0])
              + '\n' + 'Lesson ID   : '+str(Lesson[1])
              + '\n' + 'Student ID  : '+str(Lesson[2]) 
              + '\n' + 'Student Name: '+str(Lesson[3]) 
              + '\n' + 'Coach ID    : '+str(Lesson[4]) 
              + '\n' + 'Coach Name  : '+str(Lesson[5]) 
              + '\n' + 'Date        : '+str(Lesson[6]) 
              + '\n' + 'Time        : '+str(Lesson[7]) 
              + '\n' + 'Period      : '+str(Lesson[8]) 
              + '\n' + 'Sport Code  : '+str(Lesson[9]) 
              + '\n' + 'Sport Name  : '+str(Lesson[10]) 
              + '\n' + 'Center Code : '+str(Lesson[11]) 
              + '\n' + 'Center Name : '+str(Lesson[12])
              + '\n' + 'FeedBack    : '+str(Lesson[13]) 
              + '\n' + 'Coach Rate  : '+str(Lesson[14])
              + '\n------------------------------------------------\n')
    OpenFile.close()
     
#--------------------------------------------------------

#search record menu
def SearchRecordMenu():
    #search record menu
    print('\n********         Search Record Menu           ********')
    print('__________________________________________________________')
    print('1. Search Coach By Coach ID')
    print('2. Search Coach By Coach Overall Performance(Rating)')
    print('3. Search Sport By Sport ID')
    print('4. Search Student By Student ID')
    print('5. Back')
    
    SearchOption = int(input("Enter one option: "))
    if(SearchOption == 1):
        #Search Coach By Coach ID
        SearchCID()
    elif(SearchOption == 2):
        #Search Coach By Coach Overall Performance(Rating)
        SearchCRating()
    elif(SearchOption == 3):
        #Search Sport By Sport ID
        SearchSID()
    elif(SearchOption == 4):
        #Search Student By Student ID
        SearchStudentID()
    elif(SearchOption == 5):
        #back
        AdminMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    SearchRecordMenu()
#search record functions ------------------------------------
#Search Coach By Coach ID
def SearchCID():
    print("\nSearch Coach By Coach ID ")
    CoachID = int(input("Enter Coach ID: "))
    OpenFile = open('CoachRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('CoachRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Coachs = json.loads(r)
        if CoachID == Coachs[0]:
            print('CoachID     : '+ str(Coachs[0]) 
              + '\n' + 'Name        : '+str(Coachs[1]) 
              + '\n' + 'Phone       : '+str(Coachs[2]) 
              + '\n' + 'Address     : '+str(Coachs[3]) 
              + '\n' + 'Join in Date: '+str(Coachs[4]) 
              + '\n' + 'Leave Date  : '+str(Coachs[5]) 
              + '\n' + 'Hourly Rate : '+str(Coachs[6]) 
              + '\n' + 'Sport Code  : '+str(Coachs[7]) 
              + '\n' + 'Sport Name  : '+str(Coachs[8]) 
              + '\n' + 'Rating      : '+str(Coachs[9]) 
              + '\n' + 'Center Code : '+str(Coachs[10]) 
              + '\n' + 'Center Name : '+str(Coachs[11])+'\n------------------------------------------------\n')
    OpenFile.close()

#Search Coach By Coach Overall Performance(Rating)
def SearchCRating():
    print("\nSearch Coach By Coach Overall Performance(Rating) ")
    CoachOP = int(input("Enter Coach Overall Performance(Rating: 1-5): "))
    OpenFile = open('CoachRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('CoachRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Coachs = json.loads(r)
        if CoachOP == Coachs[9]:
            print('CoachID     : '+ str(Coachs[0]) 
              + '\n' + 'Name        : '+str(Coachs[1]) 
              + '\n' + 'Phone       : '+str(Coachs[2]) 
              + '\n' + 'Address     : '+str(Coachs[3]) 
              + '\n' + 'Join in Date: '+str(Coachs[4]) 
              + '\n' + 'Leave Date  : '+str(Coachs[5]) 
              + '\n' + 'Hourly Rate : '+str(Coachs[6]) 
              + '\n' + 'Sport Code  : '+str(Coachs[7]) 
              + '\n' + 'Sport Name  : '+str(Coachs[8]) 
              + '\n' + 'Rating      : '+str(Coachs[9]) 
              + '\n' + 'Center Code : '+str(Coachs[10]) 
              + '\n' + 'Center Name : '+str(Coachs[11])+'\n------------------------------------------------\n')
    OpenFile.close()


#Search Sport By Sport ID
def SearchSID():   
    print("\nSearch Sport By Sport Code")
    SportID = int(input("Enter Sport Code: "))
    OpenFile = open('SportRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('SportRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Sports = json.loads(r)
        if SportID == Sports[0]:
            print('Sport Code: '+ str(Sports[0]) 
                  + '\n' + 'Sport Name: '+ str(Sports[1])+'\n')
    OpenFile.close()

    
#Search Student By Student ID
def SearchStudentID(): 
    print("\nSearch Student By Student ID ")
    StudentID = int(input("Enter Student ID: "))
    OpenFile = open('StudentRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('StudentRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Student = json.loads(r)
        if StudentID == Student[0]:
            print('StudentID     : '+ str(Student[0]) 
              + '\n' + 'Name        : '+str(Student[1]) 
              + '\n' + 'Phone       : '+str(Student[2]) 
              + '\n' + 'Address     : '+str(Student[3]) 
              + '\n------------------------------------------------\n')
    OpenFile.close()  
#------------------------------------------------------------
#sort and display record
def SortRecordMenu():
    #display record menu
    print('\n********    Sort and Display Record Menu      ********')
    print('__________________________________________________________')
    print('1. Sort and Display Coaches in ascending order by names.')
    print('2. Sort and Display Coaches Hourly Pay Rate in ascending order')
    print('3. Sort and Display Coaches Overall Performance in ascending order')
    print('4. Back')
    
    SortOption = int(input("Enter one option: "))
    if(SortOption == 1):
        #Sort and Display Coaches in ascending order by names.
        SortCoachByName()
    elif(SortOption == 2):
        #Sort and Display Coaches Hourly Pay Rate in ascending order
        SortCoachbyPayRate()
    elif(SortOption == 3):
        #Sort and Display Coaches Overall Performance in ascending order
        SortCoachByOP()
    elif(SortOption == 4):
        #back
        AdminMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    SortRecordMenu()
#sort record functions ----------------------------------
#Sort and Display Coaches in ascending order by names.
def SortCoachByName():
    print("Sort and Display Coaches in ascending order by names")
    OpenFile = open('CoachRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('CoachRecords.txt') == 0:
        print('No Records')
    mylist = []
    for r in Record:
        Coachs = json.loads(r)
        mylist.append(Coachs)
    mylist.sort(key=ByName)
    for Coach in mylist:
        print('CoachID     : '+ str(Coach[0]) 
              + '\n' + 'Name        : '+str(Coach[1]) 
              + '\n' + 'Phone       : '+str(Coach[2]) 
              + '\n' + 'Address     : '+str(Coach[3]) 
              + '\n' + 'Join in Date: '+str(Coach[4]) 
              + '\n' + 'Leave Date  : '+str(Coach[5]) 
              + '\n' + 'Hourly Rate : '+str(Coach[6]) 
              + '\n' + 'Sport Code  : '+str(Coach[7]) 
              + '\n' + 'Sport Name  : '+str(Coach[8]) 
              + '\n' + 'Rating      : '+str(Coach[9]) 
              + '\n' + 'Center Code : '+str(Coach[10]) 
              + '\n' + 'Center Name : '+str(Coach[11])+'\n------------------------------------------------\n')
    OpenFile.close()
 
    
#Sort and Display Coaches Hourly Pay Rate in ascending order
def SortCoachbyPayRate():
    print("Sort and Display Coaches Hourly Pay Rate in ascending order")
    OpenFile = open('CoachRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('CoachRecords.txt') == 0:
        print('No Records')
    mylist = []
    for r in Record:
        Coachs = json.loads(r)
        mylist.append(Coachs)
    mylist.sort(key=ByPayRate)
    for Coach in mylist:
        print('CoachID     : '+ str(Coach[0]) 
              + '\n' + 'Name        : '+str(Coach[1]) 
              + '\n' + 'Phone       : '+str(Coach[2]) 
              + '\n' + 'Address     : '+str(Coach[3]) 
              + '\n' + 'Join in Date: '+str(Coach[4]) 
              + '\n' + 'Leave Date  : '+str(Coach[5]) 
              + '\n' + 'Hourly Rate : '+str(Coach[6]) 
              + '\n' + 'Sport Code  : '+str(Coach[7]) 
              + '\n' + 'Sport Name  : '+str(Coach[8]) 
              + '\n' + 'Rating      : '+str(Coach[9]) 
              + '\n' + 'Center Code : '+str(Coach[10]) 
              + '\n' + 'Center Name : '+str(Coach[11])+'\n------------------------------------------------\n')
    OpenFile.close()

    
#Sort and Display Coaches Overall Performance in ascending order
def SortCoachByOP():
    print("Sort and Display Coaches Overall Performance in ascending order")
    OpenFile = open('CoachRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('CoachRecords.txt') == 0:
        print('No Records')
    mylist = []
    for r in Record:
        Coachs = json.loads(r)
        mylist.append(Coachs)
    mylist.sort(key=ByOP)
    for Coach in mylist:
        print('CoachID     : '+ str(Coach[0]) 
              + '\n' + 'Name        : '+str(Coach[1]) 
              + '\n' + 'Phone       : '+str(Coach[2]) 
              + '\n' + 'Address     : '+str(Coach[3]) 
              + '\n' + 'Join in Date: '+str(Coach[4]) 
              + '\n' + 'Leave Date  : '+str(Coach[5]) 
              + '\n' + 'Hourly Rate : '+str(Coach[6]) 
              + '\n' + 'Sport Code  : '+str(Coach[7]) 
              + '\n' + 'Sport Name  : '+str(Coach[8]) 
              + '\n' + 'Rating      : '+str(Coach[9]) 
              + '\n' + 'Center Code : '+str(Coach[10]) 
              + '\n' + 'Center Name : '+str(Coach[11])+'\n------------------------------------------------\n')
    OpenFile.close()

#--------------------------------------------------------
#Modify record menu
def ModifyRecordMenu():
    #Modify record menu
    print('\n********      Modify Record Menu              ********')
    print('__________________________________________________________')
    print('1. Modify Coach Record')
    print('2. Modify Sport Record')
    print('3. Modify Sport Sechedule Record')
    print('4. Back')
    
    ModifyOption = int(input("Enter one option: "))
    if(ModifyOption == 1):
        #Modify coach
        ModifyCoachRecord()
    elif(ModifyOption == 2):
        #Modify sport
        ModifySportRecord()
    elif(ModifyOption == 3):
        #Modify Sport Sechedule record
        ModifySportSecheduleRecord()
    elif(ModifyOption == 4):
        #back
        AdminMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    ModifyRecordMenu()
    
#modify record functions ------------------------------------
#Modify coach
def ModifyCoachRecord():
    print("\nModify Coach Record Page\nNote: Only Coach personal information allowed to update")
    CoachID = int(input('Enter Coach ID: '))
    #check if the Coach ID is avaiable or not
    fileOpen = open('CoachRecords.txt', 'r')
    Records = fileOpen.readlines()
    available = False
    for r in Records:
        Coachs = json.loads(r)
        if CoachID == Coachs[0]:
            available = True
            break
    if not available:
        print('Coach not available...')
        os.system("PAUSE")
        ModifyRecordMenu()
    #Get the new details  
    CoachPhone = input("Enter Coach Phone: ")
    CoachAddress = input("Enter Coach Address: ")
    HourlyRate = int(input("Enter Hourly Rate: "))
    CoachRating = int(input("Enter Coach overall performaance(1-5): "))
    #update the details
    Coachs[2] = CoachPhone
    Coachs[3] = CoachAddress
    Coachs[6] = HourlyRate
    Coachs[9] = CoachRating
    #move the data into temp file and clean the old file
    with open('CoachRecords.txt') as org:
        with open('temp.txt', 'w') as temp:
            for data in org:
                CoachRecord = json.loads(data)
                if (CoachRecord[0] != CoachID):
                    temp.write(data)
    #move back the data into the old file and clean the temp file
    with open('temp.txt') as temp:
        with open('CoachRecords.txt', 'w') as org:
            for data in temp:
                org.write(data)
    #add the updated record into the old file
    IntoJson = json.dumps(Coachs)
    fileOpen2 = open('CoachRecords.txt', 'a')
    fileOpen2.writelines(IntoJson)
    fileOpen2.writelines('\n')
    print("\nRecord has been updated successfully, ")
   
    
#Modify sport
def ModifySportRecord():
    print("\nModify Sport Record Page\nNote: Only Sport name allowed to update")
    SportID = int(input('Enter Sport ID: '))
    #check if the sport id is avaiable or not
    fileOpen = open('SportRecords.txt', 'r')
    Records = fileOpen.readlines()
    available = False
    for r in Records:
        Sports = json.loads(r)
        if SportID == Sports[0]:
            available = True
            break
    if not available:
        print('Sport not available...')
        os.system("PAUSE")
        ModifyRecordMenu()
    #Get the new name  
    SportName = input('Enter SportName: ')
    #update the name
    Sports[1] = SportName
    #move the data into temp file and clean the old file
    with open('SportRecords.txt') as org:
        with open('temp.txt', 'w') as temp:
            for data in org:
                SportRecord = json.loads(data)
                if (SportRecord[0] != SportID):
                    temp.write(data)
    #move back the data into the old file and clean the temp file
    with open('temp.txt') as temp:
        with open('SportRecords.txt', 'w') as org:
            for data in temp:
                org.write(data)
    #add the updated record into the old file
    IntoJson = json.dumps(Sports)
    fileOpen2 = open('SportRecords.txt', 'a')
    fileOpen2.writelines(IntoJson)
    fileOpen2.writelines('\n')
    print("\nRecord has been updated successfully, ")
     
#Modify Sport Sechedule record
def ModifySportSecheduleRecord():
    print("\nModify Lesson Record Page\nNote: Only Lesson Time, Date, and period allowed to update")
    LessonID = int(input('Enter Lesson ID: '))
    #check if the sport id is avaiable or not
    fileOpen = open('SecheduleSportRecords.txt', 'r')
    Records = fileOpen.readlines()
    available = False
    for r in Records:
        Lessons = json.loads(r)
        if LessonID == Lessons[0]:
            available = True
            break
    if not available:
        print('Sport not available...')
        os.system("PAUSE")
        ModifyRecordMenu()
    #Get the new details  
    LessonDate = input("Enter lesson Date(yyyy/mn/dd): ")
    LessonTime = input("Enter lesson Time: ")
    LessonPeriod = input("Enter lesson period: ")
    #update the details
    Lessons[3] = LessonDate
    Lessons[4] = LessonTime
    Lessons[5] = LessonPeriod
    #move the data into temp file and clean the old file
    with open('SecheduleSportRecords.txt') as org:
        with open('temp.txt', 'w') as temp:
            for data in org:
                LessonRecord = json.loads(data)
                if (LessonRecord[0] != LessonID):
                    temp.write(data)
    #move back the data into the old file and clean the temp file
    with open('temp.txt') as temp:
        with open('SecheduleSportRecords.txt', 'w') as org:
            for data in temp:
                org.write(data)
    #add the updated record into the old file
    IntoJson = json.dumps(Lessons)
    fileOpen2 = open('SecheduleSportRecords.txt', 'a')
    fileOpen2.writelines(IntoJson)
    fileOpen2.writelines('\n')
    print("\nRecord has been updated successfully, ")
      
#------------------------------------------------------------    

#student Menu **********************************************
def StudentMenu(StdID, StdName):
    #student menu
    print('\n********          Student Menu                ********')
    print('__________________________________________________________')
    print('1. Registere new sport schedule')
    print('2. View Coach')
    print('3. View registered Sport lesson')
    print('4. View profile')
    print('5. Modify personal information')
    print('6. Provide feedback and star to Coach')
    print('7. Log out')
    
    StudentOption = int(input("Enter one option: "))
    if(StudentOption == 1):
        #Registere New lesson
        RegistereNewlesson(StdID, StdName)
    elif(StudentOption == 2):
        #View coach
        ViewCoach(StdID)
    elif(StudentOption == 3):
        #View Registered lesson
        ViewRegisteredlesson(StdID)
    elif(StudentOption == 4):
        #View Profile
        ViewProfile(StdID)
    elif(StudentOption == 5):
        #Modify Student Record
        ModifyStudentRecord(StdID)
    elif(StudentOption == 6):
        #Provide Feedback And Rate
        ProvideFeedbackAndRate(StdID)
    elif(StudentOption == 7):
        #log out
        print("\nYou have logged out...")
        os.system("PAUSE")
        os.system("CLS")
        MainMenu()
    else:
        print("\n !!! Invalid input, Press anykey to continue \n")
    os.system("PAUSE")
    os.system("CLS")
    StudentMenu(StdID, StdName)   

#Registere New lesson
def RegistereNewlesson(StdID, StdName): 
    print("         Registere New lesson  ")
    #choose sport schedule
    print("\nChoose sport schedule from the avaiable schedules down: ")
    DisplaySportSecheduledRecord()
    SportSecheduleID = int(input("Enter Lesson ID: "))
    Openfile = open('SecheduleSportRecords.txt', 'r')
    Records = Openfile.readlines()
    availableSports = False
    for r in Records:
        Sports = json.loads(r)
        if SportSecheduleID == Sports[0]:
            availableSports = True
            CoachID = Sports[1]      
            CoachName = Sports[2] 
            LessonDate = Sports[3] 
            LessonTime = Sports[4] 
            LessonPeriod = Sports[5] 
            SCode = Sports[6] 
            SName = Sports[7] 
            SCCode = Sports[8]
            SCName = Sports[9] 
            break
    if not availableSports:
        print('Sport Schedule is not available...')
        os.system("PAUSE")
        RegistereNewlesson(StdID, StdName)
    Openfile.close()
    #get student details
    Feedback = ''
    Rate = 0
    StudentID = StdID
    StudentName = StdName
    RegisteredLessonID = GetNumberOfRecords('RegisteredLesson.txt')+1
    print("Registered Lesson ID is: ", RegisteredLessonID)
    RegisteredLesson = [RegisteredLessonID,SportSecheduleID,StudentID, StudentName,CoachID, CoachName,LessonDate,LessonTime,LessonPeriod, SCode, SName, SCCode, SCName, Feedback, Rate]
    listIntoJson = json.dumps(RegisteredLesson)
    OpenF = open('RegisteredLesson.txt', 'a+')
    OpenF.writelines(listIntoJson)
    OpenF.writelines('\n')
    OpenF.close()
    print("\nRecord has been added successfully..\n")
    
#View coach
def ViewCoach(StdID):       
    OpenFile = open('RegisteredLesson.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('RegisteredLesson.txt') == 0:
        print('No Records')
    for r in Record:
        Lesson = json.loads(r)
        if StdID == Lesson[2]:
            print('Registered Lesson ID: '+ str(Lesson[0])
              + '\n' + 'Lesson ID   : '+str(Lesson[1])
              + '\n' + 'Coach ID    : '+str(Lesson[4]) 
              + '\n' + 'Coach Name  : '+str(Lesson[5]) 
              + '\n' + 'Sport Name  : '+str(Lesson[10])  
              + '\n' + 'Center Name : '+str(Lesson[12])
              + '\n' + 'FeedBack    : '+str(Lesson[13]) 
              + '\n' + 'Coach Rate  : '+str(Lesson[14])
              + '\n------------------------------------------------\n')
    OpenFile.close()
 
#View Registered lesson
def ViewRegisteredlesson(StdID):
    OpenFile = open('RegisteredLesson.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('RegisteredLesson.txt') == 0:
        print('No Records')
    for r in Record:
        Lesson = json.loads(r)
        if StdID == Lesson[2]:
            print('Registered Lesson ID: '+ str(Lesson[0])
              + '\n' + 'Lesson ID   : '+str(Lesson[1])
              + '\n' + 'Student ID  : '+str(Lesson[2]) 
              + '\n' + 'Student Name: '+str(Lesson[3]) 
              + '\n' + 'Coach ID    : '+str(Lesson[4]) 
              + '\n' + 'Coach Name  : '+str(Lesson[5]) 
              + '\n' + 'Date        : '+str(Lesson[6]) 
              + '\n' + 'Time        : '+str(Lesson[7]) 
              + '\n' + 'Period      : '+str(Lesson[8]) 
              + '\n' + 'Sport Code  : '+str(Lesson[9]) 
              + '\n' + 'Sport Name  : '+str(Lesson[10]) 
              + '\n' + 'Center Code : '+str(Lesson[11]) 
              + '\n' + 'Center Name : '+str(Lesson[12])
              + '\n' + 'FeedBack    : '+str(Lesson[13]) 
              + '\n' + 'Coach Rate  : '+str(Lesson[14])
              + '\n------------------------------------------------\n')
    OpenFile.close()
    
#View Profile
def ViewProfile(StdID):
    OpenFile = open('StudentRecords.txt', 'r+')
    Record = OpenFile.readlines()
    if GetNumberOfRecords('StudentRecords.txt') == 0:
        print('No Records')
    for r in Record:
        Student = json.loads(r)
        if StdID == Student[0]:
            print('StudentID     : '+ str(Student[0]) 
              + '\n' + 'Name        : '+str(Student[1]) 
              + '\n' + 'Phone       : '+str(Student[2]) 
              + '\n' + 'Address     : '+str(Student[3]) 
              + '\n------------------------------------------------\n')          
    OpenFile.close()  
    
#Modify Student Record
def ModifyStudentRecord(StdID):
    print("\n Modify Student Profile\nNote: Only Student personal information allowed to update")
    fileOpen = open('StudentRecords.txt', 'r')
    Records = fileOpen.readlines()
    for r in Records:
        Student = json.loads(r)
        if StdID == Student[0]:
            break
    #Get the new details  
    StudentPhone = input("Enter Student Phone: ")
    StudentAddress = input("Enter Student Address: ")
    Password = input("Enter Password: ")
    #update the details
    Student[2] = StudentPhone
    Student[3] = StudentAddress
    Student[4] = Password
    #move the data into temp file and clean the old file
    with open('StudentRecords.txt') as org:
        with open('temp.txt', 'w') as temp:
            for data in org:
                StudentRecord = json.loads(data)
                if (StudentRecord[0] != StdID):
                    temp.write(data)
    #move back the data into the old file and clean the temp file
    with open('temp.txt') as temp:
        with open('StudentRecords.txt', 'w') as org:
            for data in temp:
                org.write(data)
    #add the updated record into the old file
    IntoJson = json.dumps(Student)
    fileOpen2 = open('StudentRecords.txt', 'a')
    fileOpen2.writelines(IntoJson)
    fileOpen2.writelines('\n')
    print("\nProfile has been updated successfully, ")
   


#Provide Feedback And Rate
def ProvideFeedbackAndRate(StdID):
    print("\n Provide Feedback and Rate to Specific Coach")
    ViewCoach(StdID)
    CoachID = int(input("Enter Coach ID: "))
    fileOpen = open('RegisteredLesson.txt', 'r')
    Records = fileOpen.readlines()
    available = False
    for r in Records:
        Student = json.loads(r)
        if StdID == Student[2] and CoachID == Student[4]:
            available = True
            break
    if not available:
        print('Coach Not Found...')
        os.system("PAUSE")
        ProvideFeedbackAndRate(StdID)
    #Get the new details  
    Feedback = input("Enter Your Feedback: ")
    Rate = int(input("Enter Your Rating(1-5): "))
    #update the details
    Student[13] = Feedback
    Student[14] = Rate
    #move the data into temp file and clean the old file
    with open('RegisteredLesson.txt') as org:
        with open('temp.txt', 'w') as temp:
            for data in org:
                StudentRecord = json.loads(data)
                if (StudentRecord[0] != StdID):
                    temp.write(data)
    #move back the data into the old file and clean the temp file
    with open('temp.txt') as temp:
        with open('RegisteredLesson.txt', 'w') as org:
            for data in temp:
                org.write(data)
    #add the updated record into the old file
    IntoJson = json.dumps(Student)
    fileOpen2 = open('RegisteredLesson.txt', 'a')
    fileOpen2.writelines(IntoJson)
    fileOpen2.writelines('\n')
    print("\nFeedback and Rating has been added successfully, ")
            
#local functions*********************************
#Create ID by defining the number of records inside the text file
def GetNumberOfRecords(fileName):
    numberOfRecords = 0
    fileOpen = open(fileName, 'r+')
    if fileOpen == 0:
        return 0
    Record = fileOpen.readlines()
    for r in Record:
        numberOfRecords += 1
    return numberOfRecords
#sort by coach name
def ByName(MyList):
    return MyList[1]
#sort by pay rate 
def ByPayRate(MyList):
    return MyList[6]
#sort by overall performance
def ByOP(MyList):
    return MyList[9]


    
#***********************************************
#start the system
MainMenu()
