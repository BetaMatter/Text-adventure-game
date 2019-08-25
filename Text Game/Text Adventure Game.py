import random


name = ""
killed_noble = False
got_evil_sword = False
keep_noble = False
killed_fortune_teller = False
killed_inn = False
dark_cloud_knowledge = False
visited_castle = False
visited_fortune_teller = False
visited_forest_clearing = False


def askname():
    global name
    name = input("Create a name for your character: ")
    print(f"\nHello {name}\n")


def cant_do_that():
    cantdo = ["\nI don't understand \n",
              "\nI don't know what you mean \n",
              "\nI can't seem to do that now \n",
              "\nDoesn't work... \n",
              "\nNada \n",
              "\nNope \n",
              "\nCan't do that \n",
              "\nMaybe try something else \n"]
    return random.choice(cantdo)


def playgame():
    global name
    global killed_noble
    global got_evil_sword
    global keep_noble
    global killed_fortune_teller
    global killed_inn
    global dark_cloud_knowledge
    global visited_castle
    global visited_fortune_teller
    global visited_forest_clearing
    answer = input("Would you like to play? \n \n")
    if answer.casefold().strip() in ("yes", "y"):
        name = ""
        got_evil_sword = False
        killed_noble = False
        killed_fortune_teller = False
        keep_noble = False
        killed_inn = False
        dark_cloud_knowledge = False
        visited_castle = False
        visited_fortune_teller = False
        visited_forest_clearing = False
        askname()
        forest1()
    elif answer.casefold().strip() in ("no", "n"):
        input("Press enter to close game")
    else:
        print(cant_do_that())
        playgame()


def forest1():
    answer = input("You are a knight of a well renowned king.\n"
                   "Your castle has recently been overtaken by mysterious forces.\n"
                   "Castle destroyed, many people killed. You black out as you make it outside the castle walls.\n"
                   "You awaken in a forest with thick bushes on your left and a small clearing on your right.\n"
                   "Where do you start?\n \n")
    if answer.casefold().strip() in ("left", "bushes", "thick bushes", "bush", "thick bush"):
        forest_bush()
    elif answer.casefold().strip() in ("right", "clearing", "small clearing"):
        forest_clearing()
    else:
        print(cant_do_that())
        forest1()


def forest_bush():
    answer = input("\nAs you approach the bushes a creature half the size of you jumps out. \n"
                   "It has the appearance of a cat and the tail of a rat. It bares its teeth ready to attack. \n"
                   "You still have your sword and shield, and you are still suited in your armour. \n"
                   "What do you do? \n \n")
    if answer.casefold().strip() in ("fight", "attack", "strike", "kill", "attack it", "kill it"):
        forest_rat_fight()
    elif answer.casefold().strip() in ("run", "escape", "flee", "run away"):
        forest_rat_death()
    elif answer.casefold().strip() in ("help", "hug", "pet", "love", "help it", "hug it", "pet it", "love it",
                                       "help him", "hug him", "pet him", "love him"):
        forest_rat_pet()
    else:
        print(cant_do_that())
        forest_bush()


def forest_rat_pet():
    answer = input("\nYou pet the rat and it purrs back in happiness. The creature takes a liking to you \n"
                   "and decides to follow you on your adventure. \n"
                   "This is a secret. \n"
                   "You continue through the bushes and make it out the forest "
                   "and can see a castle in the distance on your left \n"
                   "and small stone post with birds circling it on your right. \n"
                   "Where would you like to go? \n \n")
    if answer.casefold().strip() in ("left", "castle", "castle in distance", "castle in the distance"):
        castle1()
    elif answer.casefold().strip() in ("right", "stone post", "small stone post", "stone", "small post", "birds",
                                       "bird", "post"):
        stone_post()
    else:
        print(cant_do_that())
        forest_rat_pet()


def forest_rat_death():
    print("\nYou are not faster than the creature and bites into your legs and scratches you. \n"
          "As you finally manage to get away you realize your wounds are too severe and you begin to bleed out. \n")
    died()


def forest_rat_fight():
    answer = input("\nYou slice through the creature with ease and it lies there lifeless. \n"
                   "You continue through the bushes and make it out the forest "
                   "and can see a castle in the distance on your left \n"
                   "and small stone post with birds circling it on your right. \n"
                   "Where would you like to go? \n \n")
    if answer.casefold().strip() in ("left", "castle", "castle in distance", "castle in the distance"):
        castle1()
    elif answer.casefold().strip() in ("right", "stone post", "stone", "small stone post", "small post", "birds",
                                       "bird", "post"):
        stone_post()
    else:
        print(cant_do_that())
        forest_rat_fight()


def stone_post():
    global got_evil_sword
    if got_evil_sword:
        stone_post_revisit()
    else:
        answer = input("\nYou come up to a stone post with a hilt sticking out the top. \n"
                       "There are dead bodies strewn about, and vultures can be seen high in the sky. \n"
                       "The sword in the stone is emitting a evil miasma. \n"
                       "Do you try to take the sword? \n \n")
        if answer.casefold().strip() in ("yes", "take", "take the sword", "grab", "grab sword", "pull", "pull sword"):
            stone_post_sword()
        elif answer.casefold().strip() in ("no", "walk away", "don't take", "dont take",
                                           "don't take sword", "dont take sword"):
            left_evil_sword()
        else:
            print(cant_do_that())
            stone_post()


