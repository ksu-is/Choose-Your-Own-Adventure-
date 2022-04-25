name = input ("Type Your name: ")
print ("Welcome", name, "to this adventure" )

answer =input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?" ).lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across it. Typpe walk to walk around  and swim to swim across:")

    if answer == "swim":
        print("you swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game")
    else:
        print('Not a valid option. You lose')
        
elif answer == "right":
    answer = input("you come to a bridge, it looks wobbly, do you want to cross it or head back? (cross/go back) ")
    
    if answer == "back":
        print("You go back and get eaten by a big monster and lose")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger. Do you talk to them (yes/no)")
    
    if answer == "yes":
        print("You talk to the stranger and they give you gold. You win!")
    elif answer == "no"
        print("you ignore the stranger and they are offended and you lose")
    else: 
        print('Not a valid option. You lose')
else:
    print('Not a valid option. You lose')
    
    
   
else:
    print('Not a valid option. You lose')
    
print("Thanks for playing our game")
