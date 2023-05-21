#HANNAH MEGHNA JOSHUA
#TP063243
def main():
    
    import datetime
    from datetime import date
#Admin Account Creation
    def CreateAdminAccount():
        adminLogin = []
        adminFname = input('Enter first name:')
        adminLname = input('Enter last name:')

        adminLogin.append(adminFname)
        adminLogin.append(adminLname)

        adminUserName = adminFname+'@HMJ'
        adminPass = adminFname+'123'

        print('Your username is:',adminUserName)#Creating default admin usernames and passwords
        print('Your password is:',adminPass)

        adminLogin.append(adminUserName)
        adminLogin.append(adminPass)

        adminLogin = str(adminLogin)[1:-1]
        adminLogin = adminLogin.replace("'","") #Since it is writing as a list, it is converted to a list without the speech marks and brackets
        adminLogin = adminLogin.replace(" ","")#The spaces before and after the text are removed so it doesnt affect the matching of data
        #Writing the credentials to a file
        with open('Admin Details.txt','a') as a:
            f = a.write(adminLogin)
            f = a.write(',')
            f = a.write('\n')
############################################################################################################################################
#Update Client Details
    def UpdateDetails():
        print('\n.........................UPDATE CLIENT DETAILS.........................')
        clientAccNum = input('Enter client account number:')

        found = False

        with open('ClientDetails.txt','r') as a:
            #Read the file with customer Details
            f = a.readlines()
            for i in f:

                updateDetails = list(i.split(","))#Make the lines to a list 

                if clientAccNum == updateDetails[9]:#Checks if the name matches the first item in the list 
                    found =  True#Used as a boolean to check if the name was found or not 
                    print('CLIENT FOUND')
                    #Admins have a choice of details to update
                    try:
                        update = input('What detail would you like to update?\n\
A: Email\n\
B: Phone Number\n\
C: Occupation\n\
D: Go Back to main page\n').upper()
                    except ValueError:
                        print('Invalid Input')
                    with open ('ClientDetails.txt','r') as a:
                        f1 = a.readlines()

                    if update == 'A':
                        emailSearch = input('Enter the updated email:')
                        email = updateDetails[5]

                        with open('ClientDetails.txt','r') as file:
                            
                            data = file.read()
                            data = data.replace(email,emailSearch)
                            
                        with open('ClientDetails.txt','w') as file:
                            file.write(data)
                        print('DETAILS HAVE BEEN UPDATED')

                    elif update == 'B':
                        phoneSearch = input('Enter the updated phone number:')
                        phone = updateDetails[6]

                        with open('ClientDetails.txt','r') as file:
                            data = file.read()
                            data = data.replace(phone,phoneSearch)
                        with open('ClientDetails.txt','w') as file:
                            file.write(data)
                        print('DETAILS HAVE BEEN UPDATED')

                    elif update == 'C':
                        occSearch = input('Enter the updated occupation:')
                        occupation = updateDetails[3]

                        with open('ClientDetails.txt','r') as file:
                            data = file.read()
                            data = data.replace(occupation,occSearch)
                        with open('ClientDetails.txt','w') as file:
                            file.write(data)
                        print('DETAILS HAVE BEEN UPDATED')
                    elif update == 'D' :
                        return AdminPortal()
                    else:
                        print('Invalid Value')
                        UpdateDetails()

                    cont1 = input('Do you want to update more details? Y/N').upper()
                    if cont1 == 'Y':
                        UpdateDetails()
                    elif cont1 == 'N':
                        AdminPortal()
                    
            if found == False:
                print('Client not found')
                AdminPortal()
