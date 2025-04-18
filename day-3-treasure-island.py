# This is a "Choose Your Own Adventure" text based game called Treasure Island. It features multiple paths, Input Validation with Flags and if/elif/else statements for logic. 

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.\nYour mission is to find the treasure.")
game_over = False
game_won = False
reached_cabin = False

choice1 = input("You've reached a crossroad. You can go left or right, which way will you go?"
                "\nType \"left\" to go left or type \"right\" to go right\n").lower()

if choice1 == "left":
    choice2 = input("You see an old dock with a ghostly looking boat that is docked. "
                    "Do you enter the boat?"
                    "\nType \"yes\" to get onto the boat or type \"no\" to walk away from the boat\n").lower()

    if choice2 == "no":
        game_over = True
        print("You decide it is best to not get on the boat and you turn around to walk away, but when you do "
              "you slip on the wet wood and fall into the water that is filled with Piranhas and you die.")

    elif choice2 == "yes":
        choice3 = input("You get on the boat and it starts to sail away from the dock. After some time, "
                        "the boat reaches an island with an old log cabin, do you enter?"
                        "\nType \"yes\" if you want to enter the cabin or type \"no\" if you want to walk away from the cabin\n").lower()

        if choice3 == "no":
            game_over = True
            print("You approach the door, but when you are about to open it, something in your mind tells you not too "
                  "and you walk away, never to find the treasure chest.")

        elif choice3 == "yes":
            reached_cabin = True

        else:
            game_over = True
            print("The gods are not happy with your response and have banished you.")

    else:
        game_over = True
        print("The gods are not happy with your response and have banished you.")

elif choice1 == "right":
    choice4 = input("You come across a murky lake. You see a golden glimmer in the water "
                    "Do you reach for it? "
                    "\nType \"yes\" to reach for the object in the water or type \"no\" to ignore the object and walk away\n").lower()

    if choice4 == "yes":
        game_over = True
        print("You reach into the water to grab the glimmering object and once you wrap your fingers around it, "
              "a hand grabs your wrist and pulls you into the water. Dragging you into the deep water and you drown.")

    elif choice4 == "no":
        choice5 = input("You choose not to grab the object and instead, head towards an old cabin in the distance "
                        "Do you want to enter the cabin? "
                        "\nType \"yes\" to enter the cabin or type \"no\" to turn around and leave the cabin.\n").lower()

        if choice5 == "no":
            choice6 = input("You decide to not enter the cabin and turn around. When you do, you see a minotaur "
                            "with a bow on its back and a sword in it's hand, ready to fight you. "
                            "Do you fight the minotaur or do you run away? "
                            "\nType \"fight\" if you choose to fight or type \"run\" to run away from the minotaur.\n").lower()

            if choice6 == "fight":
                game_over = True
                print("You decide to fight the beast. You reach your hand over to your waist, to grab a sword and "
                      "you realize you don't have a sword... The minotaur stabs you with their sword and kills you.")

            elif choice6 == "run":
                game_over = True
                print("You turn around to run away, then you feel a sudden sharp pain in your back, "
                      "the minotaur has shot you with their bow and you fall to your knees, as the light fades from your eyes.")

            else:
                game_over = True
                print("The gods are not happy with your response and have banished you.")

        elif choice5 == "yes":
            reached_cabin = True

        else:
            game_over = True
            print("The gods are not happy with your response and have banished you.")

    else:
        game_over = True
        print("The gods are not happy with your response and have banished you.")

else:
    game_over = True
    print("The gods are not happy with your response and have banished you.")

if reached_cabin:
    choice7 = input("You enter the cabin and inside are 3 doors. a Blue Door, a Red Door and a Yellow Door "
                    "Which door do you choose? "
                    "\nType \"blue\" to go through the Blue Door, or Type \"yellow\" to go through the Yellow Door, or "
                    "Type \"red\" to go through the Red Door.\n").lower()

    if choice7 == "blue":
        game_over = True
        print("You open the Blue Door and see an empty void, then the next minute you are sucked in, never to be seen again.")

    elif choice7 == "red":
        game_over = True
        print("You open the Red Door and a burst of fire and lava shoots out, scorching you alive.")

    elif choice7 == "yellow":
        game_won = True
        print("You open the Yellow Door and inside, you see a bright shimmer of gold. YOU FOUND IT, YOU FOUND THE TREASURE!")

    else:
        game_over = True
        print("The gods are not happy with your response and have banished you.")

if game_over:
    print("Game Over!")

if game_won:
    print("You won!")
