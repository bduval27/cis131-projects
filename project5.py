'''
script: Project 5: Sorting
action: a menu driven application that opens a file and reads employee data
        and now it opens a students.txt file and reads student data
        opens the scores.txt file and displays student academic info
        added functionality for student search by ID
        displays which students are eligible for honor roll
        displays student information sorted by last name
        displays sutdent information sorted by student ID
author: Branden Duval
date: 05/16/2025
'''

# importing necessary modules
from abc import ABC, abstractmethod
from datetime import date

# abstract base class
class Person(ABC):
    # initialization function
    def __init__(self, lastName = 'Null', firstName = 'Null', idNumber = 0, emailAddress = 'Null', phoneNumber = 'Null'):
        self._lastName = lastName # inherited
        self._firstName = firstName # inherited
        self._idNumber = idNumber # inherited, uneditable
        self._emailAddress = emailAddress # inherited
        self._phoneNumber = phoneNumber # inherited

    @abstractmethod
    def __str__(self):
        return(f'Employee: {self._lastName}, {self._firstName}, ID: {self._idNumber}, Email: {self._emailAddress}, Phone: {self._phoneNumber}')
    
    @abstractmethod
    def __repr__(self):
        return(f'Employee: {self._lastName}, {self._firstName}, ID: {self._idNumber}, Email: {self._emailAddress}, Phone: {self._phoneNumber}')

# concrete sublcass  
class Employee(Person):
    
    # dictionaries for later 
    roleDictionary = {'001': 'Staff', '002': 'Faculty'}
    classificationDictionary = {'001': 'Full', '002': 'Part'} # instructions say 'Full-Time' and 'Part-Time,' but the txt document provided only uses 'Full' and 'Part'
    
    # initializing function, date time set for 01/01/1970 epoch
    def __init__(self, lastName = 'Null', firstName = 'Null', idNumber = 0, emailAddress = 'Null', phoneNumber = 'Null', hireDate = date(1970, 1, 1), classificationPerson = 'Null', rolePerson = 'Null', annualSalary = 0):
        super().__init__(lastName, firstName, idNumber, emailAddress, phoneNumber) # inherited from base class 
        self._hireDate = hireDate
        self._rolePerson = rolePerson
        self._classificationPerson = classificationPerson
        self._annualSalary = annualSalary

    @property
    def hireDate(self):
        return self._hireDate
    
    @hireDate.setter
    def hireDate(self, hireDate):
        if hireDate is not int: # checks for integers if an object is created
            print('Hire Date must be entered as an integer in the form of "0000/00/00')
        
        self._hireDate = hireDate

    @property
    def rolePerson(self):
        return self._rolePerson
    
    @rolePerson.setter
    def rolePerson(self, rolePerson):
        if rolePerson not in Employee.roleDictionary.values(): # checks for the values in the dictionary if an object is created
            print('Invalid employee role.')

        self._rolePerson = rolePerson

    @property
    def classificationPerson(self):
        return self._classificationPerson
    
    @classificationPerson.setter
    def classificationPerson(self, classificationPerson):
        if classificationPerson not in Employee.classificationDictionary.values(): # checks for the values in the dictionary if an object is created
            print('Invalid employee classification.')

        self._classificationPerson = classificationPerson

    @property
    def annualSalary(self):
        return self._annualSalary
    
    @annualSalary.setter
    def annualSalary(self, annualSalary):
        if annualSalary is not float: # checks for floats if an object is created
            print('Annual salary must be a value with a decimal.')
        
        if annualSalary < 0: # check for negative integers if an object is created
            print('Annual salary must not be negative.')

        self._annualSalary = annualSalary
    
    # string representation for Employee subclass
    def __str__(self):
        return(f'Employee (Name: {self._lastName, self._firstName}, Classification: {self._classificationPerson}, Role: {self._rolePerson}, Annual Salary: {self._annualSalary:.2f})')
    
    # string representation for Employee subclass
    def __repr__(self):
        return(f'Employee (Name: {self._lastName, self._firstName}, Classification: {self._classificationPerson}, Role: {self._rolePerson},Annual Salary: {self._annualSalary:.2f})')

