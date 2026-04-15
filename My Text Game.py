# My Text Game
# Intro
print("""You wake up in the middle of the night and hear loud screams outside your home.
You grab your trusty sword and go outside to check the situation.
You find a group of 3 goblins running away with a young woman.
you follow them until they enter a cave, which you can only assume is their hideout.
You wonder what they want with a human woman in the middle of the night.
Before you are lost in thought, you shake your head and focus on saving the woman.
You take a deep breath, gather your courage, and enter the cave!
As you walk in you notice that the cave splits into two paths.\n""")

# While loop for path
while True:
    # Path choice with if statements
    path1 = str(input("Do you go Right or Left? "))
    if path1.upper() == "RIGHT":
        print("""\nAs you go down the right path, you start seeing light, as you get closer you find a large room
with a fireplace in the middle, a cage containing the kidnapped woman, and the 3 goblins talking.
You try to listen, but you can't make out what they're saying.
It must be some goblin language that you don't understand. As you wait for a few minutes,
one of them goes towards a cloth on the floor, lays down and starts snoring.
The second goes towards the fireplace, where he starts adding herbs to a large boiling cauldron.
The third, who looks older and slightly smarter, so you assume he's the leader, walks up to the woman, stairs at her, 
and starts rubbing his belly and licking his lips, she whimpers in fear, but he just laughs with content.
Now you know why they took the woman! They're going to eat her! 
You need to save her, what will you do?\n""")

        # While loop for attack
        while True:
            action1 = str(input("Attack the sleeping goblin (S), attack the cook (C), or attack the boss (B)? "))
            if action1.upper() == "S":
                print("""\nYou approach the sleeping goblin and stab him in his sleep. He dies, but the other goblins
see you, the cook throws hot boiling water on your face, blinding you with excruciating pain
as you scream in agony, the boss runs his sword through your heart. The last thing you heard
was the cook saying 'fresh meat'. You're dead!\n""")
                print("Try Again!\n")
            elif action1.upper() == "C":
                print("""\nAs you approach the cook, he chokes on the soup he was tasting. As he fumbles, you slash his
neck instantly decapitating him. His head drops in the cauldron splashing hot water on you.
As you get distracted by the hot water, the boss approaches you with a drawn sword!
As you pull out your sword to clash with him, you feel a dagger slitting your throat.
Everything goes black, the sleeping goblin woke up and killed you. You're dead!\n""")
                print("Try Again!\n")
            elif action1.upper() == "B":
                print("""\nYou sneak up on the boss, and without hesitation, you decapitate him with one strike!")
The cook sees this, he fumbles up, then slips and falls into the cauldron.
You hear screams, then gurgling, then the sound dies.
As for the sleeping goblin, he wakes up hearing the cook scream and boil, he looks in your
direction and sees his boss' head on the floor, he gulps and starts running, only to slip and
break his neck. 'Now that was easier than I thought' you thought to yourself.
'Oh yeah the woman!' you remembered. You look at the woman, her eyes are wide, she looks happy!
At last, her hero is here to save her. She tells you 'Please save me!'.
You nod heroically, and as you hurry to open the cage, you realize there is a lock!
You wonder 'who has it?', you start searching the boss' body, but it's not there! then you
check the sleeping goblin, you find nothing on him either. 'Shit!' you say to yourself,
'the cook must have it'. You look at the woman and tell her
'Well, I guess I'll see you in the morning', she looks surprised and says 'What?!'
You light a torch, turn the cauldron fire off and tell the woman 'Good night!'
She yells 'Wait don't leave!', but you just head home. After all, it's a big cauldron
It won't cool off till next morning! You go home to finish your sleep.\n""")
                print("Game Over. You Won!")
                break  # Exits the attack loop
            else:
                print("Invalid Input, Try Again!\n")
        break  # Exits the path loop
    elif path1.upper() == "LEFT":
        print("""\nAs you follow the left path it gets darker, you're unable to see anything, as you keep going 
there is a sudden drop 100 meters high with rocks at the bottom. You trip and fall! You're dead!\n""")
        print("Try Again!\n")
    else:
        print("Invalid Input, Try Again!\n")
