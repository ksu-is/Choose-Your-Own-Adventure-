name = input ("Type Your name: ")
print(
                                                                                 
                                                                       '.-'._____.'-.'
                                                                        /\_\_  _/_/\
                                                                       / / @ \/ @ \ \
                                                                       \ \___/\___/ /
                                                                        \____\/____/
       "+-----------------------------------------------+        ___ ____/:     :\____ ___
       |Welcome", name, "to this adventure             |       .'          \   /          '.
       |You are playing as Scrappy the Owl on his way  |      /             -.-             \
       |to his first day of Dr. Thomas Application     |     /          +-| |---/ /+        '\  
       |Development class at Kennesaw State University.|    |           | | |--/ /-|          |
       |But Georgia traffic is backed up. So you will  |   (     /' .   | | | / /     .'\   '.)
       |have to trek the rest of the way on foot.      |   /   _/   ".  +-| | \ \--+ ."  \_. '\
       |       You 100 minutes to get to class.        |  |    |      ".+-| |--\ \ |"     |'.  |
       |               Good Luck!                      |  |    |       ||-| |---\ \|      | :  |
       +-----------------------------------------------+   \   |       |_____._____|      | : /
                                                           ")
hp = 100
While true:
q1 =input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go?" ).lower()

if q1.lower() == "left":
    q11 = input("You come to a river, you can walk around it or swim across it. Type walk to walk around  and swim to swim across:")

    if q11.lower() == "swim":
        q12 = ("You see an alligator swimming directly at you. Do you fight or keep swimminng?")
            if q12.lower() == 'fight':
                print('You manage to fend off the alligator, but not without taking some damage."
                      hp -=10
                Break
            elif q12.lower() == 'swim':
                print('You try to swim faster but the alligator is too fast for you in the water. he takes a big bite out of your leg before you reach the other side.')
                break
            else:
                print(error)
    elif q11.lower() == "walk":
        q13 = input("A badger growls at you and looks prone to fight. Do you fight or runaway?")
            if q13.lower() == 'fight':
                print('You take some nasty hits from a ferocious beast, but eventually it retreats back to its lair')
                break
            elif q13.lower() == 'run':
                print('Good choice! fighting an animal like that would be suicide!')
                break
            else:
                print(error)
    else:
        print(error)
elif q1.lower() == "right":
    q14 = input('You come across a large mountain. Do you go over or around?)
        if q14.lower() == 'over':
            q15 = input('As you climb, you encounter upon a bunch of goats that inhabit this mountain. Do you want to pet the goat?')
                if q15.lower() == 'yes':
                    print('You have made a new friend! You are very careful when aproaching and the goat decides not to buck you off the mountain. It has such soft fur!')
                    break
                elif q15.lower() == 'no':
                    print('taking a long climb over the mountain to get away from the goats has made the expedition harder. You notice you are quite exhausted because of it. But you must move on.')
                    break
                else:
                    print(error)
                    break
               
       elif q14.lower() == 'around':
           q16 = input('Oh my god! Its a grizzly bear! Do you try to intimidate it or do you want to fight?')
                if q16.lower() = 'fight':
                       print('you manage to find a stick and impale the bear in the chest. The bear bleeds out.')
                       break
                elif q16.lower() = 'intimidate':
                       print('big mistake. The bear swipes at you twice. Do you continue to fight or do you try to run away(stay/run)')
                       break
       if hp > 80;
             q17 = input('As you are running through the forest you trip over the portal gun and it fires a portal which you fall into. you sudenly find yourself in the marvels new your city. Do you walk towards avengers tower or the sanctum sanctorum?(Avengers Tower/Sanctum Sanctorum)')          
             if q17.lower() = 'Avengers Tower'         
                   print('You find Captain America onlooking a giant army of symbiotes about to attack the city. He looks at Scrappy and says that their is no time to waste and gives him a shield. Scrappy and Captain America fight of the symbiotes threatning the city.')   
                    break
             elif q17.lower() = 'Sanctum Sanctorum'
                   print('You find Doctor Strange and Wong seeing the symbiotes ooze through the city. Wong sees that Scrappy is strong and magically inclined and gives him a sling ring. Scrappy, Doctor Strange, and Wong all open up a huge portal that sends the symbiote army into the sun.') 
                   break
                
              if hp > 60; 
                q18 = input('you are left in a dark forest alone with your thoguths. Do you walk further in the forest or turn back?')
                  if q18.lower() = 'turn back':
                    print('you manage to get out of the forest and find the police')
                       break
         
                       
              
           
       else:
            print(error)
else:
    print(error)
 
if hp < 20:
      answer = input('Youve finally made it on campus... And with a few minutes left to spare! However, You start to feel a dark presence in the air.
                     All of a sudden, Radagon from Elden Ring appears. Choose either magic, fire, lightning, or holy:')
                     if answer.lower() = 'magic':
                            print('You are able to defeat him.')
                            hp -=15
                     elif answer.lower() = 'fire':
                            print('good choice! He seems to be weak to fire so you beat him quicker.')
                            hp -=10
                     elif answer.lower() = 'lightning':
                            print('You are able to defeat him.')
                            hp -=15
                     elif answer.lower() = 'holy':
                            print('Oh no! It seems as though he is resistant to holy!')
                            hp -=20
def time_check():
       if hp > 9:
             game_over = print("You made it to class with time to spare! Thank you for playing!")
             quit()
       elif hp < 1:
             game_over = print("You are out of time, " + name + ". You are late to your class.")
             quit()
       else:
             game_over = print("You made it just in time! Next time, try to not cut it so close ;)")
             quit()
time_check()