# concrete subclass
class Student(Person):

    courseNameList = ['Art', 'Latin', 'Greek', 'Mathematics', 'Science', 'Painting', 'Sculpting']

    def __init__(self, lastName = 'Null', firstName = 'Null', idNumber = 0, emailAddress ='Null', phoneNumber ='Null'):
        super().__init__(lastName, firstName, idNumber, emailAddress, phoneNumber)
        self._coursesStudentDict = {'courseName':'Score'}

    @property
    def coursesStudentDict(self):
        return self._coursesStudentDict
    
    @coursesStudentDict.setter
    def coursesStudentDict(self, coursesStudentDict):

        self._coursesStudentDict = coursesStudentDict

    # string representation for student subclass
    def __str__(self):
        return(f'Student (Name: {self._lastName, self._firstName}, ID: {self._idNumber}, Email: {self._emailAddress}, Phone: {self._phoneNumber} )')
    
    # string representation for student subclass
    def __repr__(self):
        return(f'Student (Name: {self._lastName, self._firstName}, ID: {self._idNumber}, Email: {self._emailAddress}, Phone: {self._phoneNumber} )')

# the meat of the program
def getEmployees():
    '''
    Function used to get and record the Employee Data
    
    action: opens the employees.txt file
            manipulates the data within the file
            stores the data within a list
    input:  data from the text file
    output: employee data into employeeList
    return: employeeList
    '''

    employeeList = [] # empty list to store employee information
    
    with open('employees.txt', mode='r') as employees: # opens the employees.txt file to read
        next(employees) # skips the header, thank you StackOverflow user 'wim'
        print('Starting application...\n') # displays a message when the program gets to work
        print('Adding employees...\n') # displays a follow up message telling the user that it is adding employees to the list
        for line in employees: # for each line in the employees.txt file
            records = line.strip().split() # sets a variable as the lines stripped and split of anything that is not a letter
            
            # throws these variables into records after being split
            firstName, lastName, idNumber, emailAddress, phoneNumber, hireDate, classificationPerson, rolePerson, annualSalary = records
            
            if rolePerson not in Employee.roleDictionary.values(): # if the role provided isnt within the dictionary...
                print(f'Invalid Role ({rolePerson}) for {lastName}, {firstName}. Skipping...') # ...show which entry it is and skip it...
                continue # ...and then move onto the next entry

            if classificationPerson not in Employee.classificationDictionary.values(): # if the classification isnt within the dictionary...
                print(f'Invalid Classification ({classificationPerson}) for {lastName}, {firstName}. Skipping...') # ... show which entry it is and skip it...
                continue # ...and then move onto the next entry

            try:
                annualSalary = float(annualSalary) # sets annual salary to a float
                if annualSalary < 0: # if annual salary is negative...
                    print('Invalid salary amount, annual salary cannot be negative. Skipping.') # ... skip the data...
                    continue # ...and move on
            except ValueError: 
                print('Invalid Data, skipping...') # skips incorrect values
                continue # and moves on
            
            employee = Employee(firstName, lastName, idNumber, emailAddress, phoneNumber, hireDate, classificationPerson, rolePerson, annualSalary) # builds the object as variable 'employee'
            employeeList.append(employee) # throws the new employee variable into the empty list created earlier 
            print(f'Adding employee {employee._firstName} {employee._lastName}...') # displays a message when adding an employee to the list

    return employeeList # returns the now filled list so that we can manipulate it in the following functions

