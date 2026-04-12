from datetime import date

"""
Hi, just a note: Use Ctrl + F to navigate in the code to certain functions.

I wil be marking them with 'part', so just put the keyword part in the ctrl + f finding menu to get to somewhere
It might be case sensitive, I haven't checked, so better safe than sorry

This doesn't affect the code even though it's technically an actual string with proper syntax,
but Python ignores it because it isn't inside an actual variable, so it does nothing. Just a fun fact
"""

# part: Definitions
def menuScreen() -> None:
    print("""Good morning isko/iska!
Welcome to the ASH (All-around Student Helper) app!
""")
    print("="*50)
    print("""Options:
[1] - Student Grade Calculator
[2] - Reqs Tracker
[3] - Course Brochure
[4] - Exit (See you later)!
""")
    print("="*50)

def textClear() -> None:
    """
    Just a 'text clearing' effect, so I don't have to rewrite the lines everytime.
    
    """
    
    print("\n" * 50)
    print("-" *50) # Resets the text, well kind of, just the illusion of it
    
def continueCode(continueMessage="Press enter to continue.") -> None:
    input(continueMessage)

def quicksortFunction(sortingList: list[list]) -> list[list]:
    
    if len(sortingList) <= 1:
        return sortingList # If the list is empty | 1 element, meaning it's sorted, it just finishes the function
    
    divider = sortingList[len(sortingList)//2][2] # Finds the middle element
    
    lessThan: list[int] = [item for item in sortingList if item[2] < divider] # Everything less than the middle gets separated
    middle: list[int] = [item for item in sortingList if item[2] == divider] # Everything in the middle gets separated
    greaterThan: list[int] = [item for item in sortingList if item[2] > divider] # Everything greater than the middle gets separated
    
    # ^ This sorting is caused by the fact that it's a self-referring function
    # It will continue sorting each list (since the quicksortFunction is used on each separated list) until each list is empty or 1 element.
    # Let's say you have a list [1, 2, 3, 4]
    # The middle would be 2, so the lists would
    # lessThan: 1
    # middle: 2
    # greaterThan: 3, 4
    
    # then this greaterThan is split, with 3 or 4 being the middle, I don't know
    # becoming separate lists of 3, and 4, which ends the self-referring function finally
    
    # A self-referring function will run until it stops referring to itself, in this case, if it gets to the sortingList being 1 element
    # or less, as seen in the if function above, which returns the sortingList itself
    
    return quicksortFunction(lessThan) + middle + quicksortFunction(greaterThan)
    
def studentGradeCalc() -> None: # part : Student Grade Calculator
    
    """
    Code Summary:
    Asks for grades in [subjects]
    Computes grades
    Outputs grades
    Ends
    
    """ 
    
    # Variable Definition
    """

    Hey! What's this : float thing? And also why is there a : float infront of my variables? These are called type hints!
    Variable: type = value
    ^ This is the format for them, they don't force the variable to be like that, but they're like a comment. It tells you what
    value I, the coder, think it should have
    
    """
    
    totalGrade: float = 0.0
    totalCredits: float = 0.0
    counter: int = 0
    
    textClear()
    subjectNames: list[str] = []
    subjectCredits: list[float] = []
    
    while True:
        try:
            numSubjects = int(input("How many subjects do you have? "))
            
            for count in range(numSubjects): # Runs the loop for the amount of subjects, one iteration per subject
                subjectName = input("Subject Name: ")
                subjectNames.append(subjectName)
                if subjectName.strip() != "":
                    subjectCredits.append(float(input("Subject Credits: ")))
                else:
                    input("Invalid input! ")
                
            break
        except:
            continueCode("Invalid input. Restarting process. PRESS ENTER TO CONTINUE")
            textClear()

    # Inputs
    for subject in subjectNames:

        while True:
            
            try:
                
                gradeInput: float = float(input(f"What is your grade in {subject} [Raw Grade%]: "))
                
                while not (0 <= gradeInput <= 100): # while not here is like while except it checks for the inverse (opposite) of the operation/condition
                    print("Invalid input!")
                    gradeInput = float(input(f"What is your grade in {subject} [Raw Grade%]: "))
                    
                # Start of grade conversion
                match gradeInput:
                    case grade if grade >= 96:
                        gradeInput = 1.00
                    case grade if grade >= 90:
                        gradeInput = 1.25
                    case grade if grade >= 84:
                        gradeInput = 1.5
                    case grade if grade >= 78:
                        gradeInput = 1.75
                    case grade if grade >= 72:
                        gradeInput = 2.00
                    case grade if grade >= 66:
                        gradeInput = 2.25
                    case grade if grade >= 60:
                        gradeInput = 2.50
                    case grade if grade >= 55:
                        gradeInput = 2.75
                    case grade if grade >= 50:
                        gradeInput = 3.00
                    case grade if grade >= 40:
                        gradeInput = 4.00
                    case grade if grade < 40:
                        gradeInput = 5.00
                # End of grade conversion
                    
                totalGrade += gradeInput * subjectCredits[counter]
                totalCredits = sum(subjectCredits)
                
                """
                For anyone wondering, the += just shortens code for efficiency.
                Instead of a = a + b, it becomes a += b, and they have the same output.
        
                """
                
                break # < This just ends the while loop, btw
                
            except ValueError:
                print("Invalid value entered. ")
            
        counter += 1
            

    textClear()

    # Grade Computation
    overallGrade = round(totalGrade/totalCredits, 2)

    print(f"General Weighted Average: {overallGrade:.2f}")

    # End of part: Student Grade Calculator
    
def reqsTracker() -> None: # part: Reqs Tracker
    
    textClear()
    
    # Definitions
    reqsList: list[list] = []
    reqsSubject: list[str] = []
    reqsTypeValue: list[int] = []
    reqsType: list[str] = []
    reqsDateValues: list[int] = []
    
    try: # Again, falesafe
        continueCode("""Welcome to the Reqs Tracker!
Instructions: Input first the subject, then the type (AA/FA/ILA), then it's submission date/deadline.
(When finished, leave the space for subject empty.) [Enter to continue]
""")
        while True:
            
            textClear()
            
            userInput = input("Subject [Leave empty to finish]: ").strip()
            if userInput == "":
                break # ends the while loop if user inputs quit
            else:
                reqsSubject.append(userInput) # adds the input into the list
            
            # The next two programs are repeats of the first with a little variation
            
            userInput = input("Type: [1 - ILA] [2 - FA] [3 - AA]: ")
            
            reqsTypeValue.append(int(userInput))

            
            match int(userInput):
                case 1:
                    reqsType.append("ILA")
                case 2:
                    reqsType.append("FA")
                case 3:
                    reqsType.append("AA")
                case 4:
                    input("Invalid input!")
                    break
                        
                
            userInput = input("""Due Date: [YYYY], [MM], [DD] (No leading zeros!)
""").title()
            
            # This goes through each part in the date and converts them into integers, while deleting any leading/trailing white space
            year, month, day = map(int, userInput.split(","))
            dateValue = date(year, month, day).toordinal()

            
            reqsDateValues.append(dateValue)
        
        textClear()
        
        for item in range(len(reqsSubject)):            
            reqsList.append([reqsSubject[item], reqsType[item], reqsDateValues[item]]) # This appends every list of reqsSubjects, types, and dateValues to the reqsList
            
        
        sortedStuff = quicksortFunction(reqsList) # Sorts the reqs list by date
        
        for item in range(len(sortedStuff)): # Prints out the sorted reqs list
            importance = len(sortedStuff) # Adds importance, the later the date the lower the importance and vice versa
            print(f"IMPORTANCE: {importance} SUBJECT: {sortedStuff[item][0].upper()}, TYPE: {sortedStuff[item][1]}")
            importance -= 1 
        
    except ValueError:
        input("Invalid input! Press enter to continue. ")
            
            
            
        

def courseBrochure() -> None: # part: CourseBrochure
    print("\n"*50)
    print("Welcome to the Course Brochures!")
    print(" ---------------------------- ")
    seegrade = int(input("What grade would you like to see their course's titles: "))

    if seegrade == 7:
        
        print()
        print("IS - Introduction to Science and Earth Systems")
        print("Computer Science 1 - Introduction to Computing")
        print("Mathematics 1 - Algebra 1")
        print("ADTech 1 - Art, Design and Technology: Basic Principles and Processes")
        print("English 1 - Communication Arts 1")
        print("Filipino 1 - Wika at Panitikang Pilipino")
        print("Social Science 1 - Philippine History")
        print("""PEHM 1 - Physical Fitness and Basic Movement Education 1
                          Growth and Development, Mental and Emotional Health
                          Philippine Music Then and Now""")                
        print("Values Education 1 - Adolescent Living and Character Building")
        print()
        
    elif seegrade == 8:
        
        print()
        print("Biology 1 - Fundementals of Biology 1")
        print("Chemistry 1 - General Chemistry 1")
        print("Physics 1 - Introduction to Physics")
        print("Computer Science 2 - Coding in a Connected World: Development of Computational Thinking Skills")
        print("Mathematics 2 - Algebra 2")
        print("Mathematics 3 - Geometry")
        print("ADTech 2 - Art, Design and Technology: Resistant Materials and Electronics")
        print("English 2 - Communication Arts 2")
        print("Filipino 2 - Kommunikasyon at Panitikang Pilipino")
        print("Social Science 2 - World History")
        print("""PEHM 2 - Physical Fitness and Basic Movement Education 2
                          Family Health And Preventive Drug Education
                          Asian Music and Its Influences on Philippine Soundscapes""")                
        print("Values Education 2 - Toward Adolescent Wholeness")
        print("Earth Science - Earth Systems, Energy and Change")
        print()
        
    elif seegrade == 9:
    
        print()
        print("Biology 2 - Fundementals of Biology 2")
        print("Chemistry 2 - General Chemistry 2")
        print("Physics 2 - Fundamentals of Physics")
        print("Computer Science 3 - Objects Oriented Programming 1")
        print("Mathematics 4 - Algebra 3")
        print("Statistics 1 - Data and Probability 1")
        print("ADTech 3 - Art, Design and Technology: Exploring Technologies")
        print("English 3 - Communication Arts 3")
        print("Filipino 3 - Retorika, Pagsusuri At Ang Noli Me Tangere")
        print("Social Science 3 - Citizenship and Civic Education")
        print("""PEHM 3 - Group-Oriented Activities in Sports and Leisure Education 1 
                          Safety Education, First Aid and Disease Prevention 
                          Western Music and its influence to Philippine Music""")                
        print("Values Education 3 - Values and Standards for a Meaningful Life")
        print()

    elif seegrade == 10:
        
        print()
        print("Biology 3 - Foundations of Molecular and Cellular Biology")
        print("Chemistry 3 - General Chemistry 3")
        print("Physics 3 - Fundamentals of Physics 2")
        print("Computer Science 4 - Objects Oriented Programming 2")
        print("Mathematics 5 - Algebra 4")
        print("Statistics 2 - Data and Probability 2")
        print("English 4 - Communication Arts 4")
        print("Filipino 4 - Akademikong Pagsulat at El Filibusterismo")
        print("Social Science 4 - Governance and Sustainable Futures")
        print("""PEHM 4 - Group-Oriented Activities in Sports and Leisure Education 2 
                          Consumer Health, Community and Environmental Health  
                          Music Technology """)                
        print("Values Education 4 - The Thinking Person's Being and Becoming")
        print()

    elif seegrade == 11:
        
        print()
        print("Biology 4 - Contemporary Biology")
        print("Chemistry 4 - Fundamnetals of Organic and Biological Chemistry")
        print("Physics 4 - Fundamentals of Physics 3")
        print("Mathematics 6 - Differential Calculus")
        print("English 5 - English for Academic and Professional Purposes: Oral and Written Communication")
        print("Filipino 5 - Komunikasyong Makaagham Tungo sa Maka-Pilipinong Pananaliksik")
        print("Social Science 5 - Basic Principles of Economics")
        print("Research 1 - Research and Development 1: Proposal Writing and Implementation")
        print()

    elif seegrade == 12:
        
        print()
        print("Mathematics 7 -  Integral Calculus")
        print("English 5 - Science Communication")
        print("Filipino 5 - Maka-Pilipinong Pananaliksik sa Wika, Kultura, Agham at Teknolohiya ")
        print("Social Science 5 - Community Development and Engagement")
        print("Research 1 - Research and Development 2: Validation, Synthesis and Communication")
        print()
        
    else:
        
        print("INVALID INPUT!!")
        
def backToMenu() -> None:
    continueCode("Press enter to continue. ")
    textClear()


# part: Main Code Loop
Loop = True




while Loop:
    
    # Asking the user to choose a program
    
    try: # A try and except runs a block of code, and if it runs into an error, it runs the except code, basically just error handling
        
        """
        What is the match | case?
        It's an if - else function except you can put the condition in one thing (match) and then the outputs on another, the "cases" check if the condition in match
        match their own condition, ie if you have, 'match 3' and "case 2", then "case 2" wouldn't run, but a "case 3" would, since the two values match.
        Just a quick exposition.
        
        """
        menuScreen()
        match int(input("Option Selected: ")):
            
            case 1:
                studentGradeCalc()
                backToMenu()
                
            case 2:
                reqsTracker()
                # So that it doesn't automatically clear right after        
                backToMenu()
            
            case 3:
                courseBrochure() 
                backToMenu()
                
            case 4:
                Loop = False
                print("""
Goodbye isk(o/a)! Return soon!""")
                continueCode("Press enter to exit. ")
                
                
            case _: # a default case
                print("""Not an option!
                """)    
                backToMenu()
        

    
    except ValueError:
            
        input("Invalid input. Please input a number | integer...[Press enter to continue. ]: ")
        textClear()
        

    

  
            
        
