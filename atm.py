print("this is atm program")
str=input("Please, enter your name :: ")
print("welcome to the atm ",str)
i=1
while(i<3):
     print("1. Press 1 to check your available balance\n2. Press 2 to withdrawal cash\n3. Press 3 to deposits cash\n4. Press 4 to exit")
     print(str,"enter your choice :: ")
     choice=int(input())
     if(choice==1):
            print("Enter your details :: ")
            str1=input("please, enter your username :: ")
            acc=int(input("Enter your account number :: "))
            pin=int(input("Enter your atm pin :: "))
            print("you have successfully logged in")
            print("your available balance is 30000")
            i=i+1
     elif(choice==2):
              print("Enter your details :: ")
              str1=input("please, enter your username :: ")
              acc=int(input("Enter your account number :: "))
              pin=int(input("Enter your atm pin :: "))
              print("you have successfully logged in")
              print("you have 15000 ruppee in your account")
              cash=int(input("how much money you want to withdrawal :: "))
              rem=15000-cash
              print("you have successful withdrawal your money and your remaining balance is \n",rem)
              print("THANKYOU FOR USING OUR SERVICES")
              i=i+1
     elif(choice==3):
              print("Enter your details :: ")
              str1=input("please, enter your username :: ")
              acc=int(input("Enter your account number :: "))
              pin=int(input("Enter your atm pin :: "))
              print("you have successfully logged in")
              cash=int(input("how much money you want to deposit in your account :: "))
              total=15000+cash
              print("your money has been succesfully added to your account and you total balance is \n",total)
              i=i+1
     elif(choice==4):
              print("are you want to exit ?\n 1. press 1 for yes \n 2. press 2 for no")
              choice1=int(input())
              if(choice1==1):
                        break
              elif(choice1==2):
                          i=i+1
                          continue
              else:
                           print("you have entered wrong input")
     else:
            print("you have entered wrong input")
    
    
            
    
    