def getStudents():
    '''
    Function used to get and record student information
    
    action: opens a file titled students.txt
            manipulates the data within the file
            stores the data within a new list
    input:  data from the provided text files
    output: student information into studentList
    return: none
    '''
    
    # declared empty list to store information
    studentList = []

    # opens the students.txt file to read the information
    with open('students.txt', mode = 'r') as students:
        next(students) # skips the header of the txt file
        print('\nAdding Students...\n') # tells the user that it is doing its job
        for line in students: # for each line in the students.txt file
            studentRecords = line.strip().split() # strips unneeded characters and splits the data up
            
            # stores the variables within studentRecords
            firstName, lastName, idNumber, emailAddress, phoneNumber = studentRecords
            
            # creates a Student object and stores it as student
            student = Student(firstName, lastName, idNumber, emailAddress, phoneNumber)
            studentList.append(student) # throws the object into a list
            print(f'Adding student {student._firstName} {student._lastName}...') # tells the user that it is doing its job by specifying which student is being added

    return studentList # returns a filled list with student information

def getStudentAcademicReport(student):
    '''
    Function used to retrieve student scores from a text file
    
    action: opens the scores.txt file to read
            takes the course names from the header and saves them to a dictionary as a key
            continues to the next line where it stores the ID numbers and grades and stores them as a value
            matches IDs from the scores.txt file to the IDs from the student object
            collects the matching IDs and student info and tacks them on to the academic info
    input:  data from the scores.txt file as well as student list
    output: academic info into a dictionary
    return: a tuple for later use within the display functions
    '''
    # print('\nAdding Student Scores...\n')
    # print(f'Adding scores for {student._firstName} {student._lastName}...') # provides a message to the user 
    with open('scores.txt', mode = 'r') as scores: # opens the text file as read
        # print('\nAdding Student Scores...\n')
        # print(f'Adding scores for {student._firstName} {student._lastName}...') # provides a message to the user 
        for firstLine in scores: # for the header within the text file
            courseNameList = firstLine[2:].strip().split() # skip ID and clean up the string
            for otherLines in scores: # for everything after the header
                scoreRecords = otherLines.strip().split() # stores a cleaned up version of otherLines as scoreRecords
                idNumber = scoreRecords[0] # identifies ID number as the first column of numbers within the text file

                if int(student._idNumber) == int(idNumber): # if their ID is found within the scores.txt file
                    # print(f'Adding scores for {student._firstName} {student._lastName}...') # provides a message to the user
                    for i in range(len(courseNameList)): # for whatever amount of courses found within the scores.txt file
                        courseName = courseNameList[i] # stores the ith courseName from whatever loop
                        courseScore = scoreRecords[1:][i] # stores the ith course score from the scoreRecords list, barring ID

                        if courseName in Student.courseNameList: # if the courseName from the txt file is found within the courseNameList in the student object
                            coursesDict = {courseName : courseScore}
                            student.coursesStudentDict.update(coursesDict)
                    
                    # converts the value for each grade key to an int and if no course names are found, it converts them to 0
                    artGrade = int(student.coursesStudentDict.get('Art', 0))
                    greekGrade = int(student.coursesStudentDict.get('Greek', 0))
                    latinGrade = int(student.coursesStudentDict.get('Latin', 0))
                    scienceGrade = int(student.coursesStudentDict.get('Science', 0))
                    mathGrade = int(student.coursesStudentDict.get('Mathematics', 0))
                    
                    # temporary list
                    gradesReport = [artGrade, greekGrade, latinGrade, scienceGrade, mathGrade]

                    # uses the temporary list to do the math needed to find the high, low, and average grades
                    highestGrade = max(gradesReport)
                    lowestGrade = min(gradesReport)
                    averageGrade = sum(gradesReport) / len(gradesReport)
                    
                    # determines the letter grade based on Pima's grading criteria
                    if averageGrade >= 90:
                        letterGrade = 'A'
                    elif averageGrade >= 80:
                        letterGrade = 'B'
                    elif averageGrade >= 70:
                        letterGrade = 'C'
                    elif averageGrade >= 60:
                        letterGrade = 'D'
                    else:
                        letterGrade = 'F'

                    studentTuple = student._lastName, student._firstName, student._idNumber, artGrade, greekGrade, latinGrade, scienceGrade, mathGrade, highestGrade, lowestGrade, averageGrade, letterGrade

    return tuple(studentTuple)