###################################################################################################
#Register a Client
    def registration():
        clientInfo = []
        print('.........................Customer Registration Page.........................')
        firstName = str(input('Enter first name:'))
        
        lastName = str(input('Enter last name:'))
        clientInfo.append(firstName)
        clientInfo.append(lastName)

        while True:
            try:
                print('ENTER DATE OF BIRTH')
                birthYear = int(input('Enter the year YYYY :'))
                
                currentYear = datetime.datetime.now().year
                
                currentYear = int(currentYear)
                if birthYear > currentYear:
                    print('Please input a valid year')
                elif birthYear <= currentYear:
                    break
            except ValueError:
                print('Please enter a valid number')
                
        while True:
            try:
                birthMonth = int(input('Enter the month MM :'))
                if birthMonth>12:
                    print('Please input a valid month')
                elif birthMonth<=12:
                    break
            except ValueError:
                print('Please enter a valid number')
                
        while True:
            try:
                birthDay = int(input('Enter the day DD :'))
                if birthDay > 31:
                    print('Please enter a valid day number')
                elif birthDay<=31:
                    break
            except ValueError:
                print('Please enter a valid number')

        birthDate = datetime.date(birthYear,birthMonth,birthDay)
        
        dob = str(birthDate)
        clientInfo.append(dob)
        occupation = input('Enter occupation:')
        clientInfo.append(occupation)
        while True:#Validation
            pin =input('Enter 4 digit pin number to secure your account:')
            if (len(pin)) > 4:
                print('Too long. Pin must be 4 characters.')
            elif (len(pin)) < 4:
                print('Too short. Pin must be 4 characters.')
            elif (len(pin)) == 4:
                print('Valid pin entered')
                clientInfo.append(pin)
                break
        email = input('Enter E-mail ID:')
        clientInfo.append(email)
        phoneNum = input('Enter phone number:')
        clientInfo.append(phoneNum)
        while True:
            accountType = input('Do you want to create a savings account or a current account?\n\
\nMinimum Deposit for Savings account = 100RM\n\
Minimum Deposit for Current account = 500RM\n\
\nChoose S for savings or Choose C for current:').upper()

            if accountType == 'C' or accountType == 'S':
                break
            else:
                print('Invalid value')
        
        #Validation
        try:
            deposit = int(input('Enter the amount to deposit in RM:'))
        except ValueError:
            print('Please enter a valid amount(numerals)')
        #First deposit should meet the requirements of a savings account or a current account
        while True:
            if accountType == 'S' and deposit >= 100:
                print('Valid Deposit')
                clientInfo.append(accountType) 
                clientInfo.append(deposit)
                break
            elif accountType == 'S' and deposit < 100:
                print('Amount entered is below the limit of savings account')
                deposit = int(input('\nEnter the amount you want to deposit in RM:'))

            elif accountType == 'C' and deposit >= 500:
                print('Valid Deposit')
                clientInfo.append(accountType) 
                clientInfo.append(deposit)
                break

            elif accountType == 'C' and deposit < 500:
                print('Amount entered is below the limit of savings account')
                
                deposit = int(input('Enter the amount you want to deposit in RM:'))

            else:
                print('Invalid Value')
                accountType = input('Do you to create a savings account or a current account?\n\
Choose S for savings or Choose C for current:')
                deposit = int(input('Enter the amount you want to deposit in RM:'))
                    
                        
# Auto-generating accont numbers
        with open('Customer Account Number.txt','r') as a:
            f = a.read()
            f = int(f)
            newAccNum = f+20
            
            newAccNum = str(newAccNum)

        with open('Customer Account Number.txt','w') as a:
            f = a.write(newAccNum)
            startAccNum = newAccNum

        print('\nACCOUNT CREATED')

        print('\nTHESE ARE THE LOGIN CREDENTIALS')
        print('Your Account number is:',newAccNum)
        clientInfo.append(newAccNum)

                
        password = lastName[:3]+newAccNum[3:] #creating a default password

        print('Your password is:',password)
        clientInfo.append(password)
        #Writing the details into a text file. Each line is for 1 customer
        clientInfo = str(clientInfo)[1:-1]
        clientInfo = clientInfo.replace("'","")
        clientInfo = clientInfo.replace(" ","")

        with open('ClientDetails.txt','a') as a:
            f = a.write(clientInfo)
            f = a.write(',')
            f = a.write('\n')

        customerName = []
        
        customerName.append(firstName)
        customerName.append(newAccNum)

        #Writing their name to the text file 
        customerName = str(customerName)[1:-1]
        customerName = customerName.replace("'","")
        customerName = customerName.replace(" ","")

        with open('Customer Statements.txt','a')as a:
            f = a.write(customerName)
            f = a.write(',')#Appends a comma after the value is written
            f = a.write('\n')#Makes it a new line for the next input
            