def stone_post_revisit():
    answer = input("\nYou revisit the stone post and see a hole where the sword used to be. \n"
                   "There is nothing else left to do here. \n"
                   "There is a castle to the north and a travellers inn to the south. \n"
                   "Where do you go? \n \n")
    if answer.casefold().strip() in ("castle", "north", "to castle", "to north", "go north", "go to castle"):
        castle1()
    elif answer.casefold().strip() in ("inn", "south", "travellers inn", "go south", "go to travellers inn",
                                       "go to inn"):
        traveller_inn()
    else:
        print(cant_do_that())
        stone_post_revisit()


def stone_post_sword():
    global killed_fortune_teller
    global got_evil_sword
    global killed_noble
    if killed_noble or killed_fortune_teller:
        pulled_evil_sword()
    else:
        print("\nYou grab the sword and feel a shock throughout your body. \n"
              "Energy leaves you, you begin to feel tired until you collapse. \n"
              "Your body now joins the others. \n")
        died()


def left_evil_sword():
    answer = input("\nYou leave the sword and see castle to the north and a travellers inn to the south. \n"
                   "Where do you go? \n \n")
    if answer.casefold().strip() in ("castle", "north", "to castle", "to north", "go north", "go to castle"):
        castle1()
    elif answer.casefold().strip() in ("inn", "south", "travellers inn", "go south", "go to travellers inn",
                                       "go to inn"):
        traveller_inn()
    else:
        print(cant_do_that())
        left_evil_sword()


def pulled_evil_sword():
    global got_evil_sword
    got_evil_sword = True
    answer = input("\nYou pull the sword from its rocky sheath. \n"
                   "You have obtained the evil sword. \n"
                   "There is a castle to the north and a travellers inn to the south. \n"
                   "Where do you go? \n \n")
    if answer.casefold().strip() in ("castle", "north", "to castle", "to north", "go north", "go to castle"):
        castle1()
    elif answer.casefold().strip() in ("inn", "south", "travellers inn", "go south", "go to travellers inn",
                                       "go to inn"):
        traveller_inn()
    else:
        print(cant_do_that())
        pulled_evil_sword()


def castle1():
    global visited_castle
    if visited_castle:
        castle_revisit()
    else:
        answer = input("\nYou arrive at the castle and the guards let you in. \n"
                       "You assume they recognise your armour and don't question it. \n"
                       "A man runs up to you and says \n"
                       "\"You look very distressed sir. I am a fortune teller, \n"
                       "if you come with me back to my house "
                       "I will use my crystal ball and help you find what you are looking for.\" \n"
                       "Do you decide to go with this fortune teller? \n \n")
        if answer.casefold().strip() in ("yes", "follow", "go", "fortune teller", "go with", "go with fortune teller"):
            visited_castle = True
            follow_fortune_teller()
        elif answer.casefold().strip() in ("no", "don't follow", "dont follow", "do not follow"):
            visited_castle = True
            castle_courtyard()
        else:
            print(cant_do_that())
            castle1()


def castle_exit():
    global dark_cloud_knowledge
    if not dark_cloud_knowledge:
        answer = input("\nAs you head out the castle gates you can see a small stone post with birds circling south, \n"
                       "a travellers inn further past the stone post, and a forest clearing.\n"
                       "Where do you go?\n \n")
        if answer.casefold().strip() in ("south", "go south"):
            print("\nBoth the stone post and the inn are south. Which do you mean?")
            castle_exit()
        elif answer.casefold().strip() in ("stone post", "stone", "small stone post", "post", "birds", "small post"):
            stone_post()
        elif answer.casefold().strip() in ("travellers inn", "traveller inn", "inn",
                                           "go to travellers inn", "go to inn"):
            traveller_inn()
        elif answer.casefold().strip() in ("castle", "courtyard", "go back", "back", "go back inside"):
            castle_courtyard()
        elif answer.casefold().strip() in ("forest", "forest clearing", "clearing"):
            forest_clearing()
        else:
            print(cant_do_that())
            castle_exit()
    else:
        answer = input("\nAs you head out the castle gates you can see a small stone post with birds circling south, \n"
                       "a travellers inn further past the stone post and a forest clearing.\n"
                       "You can also see dark cloud over a ruined castle in the distance. \n"
                       "Where do you go?\n \n")
        if answer.casefold().strip() in ("south", "go south"):
            print("\nBoth the stone post and the inn are south. Which do you mean?")
            castle_exit()
        elif answer.casefold().strip() in ("stone post", "stone", "small stone post", "post", "birds", "small post"):
            stone_post()
        elif answer.casefold().strip() in ("travellers inn", "traveller inn", "inn",
                                           "go to travellers inn", "go to inn"):
            traveller_inn()
        elif answer.casefold().strip() in ("courtyard", "go back", "back", "go back inside"):
            castle_courtyard()
        elif answer.casefold().strip() == "castle":
            print("\nWhich castle?")
            castle_exit()
        elif answer.casefold().strip() in ("dark clouds", "dark cloud", "cloud", "ruined castle", "ruins", "ruin"):
            ruined_castle()
        elif answer.casefold().strip() in ("forest", "forest clearing", "clearing"):
            forest_clearing()
        else:
            print(cant_do_that())
            castle_exit()


