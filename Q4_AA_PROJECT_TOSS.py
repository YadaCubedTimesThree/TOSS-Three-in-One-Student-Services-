# Definitions

# START OF CLASS GRADE CALCULATOR
class GradeCalculator():
    
    def __init__(self, master):
        self.counter = 0
        self.error = 0
        self.grades = 0
        self.creditsTotal = 0
        self.master = master


    def gradeCalc(self):
        
        # Create the window itself
        self.gradeWindow = Toplevel(self.master)
        
        self.gradeWindow.geometry('500x500')
        self.gradeWindow.title("Grade Calculator")
        self.gradeWindow.config(background="#B3FFF8")

        self.gradeWindow.icon = PhotoImage(file='waling.png')
        
        enterSubject = Label(self.gradeWindow, text="--Amount of Subjects")
        enterSubject.config(font=('Arial', 20), relief=RAISED, bd=20, padx=10, pady=10)
        enterSubject.place(x=150, y=10)
        
        self.amountSubject = Entry(self.gradeWindow)
        self.amountSubject.config(font=('Arial', 20), relief=RAISED, bd=10, width=5)
        self.amountSubject.place(x=10, y=10)
        
        enter = Button(self.gradeWindow, text="Enter", command=self.getSubjectCount)
        enter.config(font=('Arial', 10), relief=RAISED, bd=10, width=5)
        enter.place(x=10, y=60)

    def getSubjectCount(self):
        
        # Get the amount of subjects
        
        try:
            # Close subjects entry
            self.amountSubjectGlobal = int(self.amountSubject.get())
            self.amountSubject.delete(0, END)
            self.amountSubject.config(state="disabled")
            
            # After closing the subjects entry, proceed to grades and credits
            self.gradeEnter()
            self.creditsEnter()
            
        except ValueError:
            
            # If input is wrong, make the text red
            
            self.amountSubject.config(fg="red")


    def gradeEnter(self):
        
        # Enter the grades

        enterGrade = Label(self.gradeWindow, text="--Grade in Subject")
        enterGrade.config(font=('Arial', 20), relief=RAISED, bd=20, padx=10, pady=10)
        enterGrade.place(x=150, y=120)
        
        self.subjectGrade = Entry(self.gradeWindow)
        self.subjectGrade.config(font=('Arial', 20), relief=RAISED, bd=10, width=5)
        self.subjectGrade.insert(0, "0")
        self.subjectGrade.place(x=10, y=140)


    def creditsEnter(self):
        
        # Enter the credits

        enterCredits = Label(self.gradeWindow, text="--Credits of Subject")
        enterCredits.config(font=('Arial', 19), relief=RAISED, bd=23, padx=10, pady=10)
        enterCredits.place(x=150, y=210)
        
        self.subjectCredits = Entry(self.gradeWindow)
        self.subjectCredits.config(font=('Arial', 20), relief=RAISED, bd=10, width=5)
        self.subjectCredits.insert(0, "1.0")
        self.subjectCredits.place(x=10, y=230)
        
        # Check if both grade and credit inputs are valid
        enterButton = Button(self.gradeWindow, text="Enter")
        enterButton.config(font=('Arial', 10), relief=RAISED, bd=10, width=5, command=self.recordGrade)
        enterButton.place(x=150, y=300)


    def recordGrade(self):
        
        # If inputs are valid, take the values and clear out the inputs
        
        if self.counter < int(self.amountSubjectGlobal):

            try:
                # This is where the inputs are validated
                gradeOfStudent = int(self.subjectGrade.get())
                creditOfSubject = round(float(self.subjectCredits.get()), 2)

                if (0 <= gradeOfStudent <= 100) and (creditOfSubject > 0):
                    
                    # Resetting and also taking the inputs
                    self.grades += (gradeOfStudent * creditOfSubject)
                    self.creditsTotal += creditOfSubject
                    self.counter += 1
                    
                    # Just for checking if the code works
                    print(gradeOfStudent)
                    print(creditOfSubject)
                    print(self.counter)
                    print(self.grades)
                    print(self.creditsTotal)
                    # Delete these later
                    
                    # Delete error message, if possible
                    if self.error == 1:
                        self.errorMessage.destroy()
                    
                    # Clear out entries
                    self.subjectGrade.delete(0, END)
                    self.subjectCredits.delete(0, END)
                    
                    # Reset the entries
                    self.subjectGrade.insert(0, "0")
                    self.subjectCredits.insert(0, "1.0")

                    self.subjectGrade.config(fg='black')
                    self.subjectCredits.config(fg='black')
                    
                    # Input again
                    self.gradeCalculation()

                else:
                    # Call error code
                    self.showError()

            except ValueError:
                # Call error code
                self.showError()


    def showError(self):
        
        # Error code
        self.subjectGrade.config(fg='red')
        self.subjectCredits.config(fg='red')

        self.errorMessage = Label(self.gradeWindow, text="Input in either field is invalid.")
        self.errorMessage.config(font=('Arial', 15), relief=RAISED, bd=2)
        self.errorMessage.place(x=150, y=340)

        self.error = 1


    def gradeCalculation(self):

        #GWA Formula
        userGWA = round((self.grades / self.creditsTotal), 2)

        # GWA Conversion
        match userGWA:
            case x if x >= 96:
                finalGWA = 1.00
            case x if x >= 90:
                finalGWA = 1.25
            case x if x >= 84:
                finalGWA = 1.5
            case x if x >= 78:
                finalGWA = 1.75
            case x if x >= 72:
                finalGWA = 2.00
            case x if x >= 66:
                finalGWA = 2.25
            case x if x >= 60:
                finalGWA = 2.50
            case x if x >= 55:
                finalGWA = 2.75
            case x if x >= 50:
                finalGWA = 3.00
            case x if x >= 40:
                finalGWA = 4.00
            case x if x < 40:
                finalGWA = 5.00
        
        # Close the inputs if all credits and grades have been entered
        if self.counter == int(self.amountSubjectGlobal):
            
            # Clear inputs
            self.subjectGrade.delete(0, END)
            self.subjectCredits.delete(0, END)
            
            # Close inputs
            
            self.subjectGrade.config(state="disabled")
            self.subjectCredits.config(state="disabled")
            
            # Check if user is failing or not, display GWA
            if finalGWA <= 3:
                totalGWA = Label(self.gradeWindow, text=f"GWA: {finalGWA} or {userGWA}")
                totalGWA.config(font=('Arial', 20), relief=RAISED, bd=5, fg='green')
                totalGWA.place(x=10, y=400)
            else:
                totalGWA = Label(self.gradeWindow, text=f"GWA: {finalGWA} or {userGWA} !FAILING!")
                totalGWA.config(font=('Arial', 20), relief=RAISED, bd=5, fg='red')
                totalGWA.place(x=10, y=400)
            
            # Reset variables for next run
            self.counter = 0
            self.error = 0
            self.grades = 0
            self.creditsTotal = 0
            
            # Exit message
            exitMessage = Label(self.gradeWindow, text="You may now exit the program.")
            exitMessage.config(font=('Arial', 10), relief=RAISED, bd=5)
            exitMessage.place(x=10, y=450)
            