###################################################################################################
#Menu once the Admin logs in 
    def AdminPortal():
        while True:
            try:
                adminChoice = input('..............................................\n\
Welcome to the HMJ portal!\n\
A: Register a customer\n\
B: Update Details\n\
C: Print Customer Statement of Account Report\n\
D: Go back to main page\n').upper()

                if adminChoice == 'A':
                    registration()
                    AdminPortal()
                elif adminChoice == 'B':
                    UpdateDetails()
                    return
                elif adminChoice == 'C':
                    statement()
                elif adminChoice == 'D':
                    main()
                else:
                    print('Invalid Value')
            except ValueError:
                print('Please input a valid value')
###################################################################################################
#Admin login Page
    def AdminLogin():
        print('\nADMIN LOGIN PAGE')
        adminName = input('Enter your name:')
        found = False
        with open('Admin Details.txt','r') as a:
            f = a.readlines()
            for i in f:
                
                login = list(i.split(","))#Changing the line in the file to a list to read each element

                if adminName == login[0]:

                    found = True
                    
                    while True:
                        #Looping until the values match the credentials in the list
                        print('\nENTER ADMIN LOGIN DETAILS TO ACCESS')
                        adminUser = input('Enter your Admin username:')
                        adminPass = input('Enter your Admin password:')
                        #Checks if the credentials match the default 
                        if adminUser == login[2] and adminPass == login[3]:
                            print('LOGIN SUCCESSFULL')
                            return AdminPortal()
                        else:
                            print('Wrong Credentials')

            if found == False:
                print('User not found!Try registering first')
                AdminLogin()
###################################################################################################
#Option to allow cstomers to deposit money into their account
    def CustomerDeposit(loginDetails):
        
        with open('ClientDetails.txt','r') as a:
            f = a.readlines()
            
            for i in f:
                #Changing the line in the file to a list to read each element
                clientLogin = list(i.split(","))
                if clientLogin[0] == loginDetails:
                    dt = date.today() #assigning today's date to variable to record the date the deposit took place
                    while True:
                        try:
                            deposit = int(input('How much RM would you like to deposit?'))
                            break
                        except ValueError:
                            print('Invalid Value')


                    with open('ClientDetails.txt','r') as a:
                        #Adding the money into the balance
                        f = a.read()
                        money = clientLogin[8]
                        money = int(money)  #Changing money to integer to calculate the balance after deposit
                        newAmount = money+deposit
                        newAmount = str(newAmount)
                        money = str(money)#CHanginf it back to string to write it to the file

                    #Updating the text file with the new balance
                    with open('ClientDetails.txt','r') as a:
                        data = a.read()
                        data = data.replace(money,newAmount)#Replacing the old balance with the new balance after deposit
                    with open('ClientDetails.txt','w') as file:
                        file.write(data)

                    print('DEPOSIT SUCCESSFUL!\n')

                    #Writing this activity to the text file for statements
                    deposit = str(deposit)
                    with open('Customer Statements.txt','r+') as a:
                        lines = a.readlines()
                        for i, line in enumerate(lines):
                            if line.startswith(loginDetails):
                                dt=str(dt)
                                lines[i] = lines[i].strip()+ dt+'/'+'Deposit|'+deposit+','
                            a.seek(0)
                            for line in lines:
                                a.write(line+'\n')
                            
                                
                    cont1 = input('Do you want to continue with our services? Y/N').upper()
                    if cont1 == 'Y':
                        CustomerMenu(loginDetails)
                    elif cont1 == 'N':
                        print('Thank you for banking with us! Have a great day')
                        main()