def castle_revisit():
    print("\nThe guards let you back in and you make your way to the courtyard.")
    castle_courtyard()


def castle_courtyard():
    answer = input("\nYou look around the courtyard and see people walking around living their lives. \n"
                   "All you can do from here is visit the fortune teller and leave the castle. \n"
                   "What will you do? \n \n")
    if answer.casefold().strip() in ("fortune teller", "visit fortune teller", "visit the fortune teller"):
        follow_fortune_teller()
    elif answer.casefold().strip() in ("leave", "exit", "leave the castle"):
        castle_exit()
    else:
        print(cant_do_that())
        castle_courtyard()


def fortune_teller_revisit():
    global killed_fortune_teller
    if killed_fortune_teller:
        fortune_teller_bloody_revisit()
    else:
        answer = input("\n\"Welcome back traveling knight. I'm afraid I can't help you anymore than I already have,\n"
                       "unless you have money.\""
                       "What will you do? \n \n")
        if answer.casefold().strip() in ("kill", "kill him", "murder", "murder him", "attack", "attack him"):
            kill_fortune_teller()
        elif answer.casefold().strip() in ("leave", "exit"):
            castle_courtyard()
        else:
            print(cant_do_that())
            fortune_teller_revisit()


def fortune_teller_bloody_revisit():
    print("\nAs you walk back in you see the bloody remains of the fortune teller, "
          "with his body still there. \n"
          "No one has found him yet. \n"
          "You decide there is nothing left for you to do here and leave to the courtyard. \n")
    castle_courtyard()


def follow_fortune_teller():
    global dark_cloud_knowledge
    global visited_fortune_teller
    if visited_fortune_teller:
        fortune_teller_revisit()
    else:
        visited_fortune_teller = True
        dark_cloud_knowledge = True
        answer = input("\nYou follow the fortune teller to his house and he brings you in front of his crystal ball. \n"
                       "\"Inside my crystal ball I can see... your name is " + name + ". \n"
                       "You are looking for knowledge of what happened to your past life. \n"
                       "That which you seek is outside these castle walls. \n"
                       "Head out the south gates and go towards the dark clouds. \n"
                       "I'm sorry that's all I can tell you... for free.\" \n"
                       "Maybe his information will be useful to you. \n"
                       "What will you do now? \n \n")
        if answer.casefold().strip() in ("kill", "murder", "kill him", "strike", "strike him", "attack", "attack him"):
            kill_fortune_teller()
        elif answer.casefold().strip() in ("leave", "exit"):
            castle_courtyard()
        else:
            print(cant_do_that())
            follow_fortune_teller()


def kill_fortune_teller():
    global killed_fortune_teller
    killed_fortune_teller = True
    print("\nYou strike down the fortune teller, his blood streams across his walls. \n"
          "After cleaning your sword, you sheath and head out to the courtyard \n")
    castle_courtyard()


def forest_clearing():
    global visited_forest_clearing
    if not visited_forest_clearing:
        answer = input("\nYou make your way through the clearing and come across a familiar face. \n"
                       "A noble from your castle lies on the ground, just awoken he sits up and looks at you. \n"
                       "\"You! Explain what has happened and why I don't remember anything. \n"
                       "Where am I?! Where is my father?! My uncle?! Forget that, get me out of here right now.\" \n"
                       "This guy asks a lot of questions. Should you bring him with you? \n \n")
        if answer.casefold().strip() in ("kill", "kill him", "murder", "murder him", "cut",
                                         "cut him", "strike", "strike him"):
            visited_forest_clearing = True
            forest_kill_noble()
        elif answer.casefold().strip() in ("bring", "bring him with you", "bring him", "take", "take him with",
                                           "take him", "keep", "keep him"):
            visited_forest_clearing = True
            forest_keep_noble()
        elif answer.casefold().strip() in ("leave", "leave him", "walk away", "ignore him", "ignore"):
            visited_forest_clearing = True
            forest_clearing_exit()
        else:
            print(cant_do_that())
            forest_clearing()
    else:
        forest_clearing_revisit()