# END OF CLASS GRADE CALCULATOR
    
    
class RequirementsTracker():
    
    def __init__(self):
        
        pass
        
    def receiveData():
        
        assignmentType = self.placeholder.get()
        assignmentDue = self.dates.get()
        subjectAssignment = self.subject.get()
        
    def reqsTracker(self):
        
        
        
        from tkcalendar import DateEntry
        
        reqsWindow = Toplevel()
        
        reqsWindow.geometry('500x500')
        reqsWindow.title('Requirements Tracker')
        reqsWindow.config(background="#B3FFF8")
        
        reqsWindow.icon = PhotoImage(file="waling.png")
        
        # Date entering
        self.dates = DateEntry(reqsWindow, date_pattern='yyyy-mm-dd')
        self.dates.config(font=('Arial',20))
        self.dates.place(x=280, y=10)
        
        #Subject Entering
        self.subject = Entry(reqsWindow)
        self.subject.config(font=('Arial', 20), relief=RAISED, bd=5, width = 10)
        self.subject.place(x=10, y=10)
        
        
        #Type Entering
        possibleTypes = ['FA','AA/SA','LT']
        
        # Creation of the selection menu 
        for i in range(len(possibleTypes)):
            selectType = Radiobutton(reqsWindow,text=possibleTypes[i], variable=self.placeholder, value=i, relief=RAISED, bd = 5)
            selectType.place(x=200,y=10+(i*25))
        
        #Enter
            
        enter = Button(reqsWindow, text="Enter All", command=receiveData)
        enter.place(x=10, y= 50)
        
    
        
        
    
