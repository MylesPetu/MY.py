# from weapons import Weapons
# round = [pretext + question, live, die]
# w = Weapons()
from dice import Dice

import random
import os
d = Dice()
user_name = input("Enter your name: ").capitalize()
# To clear the terminal after the username has been entered
os.system("cls")
user_weapon = ""
# The Introduction to the game
intro = [
    f"As the clock strikes midnight at St. Ignatius Boarding School in Nigeria, a sense of dread fills the air. The students are fast asleep, unaware of the lurking danger that awaits them. Among them is {user_name}, a brave Nigerian student who is at the center of a terrifying ordeal."
]
round1 = [
    f"As the footsteps draw nearer, panic sets in. Will you hide under the bed, hoping to evade the danger? \n"
    f"Or will you make a dash for the dormitory's entrance, risking a confrontation with the unknown?\n"
    "Hide Under the Bed (press 1) or Run to the Dormitory's Entrance? (press 2)\n",

    f"Run to the Dormitory's Entrance: {user_name} dashes towards the dormitory's entrance, \n"
    f"narrowly avoiding Madam Koi Koi's grasp. You escape into the hallway, heart pounding with fear.\n",

    f"You quickly dive under the bed, hoping to evade the approaching danger. \n"
    f"However, your attempts are in vain as Madam Koi Koi snatches you from beneath, sealing your fate.\n"
]

round2 = [
    f"With each heartbeat echoing in your ears, you must make a split-second decision. \n"
    f"Will you seek solace in the sacred halls of the chapel, where divine protection may offer sanctuary? \n"
    f"Or will you seek refuge among the rows of books in the library, hoping to evade the danger lurking in "
    f"the shadows?\n"
    "Seek Sanctuary in the Chapel (Press 1) or Take Refuge in the Library (Press 2)\n",

    f"Seek Sanctuary in the Chapel: {user_name} races to the chapel, seeking refuge in its sacred halls. \n"
    f"As you enter, a sense of peace washes over you, weakening Madam Koi Koi's powers. \n"
    f"You discover a hidden passage leading deeper into the school.\n",

    f"Take Refuge in the Library: {user_name} hides in the library, hoping to find safety among the rows of books. \n"
    f"However, you fall prey to Madam Koi Koi's dark magic, meeting a tragic end.\n"
]

round3 = [
    f"With danger lurking around every corner, you must decide your next move wisely. \n"
    f"Will you venture into the abandoned wing, hoping to uncover its secrets? \n"
    f"Or will you make a desperate bid for freedom, hoping to escape the clutches of the unseen menace?\n"
    "Enter the Abandoned Wing (Press 1) or Make a Break for the Main Gate (Press 2)?\n",

    f"Enter the Abandoned Wing: With determination fueling your every step, {user_name} sprints \n"
    f"through the abandoned wing. \n"
    f"Guided by a dim glitter at the end of the hallway, you discover ancient secrets hidden within the school.\n",

    f"Make a Break for the Main Gate: Your curiosity leads you to the main gate, \n"
    f"but you realize too late that it's a trap set by Madam Koi Koi. You fall victim to her dark powers.\n"
]

round4 = [
    f"As you face new challenges, you must decide how to confront the looming danger. \n"
    f"Will you rely on the protective charm passed down by your grandmother? \n"
    f"Or will you trust in your instincts to guide you through the darkness?\n"
    "Use a Protective Charm (Press 1) or Trust in Instincts Alone (Press 2)?\n",

    f"Use a Protective Charm: Feeling around in your pocket, you remember the \n"
    f"talisman passed down by your grandmother.\n"
    f"You invoke its protective powers, forming a barrier against Madam Koi Koi's malevolent magic.\n",

    f"Trust in Instincts Alone: You rely on your instincts to guide you through the night, \n"
    f"but soon realize why she is the most feared witch in the land.\n"
]

round5 = [
    f"As the night wears on, you face a crucial decision. \n"
    f"Will you seek refuge in a teacher's quarters, hoping for protection and guidance? \n"
    f"Or will you confront Madam Koi Koi head-on, armed only with your courage and determination?\n"
    "Seek Help from a Teacher (Press 2) or Face the Witch Alone (Press 1)?\n",

    f"Face the Witch Alone: Braving the darkness, you confront Madam Koi Koi head-on, armed only "
    f"with your courage and determination.\n",

    f"Seek Help from a Teacher: You seek refuge in a teacher's quarters, hoping for protection and guidance. \n"
    f"However, the teacher is revealed to be an ally of Madam Koi Koi, leading to your demise.\n"
]

