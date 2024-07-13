import string

users = ["Uchechukwu", "Boluwatife", "Adewunmi", "Tauhid", "Atilola"]
caps = string.ascii_uppercase

numbers = []

for i in range(10):
    numbers.append(str(i))

special_chars = ["!", "@", "#", "$"]
name_check = False

def name_available(name):
    if name.title() in users:
        return False
    else:
        return True

def number_found(name):
    found = False
    for number in numbers:
        if name.find(number) > -1:
            found = True
    return found

def caps_found(pw):
    found = False 
    for letter in caps:
        if pw.find(letter) > -1:
            found = True
    return found

def special_found(pw):
    found = False
    for char in special_chars:
        if pw.find(char) > -1:
            found = True
    return found

while True:
    if not name_check:
        username = input("Create your username: ")
        if name_available(username):
            if not number_found(username):
                if 2 < len(username) < 15:
                    name_check = True
                    users.append(username)
                    print("username created")
            else:
                print("Username cannot contain numbers")
        else:
            print("Please choose another username")
    else:
        password = input("Create your Password: ")
        if caps_found(password):
            if special_found(password):
                if number_found(password):
                    if len(password) > 7:
                        print(f"Your username is {username} and your password is {password}")

                        break
                    else:
                        print("Password must be at least 8 characters long")
                else:
                    print("Password must contain a number")

            else:
                print('password must contain a special character ("!", "@", "#", "$")')
        else:
            print("password must contain a capital letter")

print()
print()
print("""Welcome to 'SURVIVE THE DAY!' an adventure game that tests your instinct to see how you can survive in a cruel 
world. Grab some popcorns! and take a chance at SURVIVAL""")
print()
print()
story1="""Game starts, you're listening to 'ALL OF ME' by John Legend somehow in a moving train - still cannot figure out 
how you got there and the next you're awoken by a JERK in the train. You realise you are the only one in the train and 
you are alredy past your stop; Interestingly, you have a flat battery. You can either get down at the last stop or get 
down now. [last stop/now] ?"""

story2="""After twenty minutes, the train finally stops. You get down and find your way out of the train station, then 
you realise that you're in a very crowded neighbourhood. You can either meet one of the people in the neighborhood to 
find out where you are or find the location yourself. [meet/find]?"""

story3="""You meet and ask a person dressed in yellow. You engage him and he tells you that you are two hundred miles away
from home. He offers to help you by taking you to the nearest bus station but with a risk or drive you home himself but 
with a price.  [bus station/home]?"""

story4="""On your way to the bus station, you realise that the guy dressed in yellow is no where to be found. Suddenly 
you feel a hand on your shoulder accompanied by a sharp pain on your head......You fall unconscious! You're awoken with a 
loud noise, you're at the corner of the room without shoes. You look around and you see a masked man in a room with just 
one window.  [attack the man/wait]?"""

story5="""You enter his small yellow car and there is an uncomfortable silence. After a while you begin to feel comfortable
and then you look out the window. Almost immediately, you feel a sharp pain on your neck, you have been injected......You 
become unconscious! You're awoken with water being poured on your head, you feel really dizzy making it hard to see the 
person just beside you. The person dropped a plate of food.  [eat or starve]?"""

story6="""You walk for about ten minutes then you see a signboard which tells you that you are about two hundred miles away
from home. You look around and realise that there is only one house with smoke coming out of its chimney. You decide to go 
to the occupied house or go to the house which looks unoccupied.  [occupied/unoccupied]?"""

story7="""You walk towards the house and knock, you are recieved warmly. After some minutes of being in the living room, 
you smell something which put you to sleep immediately......You are unconscious! You're awoken by the pattering of rain 
against a window, you look around to see an empty, dirty room. Just then a woman enters the room and starts to clean. Then 
she comes towards your feet, unties you and tells you to run.  [kick/run away]?"""

