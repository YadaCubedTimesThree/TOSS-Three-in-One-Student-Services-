# Definitions

# START OF CLASS GRADE CALCULATOR
class GradeCalculator():
    
    ### Calculate the grade, and then output a GWA, and also check if the person is failing or passing
    
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
        self.gradeWindow.title("TOSS - Grade Calculator")
        self.gradeWindow.config(background="#FFFFCC")

        self.gradeWindow.icon = PhotoImage(file='logo.png')
        
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
    
    ### Rank requirements by priority levels
    
    ### INIT
    def __init__(self):
        
        self.placeholder = IntVar()
        self.reqsWindow = Toplevel()
        
        # Defining the list
        self.assignmentsList = [ ]
        self.subjectsList = [ ]
        
        titleLabel = Label(self.reqsWindow, text = "Assignment Rankings:", font=('Arial',25), relief=RAISED, bd=10)
        titleLabel.place(x=20,y=170)
        
        self.placeholderText = Label(self.reqsWindow, text="MOST IMPORTANT ASSIGNMENT", font=('Arial',16), relief=RAISED, bd=5, fg = 'orange')
        self.placeholderText.place(x=20, y=250 * 1)
            
        self.placeholder2 = Label(self.reqsWindow, text="2ND MOST IMPORTANT ASSIGNMENT", font=('Arial',16), relief=RAISED, bd=5, fg = 'red')
        self.placeholder2.place(x=20, y=200 + 50 * 2)
            
        self.placeholder3 = Label(self.reqsWindow, text="3RD MOST IMPORTANT ASSIGNMENT", font=('Arial',16), relief=RAISED, bd=5, fg = '#dd0000')
        self.placeholder3.place(x=20, y=200 + 50 * 3)
        
        self.placeholderTexts = [self.placeholderText, self.placeholder2, self.placeholder3]
        
    def receiveData(self):
        
        from datetime import date
        
        # Checks if the input is empty or not, ends the function if it is empty
        if (not self.assignmentDesc.get().strip()):
            
            self.enter.config(fg='red')
            
            return None
        
        # Reset the enter button
        self.enter.config(fg='black')
        
        # Get the values from the inputs
        assignmentType = self.placeholder.get()
        assignmentDue = self.dates.get_date()
        subjectAssignment = self.subject.get()
        detailsAssignment = self.assignmentDesc.get()
        
        # Convert into days left
        dueDate = (assignmentDue - date.today()).days
        
        # How important the assignemnt is
        assignmentValue = dueDate - assignmentType
        
        # Append all needed data for the for loop
        self.assignmentsList.append((assignmentValue, subjectAssignment, detailsAssignment, assignmentType, assignmentDue))

        self.assignmentsList.sort()
        
        print(self.assignmentsList)
        
        counter = 0
        for value, subject, assignment, typeOfAssignment, date in self.assignmentsList:
            
            self.placeholderTexts[counter].config(text=f"{subject}, {assignment}, {self.possibleTypes[typeOfAssignment]}, {date}")
            counter += 1
            
            if counter == 3:
                break
            
            
        
            
        
    
    def reqsTracker(self):
           
        # Creation of the window
        
        # Need this for the date calculating stuff
        from tkcalendar import DateEntry
        
        self.reqsWindow.geometry('500x500')
        self.reqsWindow.title('TOSS - Requirements Tracker')
        self.reqsWindow.config(background="#B3FFAA")
        
        self.reqsWindow.icon = PhotoImage(file="logo.png")
        
        # Date entering
        self.dates = DateEntry(self.reqsWindow, date_pattern='yyyy-mm-dd')
        self.dates.config(font=('Arial',20))
        self.dates.place(x=280, y=10)
        
        #Assignment Entering
        self.assignmentDesc = Entry(self.reqsWindow)
        self.assignmentDesc.config(font=('Arial', 20), relief=RAISED, bd=5, width = 10)
        self.assignmentDesc.place(x=280, y= 50)
        
        placeholderLabel = Label(self.reqsWindow, text="Reqs Description:")
        placeholderLabel.config(font=('Arial', 8), relief=RAISED, bd=5)
        placeholderLabel.place(x=280,y=90)
        
        #Subject Entering
        self.subject = Entry(self.reqsWindow)
        self.subject.config(font=('Arial', 20), relief=RAISED, bd=5, width = 10)
        self.subject.place(x=10, y=10)
        
        #Default input
        self.subject.insert(0,'ADTech')
        
        
        #Type Entering
        self.possibleTypes = ['FA','AA/SA','LT']
        
        # Creation of the selection menu 
        for i in range(len(self.possibleTypes)):
            selectType = Radiobutton(self.reqsWindow,text=self.possibleTypes[i], variable=self.placeholder, value=i, relief=RAISED, bd = 5)
            selectType.place(x=200,y=10+(i*25))
        
        #Enter
        
        self.enter = Button(self.reqsWindow, text="Enter All", command=self.receiveData)
        self.enter.place(x=10, y= 50)
        