def forest_clearing_revisit():
    global keep_noble
    global killed_noble
    global visited_forest_clearing
    if keep_noble:
        answer = input("\nYou walk back to the peaceful clearing, sit down, clear your head and rest a moment. \n"
                       "After being woken by the noble, "
                       "you gather your things and determine there is nothing left to do here. \n"
                       "Making your way out the clearing you see a castle to the north, \n"
                       "a stone post with birds circling it, and a travellers inn to the south. \n"
                       "Where do you go? \n \n")
        if answer.casefold().strip() in ("north", "castle"):
            castle1()
        elif answer.casefold().strip() in ("stone post", "stone", "small stone post", "small post", "birds", "post"):
            stone_post()
        elif answer.casefold().strip() in ("south", "traveller inn", "travellers inn", "inn"):
            traveller_inn()
        else:
            print(cant_do_that())
            forest_clearing_revisit()
    elif killed_noble:
        answer = input("\nYou come back to see the nobles dead body. \n"
                       "There isn't much else to do here, you walk back out the forest clearing. \n"
                       "Making your way out the clearing you see a castle to the north, \n"
                       "a stone post with birds circling it and a travellers inn to the south. \n"
                       "Where do you go? \n \n")
        if answer.casefold().strip() in ("north", "castle"):
            castle1()
        elif answer.casefold().strip() in ("stone post", "stone", "small stone post", "small post", "birds", "post"):
            stone_post()
        elif answer.casefold().strip() in ("south", "traveller inn", "travellers inn", "inn"):
            traveller_inn()
        else:
            print(cant_do_that())
            forest_clearing_revisit()
    else:
        answer = input("\nEntering the forest clearing you see your noisy friend you left before. \n"
                       "\"Well then, thanks for showing up again, are you finally going to answer my questions?\""
                       "This guy with even more questions now. Should you bring him with you? \n \n")
        if answer.casefold().strip() in ("kill", "kill him", "murder", "murder him", "cut",
                                         "cut him", "strike", "strike him"):
            visited_forest_clearing = True
            forest_kill_noble()
        elif answer.casefold().strip() in ("bring", "bring him with you", "bring him", "take", "take him with",
                                           "take him"):
            visited_forest_clearing = True
            forest_keep_noble()
        elif answer.casefold().strip() in ("leave", "leave him", "walk away", "ignore him", "ignore"):
            visited_forest_clearing = True
            forest_clearing_exit()
        else:
            print(cant_do_that())
            forest_clearing_revisit()


def forest_clearing_exit():
    answer = input("\nYou walk past the noble and continue past the clearing. \n"
                   "Making your way out the clearing you see a castle to the north, \n"
                   "a stone post with birds circling it, and a travellers inn to the south. \n"
                   "Where do you go? \n \n")
    if answer.casefold().strip() in ("north", "castle"):
        castle1()
    elif answer.casefold().strip() in ("stone post", "stone", "small stone post", "small post", "birds", "post"):
        stone_post()
    elif answer.casefold().strip() in ("south", "traveller inn", "travellers inn", "inn"):
        traveller_inn()
    else:
        print(cant_do_that())
        forest_clearing_exit()


def forest_kill_noble():
    global killed_noble
    killed_noble = True
    answer = input("\nYou strike the noble down and he screams in pain. \n"
                   "The wound you inflicted are grievous and he will not survive. \n"
                   "With the body of the noble bleeding out on the ground you continue past the clearing. \n"
                   "Making your way out the clearing you see a castle to the north, \n"
                   "a stone post with birds circling it, and a travellers inn to the south. \n"
                   "Where do you go? \n \n")
    if answer.casefold().strip() in ("north", "castle"):
        castle1()
    elif answer.casefold().strip() in ("stone post", "stone", "small stone post", "small post", "birds", "post"):
        stone_post()
    elif answer.casefold().strip() in ("south", "traveller inn", "travellers inn", "inn"):
        traveller_inn()
    else:
        print(cant_do_that())
        forest_kill_noble()


def forest_keep_noble():
    global keep_noble
    keep_noble = True
    answer = input("\nYou tell the noble to shut up and he sees you grab hold of your sword and cowers. \n"
                   "He follows you as you leave the clearing. \n"
                   "Making your way out the clearing you see a castle to the north, \n"
                   "a stone post with birds circling it, and a travellers inn to the south. \n"
                   "Where do you go? \n \n")
    if answer.casefold().strip() in ("north", "castle"):
        castle1()
    elif answer.casefold().strip() in ("stone post", "stone", "small stone post", "small post", "birds", "post"):
        stone_post()
    elif answer.casefold().strip() in ("south", "traveller inn", "travellers inn", "inn"):
        traveller_inn()
    else:
        print(cant_do_that())
        forest_keep_noble()


def traveller_inn():
    global got_evil_sword
    global killed_inn
    if killed_inn:
        traveller_inn_bloody()
    else:
        if got_evil_sword:
            traveller_inn_sword()
        else:
            traveller_inn_innkeeper()


def traveller_inn_innkeeper():
    answer = input("\nThe inn is bustling. You walk up to the innkeeper and he says \n"
                   "\"How's it going friend, what can I do for ya? \n"
                   "I know a lot around these parts, wanna hear some news?\" \n \n")
    if answer.casefold().strip() in ("ask", "yes", "question", "inquiry"):
        traveller_inn_innkeeper_conv()
    elif answer.casefold().strip() in ("leave", "exit"):
        traveller_inn_exit()
    elif answer.casefold().strip() in ("kill", "murder", "kill him", "murder him", "kill them", "murder them",
                                       "strike", "attack"):
        traveller_inn_death()
    else:
        print(cant_do_that())
        traveller_inn_innkeeper()