story8="""Fortunately, the door is unlocked so you decide to spend the night there. You hear a sound and looked frantically
around but it was only a mouse. Suddenly you got hit at the back of your head......You fell unconscious! You're awoken by 
slamming doors which sounds close by. You feel the urge to pretend like you're still asleep.  [sleep/wake]?"""

story9="""You realise that time is far spent so you speedwalk out of the train station. You're now on a lonely crossroad 
and you can either turn left or right.   [left/right]?"""

story10="""You turn left and after walking for a few minutes, you hear tiny footsteps and feel something wet on your right 
foot. You look down to see a white Pomeranian dog with a collar.  [collar/run]? """

story11="""You check the collar and see an address and the picture of a house. You look around and see the same house far 
ahead. You walk there, knock and almost immediately the door creaks open. You walk in and announce your presence, a few 
seconds later you are hit with a bat......You fell unconscious! You're awoken by the barking of a dog by your right hand 
side, you look around and you see a ladder at your other side will you pet the dog or climb the ladder?    [pet/climb]?"""

story12="""You've been running for a while so you stop to catch your breath behind a withered tree. Suddenly you heard 
footsteps and before you could turn, your nose is covered and you fall down...... You are unconscious! You're awoken by 
the blair of a siren, causing you to jump off the wooden chair. You look around to see a hefty man behind you. 
[push/slap]"""

story13="""You turn right and you feel like you're slowing down due to thirst. You continue your journey and see a young 
man on a bicycle with a jug of water. You either stop him for directions or for water.   [directions/water]? """ 

story14="""You stop the young man for directions and he tells you to climb on his bicycle so he could take you to the bus 
station. In a twinkling of an eye you were tripped over and hit on the head with a rock......You fall unconscious! You're 
awoken by the choking smell of burnt food. You start to cough and a young man enters the room. He comes close to you and 
starts to put a tape over your mouth. You decided to bite him or struggle.  [bite/struggle]"""

story15="""You stop the young man for water and he happily gives you the jug. As you were drinking, you get hit on the 
head with a stick...... You fall unconscious! You're awoken by the urge to go to the bathroom. You decide to either bang 
on the door or call for help.  [bang/shout]?"""

end_story1="""You decide to attack the man with your elbow. Immediately you attack him, he hit you back with a strong 
force!!!"""

end_story2="""You decide to wait for the masked man to leave. After a while of just looking at you, he finally leaves. You 
stood up, took the half broken table towards the window and climbs up. You looked down and see a flower bed. You jumped 
down to the flower bed and break your neck!!!"""

end_story3="""You start eating but the food is too spicy and you have no water, you begin to choke!!!"""

end_story4="""After an hour a masked man comes in, seeing that you have not touched the food, he took it and poured it on 
you. Your vision has been compromised!!!"""

end_story5="""You kick the woman in her stomach, she falls but before you can escape, you bump into a huge man. What a life!!!"""

end_story6="""You open the door and run down the only path. While running, you look back and hear huge footsteps coming 
after you. You hit a tree and fell!!!"""

end_story7="""You decide to pretend to be asleep. You hear a man's voice, just then you feel him lift you up, you 
immediately start to hit his back and he dropped you roughly!!!"""

end_story8="""You decide to stay awake. A man walks in and unties you, just as he is about to lift you up, you punch him 
in the face. Immediately he attacks you back!!!"""

end_story9="""You walk towards the dog slowly and when you bend down, the dog charges at you!!!"""

end_story10="""You start to climb the ladder but halfway through it, you fall down and dislocate your shoulder!!!"""

end_story11="""You decide to push him but he overshadows you and throws you on his shoulder!!!"""

end_story12="""You decide to slap him and immediately you did, he twists your wrist!!! """

end_story13="""You bite the young man so hard and he gets angry and attacks you back!!!"""

end_story14="""You try to stop him from putting the tape on your mouth but you end up tipping your chair over and hitting 
your head on the floor!!!"""

end_story15="""You decide to bang on the door but before you get to the door you slip and fall because of the puddle of 
water!!!"""