round6 = [
    f"As you face Madam Koi Koi once more, you must choose your strategy carefully. \n"
    f"Will you use a mirror to deflect the witch's spells? \n"
    f"Or will you flee blindly through the corridors, hoping to outrun her grasp?\n"
    "Use a Mirror to Reflect the Witch's Spells (Press 1) or Run Blindly Through the Corridors (Press 2)?\n",

    f"Use a Mirror to Reflect the Witch's Spells: Thinking quickly, you grab a mirror and use it \n"
    f"to deflect Madam Koi Koi's spells back at her.\n",

    f"Run Blindly Through the Corridors: Panic-stricken, you flee blindly through the dark corridors, \n"
    f"hoping to outrun the witch's grasp. How can you outrun an agent of the night?\n"
]

round7 = [
    f"With the night growing darker, you face a pivotal moment. \n"
    f"Will you seek sanctuary in the headmaster's office, hoping for safety amidst protective wards? \n"
    f"Or will you rally your friends to your side, trusting in the power of friendship to overcome the darkness?\n"
    "Find Sanctuary in the Headmaster's Office (Press 2) or Trust in the Power of Friendship (Press 1)\n",

    f"Trust in the Power of Friendship: Rallying your friends to your side, you form a protective circle of \n"
    f"unity and strength. \n"
    f"Together, they stand against the witch's dark forces, emerging victorious as dawn breaks on the horizon.\n",

    f"Is it that you didn't learn your lesson?!\n"
    f"Find Sanctuary in the Headmaster's Office: Seeking refuge in the headmaster's office, you hope to \n"
    f"find safety amidst protective wards. However, you discover that the headmaster is under the witch's control, \n"
    f"leading to your demise.\n"
]

round8 = [
    f"As dawn approaches, you face your ultimate challenge. \n"
    f"Will you summon all your courage to face Madam Koi Koi head-on? \n"
    f"Or will you succumb to fear and beg for mercy?\n"
    "Face Madam Koi Koi with Courage (Press 1) or Beg for Mercy (Press 2)?\n",

    f"Face Madam Koi Koi with Courage: Confronting Madam Koi Koi with unwavering courage, you refuse \n"
    f"to back down in the face of danger. Through sheer determination and bravery... \n",

    f"Kilode???\n Are you sure you're alright?!\n"
    f"Beg for Mercy: Succumbing to fear, Omo! you beg for mercy at the feet of Madam Koi Koi, hoping to spare \n"
    f"your life \n you beg tire but she no gree.\n"
    f"The witch shows no mercy, and you meet a tragic end at her hands.\n"
]

fight = ["In the heated battle between you and Madam Koi Koi, You guys have landed each other heavy blows \n"
         "She has a broken rib and a fractured nose with a missing eyeball\n"
         "you have a severed hanging left hand  and for some "
         "reason you don't have liver again, physically and literally\n you guys tumbled back into the chapel"]


# Since we can't pass userWeapon directly into this fil
def fighting(userWeapon):
    choices = ["a", "b", "c"]
    input("Press enter to roll a dice and attack...")
    x = random.choice(choices)
    points = d.roll()
    if x == "a":
        print(
            f"As per sharp guy you dodge slap from left and give her right\n hook with the {userWeapon} you picked up "
            f"she stagger but she no fall")
        return 2

    elif x == "b":
        print(
            f"With the {userWeapon} in your only functional hand you throw it with \nall your might and she wails out "
            f"in excruciating pain")
        return 4

    elif x == "c":
        print(
            f"You throw the {userWeapon} as a distraction and as she rushes you, you remember the move from Karate kid\n "
            f"You do a one leg left spin and as momentum fades you throw an unbelievable back flip")
        return 6



def beating():
    choices = ["a", "b", "c"]
    input("Madam Koi Koi rolls a dice and attacks...\nPress enter")
    x = random.choice(choices)
    y = random.randint(1, 6)
    points = y
    if x == "a":
        print("You blink and she wiped you dirty slap! you can't hear again", )
        return 2

    elif x == "b":
        print("You swerve thinking you're fast but she's faster "
              "she gave you knock with her Koi Koi shoe, now everything you see is double (Shege inclusive.)")
        return 4

    elif x == "c":
        print("You try to dodge but she dazed you with one maddddd uppercut, your mouth tastes like nothing but blood")
        return 6