###################################################################################################
#Option to allow the customer to withdraw money from their balanace
    def CustomerWithdraw(loginDetails):
        with open('ClientDetails.txt','r') as a:
            f = a.readlines()
            for i in f:
                #Creating a list from the first like in the file 
                clientLogin = list(i.split(","))
                if clientLogin[0] == loginDetails:
                    dt = date.today()

                    while True:
                        try:#Excepts value error. Will print an error message if a differetn data type is entered 
                            withdraw = int(input('How much RM do you want to withdraw?'))
                            break
                        except ValueError:
                            print('Please input a valid number')

                    with open('ClientDetails.txt','r') as a:
                        #Deducting the withdrawal from the balance
                        data = a.read()
                        balance = clientLogin[8]#Reading values from the list made from the line
                        account = clientLogin[7]
                        balance = int(balance)
                        leftover = balance - withdraw
                        
                    #checking if the withdrawal matches the requirements of a savings and current account
                    if account == 'S' and leftover < 100:
                        print('Withdrawal failed!Your balance is less than 100RM after withdrawal')
                        CustomerWithdraw(loginDetails)
                    elif account == 'C' and leftover < 500:
                        print('Withdrawal failed!Your balance is less than 500RM after withdrawal')
                        CustomerWithdraw(loginDetails)
                    else:
                        balance = str(balance)
                        leftover = str(leftover)#Changing both variables to string to writr them back to the file 
                        print('Withdrawal Success')

                    #updating the new balance back to the file 
                    with open('ClientDetails.txt','r') as a:
                        data = a.read()
                        data = data.replace(balance,leftover)
                    with open('ClientDetails.txt','w') as file:
                        file.write(data)

                    #Writing the withdrawal activity to the statement text file
                    withdraw = str(withdraw)
                    with open('Customer Statements.txt','r+') as a:
                        lines = a.readlines()
                        for i, line in enumerate(lines):
                            if line.startswith(loginDetails):
                                dt=str(dt)
                                lines[i] = lines[i].strip()+ dt+'/'+'Withdrawn|'+withdraw+','
                            a.seek(0)
                            for line in lines:
                                a.write(line)
##                            a.write('\n')
                    cont2 = input('Do you want to continue with our services? Y/N').upper()
                    if cont2 == 'Y':
                        CustomerMenu(loginDetails)
                    elif cont2 == 'N':
                        print('Thank you for banking with us! Have a great day')
                        main()
###################################################################################################
#Option to check balance before or after transactions
    def CheckBalance(loginDetails):
        with open('ClientDetails.txt','r') as a:
            f = a.readlines()
            for i in f:
                clientLogin = list(i.split(","))
                if clientLogin[0] == loginDetails:

                    balance = clientLogin[8]

                    with open('ClientDetails.txt','r') as file:
                        f = file.readlines()
                        #Read the value and the index given to outut the balance
                        balance = clientLogin[8]
                        print('Your balance is:',balance,'RM')

                    cont3 = input('Do you want to continue with our services? Y/N')
                    if cont3 == 'Y' or cont3 == 'y':
                        CustomerMenu(loginDetails)
                    elif cont3 == 'N' or cont3 == 'n':
                        print('Thank you for banking with us! Have a great day')
                        return balance
                        main()
###################################################################################################
#Option to change and update customers passowords
    def ChangePassword(loginDetails):
        with open('ClientDetails.txt','r') as a:
            f = a.readlines()
            for i in f:
                
                clientLogin = list(i.split(","))
                
                if clientLogin[0] == loginDetails:
                    while True:
                        newPass = input('Enter your new password:')
                        if (len(newPass)) < 7:
                            #Ensuring password is string enough by length
                            print('Password is too weak')
                             
                        else:
                            print('Valid Password')
                            #Replace the updated value back to the file 
                            password = clientLogin[10]
                            with open('ClientDetails.txt','r') as file:
                                data = file.read()
                                data = data.replace(password,newPass)
                            with open('ClientDetails.txt','w') as a:
                                a.write(data)

                            cont4 = input('Do you want to continue with our services? Y/N')
                            if cont4 == 'Y' or cont4 == 'y':
                                CustomerMenu(loginDetails)
                            elif cont4 == 'N' or cont4 == 'n':
                                print('Thank you for banking with us! Have a great day')
                                main()
                            break
###################################################################################################
#Menu after Customer logs in 
    def CustomerMenu(loginDetails):
        while True:
            try:
                customerChoice = input('\nWhat would you like to do:\n\
A: Deposit Money\n\
B: Withdraw Money\n\
C: Check Balance\n\
D: Change Password\n\
E: Print Bank Statements\n\
F: Logout\n').upper()

                if customerChoice == 'A':
                    CustomerDeposit(loginDetails)
                elif customerChoice == 'B':
                    CustomerWithdraw(loginDetails)
                elif customerChoice == 'C':
                    CheckBalance(loginDetails)
                elif customerChoice == 'D':
                    ChangePassword(loginDetails)
                elif customerChoice == 'E':
                    statement()
                elif customerChoice == 'F':
                    print('Thank you for banking with us! Have a great day')
                    main()
                else:
                    print('Please enter a valid choice')
            except ValueError:
                print('Please input a valid option')