def courseBrochure():
    from PIL import Image, ImageTk # For image creation
    
    #Course Window Creation
    courseWindow = Toplevel()
    
    courseWindow.geometry('1000x900')
    courseWindow.title("Course Brochure")
    courseWindow.config(background="#B3FFF8")

    courseWindow.icon = PhotoImage(file='waling.png')
    
    curriculum = Image.open("courseDescriptions.png")
    curriculum = curriculum.resize((800,300))
    
    curriculum2 = Image.open("courseDescriptions2.png")
    curriculum2 = curriculum2.resize((800,450))
    
    courseBrochure = ImageTk.PhotoImage(curriculum)
    courseBrochure2 = ImageTk.PhotoImage(curriculum2)
    
    # Placing the image itself
    curriculum = Label(courseWindow, image=courseBrochure, relief=RAISED, bd = 5)
    curriculum.image = courseBrochure
    curriculum.pack()
    
    curriculum2 = Label(courseWindow, image=courseBrochure2, relief=RAISED, bd = 5)
    curriculum2.image = courseBrochure2
    curriculum2.pack()
  
    
    

def readMe():
    
    # Window for the Read Me file in general
    
    readMeWindow = Toplevel()
    
    readMeWindow.geometry('500x500')
    readMeWindow.title("README")
    readMeWindow.config(background="#B3FFF8")

    readMeWindow.icon = PhotoImage(file='waling.png')
    
    
    #PLACEHOLDER text for the README file
    readMeFile = Label(readMeWindow, text="""This
text will serve as a placeholder
for the upcoming readme file.

Made with love, yadayadayada""")
    
    readMeFile.configure(font=('Arial', 8), relief=RAISED, bd = 6, fg = 'orange')
    readMeFile.place(x = 20,y = 20)
    
def gradeCalculator():
    
    # Just calling the class
    openGradeCalc = GradeCalculator(window)
    openGradeCalc.gradeCalc()
    
def requirementsTracker():
    
    openReqsTracker = RequirementsTracker()
    openReqsTracker.reqsTracker()
    
# MAIN CODE

from tkinter import *

# Window Creation
window = Tk()

window.geometry('700x500')
window.title("Three-in-One-Student-Services")
window.config(background="#B3FFF8")

icon = PhotoImage(file='waling.png')
window.iconphoto(True,icon)

# Text
label = Label(window,text="Welcome to TOSS!", font=('Arial', 30,'bold'),bg='white', relief=RAISED, bd = 10, padx = 5, pady = 5)
label.place(x=175,y=100)

# Menu Selection Buttons
#GRADE CALCULATOR
button = Button(window, text = 'Grade Calculator')
button.place(x=175, y = 200)
button.config(command=gradeCalculator)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

#REQS TRACKER
button = Button(window, text = 'Requirements Tracker')
button.place(x=175, y = 275)
button.config(command=requirementsTracker)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

#COURSE BROCHURE
button = Button(window, text = 'Course Brochure')
button.place(x=175, y = 350)
button.config(command=courseBrochure)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

button = Button(window, text = 'Read Me')
button.place(x=175, y = 420)
button.config(command=readMe)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

window.mainloop()

