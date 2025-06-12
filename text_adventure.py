# CHARACTER (gets picked or introduced)
# name_of_character = 'user_name' 

# Welcome Character 
# print statement to say hi

# GAME INSTRUCTIONS
# print statement

# play the game! provide their choices
# some levels have multiple choices, others have 1(pseudo 2 choices)
# want to keep track of what level they are on, and what choice user makes

# player wins/game ends

# bye for now!

world_name = 'Narnia'
character_name = input(f"Hello! Welcome to {world_name}! What is your name?: ") 

instructions = """ 
This is a text adventure game. You CHOOSE your destiny. 
When presented with a choice, choose the path that best suites you!
"""

inventory = [] 

def level_1():
    print("You wake up in a mysterious forest 🌲\n")
    
    choice_1 = input("Go left(a) or right(b)?: ").strip().lower()
    
    if choice_1 == "a":
        choice_1_left()  
    else: 
        choice_1_right()
        
def choice_1_left():
    print("You find a river full of glittering fish 🐟\n") 
    # Option to grab fish 
    choice_2 = input("Would you like to add Glittering Fish to your inventory? Yes(a) or No(b): ").strip().lower() 
    
    if choice_2 == 'a':
       inventory.append("Glittering Fish") 
       print("Glittering fish has been added to your inventory!\n") 
       return 2
       
    else:
       print("You leave the fish alone and continue on!\n") 
       return 2
       
def choice_1_right():
    # print("A wizard appears and challenges you to a riddle 🧙‍♂️") 
    return 2 

# Start Level 2
# Wizard challenges us with a riddle 
# We accept his challenge 
# If we have glittering fish: options are to solve, or to use fish 
# Use fish, move to level 4 

# if we don't, options are to solve or sent back to level 1
# If we solve, we move to level 3 

def level_2():
    # Start with Wizard's riddle 
    print("A wizard appears and challenges you to a riddle 🧙‍♂️\n") 
    
    challenge = input("Do you accept his challenge? Yes(a) or No(b): ").strip().lower()
    
    # Breakpoint 
    if challenge == "a":
        pass 
    else:
        print("The wizard challenges you again, but this time says pretty please. Since he's being polite... \n")
       
    riddle = """ 
    What is the thing that you throw away the outside, cook the inside, then eat the outside and throw away the inside?
    """
    
    if "Glittering Fish" in inventory:
        # options for solving riddle (or throwing fish) 
        # 1. possible answer
        # 2. possible answer 2
        # 3. Use fish
        # 4. Give up 
        print(f"The wizard presents the following riddle: {riddle}\n")
        
        answer = input("(a) Fish, (b) Corn, (c) I have no idea, (d) Use Fish: Enter the number of your choice: ").strip().lower() 
        
        if answer == "a":
            # move to level 3, solved the riddle 
            print("You've solved the riddle! The wizard congradulates you, and let's you continue on.\n") 
            return 3
        elif answer == "b":
            # incorrect answer, send back to level 1
            print("Sorry, but that was incorrect. The wizard casts a spell, you see a bright light, then you wake up back in the mysterious forest.\n")
            return 1  
        elif answer == "c":
            # giving up, back to level 
            print("The wizard insults your lack of effort, then casts a spell, you see a bright light, then you wake up back in the mysterious forest.\n")
            return 1
        else:
            # using fish, secret buff, moving to level 4 
            print("You use the Glittering Fish, which turns out to be a magical fish! You are instantly teleported away from the wizard.\n")
            inventory.pop()
            print("Glittering Fish was removed from inventory") 
            return 4
    else: 
        # options with no fish 
        # 1. possible answer
        # 2. possible answer 2
        # 4. Give up 
        print(f"The wizard presents the following riddle: {riddle}")
        
        answer = input("(a) Fish, (b) Corn, (c) I have no idea: Enter the number of your choice: ").strip().lower() 
        
        if answer == "a":
            # move to level 3, solved the riddle 
            print("You've solved the riddle! The wizard congradulates you, and let's you continue on.\n") 
            return 3
        elif answer == "b":
            # incorrect answer, send back to level 1
            print("Sorry, but that was incorrect. The wizard casts a spell, you see a bright light, then you wake up back in the mysterious forest.\n")
            return 1   
        else:
            # giving up, back to level 
            print("The wizard insults your lack of effort, then casts a spell, you see a bright light, then you wake up back in the mysterious forest.\n")
            return 1 
        
     
    
    

 
    
    
def level_3(): 
    pass 

def level_4():
    pass 


def main():
    # While resest is false, we go through
    # if resest is set True, start from very beginning 
    
    print(instructions)
    current = 1
    while True:
        if current == 1:
            current = level_1()
        elif current == 2:
            current = level_2()
        elif current == 3:
            current = level_3()
        elif current == 4:
            current = level_4()
        else:
            break   # game over or exit code
    
    
main() 