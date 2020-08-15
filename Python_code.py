import os
clear = lambda: os.system('cls') 
clear()
print("Enter Your -:\nName\nContact no.\nE-mail_id")
nm=input('NAME:- ')
cnt=input('Contact no.:- ')
eml=input('E-Mail_ID:- ')
print("Press Enter to password")
psw=input("Password\n")
if psw=="vscode":
    print("\n..........................Welcome to the Quiz..........................")
    print("Select subject")
    print("1. C\n2. C++\n3. Python\n4. Java")
    sub= int(input("Enter the no. to start quiz "))
    while sub>=1 or sub<=4:
        if sub== 1 :
            print("Your C quiz has been started")
            print('Instruction for candidate :-\n')
            print("1.Read all the questions carefully.\n2.Do not resize(minimize) the browser during the test.\n3.Never click 'BACK' button on browser.\n4.No NEGATIVE marking will be there.\n5.Use 'lowercase' and 'numbers' only to print the output of program.\n'ALL THE BEST'.\nPress Enter To Start Test")
            input( )
            count=0
            print('Q1. C is which type of language. \n  A.High Level Launguage\n  B.Low Level Language\n  C.Mid Level Language\n  D.None of these')
            ans=input("\n")
            if ans=="c":
                count+=1
        
            else:
                pass

            print("Q2. The keyword used to  control from a function back to the calling function is\n  A.switch\n  B.goto\n  C.go back\n  D.return")
            ans=input("\n")
            if ans=="d":
                count+=1
            else:
                pass  

            print("Q3. Which of the following function sets first n characters of a string to a given character?\n  A.strinit()\n  B.strnset()\n  C.strset()\n  D.strcset()")
            ans=input("\n")
            if ans=="b":
                count+=1
            else:
                pass

            print("Q4. If the two strings are identical, then strcmp() function returns\n  A.-1\n  B.1\n  C.0\n  D.Yes")
            ans=input("\n")
            if ans=='c':
                count+=1
            else:
                pass

            print('Q5. The library function used to find the last occurrence of a character in a string is\n  A.strnstr()\n  B.laststr()\n  C.strrchr()\n  D.strstr()')    
            ans=input("\n")
            if ans=='c':
                count+=1
            else:
                pass
            t="THANK YOU"
            print(t.center(18,"*"))
            print(f"Your score is {count} out of 5")
            break
        elif sub == 2:
            print("Your C++ quiz has been started")
            print('Instruction for candidate :-\n')
            print("1.Read all the questions carefully.\n2.Do not resize(minimize) the browser during the test.\n3.Never click 'BACK' button on browser.\n4.No NEGATIVE marking will be there.\n5.Use 'lowercase' and 'numbers' only to print the output of program.\n'ALL THE BEST'.\nPress Enter To Start Test")
            input( )
            count=0
            print('Q1. 	Which of the following type of class allows only one object of it to be created? \n  A.Virtual class\n  B.Abstract class\n  C.Singleton class\n  D.Friend class')
            ans=input("\n")
            if ans=="c":
                count+=1
            else:
                pass

            print("Q2. Which of the following is not a type of constructor?\n  A.Copy constructor\n  B.Friend constructor\n  C.Default constructor\n  D.Parameterized constructor")     
            ans=input("\n")
            if ans=="b":
                count+=1
            else:
                pass  

            print("Q3.Which of the following statements is correct?\n  A.Base class pointer cannot point to derived class\n  B.Derived class pointer cannot point to base class.\n  C.Pointer to derived class cannot be created.\n  D.Pointer to base class cannot be created.")
            ans=input("\n")
            if ans=="b":
                count+=1
            else:
                pass

            print("Q4. Which of the following is not the member of class?\n  A.Static function\n  B.Friend function\n  C.Const function\n  D.Virtual function")
            ans=input("\n")
            if ans=='b':
                count+=1
            else:
                pass

            print('Q5. Which of the following concepts means determining at runtime what method to invoke?\n  A.Data hiding\n  B.Dynamic Typing\n  C.	Dynamic binding\n  D.Dynamic loading')    
            ans=input("\n")
            if ans=='c':
                count+=1
            else:
                pass
            t="THANK YOU"
            print(t.center(18,"*"))
            print(f"Your score is {count} out of 5")
            break
        elif sub == 3:
            print("Your Python quiz has been started")
            print('Instruction for candidate :-\n')
            print("1.Read all the questions carefully.\n2.Do not resize(minimize) the browser during the test.\n3.Never click 'BACK' button on browser.\n4.No NEGATIVE marking will be there.\n5.Use 'lowercase' and 'numbers' only to print the output of program.\n'ALL THE BEST'.\nPress Enter To Start Test")
            input( )
            count=0.
            print('Q1. print type(type(int)) \n  A.type "int"\n  B.type "type"\n  C.Error\n  D.0')
            ans=input("\n")
            if ans=="b":
                count+=1
                
            else:
                pass

            print("Q2. chr(ord('A'))\n  A. A\n  B. B\n  C. a\n  D. Error")
            ans=input("\n")
            if ans=="d":
                count+=1
            else:
                pass  

            print("Q3. What is called when a function is defined inside a class?\n  A.Module\n  B.Class\n  C.Another Function\n  D.Method")
            ans=input("\n")
            if ans=="a":
                count+=1
            else:
                pass

            print("Q4. Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?\n  A.[3, 4, 5, 20, 5, 25, 1, 3]\n  B.[1, 3, 3, 4, 5, 5, 20, 25]\n  C.[3, 5, 20, 5, 25, 1, 3]\n  D.[1, 3, 4, 5, 20, 5, 25]")
            ans=input("\n")
            if ans=='c':
                count+=1
            else:
                pass

            print('Q5. Which of the following is the use of id() function in python?\n  A.Id returns the identity of the object\n  B.Every object doesn’t have a unique id\n  C.All of the mentioned\n  D.None of the mentioned')    
            ans=input("\n")
            if ans=='a':
                count+=1
            else:
                pass
            t="THANK YOU"
            print(t.center(18,"*"))
            print(f"Your score is {count} out of 5")
            break 
        elif sub == 4:
            print("Your Java quiz has been started")
            print('Instruction for candidate :-\n')
            print("1.Read all the questions carefully.\n2.Do not resize(minimize) the browser during the test.\n3.Never click 'BACK' button on browser.\n4.No NEGATIVE marking will be there.\n5.Use 'lowercase' and 'numbers' only to print the output of program.\n'ALL THE BEST'.\nPress Enter To Start Test")
            input( )
            count=0
            print('Q1. Which one of these lists contains only Java programming language keywords?\n  A.class, if, void, long, Int, continue\n  B.goto, instanceof, native, finally, default, throws\n  C.try, virtual, throw, final, volatile, transient\n  Dstrictfp, constant, super, implements, do')
            ans=input("\n")
            if ans=="b":
                count+=1
                
            else:
                pass

            print("Q2. Which will legally declare, construct, and initialize an array?\n  A.int [] myList = {'1', '2', '3'};\n  B.int [] myList = (5, 8, 2);\n  C.int myList [] [] = {4,9,7,0};\n  D.int myList [] = {4, 3, 7};")
            ans=input("\n")
            if ans=="d":
                count+=1
            else:
                pass  

            print("Q3. Which is a reserved word in the Java programming language?\n  A.method\n  B.native()\n  C.subclasses\n  D.array")
            ans=input("\n")
            if ans=="b":
                count+=1
            else:
                pass

            print("Q4. Which is a valid keyword in java?\n  A.interface\n  B.string\n  C.Float\n  D.Unsign")
            ans=input("\n")
            if ans=='a':
                count+=1
            else:
                pass

            print('Q5. Which is the valid declarations within an interface definition?\n  A.public double methoda();\n  B.	public final double methoda();\n  C.static void methoda(double d1);\n  D.protected void methoda(double d1);')    
            ans=input("\n")
            if ans=='a':
                count+=1
            else:
                pass
            t="THANK YOU"
            print(t.center(18,"*"))
            print(f"Your score is {count} out of 5")
            break
        else:
            print("Error..... Re-enter the no.")
            break
else:
    print("You Enter Wrong Password")
    