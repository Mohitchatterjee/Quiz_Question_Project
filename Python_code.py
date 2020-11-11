import os
import pyautogui
print("Enter Your -")
with open('Information.py','a') as f:
    f.write(input('NAME:- ')+'\t')
    f.write(input('Contact no.:-')+'\t')
    f.write(input('E-Mail_ID:- ')+'\t')
while True:    
    pyautogui.alert('You Have To Remind Passkey')
    psw=pyautogui.password('Enter security code\n')
    if psw=="vscode":
        os.system("cls")
        print("\n\n\n\n\n\t\t\t..........................Welcome to the Quiz..........................")
        print("\n\n\n\t\t\t\t\tSelect subject")
        print("\t\t\t\t\t1. C\n\t\t\t\t\t2. C++\n\t\t\t\t\t3. Python\n\t\t\t\t\t4. Java")
        sub= int(input("\n\t\t\t\t\tEnter the no. to start quiz "))
        pyautogui.confirm('Are You Sure ?')
        os.system("cls")
        while sub>=1 or sub<=4:
            if sub== 1 :
                print("\n\n\n\n\t\t\t\t\tYour C quiz has Been started")
                print('\n\t\t\t\t\tInstruction for candidate :-\n')
                print("\t\t\t\t\t1.Read all the questions carefully.\n\t\t\t\t\t2.Do not resize(minimize) the browser during the test.\n\t\t\t\t\t3.Never click 'BACK' button on browser.\n\t\t\t\t\t4.No NEGATIVE marking will Be there.\n\t\t\t\t\t5.Use 'lowercase' and 'numBers' only to print the output of program.\n\t\t\t\t\t\t\t\t\t'ALL THE BeST'.")
                input()
                pyautogui.confirm('Are You Ready?')
                os.system("cls")
                count=0
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ1. C is which type of language. \n\n\t\t\t\t\t\t\t\t\t\t\tA.High Level Launguage\n\t\t\t\t\t\t\t\t\t\t\tB.Low Level Language\n\t\t\t\t\t\t\t\t\t\t\tC.Mid Level Language\n\t\t\t\t\t\t\t\t\t\t\tD.None of these')
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="c":
                    count+=1
            
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ2. The keyword used to control from a function back to the calling function is\n\n\t\t\t\t\t\t\t\t\t\t\tA.switch\n\t\t\t\t\t\t\t\t\t\t\tB.goto\n\t\t\t\t\t\t\t\t\t\t\tC.go back\n\t\t\t\t\t\t\t\t\t\t\tD.return")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="d":
                    count+=1
                else:
                    pass  
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ3. Which of the following function sets first n characters of a string to a given character?\n\n\t\t\t\t\t\t\t\t\t\t\tA.strinit()\n\t\t\t\t\t\t\t\t\t\t\tB.strnset()\n\t\t\t\t\t\t\t\t\t\t\tC.strset()\n\t\t\t\t\t\t\t\t\t\t\tD.strcset()")
                ans=input("\n")
                if ans=="b":
                    count+=1
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ4. If the two strings are identical, then strcmp() function returns\n\n\t\t\t\t\t\t\t\t\t\t\tA.-1\n\t\t\t\t\t\t\t\t\t\t\tB.1\n\t\t\t\t\t\t\t\t\t\t\tC.0\n\t\t\t\t\t\t\t\t\t\t\tD.Yes")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=='c':
                    count+=1
                else:
                    pass
                os.system("cls")
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ5. The library function used to find the last occurrence of a character in a string is\n\n\t\t\t\t\t\t\t\t\t\t\tA.strnstr()\n\t\t\t\t\t\t\t\t\t\t\tB.laststr()\n\t\t\t\t\t\t\t\t\t\t\tC.strrchr()\n\t\t\t\t\t\t\t\t\t\t\tD.strstr()')    
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=='c':
                    count+=1
                else:
                    pass
                os.system("cls")
                t="THANK YOU"
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t'+t.center(19,"*"))
                print('\t\t\t\t\t\t\t\t\t\t\t'f"Your score is {count} out of 5")
                with open('Information.py','a') as f:
                    f.write(' ' +str(count))
                    f.write(' '+'\'C\'')
                    f.write('\n')
                    f.close()
                input('\t\t\t\t\t\t\t\t\t\t!! Your Mark has Been Recorded !!')
                exit()
            elif sub == 2:
                print("\n\n\n\n\t\t\t\t\tYour C++ quiz has Been started")
                print('\n\t\t\t\t\tInstruction for candidate :-\n')
                print("\t\t\t\t\t1.Read all the questions carefully.\n\t\t\t\t\t2.Do not resize(minimize) the browser during the test.\n\t\t\t\t\t3.Never click 'BACK' button on browser.\n\t\t\t\t\t4.No NEGATIVE marking will Be there.\n\t\t\t\t\t5.Use 'lowercase' and 'numBers' only to print the output of program.\n\t\t\t\t'ALL THE BeST'.\n\t\t\t\t\tPress Enter To Start Test")
                input( )
                os.system("cls")
                count=0
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ1. Which of the following type of class allows only one object of it to Be created? \n\n\t\t\t\t\t\t\t\t\t\t\tA.Virtual class\n\t\t\t\t\t\t\t\t\t\t\tB.Abstract class\n\t\t\t\t\t\t\t\t\t\t\tC.Singleton class\n\t\t\t\t\t\t\t\t\t\t\tD.Friend class')
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="c":
                    count+=1
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ2. Which of the following is not a type of constructor?\n\n\t\t\t\t\t\t\t\t\t\t\tA.Copy constructor\n\n\t\t\t\t\t\t\t\t\t\t\tB.Friend constructor\n\n\t\t\t\t\t\t\t\t\t\t\tC.Default constructor\n\t\t\t\t\t\t\t\t\t\t\tD.Parameterized constructor")     
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="b":
                    count+=1
                else:
                    pass  
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ3.Which of the following statements is correct?\n\n\t\t\t\t\t\t\t\t\t\t\tA.Base class pointer cannot point to derived class\n\t\t\t\t\t\t\t\t\t\t\tB.Derived class pointer cannot point to base class.\n\t\t\t\t\t\t\t\t\t\t\tC.Pointer to derived class cannot Be created.\n\t\t\t\t\t\t\t\t\t\t\tD.Pointer to base class cannot Be created.")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="b":
                    count+=1
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ4. Which of the following is not the memBer of class?\n\n\t\t\t\t\t\t\t\t\t\t\tA.Static function\n\t\t\t\t\t\t\t\t\t\t\tB.Friend function\n\t\t\t\t\t\t\t\t\t\t\tC.Const function\n\t\t\t\t\t\t\t\t\t\t\tD.Virtual function")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=='b':
                    count+=1
                else:
                    pass
                os.system("cls")
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ5. Which of the following concepts means determining at runtime what method to invoke?\n\n\t\t\t\t\t\t\t\t\t\t\tA.Data hiding\n\t\t\t\t\t\t\t\t\t\t\tB.Dynamic Typing\n\t\t\t\t\t\t\t\t\t\t\tC.Dynamic binding\n\t\t\t\t\t\t\t\t\t\t\tD.Dynamic loading')    
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=='c':
                    count+=1
                else:
                    pass
                os.system("cls")
                t="THANK YOU"
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t'+t.center(19,"*"))
                print('\t\t\t\t\t\t\t\t\t\t\t'f" Your score is {count} out of 5")
                with open('Information.py','a') as f:
                    f.write(' ' +str(count))
                    f.write(' '+'\'C++\'')
                    f.write('\n')
                    f.close()
                input('\t\t\t\t\t\t\t\t\t\t!! Your Mark has Been Recorded !!')
                exit()
            elif sub == 3:
                print("\n\n\n\n\t\t\t\t\tYour Python quiz has Been started")
                print('\n\t\t\t\t\tInstruction for candidate :-\n')
                print("\t\t\t\t\t1.Read all the questions carefully.\n\t\t\t\t\t2.Do not resize(minimize) the browser during the test.\n\t\t\t\t\t3.Never click 'BACK' button on browser.\n\t\t\t\t\t4.No NEGATIVE marking will Be there.\n\t\t\t\t\t5.Use 'lowercase' and 'numBers' only to print the output of program.\n\t\t\t\t\t'ALL THE BeST'.\n\t\t\t\t\tPress Enter To Start Test")
                input( )
                os.system("cls")
                count=0.
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ1. print type(type(int))\n\n\t\t\t\t\t\t\t\t\t\t\tA.type "int"\n\t\t\t\t\t\t\t\t\t\t\tB.type "type"\n\t\t\t\t\t\t\t\t\t\t\tC.Error\n\t\t\t\t\t\t\t\t\t\t\tD.0')
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="b":
                    count+=1
                    
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ2. chr(ord('A'))\n\n\t\t\t\t\t\t\t\t\t\t\tA. A\n\t\t\t\t\t\t\t\t\t\t\tB. B\n\t\t\t\t\t\t\t\t\t\t\tC. a\n\t\t\t\t\t\t\t\t\t\t\tD. Error")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="d":
                    count+=1
                else:
                    pass  
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ3. What is called when a function is defined inside a class?\n\n\t\t\t\t\t\t\t\t\t\t\tA.Module\n\t\t\t\t\t\t\t\t\t\t\tB.Class\n\t\t\t\t\t\t\t\t\t\t\tC.Another Function\n\t\t\t\t\t\t\t\t\t\t\tD.Method")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=="a":
                    count+=1
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ4. Suppose list1 is [3, 4, 5, 20, 5, 25, 1, 3], what is list1 after list1.pop(1)?\n\n\t\t\t\t\t\t\t\t\t\t\tA.[3, 4, 5, 20, 5, 25, 1, 3]\n\t\t\t\t\t\t\t\t\t\t\tB.[1, 3, 3, 4, 5, 5, 20, 25]\n\t\t\t\t\t\t\t\t\t\t\tC.[3, 5, 20, 5, 25, 1, 3]\n\t\t\t\t\t\t\t\t\t\t\tD.[1, 3, 4, 5, 20, 5, 25]")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=='c':
                    count+=1
                else:
                    pass
                os.system("cls")
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\tQ5. Which of the following is the use of id() function in python?\n\n\t\t\t\t\t\t\t\t\t\t\tA.Id returns the identity of the object\n\t\t\t\t\t\t\t\t\t\t\tB.Every object doesn’t have a unique id\n\t\t\t\t\t\t\t\t\t\t\tC.All of the mentioned\n\t\t\t\t\t\t\t\t\t\t\tD.None of the mentioned')    
                ans=input("\n\t\t\t\t\t\t\t\t\t\t\t")
                if ans=='a':
                    count+=1
                else:
                    pass
                os.system("cls")
                t="THANK YOU"
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t'+t.center(19,"*"))
                print('\t\t\t\t\t\t\t\t\t\t'f"   Your score is {count} out of 5")
                with open('Information.py','a') as f:
                    f.write(' ' +str(count))
                    f.write(' '+'\'Python\'')
                    f.write('\n')
                    f.close()
                input('\t\t\t\t\t\t\t\t\t\t!! Your Mark has Been Recorded !!')
                exit()
            elif sub == 4:
                print("\n\n\n\n\t\t\t\t\tYour Java quiz has Been started")
                print('\n\t\t\t\t\tInstruction for candidate :-\n')
                print("\t\t\t\t\t1.Read all the questions carefully.\n\t\t\t\t\t2.Do not resize(minimize) the browser during the test.\n\t\t\t\t\t3.Never click 'BACK' button on browser.\n\t\t\t\t\t4.No NEGATIVE marking will Be there.\n\t\t\t\t\t5.Use 'lowercase' and 'numBers' only to print the output of program.\n\t\t\t\t\t\t' ALL THE BeST'.\n\t\t\t\t\tPress Enter To Start Test")
                input( )
                os.system("cls")
                count=0
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\tQ1. Which one of these lists contains only Java programming language keywords?\n\n\t\t\t\t\t\t\t\t\t\tA.class, if, void, long, Int, continue\n\t\t\t\t\t\t\t\t\t\tB.goto, instanceof, native, finally, default, throws\n\t\t\t\t\t\t\t\t\t\tC.try, virtual, throw, final, volatile, transient\n\t\t\t\t\t\t\t\t\t\tD.strictfp, constant, super, implements, do')
                ans=input("\n\t\t\t\t\t\t\t\t\t\t")
                if ans=="b":
                    count+=1
                    
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\tQ2. Which will legally declare, construct, and initialize an array?\n\n\t\t\t\t\t\t\t\t\t\tA.int [] myList = {'1', '2', '3'};\n\t\t\t\t\t\t\t\t\t\tB.int [] myList = (5, 8, 2);\n\t\t\t\t\t\t\t\t\t\tC.int myList [] [] = {4,9,7,0};\n\t\t\t\t\t\t\t\t\t\tD.int myList [] = {4, 3, 7};")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t")
                if ans=="d":
                    count+=1
                else:
                    pass  
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\tQ3. Which is a reserved word in the Java programming language?\n\n\t\t\t\t\t\t\t\t\t\tA.method\n\t\t\t\t\t\t\t\t\t\tB.native()\n\t\t\t\t\t\t\t\t\t\tC.subclasses\n\t\t\t\t\t\t\t\t\t\tD.array")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t")
                if ans=="b":
                    count+=1
                else:
                    pass
                os.system("cls")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\tQ4. Which is a valid keyword in java?\n\n\t\t\t\t\t\t\t\t\t\tA.interface\n\t\t\t\t\t\t\t\t\t\tB.string\n\t\t\t\t\t\t\t\t\t\tC.Float\n\t\t\t\t\t\t\t\t\t\tD.Unsign")
                ans=input("\n\t\t\t\t\t\t\t\t\t\t")
                if ans=='a':
                    count+=1
                else:
                    pass
                os.system("cls")
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\tQ5. Which is the valid declarations within an interface definition?\n\n\t\t\t\t\t\t\t\t\t\tA.public double methoda();\n\t\t\t\t\t\t\t\t\t\tB.public final double methoda();\n\t\t\t\t\t\t\t\t\t\tC.static void methoda(double d1);\n\t\t\t\t\t\t\t\t\t\tD.protected void methoda(double d1);')    
                ans=input("\n\t\t\t\t\t\t\t\t\t\t")
                if ans=='a':
                    count+=1
                else:
                    pass
                os.system("cls")
                t="THANK YOU"
                print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t\t\t\t\t'+t.center(19,"*"))
                print('\t\t\t\t\t\t\t\t\t\t\t'f" Your score is {count} out of 5")
                with open('Information.py','a') as f:
                    f.write(' ' +str(count))
                    f.write(' '+'\'Java\'')
                    f.write('\n')
                    f.close()
                input('\t\t\t\t\t\t\t\t\t\t!! Your Mark has Been Recorded !!')
                exit()
            else:
                print("Error..... Re-enter the no.")
                break
    else:
        print("You Enter Wrong Password")
        
