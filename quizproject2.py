username=input("Sign up your Username ")
firstname=str(input("Enter your First Name "))
email=input("Enter your Email ID ")
pass1=input("Enter your password ")
pass2=input("Confirm your password! ")
if(pass1==pass2):
    print("Password confirmed")
    age=int(input("Enter your Age "))
    if(age>=18):
        print("Here are 7 Terms and Conditions. ")
        print("1. You cannot not quit the page until you finished the quiz. ")
        print("2. The total time to solve the quiz is 45 mins. ")
        print("3. Use strong internet connection. ")
        print("4. Enter the correct answer in the following form (1/2/3/4) only. ")
        print("5. Each question carry 1 mark .")
        print("6. Score will be counted on first guess only. ")
        print("7. If you give wrong answer on the first guess , you are given two chances to guess it right without any score given.")
        a=input("Do you accept the following terms and conditions (Yes/No): ")
        if((a=="yes") or (a=="Yes") or(a=="YES")):
          print("You accepted all terms and conditions.. ")
          print("Your QUIZ starts now.")
          print("Q1 What is the maximum length of a python identifier?")
          print("(1) 32")
          print("(2) 16")
          print("(3) 128")
          print("(4) No fixed length")
          guess=int(input("Enter correct answer: "))
          score=0
          if guess==4 :
           print("Good")
           score+=1
           print(f"Score = {score}")
          else:
           print("Wrong answer!")
           print("You can make 2 more guesses.")    
           chances=1
           while(guess!=4 and chances<3):
            guess=int(input("Enter correct answer: "))
            if(guess==4 ):
             print("Good")
             print("No score")
            else:
             print("Wrong answer!")
            chances+=1 
          print("Q2 How is code block indicated in Python?")
          print("(1) Brackets")
          print("(2) Identation")
          print("(3) Key")
          print("(4) None") 
          guess=int(input("Enter correct answer: "))
          if guess==2 :
           print("Good")
           score+=1
           print(f"Score = {score}")
          else:
           print("Wrong answer!")
           print("You can make 2 more guesses.")    
           chances=1
           while(guess!=2 and chances<3):
            guess=int(input("Enter correct answer: "))
            if(guess==4 ):
             print("Good")
             print("No score given on this question.")
            else:
             print("Wrong answer!")
            chances+=1 
          print("Q3 Who developed python programming language?")
          print("(1) Wick van Rossum")
          print("(2) Rasmus Lerdorf")
          print("(3) Guido van Rossum")
          print("(4) Neine Stom")  
          guess=int(input("Enter correct answer: "))
          if guess==3 :
           print("Good")
           score+=1
           print(f"Score = {score}")
          else:
           print("Wrong answer!")
           print("You can make 2 more guesses.")    
           chances=1
           while(guess!=3 and chances<3):
            guess=int(input("Enter correct answer: "))
            if(guess==3 ):
             print("Good")
             print("No score given on this question.")
            else:
             print("Wrong answer!")
            chances+=1 
          print("Q4 Which one of the following is the use of function in python?")
          print("(1) Functions don't provide better modularity for your application")
          print("(2) You can't also create your own functions")
          print("(3) Functions are reusable pieces of programs")
          print("(4) All of the mentioned")  
          guess=int(input("Enter correct answer: "))
          if guess==3 :
           print("Good")
           score+=1
           print(f"Score = {score}")
          else:
           print("Wrong answer!")
           print("You can make 2 more guesses.")    
           chances=1
           while(guess!=3 and chances<3):
            guess=int(input("Enter correct answer: "))
            if(guess==3 ):
             print("Good")
             print("No score given on this question.")
            else:
             print("Wrong answer!")
            chances+=1 
          print("Q5 A loop that never ends is referred to as a(n)_________")
          print("(1) While loop")
          print("(2) InFinite loop")
          print("(3) For loop")
          print("(4) Recursive loop")  
          guess=int(input("Enter correct answer: "))
          if guess==2 :
           print("Good")
           score+=1
           print(f"Score = {score}")
          else:
           print("Wrong answer!")
           print("You can make 2 more guesses.")    
           chances=1
           while(guess!=2 and chances<3):
            guess=int(input("Enter correct answer: "))
            if(guess==2 ):
             print("Good")
             print("No score given on this question.")
            else:
             print("Wrong answer!")
            chances+=1
          print("Q6 Which command will stop an infinite loop?")
          print("(1) Alt-C")
          print("(2) Shift")
          print("(3) For loop")
          print("(4) Ctrl-C")  
          guess=int(input("Enter correct answer: "))
          if guess==4 :
           print("Good")
           score+=1
           print(f"Score = {score}")
          else:
           print("Wrong answer!")
           print("You can make 2 more guesses.")    
           chances=1
           while(guess!=4 and chances<3):
            guess=int(input("Enter correct answer: "))
            if(guess==4 ):
             print("Good")
             print("No score given on this question.")
            else:
             print("Wrong answer!")
            chances+=1   
          print("Q7 What does the 'continue' statement do in a loop?")
          print("(1) Terminates the loop")
          print("(2) Skips the current iteration and proceeds to the next one")
          print("(3) Pauses the loop execution")
          print("(4) None")  
          guess=int(input("Enter correct answer: "))
          if guess==2 :
           print("Good")
           score+=1
           print(f"Score = {score}")
          else:
           print("Wrong answer!")
           print("You can make 2 more guesses.")    
           chances=1
           while(guess!=2 and chances<3):
            guess=int(input("Enter correct answer: "))
            if(guess==2 ):
             print("Good")
             print("No score given on this question.")
            else:
             print("Wrong answer!")
            chances+=1     
          print(f"***************************************************//{firstname}, Congratulations! you are certified on completing your quiz. //**************************************")
          print(f"***************************************************// Your Username is {username}.                                              //***********************************")
          print(f"***************************************************// Your EmailId is {email}.                                    //*************************************")
          print(f"***************************************************// Your score is {score}/7.                                   //***************************************")

        else:
          print ("The terms and conditions are not satisfied.")
          print("Terminated!!!!")        
    elif(age<18 and age>0): 
     print("You are not qualified for quiz.")   
    else:
      print("Enter valid age")             
else:
    print("Your password does not match...")
    print("You got 2 more chances!")    
    pass1=input("Enter your password ")
    pass2=input("Confirm your password! ")  
    if(pass1==pass2):
      print("Password confirmed")
      age=int(input("Enter your Age "))
      if(age>=18):
        print()
      elif(age<18 and age>0): 
       print("You are not qualified for quiz.")   
      else:
       print("Enter valid age")                 
    else:
      print("Your password does not match...")
      print("You got 1 more chance!")    
      pass1=input("Enter your password ")
      pass2=input("Confirm your password! ")
      if(pass1==pass2):
       print("Password confirmed")
       age=int(input("Enter your Age "))
       if(age>=18):
        print()
       elif(age<18 and age>0): 
        print("You are not qualified for quiz.")
       else:
        print("Enter valid age")   
      else:
        print("Terminated!!") 
                  
                  
                  
                  