def traveller_inn_death():
    print("\nYou strike down the innkeeper and as his body falls to the ground everyone else readies their weapons. \n"
          "Before you could even prepare to attack the rest of the inn, multiple men with swords strike you down, \n"
          "and you are hit with many magical missiles, obliterating you. \n")
    died()


def traveller_inn_innkeeper_conv():
    global dark_cloud_knowledge
    dark_cloud_knowledge = True
    answer = input("\n\"Multiple of my customers have mentioned a dark and gloomy castle to the east. \n"
                   "They say it's a destroyed and in ruins, with dark evil like clouds hanging above it. \n"
                   "The same kind of evil atmosphere that surrounds that sword in the stone. \n"
                   "But if I were you I wouldn't attempt to take that sword, the legends of it say that only those \n"
                   "who have committed murder of the innocent can take it from its stone. \n"
                   "That's pretty much all the news i've heard of late\" \n"
                   "That's a lot of new information, what should you do now? \n \n")
    if answer.casefold().strip() in ("leave", "exit"):
        traveller_inn_exit()
    elif answer.casefold().strip() in ("kill", "murder", "kill him", "murder him", "kill them", "murder them",
                                       "strike", "attack"):
        traveller_inn_death()
    else:
        print(cant_do_that())
        traveller_inn_innkeeper_conv()


def traveller_inn_sword():
    global dark_cloud_knowledge
    answer = input("\nYou enter the inn, but there is not a soul in sight. \n"
                   "As you walk up to the counter you see someone peering over. \n"
                   "\"If I were you I would leave this place. We can see that sword you have. \n"
                   "We know what you have done.\" \n"
                   "You look around the inn and see people all over the place hiding and peeking at you. \n"
                   "What should you do? \n \n")
    if answer.casefold().strip() in ("leave", "exit"):
        traveller_inn_exit()
    elif answer.casefold().strip() in ("kill", "kill him", "kill them", "attack", "attack him", "murder",
                                       "murder him", "murder them"):
        traveller_inn_evil()
    elif answer.casefold().strip() in ("demand", "ask", "question", "inquiry", "threaten"):
        dark_cloud_knowledge = True
        print("\n\"Look, why don't you just go back to that ruined castle with the dark cloud over it "
              "where you came from.\" \n")
        traveller_inn_sword()
    else:
        print(cant_do_that())
        traveller_inn_sword()


def traveller_inn_evil():
    global killed_inn
    killed_inn = True
    print("\nAs you unsheathe your sword, it produces dark magic tendrils \n"
          "that lash out at everyone, killing them. \n"
          "The innkeeper still alive behind the counter screams in horror as you walk up to him. \n"
          "\"Let me live I've done nothing! I have a family! I have kids, you can't possibly take me \n"
          "away from my kids can you?\" \n"
          "Before he completely finishes his sentence you slice right through his throat and leave him "
          "to bleed out \n"
          "You look around the inn. \n"
          "A bloody mess... \n"
          "There isn't anything else left to do here.")
    traveller_inn_exit()


def traveller_inn_bloody():
    print("You look around the inn and see the remains of everyone you've killed. \n"
          "A bloody mess... \n"
          "There isn't anything else left to do here. \n \n")
    traveller_inn_exit()


def traveller_inn_exit():
    global dark_cloud_knowledge
    if dark_cloud_knowledge:
        answer = input("\nWalking out the inn you can see a forest clearing, "
                       "a small stone post with birds circling it, \n"
                       "a castle to the north, and a ruined castle with dark clouds above it to the east. \n"
                       "Where do you go? \n \n")
        if answer.casefold().strip() == "castle":
            print("Which castle?")
            traveller_inn_exit()
        elif answer.casefold().strip() in ("north castle", "north"):
            castle1()
        elif answer.casefold().strip() in ("small stone post", "stone post", "post", "small post", "birds", "stone"):
            stone_post()
        elif answer.casefold().strip() in ("forest", "forest clearing", "clearing"):
            forest_clearing()
        elif answer.casefold().strip() in ("ruined castle", "ruin", "ruins", "dark clouds", "clouds", "dark cloud",
                                           "east", "east castle"):
            ruined_castle()
        else:
            print(cant_do_that())
            traveller_inn_exit()
    else:
        answer = input("\nWalking out the inn you can see a forest clearing, "
                       "a small stone post with birds circling it, \n"
                       "and castle to the north. \n"
                       "Where do you go? \n \n")
        if answer.casefold().strip() in ("north castle", "north", "castle"):
            castle1()
        elif answer.casefold().strip() in ("small stone post", "stone post", "post", "small post", "birds", "stone"):
            stone_post()
        elif answer.casefold().strip() in ("forest", "forest clearing", "clearing"):
            forest_clearing()
        else:
            print(cant_do_that())
            traveller_inn_exit()


