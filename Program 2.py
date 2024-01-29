#This program will make a two dimensional list and check each students answers with the answer key.
#In the output it will display the students name, the number correct out of 12, their percent and the letter grade
def main():
    #Declare and initialize variables
    name = ""
    inFile = ""
    examList = []
    gradeList = []
    twoDimList = []
    index = 0
    examList, gradeList = OpenFiles(examList, gradeList) #This is a value returning function call that should return examList and gradeList
    
    Logic(examList, gradeList, FindLetterGrade)#This calls the logic function

def Logic(examList, gradeList,letterGrade):#Function header
    #Declare and initialize local vars
    count = 0
    name = []
    grade = 0
    gradeTotal = 0
    percentage = 0.00
    x = ""
    x = open("output.txt", "w")#This creates an output.txt file
    personName = ""
    WriteHeadings(x)#Function call for a  function that displays headers
    for line in range(len(examList)):#Outer loop for looping through each list in examList
        gradeTotal = 0#This resets the total grade for each student through
        grade = 0#this resets the point tracker for each student
        name.append(examList[line][0].split(","))#this splits each persons name at the comma
        personName = name[count][1] + " " + name[count][0]#This assigns the personName var to each persons name but the index's are flopped so it is First Last instead of Last First
        count += 1#Moves onto the next person
        for z in range(len(gradeList)):#Loops through gradeList
            if (gradeList[z] == examList[line][z+1]):#This loops through the answer key and compares it to each students answers
                grade += 1 #If the answer matches the answer key, it adds one to grade
        gradeTotal += grade#This keeps track of each persons total grade out of 12
        percentage = (gradeTotal/12)#This calculates each person's percent
        letterGrade = FindLetterGrade(percentage)#This calls a function to find the persons letter grade from the percentage
        
        x.write("{0:13s}{1:3s}{2:^9s}{3:3s}{4:^7,.1%}{5:3s}{6:^5s}".format(personName,"", str(gradeTotal) + " of 12","",percentage,"", letterGrade))#This writes to the output file the name of the student, correct out of 12, percent, and letter grade
        x.write("\n")#This writes a new line for the next student

    x.close()#This closes the output file

def OpenFiles(examList, gradeList):#This is a value returning function header
    #This function is to open input files and return examList and gradeList
    readMe = ""
    try:
        
        readMe = open("exam.txt", "r")#Opens the exam.txt file into readMe in read mode
        for line in readMe: #EOF loop
            examList.append(line.split())#Writes what is in the exam.txt file to examList but splits it so it becomes a two-dimensional list
        readMe.close()#Closes file
        readMe = open("key.txt", "r")#Opens the key.txt file into readMe in read mode
        for line in readMe:#EOF loop
            gradeList.append(line.rstrip("\n"))#writes whats in the file to gradeList
        readMe.close()#Closes file
    except IOError:#Exception handling
        print("One of the files 'exam.txt' or 'key.txt' is missing!")
        
    return examList, gradeList


def WriteHeadings(x):
    #This function will be used to write the output headers for the program
    x.write("{0:^13s}{1:3s}{2:^9s}{3:3s}{4:^7s}{5:3s}{6:^5s}".format("Student","", "Correct","", "Percent","", "Grade"))
    x.write("\n")
    x.write("{0:13s}{1:3s}{2:9s}{3:3s}{4:7s}{5:3s}{6:5s}".format("-------------","", "---------","", "-------","", "-----"))
    x.write("\n")

def FindLetterGrade(percentage):#This function is used to determine the letter grade from the percentage
    letterGrade = ""
    if percentage * 100 >= 90:
        letterGrade = 'A'
    elif percentage * 100 >= 80:
        letterGrade = 'B'
    elif percentage * 100 >= 70:
        letterGrade = 'C'
    elif percentage * 100 >= 60:
        letterGrade = 'D'
    else:
        letterGrade = 'F'
    return letterGrade #returns each students letter grade


main()#Call the main function