# END OF CLASS REQS CALCULATOR
        
        
# Sorry, this doesn't get a class it's just one function lol
def courseBrochure():
    
    #Course Window Creation
    courseWindow = Toplevel()
    
    courseWindow.geometry('650x500')
    courseWindow.title("TOSS - Course Brochure")
    courseWindow.config(background="#FFCCAA")

    courseWindow.icon = PhotoImage(file='logo.png')
    
    ### LIST OF ALL THE COURSES
    courses = [
    ("ADTech 1", "Art, Design and Technology: Basic Principles and Processes"),
    ("ADTech 2", "Art, Design and Technology: Resistant Materials and Electronics"),
    ("ADTech 3", "Art, Design and Technology: Exploring Technologies"),

    ("Biology 1", "Fundamentals of Biology 1"),
    ("Biology 2", "Fundamentals of Biology 2"),
    ("Biology 3", "Foundations of Molecular and Cellular Biology"),
    ("Biology 4", "Contemporary Biology"),
    ("Biology 5", "Biology for a Changing World"),

    ("Chemistry 1", "General Chemistry 1"),
    ("Chemistry 2", "General Chemistry 2"),
    ("Chemistry 3", "General Chemistry 3"),
    ("Chemistry 4", "Fundamentals of Organic and Biological Chemistry"),
    ("Chemistry 5", "Applied Chemistry"),

    ("Computer Science 1", "Introduction to Computing"),
    ("Computer Science 2", "Coding in a Connected World: Development of Computational Thinking Skills"),
    ("Computer Science 3", "Object-Oriented Programming 1"),
    ("Computer Science 4", "Object-Oriented Programming 2"),

    ("Earth Science 1", "Earth Systems, Energy, and Change"),

    ("English 1", "Communications Arts 1"),
    ("English 2", "Communications Arts 2"),
    ("English 3", "Communications Arts 3"),
    ("English 4", "Communications Arts 4"),
    ("English 5", "English for Academic and Professional Purposes: Oral and Written Communication"),
    ("English 6", "Science Communication"),

    ("Filipino 1", "Wika at ang Panitikang Pilipino"),
    ("Filipino 2", "Komunikasyon at ang Panitikang Pilipino"),
    ("Filipino 3", "Retorika, Pagsusuri at ang Noli Me Tangere"),
    ("Filipino 4", "Akademikong Pagsulat at ang El Filibusterismo"),
    ("Filipino 5", "Komunikasyong Makabagong Tungo sa Maka-Pilipinong Pananaliksik"),
    ("Filipino 6", "Maka-Pilipinong Pananaliksik sa Wika, Kultura, Agham at Teknolohiya"),

    ("Health 1", "Growth and Development, Mental and Emotional Health"),
    ("Health 2", "Family Health and Preventive Drug Education"),
    ("Health 3", "Safety Education, First Aid and Disease Prevention"),
    ("Health 4", "Consumer Health, Community and Environmental Health"),

    ("Mathematics 1", "Algebra 1"),
    ("Mathematics 2", "Algebra 2"),
    ("Mathematics 3", "Geometry"),
    ("Mathematics 4", "Algebra 3"),
    ("Mathematics 5", "Algebra 4"),
    ("Mathematics 6", "Differential Calculus"),
    ("Mathematics 7", "Integral Calculus"),
    ("Mathematics 8", "Linear Algebra"),

    ("Physics 1", "Introduction to Physics"),
    ("Physics 2", "Fundamentals of Physics 1"),
    ("Physics 3", "Fundamentals of Physics 2"),
    ("Physics 4", "Fundamentals of Physics 3"),
    ("Physics 5", "Calculus-Based and Computational Physics"),

    ("Research 1", "Research and Development 1: Proposal Writing and Implementation"),
    ("Research 2", "Research and Development 2: Validation, Synthesis, and Communication"),

    ("Statistics 1", "Data and Probability 1"),
    ("Statistics 2", "Data and Probability 2"),

    ("Social Science 1", "Philippine History"),
    ("Social Science 2", "World History"),
    ("Social Science 3", "Citizenship and Civic Education"),
    ("Social Science 4", "Governance and Sustainable Futures"),
    ("Social Science 5", "Basic Principles of Economics"),
    ("Social Science 6", "Community Development and Engagement"),

    ("Values Education 1", "Adolescent Living and Character Building"),
    ("Values Education 2", "Toward Adolescent Wholeness"),
    ("Values Education 3", "Values and Standards for a Meaningful Life"),
    ("Values Education 4", "The Thinking Person's Being and Becoming"),
    
]
    ### LIST END
    
    # Placing the text
    
    courseList = Listbox(courseWindow, width=80, height=30)
    
    for course, description in courses:
        
        courseList.insert(END, f"{course}, {description}")
        
    courseList.config(font=('Arial', 8), relief=RAISED, bd=10)
    courseList.place(x=10,y=10)
    
    header = Label(courseWindow, text="\n".join(" COURSE-BROCHURE "),font=('Arial', 15),justify='center', relief=RAISED, bd=15)
    header.place(x=580, y=20)
    
    header = Label(courseWindow, text="\n".join("SCROLL-DOWN-FOR-MORE"),font=('Arial', 10),justify='center', relief=RAISED, bd=15)
    header.place(x=520, y=50)
    
    
    
    

