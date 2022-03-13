#Name: Lubabatu Ahmad Sa'i 
#Reg. No: H20CS023
#Title/Program: Admission Status Checker
#Github Repository: https://github.com/lubabatusaee36/admissionStatusChecker
while True:
    
    print("*"*45)
    print("WELCOME TO ADMISSION STATUS CHECKER PROGRAM")
    print("*"*45)
     
        #variables declaration
    name = input("Enter your name ")
        
    jamb_score = int(input("Enter your JAMB score "))


    if(jamb_score>=180):
        print("Congratulations, "+str(name)+" you are eligible for Admission.\n")

    else:
        print("Sorry, "+str(name)+" you are NOT eligible for admission\n")

    choice = input("Do You Want to Re-Check Again? Type Yes/No: ")
        
    if(choice.upper() != "YES"):
        
        print("Good Bye the program is exiting....")
        break
    else:
        continue
            