def ruined_castle():
    global got_evil_sword
    global killed_noble
    global killed_fortune_teller
    global killed_inn
    global keep_noble
    if got_evil_sword and killed_inn and killed_noble and killed_fortune_teller:
        answer = input("\nYou walk up to the castle and feel an evil presence but it doesn't faze you. \n"
                       "You wallow in the evil atmosphere, you feel at home here. \n"
                       "You make your way inside the broken castle gates and into the castle itself. \n"
                       "There is a big set of stairs in front of you and a pathway with door to your right. \n"
                       "Where do you go? \n \n")
        if answer.casefold().strip() in ("forward", "front", "in front", "stairs", "big set of stairs", "big stairs",
                                         "set of stairs", "big set of stairs in front of you", "in front of you"):
            ruined_castle_lobby()
        elif answer.casefold().strip() in ("pathway", "pathway with door", "door", "right", "door to your right",
                                           "your right"):
            ruined_castle_throne_room()
        else:
            print(cant_do_that())
            ruined_castle()
    elif keep_noble:
        answer = input("\nYou walk up to the castle ruins and feel a shiver down your spine. \n"
                       "\"I don't like this place, are you sure it's really "
                       "the solution to what happened to our castle?\" \n"
                       "You almost forgot about this loud noble following you. \n"
                       "You make your way inside the broken castle gates and into the castle itself. \n"
                       "There is a big set of stairs in front of you and a pathway with door to your right. \n"
                       "Where do you go? \n \n")
        if answer.casefold().strip() in ("forward", "front", "in front", "stairs", "big set of stairs", "big stairs",
                                         "set of stairs", "big set of stairs in front of you", "in front of you"):
            ruined_castle_lobby()
        elif answer.casefold().strip() in ("pathway", "pathway with door", "door", "right", "door to your right",
                                           "your right"):
            ruined_castle_throne_room()
        else:
            print(cant_do_that())
            ruined_castle()
    else:
        answer = input("\nYou walk up to the castle ruins and feel a shiver down your spine. \n"
                       "The same evil presence that took over your castle. \n"
                       "You make your way inside the broken castle gates and into the castle itself. \n"
                       "There is a big set of stairs in front of you and a pathway with door to your right. \n"
                       "Where do you go? \n \n")
        if answer.casefold().strip() in ("forward", "front", "in front", "stairs", "big set of stairs", "big stairs",
                                         "set of stairs", "big set of stairs in front of you", "in front of you"):
            ruined_castle_lobby()
        elif answer.casefold().strip() in ("pathway", "pathway with door", "door", "right", "door to your right",
                                           "your right"):
            ruined_castle_throne_room()
        else:
            print(cant_do_that())
            ruined_castle()


def ruined_castle_lobby():
    global killed_inn
    global killed_fortune_teller
    global killed_noble
    global got_evil_sword
    global keep_noble
    if killed_noble and killed_fortune_teller and killed_inn and got_evil_sword:
        ruined_castle_lobby_genocide()
    elif keep_noble:
        ruined_castle_lobby_kept_noble()
    else:
        ruined_castle_lobby_norm()


def ruined_castle_lobby_norm():
    answer = input("\nWalking through the castle lobby you see multiple dead bodies. \n"
                   "Getting past all the dead bodies everywhere you look around the room. \n"
                   "Most corridors and doors are destroyed or blocked by rubble. \n"
                   "One corridor to the right is relatively clear. You feel the evil presence get stronger "
                   "further down the corridor. \n"
                   "Continue down? \n \n")
    if answer.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
        ruined_castle_cursed_room()
    elif answer.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                       "do not continue"):
        print("There is no where else to go now. \n")
        ruined_castle_lobby()
    else:
        print(cant_do_that())
        ruined_castle_lobby()


def ruined_castle_lobby_kept_noble():
    global keep_noble
    global killed_noble
    answer = input("\nWalking through the castle lobby you see multiple dead bodies. \n"
                   "\"Oh god my father! Not just him, more nobles from our castle. " + name + "\n"
                   "This must be my father's castle, I couldn't even recognise it...\" \n"
                   "He stops talking and the rooms fills with silence. "
                   "One of the few times he's ever stayed quiet \n"
                   "You assess the room you're in. \n"
                   "Most corridors and doors are destroyed or blocked by rubble. \n"
                   "One corridor to the right is relatively clear. You feel the evil presence get stronger "
                   "further down the corridor. \n"
                   "Continue down? \n \n")
    if answer.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
        ruined_castle_cursed_room()
    elif answer.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                       "do not continue"):
        print("There is no where else to go now. \n")
        ruined_castle_lobby()
    elif answer.casefold().strip() in ("kill", "kill him", "murder", "murder him", "attack", "attack him",
                                       "strike", "strike him"):
        keep_noble = False
        killed_noble = True
        answer2 = input("\nAs the noble is mourning his father and friends, "
                        "you walk up behind him and pierce your blade "
                        "straight through his back and chest. \n"
                        "You retract your blade from his torso and he sits there, paralyzed in pain. \n"
                        "as his body slumps over, you decide there is nothing left here to do. \n"
                        "Continue down? \n \n")
        if answer2.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
            ruined_castle_cursed_room()
        elif answer2.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                            "do not continue"):
            print("There is no where else to go now. \n")
            ruined_castle_lobby()
        else:
            print(cant_do_that())
            ruined_castle_lobby()
    else:
        print(cant_do_that())
        ruined_castle_lobby()


