name = input ("Type Your name: ")
print ("Welcome", name, "to this adventure" )

answer =input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?" ).lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across it. Typpe walk to walk around  and swim to swim across:")

    if answer == "swim":
        print("you swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walk for many miles, ran out of water and you lost the game")
    else:print('Not a valid option. You lose')
elif answer == "right":
    print()
else:
    print('Not a valid option. You lose')