###################################################################################################
#Customer Login Page
    def CustomerLogin(loginDetails):
        with open('ClientDetails.txt','r') as a:
            f = a.readlines()
            for i in f:
                clientLogin = list(i.split(","))
                
                if clientLogin[0] == loginDetails:
                    username = input('Enter your username(account number):')
                    password = input('Enter you password:')

                    if username == clientLogin[9] and password == clientLogin[10]:
                        
                        print('LOGIN SUCCESSFULL!')
                        print('\nWELCOME',clientLogin[0],'!')
                        return CustomerMenu(loginDetails)
                        break
                        break
                    else:
                        print('Wrong Credentials')
                        CustomerLogin(loginDetails)
                        
###################################################################################################
#Finding Client from text file
    def FindClient():
        print('CLIENT LOGIN PAGE')
        loginDetails = input('Enter your name:')
        
        found = False
        
        with open('ClientDetails.txt','r') as a:
            f = a.readlines()
            for i in f:
                clientLogin = list(i.split(","))

                if loginDetails == clientLogin[0]:
                    
                    found = True
                    
                    print('CLIENT FOUND')
                    CustomerLogin(loginDetails)#passing loginDetails from another function to read the appropriate line in the file

        if found == False:        
            print('Your account does not exist. Try registering first')
            main()

        return loginDetails
