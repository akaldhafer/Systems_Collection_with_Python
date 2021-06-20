#Name: Abdulmalek Aldhafer
#GitHub username: akaldhafer
#Email: Ak_aldhafer@hotmail.com
#System title: AUTOMOBILE PARTS INVENTORY MANAGEMENT SYSTEM 


import os #to use pause and cls
import json#to make the list easier to be read 

warehouses = [["Bios", "BS", "WBS"], ["Ambry", "AY", "WAY"], ["Barrier", "BR", "WBR"]]
sections = ["Engine Section (ES)", "Body Work Section (BWS)", "Air-con Section (AS)", "Oil Change Section (OCS)", "Tire Change Section (TCS)"]

def mainMenu():
    #create the text files if they do not exist
    if not os.path.exists("parts.txt"):#a: add  , w: write  , r read
        f = open("parts.txt", "a+")
        f.close()
    if not os.path.exists("suppliers.txt"):
        f = open("suppliers.txt", "a+")
        f.close()
    #display menu
    print(" <><><   AUTOMOBILE PARTS INVENTORY MANAGEMENT SYSTEM  ><><>")
    print("1. Add part")
    print("2. Update part")
    print("3. Track part")
    print("4. Search part")
    print("5. Add a supplier")
    print("6. show Suppliers")
    print("7. Show all inventory details")
    print("8. Exit")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        addPart()
    elif (choice == 2):
        updatePart()
    elif (choice == 3):
        trackPart()
    elif (choice == 4):
        searchMenu()
    elif (choice == 5):
        addSupplier()
    elif (choice == 6):
        showSuppliers()
    elif (choice == 7):
        showParts()
    elif (choice == 8):
        exit()
    else:
        print("Invalid Choice!")
    print("\n")
    mainMenu()

def addPart():
    num = 1 #mulist = [0,1,2,3]
    #display existing warehouses to choose from
    for count in warehouses:
        print(str(num) + ". " + count[2] + " (" + count[0] + ")")
        num+=1
    warehouseChoice = int(input("Enter warehouse number: "))
    
    #display existing sections to choose from
    num = 1
    for count in sections:
        print(str(num) + ". " + count)
        num+=1

    sectionsChoice = int(input("Enter section number: "))

    partName = input("Enter the part's name: ")
    quantity = int(input("Enter the quantity: "))

    #Read File to check reserved IDs
    f = open("parts.txt", "r")
    lines = f.readlines()
    count = 0
    for line in lines:
        count += 1
    #if no IDs exist, take the latest ID in sequence
    if (count == 0):
        id = 1
    else:
        id = findFileLength("parts.txt") + 1

    #There should be pre stored suppliers to link the part to them

    print("Choose one of the added suppliers")
    showSuppliers()
    whoSupply = int(input("Enter the supplier ID: "))
    #Check if Supplier ID exist
    f = open("suppliers.txt", "r")
    lines = f.readlines()
    for line in lines:
        rPart = json.loads(line)
        if (whoSupply == rPart[0]):
            break
    if (whoSupply != rPart[0]):
        print(rPart[0])
        print("Invalid Supplier ID!")
        return
    #The part list to be stored in part text file
    part = [id, partName, quantity, warehouses[warehouseChoice-1][2], sections[sectionsChoice-1], rPart[0]]
    #The list is converted to json for easier reading
    partJson = json.dumps(part)
    f = open("parts.txt", "a")
    f.writelines(partJson)
    f.writelines("\n")
    f.close()
    #The part's ID is added to the related supplier
    updateSupplier(whoSupply, id)
    print("The part has been added successfully...")
    
def updatePart():
    #Stocks are either increased or decresed based on sign passed in parameters
    print("1. Receive parts (Increase stock)")
    print("2. Provide parts (Decrease stock)")
    choice = int(input("Enter choice: "))
    if (choice == 1):
        updateInventory('+')
    elif (choice == 2):
        updateInventory('-')
    else:
        print("Invalid Choice!")

def trackPart():
    #Tracking menu
    print("1. Display availability")
    print("2. Display low stock parts")
    print("3. Display inventory in each section")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        displayAvailability()
    elif (choice == 2):
        displayLowStock()
    elif (choice == 3):
        displaySectionInventory()
    else:
        print("Invalid Choice!")