# new honor roll function
def getHonorRoll(studentTuple):
    '''
    Function to display which students have made honor roll

    action: searches for students who have an average A grade
            displays students who have an average A grade
    input:  none
    output: students that have made honor roll
    return: none
    '''
    studentTuple = () # temp tuple
    updateList = [] # temp list
    
    # header printer
    print(f"{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Art':<10}{'Greek':<10}{'Latin':<10}{'Science':<10}{'Math':<10}{'High':<10}{'Low':<10}{'Average':<10}{'Grade':<10}")
    for student in studentList: # for each student in studentList...
        studentTuple = getStudentAcademicReport(student) # ... call getStudentAcademicReport to find a student and their grades...
        updateList.append(studentTuple) # ... and then add it to the temp list
        
        for student in updateList: # for each student in the temp list...
            # ... unpack everything
            lastName, firstName, idNumber, artGrade, greekGrade, latinGrade, scienceGrade, mathGrade, highGrade, lowGrade, avgGrade, letterGrade = student

        if letterGrade == 'A': # looks for a student that has an A letter grade
            # and then prints out their information
            print(f"{lastName:<20}{firstName:<20}{idNumber:<10}{artGrade:<10}{greekGrade:<10}{latinGrade:<10}{scienceGrade:<10}{mathGrade:<10}{highGrade:<10}{lowGrade:<10}{avgGrade:<10}{letterGrade:<10}")

# new search function
def lookUpStudentAcademicRecord(studentList):
    '''
    Function used to search for students by ID

    action: asks for an ID number
            searches for an ID number
            if found, displays the corresponding student
            if not, backs out to the main menu
    input:  user input
    output: information regarding a student
    return: none
    '''
    studentTuple = () # temp tuple

    print('Please enter the ID of the student') # asks the user for a student ID
    IDinput = str(input('>> ')) # makes sure that the input is a string 
    for student in studentList: # for each student within the studentList
        if IDinput == student._idNumber: # try to match the user input ID number to an ID number on file
            print(f"\n{'Individual Student Report':>85}\n") # if a match is found...
            studentTuple = getStudentAcademicReport(student) # call the getStudentAcademicReport function and set it as studentTuple
        if IDinput == '-1': # if sentinel is entered
            print('\nThank you for using the system.\n\nNow exiting the program...') # prints a message
            break # ends the program, I haven't been able to get this to work though
    if not studentTuple: # if no ID is found within the studentTuple
        print('That is not an ID we have on record. Please try again or enter -1 to quit.') # prints a message telling the user that there is no such ID
    if studentTuple: # if it is found, display all student grade records
        firstName, lastName, idNumber, artGrade, greekGrade, latinGrade, scienceGrade, mathGrade, highGrade, lowGrade, avgGrade, letterGrade = studentTuple
        print(f"{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Art':<10}{'Greek':<10}{'Latin':<10}{'Science':<10}{'Math':<10}{'High':<10}{'Low':<10}{'Average':<10}{'Grade':<10}")
        print(f"{lastName:<20}{firstName:<20}{idNumber:<10}{artGrade:<10}{greekGrade:<10}{latinGrade:<10}{scienceGrade:<10}{mathGrade:<10}{highGrade:<10}{lowGrade:<10}{avgGrade:<10}{letterGrade:<10}")

# function used to display all given information of an employee
def displayEmployeeEmploymentInformation(employeeList):
    print(f"{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}{'HireDate':<20}{'Classification':<20}{'Role':<10}{'Salary':<10}") # prints a formatted header
    for employee in employeeList: # for every employee added to the list in the last function
        # prints a formatted string containing the provided information
        print(f'{employee._lastName:<20}{employee._firstName:<20}{employee._idNumber:<10}{employee._emailAddress:<40}{employee._phoneNumber:<20}{employee._hireDate:<20}{employee._classificationPerson:<20}{employee._rolePerson:<10}{employee._annualSalary:<10.2f}')