###################################################################################################
#Printing out Customer Statements
    def statement():
        print('.........................CUSTOMER STATEMENT PRINTING PAGE.........................')
        found = False
        while found == False:
            name = input('Enter the name of the customer:')
            accountNum = input("Enter the customer's account number:")
            with open('Customer Statements.txt','r') as a:
                f = a.readlines()
                
                for i in f:

                    statements = list(i.split(","))

                    if name == statements[0] and accountNum == statements[1]:
                        found = True

                        #PROMTS AN INPUT FOR THE START DATE OF THE REPORT
                        print('ENTER THE START DATE FOR THE REQUIRED REPORT\n')
                        while True:
                            try:#Validates the input by checking if a different data type has been entered
                                startYear = int(input('Enter the year YYYY :'))
                                currentYear = datetime.datetime.now().year 
                                currentYear = int(currentYear)
                                if startYear > currentYear:
                                    print('Please input a valid year')
                                    
                                elif startYear <= currentYear:

                                    break
                            except ValueError:
                                print('Please enter a valid number')
                        while True:
                            try:
                                startMonth = int(input('Enter the month MM :'))
                                
                                if startMonth>12:
                                    print('Please input a valid month')
                                elif startMonth<=12:
                                    break
                                
                            except ValueError:
                                print('Please enter a valid number')                                    
                        while True:
                            try:
                                startDay = int(input('Enter the day DD :'))
                                if startDay > 31:
                                    print('Please enter a valid day number')
                                elif startDay <= 31:
                                    break
                            except ValueError:
                                print('Please enter a valid number')
                        #Combining the inputs to form a date
                        startDate = datetime.date(startYear,startMonth,startDay)
                        startDate = str(startDate)

                        #PROMTS AN INPUT FOR THE END DATE OF THE REPORT 
                        print('ENTER THE END DATE FOR THE REQUIRED REPORT\n')
                        while True:
                            try:#Validates the input by checking if a different data type has been entered
                                endYear = int(input('Enter the year YYYY :'))
                                currentYear = datetime.datetime.now().year
                                currentYear = int(currentYear)
                                if endYear > currentYear:
                                    print('Please input a valid year')
                                elif endYear <= currentYear:
                                    break
                            except ValueError:
                                print('Please enter a valid number')
                        # Took in inputs for each element of thr date to avoing logical errors
                        while True:
                            try:
                                endMonth = int(input('Enter the month MM :'))
                                if endMonth>12:
                                    print('Please input a valid month')
                                elif endMonth<=12:
                                    break
                            except ValueError:
                                print('Please enter a valid number')                                    
                        while True:
                            try:
                                endDay = int(input('Enter the day DD :'))
                                if endDay == 31:
                                    print('Please enter a valid day number')
                                elif endDay<=31:
                                    break
                            except ValueError:
                                print('Please enter a valid number')
                        #Combining the inputs to form a date
                        endDate = datetime.date(endYear,endMonth,endDay)
                        endDate = str(endDate)
                        found_flag = False
                        #Reading the list created from the line in the file
                        for j in statements:#For each element in the list
                            if j.startswith(startDate):#If the element starts with the date given
                                found_flag = True
                                start = statements.index(j)#Store the index in a variable
                                break
                            else:
                                found_flag = False
                        for h in reversed(statements):#For each element in the list reading from the end
                            if h.startswith(endDate):#Store the index in a variable
                                found_flag = True
                                end = statements.index(h)+1
                                break
                            else:
                                found_flag = False

                        if found_flag == True:
                            current = statements[start:end]# Creating a variable to state the start and end index needed to be printed

                            deposit = []
                            withdraw = []  #Lists crested to store the statements 

                            for i in current:#Looping through the list
                                index = i.index('/')#Finding the / symbol and getting thr index as it is used a separator
                                index = index+1#Adding one to that index since we need to check if it deposit or withdraw
                                typeof = i[index]

                                if typeof == 'W':#If that index is W
                                    index2 = i.index('|')#Find the | symbol in that element  
                                    index2 = index2+1#Add 1 to the index
                                    length = len(i)#To get the index of the very last character in the string
                                    amount = i[index2:length]#Assigning the amount to a variable for later calculations
                                    amount = int(amount)#Make it an interger to perform calculations
                                    withdraw.append(amount)#Append it to a list

                                elif typeof == 'D':
                                    index2 = i.index('|')
                                    index2 = index2+1
                                    length = len(i)
                                    amount = i[index2:length]
                                    amount = int(amount)
                                    deposit.append(amount)
                            with open('ClientDetails.txt','r') as a:
                                f = a.readlines()
                                for i in f:
                                    clientLogin = list(i.split(","))

                                balance = clientLogin[8]
                            print('\nCUSTOMER ACCOUNT REPORT\n\
CUSTOMER NAME:',name,'\n\
ACCOUNT NUMBER:',accountNum,'\n')
                            print(*statements[start:end],sep='\n')#Printing them in different lines
                            print('You have deposited a total of:',sum(deposit))#Prints the sum of the list of amounts
                            print('You have withdrawn a total of:',sum(withdraw))
                            print('Total Balance:',balance,'RM')
                        elif found_flag == False:
                            print('No transactions have taken place')
            if found == False:
                print('Customer does not exist')
###################################################################################################
#Super User Login to create admin accounts
        
    def SuperUser():#Super User account to create admin accounts
        superID = '1'#Super user account userame
        superPass ='2'#Super user account password
        print('ONLY SUPER USERS ALLOWED\n')
        while True:
            loginID = input('Enter SUPER USER username:')
            loginPass = input('Enter SUPER USER password:')

            if loginID == superID and loginPass == superPass:
                print('\nADMIN ACCOUNT CREATION PAGE')
                CreateAdminAccount()
                main()
                break
            else:
                print('Wrong credentials used.Try again')
    try:               
        choice = input("\n......................................Welcome to HMJ Bank......................................\n\
In order to create an admin account you have to be a Super User\n\
If you are a registered admin choose option B and you will be allowed to create customer accounts\n\
If you are a registered customer please choose Option C. \n\
If you are not a registered customer, please register yourself first with the help of an admin\n\
\nPlease choose a service\n\
A: Create an Admin Account\n\
B: Login as Admin\n\
C: Login as Customer\n")
        #Choices are availabe for the user to pick
        if choice == 'A' or choice == 'a':
            SuperUser()
        elif choice == 'B' or choice == 'b':
            AdminLogin()
            AdminPortal()
        elif choice == 'C' or choice == 'c':
            FindClient()
        else:
            print('Invalid Value!')
            main()
    except ValueError:
        print('Please enter a valid input')

main()