def searchMenu(): #Search menu
    print("1. Search by ID")
    print("2. Search supplier details by part")
    print("3. Search parts by a supplier")
    choice = int(input("Enter your choice: "))
    if (choice == 1):
        searchById()
    elif (choice == 2):
        searchSupDetails()
    elif (choice == 3):
        searchSupParts()
    else:
        print("Invalid Choice!")

def searchById():
    searchID = int(input("Enter the id to search: "))
    f = open("parts.txt", "r")
    lines = f.readlines()
    print("ID\t\tName\t\tWarehouse\t\tStock\t\tSection")
    #Check each line by line from the text file
    for line in lines:
        rPart = json.loads(line)
        if (rPart[0] == searchID):          #If the entered ID matches the ID of a line, it prints the result
            print(str(rPart[0]) + "\t\t" + rPart[1] + "\t\t" + rPart[3] + "\t\t\t" + str(rPart[2]) + "\t\t" + rPart[4])

def searchSupDetails():
    showParts()
    partID = int(input("Enter selected part ID: "))
    f = open("suppliers.txt", "r")
    lines = f.readlines()

    #After reading suppliers file, read the file line by line and break if match is found
    for line in lines:
        rPart = json.loads(line)
        if (partID in rPart[3]):
            break
    
    #Print Supplier details
    print("Part ID: " + str(partID))
    print("Supplier ID: " + str(rPart[0]))
    print("Supplier Name: " + rPart[1])
    print("Supplier Code: " + rPart[2])

def searchSupParts():
    #Display parts supplied by a particular supplier

    showSuppliers()
    supplierID = int(input("Enter selected Supplier ID: "))
    
    f = open("suppliers.txt", "r")
    lines = f.readlines()

    for line in lines:
        rPart = json.loads(line)
        if (rPart[0] == supplierID):    #Read line by line until match is found
            break

    partsList = rPart[3]        #Copy parts list of a specific supplier

    f = open("parts.txt", "r")
    lines = f.readlines()

    print("ID\t\tName\t\tQuantity\t\tSupplier ID\t\tWarehouse\t\tSection")

    for line in lines:
        lPart = json.loads(line)
        if (lPart[0] in partsList):     #Display parts supplier from only the list of a supplier
            print(str(lPart[0]) + "\t\t" + lPart[1] + "\t\t" + str(lPart[2]) + "\t\t\t" + str(lPart[5]) + "\t\t\t" + lPart[3] + "\t\t\t" + lPart[4])

def displayAvailability():
    #Display inventory stocks
    f = open("parts.txt", "r")
    lines = f.readlines()
    print("ID\t\tQuantity\tName")
    idCount = 1
    while (idCount <= findFileLength("parts.txt")):
        for line in lines:
            rPart = json.loads(line)
            if (rPart[0] == idCount):       #Display list where id matches
                print(str(rPart[0]) + "\t\t" + str(rPart[2]) + "\t\t" + rPart[1])
                idCount+=1

def displayLowStock():
    num = 1
    for count in warehouses:
        print(str(num) + ". " + count[2] + " (" + count[0] + ")")
        num+=1
    warehouseChoice = int(input("Enter warehouse number: "))
    #Search in a specific warehouse
    f = open("parts.txt", "r")
    lines = f.readlines()
    print("ID\t\tQuantity\tWarehouse\t\tName")

    for line in lines:
        rPart = json.loads(line)
        if (rPart[2] < 10 and warehouses[warehouseChoice-1][2] == rPart[3]):    #Display list where stocks is less than 10
            print(str(rPart[0]) + "\t\t" + '\033[91m' + str(rPart[2]) + '\033[0m' + "\t\t" + rPart[3] + "\t\t\t" + rPart[1])
                                        #Low stock is red-color coded

def displaySectionInventory():
    #Display inventory in each section by warehouse
    num = 1
    for count in warehouses:
        print(str(num) + ". " + count[2] + " (" + count[0] + ")")
        num+=1
    warehouseChoice = int(input("Enter warehouse number: "))
    
    f = open("parts.txt", "r")
    lines = f.readlines()

    num = 0
    while (num < len(sections)):
        print("\n----------------------" + sections[num] + "----------------------\n" )
        print("ID\t\tQuantity\tWarehouse\t\tName")

        for line in lines:
            rPart = json.loads(line)         #Results divided by each section in a warehouse
            if (warehouses[warehouseChoice-1][2] == rPart[3] and rPart[4] == sections[num]):
                print(str(rPart[0]) + "\t\t" + str(rPart[2]) + "\t\t" + rPart[3] + "\t\t\t" + rPart[1])
        num+=1

