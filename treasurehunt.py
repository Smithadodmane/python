print('''  
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
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
c1=input('You\'re at the the cross road,where do you want to go?Type "left" or "right"')

if c1 == "left":
    c2 = input('You\'ve come to the lake.'
           'There is an island in the middle of the lake.'
           'Type"wait" or "swim"').lower()
    if c2  == "wait":
        c3= input( "you have arrived at the island unharmed."
                   " There are three doors that is RED,YELLOW and BLUE."
                   "Which colour do you use?").lower()
        if c3== "red":
            print("you enterd a room of beasts. GAME OVER")
        elif c3=="blue":
            print("you enterd a room of fire. GAME OVER")
        elif c3=="yellow":
            print("YOU FOUND THE TREASURE.YOU WIN!")
    else:
        print("you fell into the hole .GAME OVER")
else:
     print("you fell into the hole .GAME OVER")
