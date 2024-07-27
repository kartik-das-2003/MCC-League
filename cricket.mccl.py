import random
u_run = 0
c_run = 0
count = 0
target_score = 0;

def invalidScore(n):
    if(n>6 or n<0):
        return False
    else:
        return True
    
print("MCCL(MAN vs COMPUTER CRICKET LEAGUE):") 
print("~ developed by Kartik Das\n")   
print("We Are Batting ! Computer Is Bowling!!")
while(True):
    computer_action = random.randint(1, 6)
    user_action = int(input("Bat:"))
    
    if(invalidScore(user_action)==False):
        print("UMPIRE::You Shoud Be Punished! :(")
        print("ACTION::Bowler Hits The Ball To Batsman Head")
        break
    else:
        print("You chose ",user_action,"and computer chose ",computer_action)
        
        if(user_action == computer_action):
            print("OUT!--OUT!--OUT!")
            break;
            
        else:
            u_run = u_run + user_action;
        
            
        print("**user:",u_run)
        print("**computer:",c_run)
    

print("")    
print("---------------Break---------------")
target_score = u_run;
print("Target Score:",target_score)
print("Computer Is Batting ! We Are Bowling!!")
while(True):
    computer_action = random.randint(1, 6)
    user_action = int(input("Ball:"))
    
    if(invalidScore(user_action)==False):
        print("UMPIRE::You Shoud Be Punished! :(")
        print("ACTION::Batsman Hits The Bat In Bowlers Head")
        break
    else:
        print("You chose ",user_action,"and computer chose ",computer_action)
        
        if(user_action == computer_action):
            print("OUT!--OUT!--OUT!")
            break;
        elif(c_run >= target_score):
            break;
        else:
            c_run = c_run + computer_action;
    
        
        print("**user:",u_run)
        print("**computer:",c_run)
        if(c_run>u_run):
            break;
   
print("")
print("---------------Match Result---------------")
if(c_run>u_run):
    print("Bad Luck!!")
    print("RESULT:Computer Wins The Match!!")
elif(c_run<u_run):
    print("Hurry!!")
    print("RESULT:You Win The Match!!")
else:
    print("RESULT:Superover Needed!")
