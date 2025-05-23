'''
script: Project 2: adding student information
action: a menu driven application that opens a file and reads employee data
        and now it opens a students.txt file and reads student data
author: Branden Duval
date: 04/18/2025
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

def getStudentScores(studentList):
    '''
    Function used to retrieve student scores from a text file
    
    action: opens the scores.txt file to read
            takes the course names from the header and saves them to a dictionary as a key
            continues to the next line where it stores the ID numbers and grades and stores them as a value
            matches IDs from the scores.txt file to the IDs from the student object
            
            '''

    with open('scores.txt', mode = 'r') as scores:
        for firstLine in scores:
            courseNameList = firstLine[2:].strip().split()
            for otherLines in scores:
                scoreRecords = otherLines.strip().split()
                idNumber = scoreRecords[0]
                for student in studentList:
                    if int(student._idNumber) == int(idNumber):
                        for i in range(len(courseNameList)):
                            courseName = courseNameList[i]
                            courseScore = scoreRecords[1:][i]
                            if courseName in Student.courseNameList:
                                coursesDict = {courseName : courseScore}
                                student.coursesStudentDict.update(coursesDict)
                        print(f'Adding scores for {student._firstName} {student._lastName}...')
    return


# function used to display all given information of an employee
def displayEmployeeEmploymentInformation(employeeList):
    print(f'{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}{'HireDate':<20}{'Classification':<20}{'Role':<10}{'Salary':<10}') # prints a formatted header
    for employee in employeeList: # for every employee added to the list in the last function
        # prints a formatted string containing the provided information
        print(f'{employee._lastName:<20}{employee._firstName:<20}{employee._idNumber:<10}{employee._emailAddress:<40}{employee._phoneNumber:<20}{employee._hireDate:<20}{employee._classificationPerson:<20}{employee._rolePerson:<10}{employee._annualSalary:<10.2f}')

# function used to display only the contact information of an employee
def displayEmployeeContactInformation(employeeList):
    print(f'{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}') # prints a formatted header with only the contact info
    for employee in employeeList: # for every employee in the created employee list
        # print a formatted string containing the contact information provided
        print(f'{employee._lastName:<20}{employee._firstName:<20}{employee._idNumber:<10}{employee._emailAddress:<40}{employee._phoneNumber:<20}')

# function used to display only the contact information of students
def displayStudentContactInfo(studentList):
    # prints a formatted header
    print(f'{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}')
    # prints the formatted string containing student contact info
    for student in studentList:
        print(f'{student._lastName:<20}{student._firstName:<20}{student._idNumber:<10}{student._emailAddress:<40}{student._phoneNumber:<20}')

# displays only the contact information of every person entered into the txt files
def displayAllPersonContactInformation(employeeList, studentList):
    # list declared, concatenates the previous 2 lists into one big list
    personList = employeeList + studentList
    # prints the header
    print(f'{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Email':<40}{'Phone':<20}')
    # prints the formatted information of each person
    for person in personList:
        print(f'{person._lastName:<20}{person._firstName:<20}{person._idNumber:<10}{person._emailAddress:<40}{person._phoneNumber:<20} ')

def displayStudentScores(studentList):
    getStudentScores(studentList)
    print(f'{'Student Academic Scores':>60}')
    print(f'{'LastName':<20}{'FirstName':<20}{'ID':<10}{'Art':<10}{'Greek':<10}{'Latin':<10}{'Science':<10}{'Mathematics':<10}')
    for student in studentList:
        print(f'{student._lastName:<20}{student._firstName:<20}{student._idNumber:<10}{student.coursesStudentDict['Art']:<10}{student.coursesStudentDict['Greek']:<10}{student.coursesStudentDict['Latin']:<10}{student.coursesStudentDict['Science']:<10}{student.coursesStudentDict['Mathematics']:<10}') 
        
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
        print('Please select an option below\n')
        print('1. Quit')
        print('2. Display Employee Employment Information')
        print('3. Display Employee Contact Information')
        print('4. Display Student Contact Information')
        print('5. Display All Person Contact Information')
        print('6. Display Student Academic Scores.')
        menuInput = int(input('> '))
        if menuInput == 1: # ends the program
            print('\nThank you for using the system.\n\nNow exiting the program...')
            break # if 1 is entered, break
        if menuInput == 2: # opens the employment info screen
            print(f'{'Employee Employment Information':>100}\n') # kind of just guessing where the middle would be
            displayEmployeeEmploymentInformation(employeeList) # calls the function that displays the employee employment info with the employeeList passed into it
        if menuInput == 3: # opens the contact info screen
            print(f'{'Employee Contact Information':>60}\n') # also guessing here, not entirely sure if there is a command or some secret math I dont know about
            displayEmployeeContactInformation(employeeList) # calls the function that displays the employee contact info with the employeeList passed into it
        if menuInput == 4:
            # thought I cracked the code by doing length of this print statement divided by 2 added to the formatted string within the function / 2
            print(f'{'Student Contact Information':>60}') # but eyeballing and vibes based assessments seemed to be the way to go
            displayStudentContactInfo(studentList)
        if menuInput == 5:
            print(f'{'All Person Contact Information':>60}') # 60 seems to be the magic number for these last print statements
            displayAllPersonContactInformation(employeeList, studentList)
        if menuInput == 6:
            displayStudentScores(studentList)
        if menuInput < 1 or menuInput > 6: # can easily be changed later to utilize and else statement, but it looks like this for now
            print(f'I am sorry, {menuInput} is not an option.\n\n') # tells the user that what they had entered is not a valid option

# used to call the functions and starts the program
employeeList = getEmployees()
studentList = getStudents()
getStudentScores(studentList)
createMenu(employeeList, studentList)