# function used to display only the contact information of an employee
def displayEmployeeContactInformation(employeeList):
    print(f"{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}") # prints a formatted header with only the contact info
    for employee in employeeList: # for every employee in the created employee list
        # print a formatted string containing the contact information provided
        print(f'{employee._lastName:<20}{employee._firstName:<20}{employee._idNumber:<10}{employee._emailAddress:<40}{employee._phoneNumber:<20}')

# function used to display only the contact information of students
def displayStudentContactInfo(studentList):
    # prints a formatted header
    print(f"{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}")
    # prints the formatted string containing student contact info
    for student in studentList:
        print(f'{student._lastName:<20}{student._firstName:<20}{student._idNumber:<10}{student._emailAddress:<40}{student._phoneNumber:<20}')

# displays only the contact information of every person entered into the txt files
def displayAllPersonContactInformation(employeeList, studentList):
    # list declared, concatenates the previous 2 lists into one big list
    personList = employeeList + studentList
    # prints the header
    print(f"{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}")
    # prints the formatted information of each person
    for person in personList:
        print(f'{person._lastName:<20}{person._firstName:<20}{person._idNumber:<10}{person._emailAddress:<40}{person._phoneNumber:<20} ')

# displays the students academic scores
def displayFullStudentAcademicReport(studentList):
    
    # temp tuple
    studentTuple = () 
    
    # temp lists
    updateList = []
    artList = []
    greekList = []
    latinList = []
    scienceList = []
    mathList = []

    print(f"{'Student Academic Scores':>80}") # moved this up here because I couldn't get it to work properly back down in the menu function, but they should probably all be within the display functions
    print(f"{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Art':<10}{'Greek':<10}{'Latin':<10}{'Science':<10}{'Math':<10}{'High':<10}{'Low':<10}{'Average':<10}{'Grade':<10}") # formatted string
    # for each student present within the student list...
    for student in studentList:
        studentTuple = getStudentAcademicReport(student) # ... call getStudentAcademicReport function and store the info as a tuple
        
        # throws the temp tuple into the temp list
        updateList.append(studentTuple)
        
        # identifies the art grade and does the math the find the high, low, and average 
        artList.append(studentTuple[3])
        artHigh = max(artList)
        artLow = min(artList)
        artAvg = sum(artList) / len(artList)
        
        # identifies the greek grade and does the math to find the high, low, and average
        greekList.append(studentTuple[4])
        greekHigh = max(greekList)
        greekLow = min(greekList)
        greekAvg = sum(greekList) / len(greekList)
        
        # identifies the latin grade and does the math to find the high, low, and average
        latinList.append(studentTuple[5])
        latinHigh = max(latinList)
        latinLow = min(latinList)
        latinAvg = sum(latinList) / len(latinList)
        
        # identifies the science grade and does the math to find the high, low, and average
        scienceList.append(studentTuple[6])
        sciHigh = max(scienceList)
        sciLow = min(scienceList)
        sciAvg = sum(scienceList) / len(scienceList)
        
        # identifies the math grade and does the math to find the high, low, and average
        mathList.append(studentTuple[7])
        mathHigh = max(mathList)
        mathLow = min(mathList)
        mathAvg = sum(mathList) / len(mathList)
    
    # for each student in the temp list
    for student in updateList:
        # unpack the info within the temp list
        lastName, firstName, idNumber, artGrade, greekGrade, latinGrade, scienceGrade, mathGrade, highGrade, lowGrade, avgGrade, letterGrade = student
        # display the student information
        print(f"{lastName:<20}{firstName:<20}{idNumber:<10}{artGrade:<10}{greekGrade:<10}{latinGrade:<10}{scienceGrade:<10}{mathGrade:<10}{highGrade:<10}{lowGrade:<10}{avgGrade:<10}{letterGrade:<10}")
    
    # displays the stats for each course; high, low, and average
    print(f"\nHigh {artHigh:>47}{greekHigh:>10}{latinHigh:>10}{sciHigh:>10}{mathHigh:>10}")
    print(f"Low {artLow:>48}{greekLow:>10}{latinLow:>10}{sciLow:>10}{mathLow:>10}")
    print(f"Average {artAvg:>44}{greekAvg:>10}{latinAvg:>10}{sciAvg:>10}{mathAvg:>10}")

