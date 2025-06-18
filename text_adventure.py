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
        return choice_1_left() 
         
    else: 
        return choice_1_right()
        
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
            print("You've solved the riddle! The wizard congradulates you, and gives you a map!\n")
            inventory.append("map") 
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
            print("You've solved the riddle! The wizard congradulates you, and gives you a map!\n")
            inventory.append("map") 
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
    print("You continue along the path, when suddenly a fork in the road appears...\n")
    
    path_choice = input("Will you (a) Go left, (b) Go right, or (c) Use map:  ").strip().lower() 
    
    # If we go left
    if path_choice == 'a':
        print("You come across a dark mysterious cave! You hear a strange sound coming from inside, and you venture on in... \n")
        print("There's a goblin! He looks to be holding some kind of key.\n")
        
        if "Glittering Fish" in inventory:
            offering = input("Will you (a) Take the key from them or (b) Offer them 'Glittering Fish': ").strip().lower()
        
            if offering == 'a':
                print("You steal the key and run away as fast as you can. As you run, the goblin curses you!\n")
                inventory.append('key')
                inventory.append("goblin curse")      
            elif offering == 'b':
                print("You offer the goblin a 'Glittering Fish' in exchange for the key. He happily accepts and starts devouring the fish!\n")
                inventory.remove("Glittering Fish")
                inventory.append("key")
        else:
            goblin = input("Will you (a) Take the key from them or (b) Ask nicely for the key: ").strip().lower()
            
            if goblin == 'a':
                print("You steal the key and run away as fast as you can. As you run, the goblin curses you!\n")
                inventory.append('key')
                inventory.append("goblin curse") 
            else:
                print("Since you asked politely, the goblin hands you the key.")
                inventory.append("key")  
        
            
        print("You continue along the path...\n")
        return 4
            
    # If we go right 
    elif path_choice == 'b':
        return 4  
    # If we use map 
    else:
        print("You read the map, and it leads to a large castle said to have treasure! It tells you to turn right at the fork and continue on.")
        return 4  


def level_4():
    print("You see a castle in distance, and make your way towards it.\n")
    augment_condition = 1 if "goblin curse" in inventory else 0
    level_4_augment = {
        "first": [
            "welcome you nicely",
            "snear at you as you pass",
        ],
        "second": [
            "allow you to pass",
            "block your way",
        ],
    }
    
    print(f'You walk up to the castle guards, who {level_4_augment["first"][augment_condition]}.\n')
    
    if augment_condition == 1:
        print("The grand king looks upon with fear, and removes you from his court.\n")
        break_curse()
    else:
        pass 
    
    if "key" in inventory:
        print("The grand king welcomes you in with open arms, and gives you a treasure chest as congratulations.\n")
        win() 
    else:
        print("The grand king welcomes you in, and invites you to his royal feast.\n")
        return 5 
    

'''
1. we have key and no curse
2. we have no key  
3. We have curse
4. we have option to break the curse 

- Make functions for winning or breaking the curse 

'''

def win():
    print("Congratulations! You have completed the quest and won the game!") 
    return 5


def break_curse():
    # Return to goblin to break the curse
    option_1 = input("The head knight offers a solution: (a) Go to the church and repent (b) Return to the goblin")
    
    if option_1 == 'a':
        print("You go the church and pray for the curse to be releaseed.\n")
        inventory.remove("goblin curse")
        return 4
    else:
        print("You return to the goblin, and they tell you must solve their riddle for the curse to be broken.\n")
        riddle = input(
            """When I am alive I do not speak. 
            Anyone who wants to takes me captive and cuts off my head. 
            They bite my bare body I do no harm to anyone unless they cut me first. 
            Then I soon make them cry.\n 
            (a) Onion (b) Goblin?  \n""")
        
        if riddle == 'a':
            print("You have solved the goblin's riddle, and the curse has been broken!\n")
            inventory.remove("goblin curse")
            return 4 
        else:
            print("The goblin has forgotten the answer.... He lifts the curse off of you\n")
            inventory.remove("goblin curse")
            return 4

def main():
    # While resest is false, we go through
    # if resest is set True, start from very beginning 
    
    print(instructions)
    current = 1
    while True:
        # View inventory option
        view_items = input("Would you like to view your current inventory? Yes(a) or No(b): \n")
        
        if view_items == 'a':
            print(f'Current Inventory: {', '.join(inventory)}\n') 
        else:
            pass 
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