def readMe():
    
    # Window for the Read Me file in general
    
    readMeWindow = Toplevel()
    
    readMeWindow.geometry('500x500')
    readMeWindow.title("TOSS - README")
    readMeWindow.config(background="#B3FFF8")

    readMeWindow.icon = PhotoImage(file='logo.png')
    
    
    #PLACEHOLDER text for the README file
    readMe = Listbox(readMeWindow, width=100, height=50,font=('Arial', 7), relief=RAISED, bd=10)
    readMeText=("""# TOSS – Three-in-One Student Services #

 - A year-long Computer Science project designed to help PISAY students manage their academic life more efficiently.

***Features***

* Clean and simple interface
* Easy to use
* Fast and efficient
* Lightweight and compact

***USAGE***

### Grade Calculator

* Input your subjects, grades, and corresponding credits
* The program calculates your GWA automatically
* Exit after viewing results

### Requirements Tracker

* Input your requirements
* The app automatically ranks the top three most important assignments
* Note: Removing completed tasks and viewing the full list are planned features (prototype stage)

### Course Brochure

* View-only section
* You may scroll through the list

### README (In-App)

* Same as this, but in the app itself

## Notes

* This project is currently a prototype, no features are final
* There is a text-only prototype available, "Q3_AA_PROJECT_TOSS_GUI_NEEDED"

## Authors

Developed for the school-year wide CS 2 AA, by:
AVILLA, SAUL
CASTILLO, KHIANE
MANALO, ZETH
PAGILAGAN, CCI
YUSON, YANNA
""")
    
    # Split every line of text into actual lines of text for the scroll box
    for line in readMeText.split("\n"):
        
        readMe.insert(END, line)

    readMe.pack()
    
    
def gradeCalculator():
    
    # Just calling the class, as it's unaccessable via just command
    openGradeCalc = GradeCalculator(window)
    openGradeCalc.gradeCalc()
    
def requirementsTracker():
    
    # Same as gradeCalculator()
    openReqsTracker = RequirementsTracker()
    openReqsTracker.reqsTracker()
    
# MAIN CODE

from tkinter import *

# Window Creation
window = Tk()

window.geometry('500x500')
window.title("Three-in-One-Student-Services")
window.config(background="#B3FFF8")

icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)

# Text
label = Label(window,text="Welcome to TOSS!", font=('Arial', 30,'bold'),bg='white', relief=RAISED, bd = 10, padx = 5, pady = 5)
label.place(x=20,y=50)

# Menu Selection Buttons
#GRADE CALCULATOR
button = Button(window, text = 'Grade Calculator')
button.place(x=20, y = 200)
button.config(command=gradeCalculator)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

#REQS TRACKER
button = Button(window, text = 'Requirements Tracker')
button.place(x=20, y = 275)
button.config(command=requirementsTracker)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

#COURSE BROCHURE
button = Button(window, text = 'Course Brochure')
button.place(x=20, y = 350)
button.config(command=courseBrochure)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

#README
button = Button(window, text = 'Read Me')
button.place(x=20, y = 420)
button.config(command=readMe)
button.config(font = ('Arial', 15), relief=RAISED, bd = 10, activebackground='grey')

window.mainloop()


    