end_story16="""You decide to shout for help and after several tries an old man with a gun comes in looking very angry!!!"""

answer = input(story1)
print()
print()
while answer != "last stop" and answer != "now" :
    print("Invalid Selection")
    answer = input(story1)
    print()
    print()
if answer == ("last stop"):
    answer = input(story2)
    print()
    print()
    while answer != "meet" and answer != "find" :
        print("Invalid Selection")
        answer = input(story2)
        print()
        print()
    if answer == ("meet"):
        answer = input(story3)
        print()
        print()
        while answer != "bus station" and answer != "home" :
            print("Invalid Selection")
            answer = input(story3)
            print()
            print()
        if answer == ("bus station"):
            answer = input(story4)
            print()
            print()
            if answer == ("attack the man"):
                print(end_story1)
                print("Sorry",username, "you lost!!!")
                print()
                print()
            elif answer == ("wait"):
                print(end_story2)
                print("Sorry",username, "you lost!!!")
                print()
                print()

        elif answer == ("home"):
            answer = input(story5)

            if answer == ("eat"):
                print(end_story3)
                print("Sorry",username, "you lost!!!")
                print()
                print()
            elif answer == ("starve"):
                print(end_story4)
                print("Sorry",username, "you lost!!!")
                print()
                print()

    elif answer == ("find"):
        answer = input(story6)
        print()
        print()

        while answer != "occupied" and answer != "unoccupied" :
            print("Invalid Selection")
            answer = input(story6)
            print()
            print()
        if answer == ("occupied"):
            answer = input(story7)

            if answer == ("kick"):
                print(end_story5)
                print("Sorry",username, "you lost!!!")
                print()
                print()
            elif answer == ("run away"):
                print(end_story6)
                print("Sorry",username, "you lost!!!")
                print()
                print()

        elif answer == "unoccupied":
            answer = input(story8)


            if answer == ("sleep"):
                print(end_story7)
                print("Sorry",username, "you lost!!!")
                print()
                print()
            elif answer == ("wake"):
                print(end_story8)
                print("Sorry",username, "you lost!!!")
                print()
                print()

elif answer == ("now"):
    answer = input(story9)
    print()
    print()

    while answer != "left" and answer != "right" :
        print("Invalid Selection")
        answer = input(story9)
        print()
        print()

    if answer == ("left"):
        answer = input(story10)
        print()
        print()

        while answer != "collar" and answer != "run" :
            print("Invalid Selection")
            answer = input(story10)
            print()
            print()
        if answer == ("collar"):
            answer = input(story11)
            print()
            print()

            if answer == ("pet"):
                print(end_story9)
                print("Sorry",username, "you lost!!!")
                print()
                print()
            elif answer == ("climb"):
                print(end_story10)
                print("Sorry",username, "you lost!!!")
                print()
                print()

        elif answer == ("run"):
            answer = input(story12)

            if answer == ("push"):
                print(end_story11)
                print("Sorry",username, "you lost!!!")
                print()

            elif answer == ("slap"):
                print(end_story12)
                print("Sorry",username, "you lost!!!")
                print()
                print()

    elif answer == ("right"):
        answer = input(story13)
        print()
        print()
        while answer != "directions" and answer != "water" :
            print("Invalid Selection")
            answer = input(story13)
            print()
            print()
        if answer == ("directions"):
            answer = input(story14)
            print()
            print()

            if answer == ("bite"):
                print(end_story13)
                print("Sorry",username, "you lost!!!")
                print()
                print()
            elif answer == ("struggle"):
                print(end_story14)
                print("Sorry",username, "you lost!!!""")
                print()
                print()

        elif answer == ("water"):
            answer = input(story15)


            if answer == ("bang"):
                print(end_story15)
                print("Sorry",username, "you lost!!!")
                print()
                print()
            elif answer == ("shout"):
                print(end_story16)
                print("Sorry",username, "you lost!!!")
                print()
                print()