def ruined_castle_lobby_genocide():
    answer = input("\nWalking through the castle lobby you see multiple dead bodies. \n"
                   "Not anything you haven't seen before. \n"
                   "Most corridors and doors are destroyed or blocked by rubble. \n"
                   "One corridor to the right is relatively clear. You feel the evil presence get stronger "
                   "further down the corridor. \n"
                   "Continue down? \n \n")
    if answer.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
        ruined_castle_cursed_room()
    elif answer.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                       "do not continue"):
        print("There is no where else to go now. \n")
        ruined_castle_lobby()
    else:
        print(cant_do_that())
        ruined_castle_lobby()


def ruined_castle_throne_room():
    global killed_noble
    global killed_inn
    global killed_fortune_teller
    global keep_noble
    global got_evil_sword
    if killed_fortune_teller and killed_inn and killed_noble and got_evil_sword:
        answer = input("\nWalking through the throne room you avoid any rubble. \n"
                       "The room is almost completely destroyed, ruins of what this throne room used to be. \n"
                       "There is a staircase in the back and you can feel the evil presence stronger going up it. \n"
                       "Continue down? \n \n")
        if answer.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
            ruined_castle_cursed_room()
        elif answer.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                           "do not continue"):
            print("There is no where else to go now. \n")
            ruined_castle_throne_room()
        else:
            print(cant_do_that())
            ruined_castle_throne_room()
    elif keep_noble:
        answer = input("\nWalking through the throne room you avoid any rubble. \n"
                       "\"I would recognise this throne room in any state! \n"
                       "This is my father's, this is our castle " + name + ". \n"
                       "We have to continue on, we have to see if I can find my father.\" \n"
                       "The room is almost completely destroyed, ruins of what this throne room used to be. \n"
                       "The only way to go is up a staircase in the back. \n"
                       "Continue down? \n \n")
        if answer.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
            ruined_castle_cursed_room()
        elif answer.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                           "do not continue"):
            print("There is no where else to go now. \n")
            ruined_castle_throne_room()
        elif answer.casefold().strip() in ("kill", "kill him", "murder", "murder him", "attack", "attack him",
                                           "strike", "strike him"):
            answer2 = input("\nWhile the noble is looking around the throne room, you come up behind him \n"
                            "and stab him straight through his torso. You retract your blade from his torso \n"
                            "and he sits there paralyzed in pain. \n"
                            "His body slumps over and you decide there is nothing left to do here. \n"
                            "The only way to go is up a staircase in the back. \n"
                            "Continue down? \n \n")
            if answer2.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
                ruined_castle_cursed_room()
            elif answer2.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                                "do not continue"):
                print("There is no where else to go now. \n")
                ruined_castle_throne_room()
        else:
            print(cant_do_that())
            ruined_castle_throne_room()
    else:
        answer = input("\nWalking through the throne room you avoid any rubble. \n"
                       "The room is almost completely destroyed, ruins of what this throne room used to be. \n"
                       "The only way to go is up a staircase in the back. \n"
                       "Continue down? \n \n")
        if answer.casefold().strip() in ("yes", "continue", "continue down", "continue further down"):
            ruined_castle_cursed_room()
        elif answer.casefold().strip() in ("no", "dont", "don't", "do not", "dont continue", "don't continue",
                                           "do not continue"):
            print("There is no where else to go now. \n")
            ruined_castle_throne_room()
        else:
            print(cant_do_that())
            ruined_castle_throne_room()