def updateInventory(sign):
    #The passed sign (+, -)
    id = int(input("Enter inventory ID: "))
    f = open("parts.txt", "r")
    lines = f.readlines()
    print("ID\t\tName\t\tWarehouse\t\tStock\t\tSection")
    #Display all parts to choose from
    for line in lines:
        rPart = json.loads(line)
        if (rPart[0] == id):
            print(str(rPart[0]) + "\t\t" + rPart[1] + "\t\t" + rPart[3] + "\t\t\t" + str(rPart[2]) + "\t\t" + rPart[4])
            break

    if (sign == '+'):
        rPart[2] += int(input("Enter the quantity you want to add: "))
    elif (sign == '-'):
        rPart[2] -= int(input("Enter the quantity you want to reduce: "))

    #Copy all content to a temp text file except the updated one
    with open("parts.txt") as f:
        with open("temp.txt", "w") as f1:
            for line in f:
                lPart = json.loads(line)
                if (lPart[0] != id):
                    f1.write(line)

    #Copy the copied content back to the original file
    with open("temp.txt") as f:
        with open("parts.txt", "w") as f1:
            for line in f:
                f1.write(line)

    #Add the updated content
    partJson = json.dumps(rPart)
    f = open("parts.txt", "a")
    f.writelines(partJson)
    f.writelines("\n")
    f.close()

def addSupplier():
    #Add supplier details
    supplierName = input("Enter supplier name: ")
    supplierCode = input("Enter supplier code: ")

    f = open("suppliers.txt", "r")
    lines = f.readlines()
    
    count = 0
    for line in lines:
        count += 1

    if (count == 0):
        id = 1
    else:
        id = findFileLength("suppliers.txt") + 1
    
    suppliedParts = []      #Will be filled by each part entry
    supplier = [id, supplierName, supplierCode, suppliedParts]      #The list to be appended

    #Converted to json to store in file
    partJson = json.dumps(supplier)
    f = open("suppliers.txt", "a")
    f.writelines(partJson)
    f.writelines("\n")
    f.close()

    print("The supplier has been added successfully...")

def showSuppliers():
    #Display all existing suppliers
    f = open("suppliers.txt", "r")
    lines = f.readlines()
    print("ID\t\tSupplier Code\t\tSupplier Name")

    for line in lines:
        rPart = json.loads(line)
        print(str(rPart[0]) + "\t\t" + str(rPart[2]) + "\t\t\t" + rPart[1])

def updateSupplier(supplierID, partID):
    #Supplier ID and part ID passed
    f = open("suppliers.txt", "r")
    lines = f.readlines()

    #Read line by line until the supplier match is found
    for line in lines:
        rPart = json.loads(line)
        if (rPart[0] == supplierID):
            break

    #Copy all suppliers info into temp file except the updated one
    with open("suppliers.txt") as f:
        with open("temp.txt", "w") as f1:
            for line in f:
                lPart = json.loads(line)
                if (lPart[0] != supplierID):
                    f1.write(line)

    #Copy suppliers info back to original file
    with open("temp.txt") as f:
        with open("suppliers.txt", "w") as f1:
            for line in f:
                f1.write(line)

    #Append the part ID to supplier list
    rPart[3].append(partID)

    #Append the updated list
    partJson = json.dumps(rPart)
    f = open("suppliers.txt", "a")
    f.writelines(partJson)
    f.writelines("\n")
    f.close()

def showParts():
    #Display all parts information
    f = open("parts.txt", "r")
    lines = f.readlines()
    print("ID\t\tName\t\tQuantity\t\tSupplier ID\t\tWarehouse\t\tSection")

    for line in lines:
        rPart = json.loads(line)
        print(str(rPart[0]) + "\t\t" + rPart[1] + "\t\t" + str(rPart[2]) + "\t\t\t" + str(rPart[5]) + "\t\t\t" + rPart[3] + "\t\t\t" + rPart[4])

def findFileLength(filename):
    #Return the number of lines in a text file
    with open(filename) as f:
        for n, l in enumerate(f):
            pass
        return n + 1

mainMenu()
