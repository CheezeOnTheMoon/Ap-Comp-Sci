

#Text Adventure
def TextAdventure():
#First question to turn around or not
    ans1 = input("You are running away from something in a field." " Do you turn around?: ")
    #Answer to turn around
    if ans1 == "Yes":
        print("You see a massive crocodile running slightly faster than you")
        FightOrRun()
    #Answer to not turn around
    if ans1 == "No":
        print("You hear a stomping noise come closer")
        RunDecision()



#Question to fight or run away
def FightOrRun():
    ans2 = input("Do you fight it or run away?: ")
    #Answer to fight it
    if ans2 == "Fight":
        print("You begin the fight")
        DuringFight()
    #Answer to run away
    if ans2 == "Run":
        print("You keep running away as fast as you can through the field until you get out of it.")
        RunDecision()


#Question of where to run
def RunDecision():
    print("It seems like it's following you for some reason, so you try to lose it.")
    ans3 = input("You see a city and a forest. Where do you run?: ")
    #Answer to run into the city
    if ans3 == "The city":
        print("You run into the city past a bunch of buildings.")
        RunIntoCity()
    #Answer to run back into the forest
    if ans3 == "The forest":
        print("You sneak past the monster back into the forest.")
        RunIntoForest()

#Question of if to go in the house in the forest
def RunIntoForest():
    ans5 = input("You run into the deeper part of the forest and find an abandoned house." "Do you go into it or pass it.: ")
    #Answer to go in the forest house
    if ans5 == "Go in":
        print("You go into the house and find an elevator." "You hear the booming footsteps behind you." )
   

#Question of how to fight the crocodile
def DuringFight():
    ans4 = input("Do you punch it, kick it, or shoot it: ")
    #Answer to punch the crocodile
    if ans4 == "Punch it":
            print("It slaps you and you die")
            TextAdventure()
    #Answer to kick the crocodile
    if ans4 == "Kick it":
            print("It eats you and you die")
            TextAdventure()
    #Answer to shoot the crocodile
    if ans4 == "Shoot it":
            print("It gets scared and runs into a river to hide, even though you can still see it.")
            print("You walk over to it and find a qr code on its neck while it thinks it is hidden and scan it on your phone.") 
            RunIntoCity()


#Question of where to enter the facility
def RunIntoCity():
    print("You run into the city and follow the line of destruction to try to find where it came from. You run past a path of destroyed buildings to a more rural part of town and find an abandoned facility that was used for growth horomone research. It looks abandoned and the gates are locked, but luckily for you the crocodile paved a way throught the fence.")
    ans6 = input("There are three different entrances you can walk through. The first is the front door, the second is the basement hatch, and the third is on a rooftop patio by a tree.")
    #Answer to walk through the front door
    if ans6 == "The front door":
        print("You walk through the front door that is now a gaping hole and find a reception area.")
        TheFrontDoor()
    #Answer to walk into the basement
    if ans6 == "The basement hatch":
        print("You walk into the basement where it is flooded by murky water up to your knees.")
    #Answer to enter through the rooftop patio
    if ans6 == "The rooftop patio":
        print("You climb up the tree next to the building and jump onto the open patio. You walk past the patio to the stairs door, but find that the door is locked.")
        
 #Answer to Fight or enter the elevator
def ElevatorOrFight():
    ans7 = input("Do you go in it or stay to fight the monster?: ")
    if ans5 == "Fight":
        print("You hear a stoming noise come closer")
        DuringFight()
    #Answer to go in the elevator
    if ans7 == "Go in the elevator":
        print("You run in the elevator and watch the house collapse as the doors close")
            
def SewerDrain():
    print("The only way you can go to is through a sewer pipe that's sticking out of the ground. Once you crawl into into you come out in a sewer tunnel. It's high and wide enough for you to stand up and walk in")
    ans8 = input("The tunnel splits to the left and to the right. Which way do you go?: ")
    if ans8 == "Go left":
        print("You go through the left tunnel and find a ladder leading up. You climb up it and find yourself in a storage closet.")
    if ans8 == "Go right":
        print("You go through the right tunnel through a long hallway and evantually find your way to a door. You open the door and water rushes through leading to a basement.")
        
def TheFrontDoor():
    ans9 = input("In the reception area there is a staircase leading up and down. Where do you go?: ")
    if ans == "Up the stairs":
        print("You walk up the stairs and find a lab a notes on the table talking about genetic modification. While your looking at them you get hit in the back of the head and knocked out.")
    if ans == "Down the stairs":
        print("You walk down the stairs and walk down a long hallway. You find a door at the end of it and open it")
        InTheDoor()



def InTheDoor():
    print("The door opens up into a large room with test tubes lining the walls and a large test tube in the back of it. As you walk towards it a person walks out from behind it. They congradulate you for making it this far, but then say that this is the end for you. A lot of strange looking monsters break out of the test tubes and run at you.") 
    ans11 = input("How do you fight them")
    if ans11 == "Throw the test tubes at them":
        print("You start throwing the test tubes at the monsters. The glass shatters when it hits them and scatters all over the floor. They can't get to you now without running on the walls.")
        DuringMonsterFight_OneTheWalls()
    if ans11 == "You punch and kick them":
        print("You die")
        TextAdventure()
    if ans11 == "You start screaming and shooting in random directions":
        print("You somehow scare them into not moving and they run away.")
        
        



def DuringMonsterFight_OnTheWalls():
    ans13 = input("They're running on the walls. What do you do?: ")
    if ans13 == "Crawl under a table":
        print("You crawl under one of the lab tables and barricade it; while the monsters struggle to get to you, you hear a loud noise coming from one of the walls. The massive crocodile smashes through it and runs at you. It slips on the broken glass and trips into all of the monsters. They fly through another wall and fall out of the building.")
        AfterTheMonsters()
    if ans13 == "Run away":
        print("They catch up to you and you die")



def AfterTheMonsters():
    print("After the monsters are gone the scientist starts panicking and tries to escape")
    ans16 = input("Do you run after him?: ")
    if ans16 == "Yes":
        print("You run after him and catch up to him. He stops running and gives up on escaping. He starts talking about how about how your dad and him were rivals and that your dad got him expelled from Harvard and that he never forgot that. He wanted to get revenge on him but he already passed so you're the only one left.")
    if ans16 == "No":
        print("He escapes and you never hear from him again")
        BadEnding()

def BadEnding():
    print("Wow! You finished the game! Too bad you go the bad ending.")





                  
TextAdventure()