def ruined_castle_cursed_room():
    global got_evil_sword
    global killed_noble
    global killed_inn
    global killed_fortune_teller
    if killed_inn and killed_fortune_teller and killed_noble and got_evil_sword:
        print("\nYou make your way into the evil room and see a man with long hair "
              "hunched over a desk facing away from you. \n"
              "You feel your sword vibrating in your hand, reacting to the evil air around you. \n"
              "He must be the one who has ruined your life. You ready your blade and begin towards him. \n"
              "\"I can feel your evil air boy, it's almost as bad as mine.\" \n"
              "As he turns around your sword sends out dark magic tendrils and pierces all four of his limbs. \n"
              "The tendrils lift him up and hold him in place. \n"
              "He screams and is unable to move. \n"
              "You chop off one arm. \n"
              "Then the next arm. \n"
              "You enjoy his screams of pain. \n"
              "After wallowing in his agony you make your final stab through his neck. \n"
              "He drops to the floor and you grab his staff which overwhelms you with its evil aura. \n"
              "Encapsulated by the evil aura you head out towards the north castle. \n \n"
              "You got the ending \"Destiny\"   1 of 5\n \n"
              "True ending.")
        endgame()
    elif killed_fortune_teller and keep_noble:
        print("\nYou make your way into the evil room and see a man with long hair "
              "hunched over a desk facing away from you.")
        if got_evil_sword:
            print("You feel your sword vibrating in your hand, reacting to the evil air around you. \n"
                  "This is your time, he must be the one who destroyed your castle. \n"
                  "The one who ruined your life. This is your time to strike. \n"
                  "But as you make you way towards him, you hear him mutter \"Your stench is weak.\" \n"
                  "He turns around suddenly and stabs you with his staff. \n"
                  "You try to strike him back but some force is hindering your ability to move. \n"
                  "He tosses you aside with ease and stabs the noble and envelops him in thorns. \n"
                  "As he retracts his staff the thorns dissipate and the noble emerges from them, looking just as evil "
                  "as the long haired man. \n"
                  "You live your final breaths as you watch the noble head out towards the north castle. \n \n"
                  "You have died. \n"
                  "You got the ending \"Atoning for your sins\"   5 of 5\n \n"
                  "Not the true ending.")
            endgame()
        else:
            print("This is your time, he must be the one who destroyed your castle. \n"
                  "The one who ruined your life. This is your time to strike. \n"
                  "But as you make you way towards him, you hear him mutter \"Your stench is weak.\" \n"
                  "He turns around suddenly and stabs you with his staff. \n"
                  "You try to strike him back but some force is hindering your ability to move. \n"
                  "He tosses you aside with ease and stabs the noble and envelops him in thorns. \n"
                  "As he retracts his staff the thorns dissipate and the noble emerges from them, looking just as evil "
                  "as the long haired man. \n"
                  "You live your final breaths as you watch the noble head out towards the north castle. \n \n"
                  "You have died. \n"
                  "You got the ending \"Atoning for your sins\"   5 of 5\n \n"
                  "Not the true ending.")
            endgame()
    elif killed_noble or killed_fortune_teller and not killed_inn:
        print("\nYou make your way into the evil room and see a man with long hair "
              "hunched over a desk facing away from you.")
        if got_evil_sword:
            print("You feel your sword vibrating in your hand, reacting to the evil air around you. \n"
                  "This is your time, he must be the one who destroyed your castle. \n"
                  "The one who ruined your life. This is your time to strike. \n"
                  "But as you make you way towards him, you hear him mutter \"Your stench is weak.\" \n"
                  "He turns around suddenly and stabs you with his staff. \n"
                  "You try to strike him back but some force is hindering your ability to move. \n"
                  "Thorns envelop your body from the staff and he says \"Your soul isn't tainted enough.'\" \n \n"
                  "You have died. \n"
                  "You got the ending \"Almost perfect\"   4 of 5")
            endgame()
        else:
            print("This is your time, he must be the one who destroyed your castle. \n"
                  "The one who ruined your life. This is your time to strike. \n"
                  "But as you make you way towards him, you hear him mutter \"Your stench is weak.\" \n"
                  "He turns around suddenly and stabs you with his staff. \n"
                  "You try to strike him back but some force is hindering your ability to move. \n"
                  "Thorns envelop your body from the staff and he says \"Your soul isn't tainted enough.'\" \n \n"
                  "You have died. \n"
                  "You got the ending \"Almost perfect\"   4 of 5")
            endgame()
    elif keep_noble:
        print("\nYou make your way into the evil room and see a man with long hair "
              "hunched over a desk facing away from you. \n"
              "This is your time, he must be the one who destroyed your castle. \n"
              "The one who ruined your life. This is your time to strike. \n"
              "He turns around, noticing both of you. \n"
              "You attempt to strike the man but he stabs you with his staff before you could do anything. \n"
              "He tosses you aside with ease and stabs the noble and envelops him in thorns. \n"
              "As he retracts his staff the thorns dissipate and the noble emerges from them, looking just as evil "
              "as the long haired man. \n"
              "You live your final breaths as you watch the noble head out towards the north castle. \n \n"
              "You have died. \n"
              "You got the ending \"Too kind for your own good\"   3 of 5\n \n"
              "Not the true ending.")
        endgame()
    else:
        print("\nYou make your way into the evil room and see a man with long hair "
              "hunched over a desk facing away from you. \n"
              "This is your time, he must be the one who destroyed your castle. \n"
              "The one who ruined your life. This is your time to strike. \n"
              "But as you make you way towards him, you hear him mutter \"You have no stench on you.\" \n"
              "He turns around suddenly and stabs you with his staff. \n"
              "You attempt to move and swing your sword at him, but some force is preventing you from moving. \n"
              "Thorns envelop your body from the staff and he says \"Begone with your 'pure soul.'\" \n \n"
              "You have died. \n"
              "You got the ending \"Innocent child\"   2 of 5\n \n"
              "Not the true ending.")
        endgame()


def endgame():
    input("Thank you for playing. \n"
          "Press enter to close the game.")


def died():
    replay = input("In your final thoughts you think about how you could have handled that situation better. \n"
                   "You have died, retry? \n \n")
    if replay.casefold().strip() in ("yes", "y", "confirm"):
        playgame()
    elif replay.casefold().strip() in ("no", "n"):
        input("\nThank you for playing. Press enter to close game.")
    else:
        print(cant_do_that())
        died()


playgame()
