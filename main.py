''' Project:
    Snake, Water, Gun Game
    1 for Snake
    -1 for Water
    0 for Gun    
'''
import random

computer = random.choice([1, -1, 0])
ch = input("Enter your choice: ")

youDict = {'s':1,'w':-1,'g':0}
mainDict={1:"Snake",-1:"Water",0:"Gun"}
you=youDict[ch]

print("You Choose: ",mainDict[you])
print("Computer Choose: ",mainDict[computer])

if(computer == you):
    print("It's a Draw!")
else:
    if(computer==1 and you==0):
        print("You won!")
    elif(computer==1 and you==-1):
        print("You Lose!")
    
    elif(computer==-1 and you==1):
        print("You won!")
    elif(computer==-1 and you==0):
        print("You Lose!")

    elif(computer==0 and you==-1):
        print("You won!")
    elif(computer==0 and you==1):
        print("You Lose!")
    
    else:
        print("Something wents wrong!")
    