# new function that displays student info sorted by last name
def displayFullAcademicReportSortedByLastName():
    sortStudentListByLastName(studentList)
    displayFullStudentAcademicReport(studentList)

# function that sorts the student list by last name
def sortStudentListByLastName(studentList):
    studentList.sort(key = lambda student: student._lastName) # got this from the python for beginners website and translated it to fit this program

# new function that displays student info sorted by student ID
def displayFullAcademicReportSortedStudentID():
    sortStudentListByStudentID(studentList)
    displayFullStudentAcademicReport(studentList)

# function that sorts the student list by student ID
def sortStudentListByStudentID(studentList):
    studentList.sort(key = lambda student: student._idNumber)

    
# opening menu function
def createMenu(employeeList, studentList):
    '''
    Menu function used to start the program
    
    action: asks the user what they would like to do within the program
    input:  user input
            employeeList
            studentList
    output: the information that is gathered from the rest of the program
    return: none
    '''
    
    # while loop for the options 
    while True:
        # changed this up from the first part because I think it looks neater
        print('\nPlease select an option below:\n')
        print('1. Quit')
        print('2. Display Employee Employment Information')
        print('3. Display Employee Contact Information')
        print('4. Display Student Contact Information')
        print('5. Display All Person Contact Information')
        print('6. Display Full Academic Report')
        print('7. Display Academic Report for one Student')
        print('8. Display Honor Roll')
        print('9. Display Full Academic Report Sorted By Last Name')
        print('10. Display Full Academic Report Sorted By Student ID')
        menuInput = int(input('> '))
        if menuInput == 1: # ends the program
            print('\nThank you for using the system.\n\nNow exiting the program...')
            break # if 1 is entered, break
        if menuInput == 2: # opens the employment info screen
            print(f"{'Employee Employment Information':>100}\n") # kind of just guessing where the middle would be
            displayEmployeeEmploymentInformation(employeeList) # calls the function that displays the employee employment info with the employeeList passed into it
        if menuInput == 3: # opens the contact info screen
            print(f"{'Employee Contact Information':>60}\n") # also guessing here, not entirely sure if there is a command or some secret math I dont know about
            displayEmployeeContactInformation(employeeList) # calls the function that displays the employee contact info with the employeeList passed into it
        if menuInput == 4:
            # thought I cracked the code by doing length of this print statement divided by 2 added to the formatted string within the function / 2
            print(f"{'Student Contact Information':>60}") # but eyeballing and vibes based assessments seemed to be the way to go
            displayStudentContactInfo(studentList)
        if menuInput == 5:
            print(f"{'All Person Contact Information':>60}") # 60 seems to be the magic number for these last print statements
            displayAllPersonContactInformation(employeeList, studentList)
        if menuInput == 6:
            displayFullStudentAcademicReport(studentList)
        if menuInput == 7:
            lookUpStudentAcademicRecord(studentList)
        if menuInput == 8:
            print(f"{'Honor Roll Report':>80}")
            getHonorRoll(studentList)
        if menuInput == 9:
            displayFullAcademicReportSortedByLastName()
        if menuInput == 10:
            displayFullAcademicReportSortedStudentID()
        if menuInput < 1 or menuInput > 10: # can easily be changed later to utilize an else statement, but it looks like this for now
            print(f'\nI am sorry, {menuInput} is not an option.\n') # tells the user that what they had entered is not a valid option

# used to call the functions and starts the program
employeeList = getEmployees()
studentList = getStudents()
createMenu(employeeList, studentList)