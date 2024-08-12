import time
from inputValidator import InputValidator
from weapons import Weapons
from dice import Dice
import story
from PIL import Image
import asciiArt as art
import os

ipvr = InputValidator()

d = Dice()
w = Weapons()

weaponChoice = ""
# using the pillow library to make images ready to be shown using .open()
# and later displaying the images using .show() 
moonlight = Image.open("./Images/moonlight.jpg")
runfromkoikoi = Image.open("./Images/runfromkoikoi.jpg")
charm = Image.open("./Images/boyusecharm.jpg")
oneonone = Image.open("./Images/challengekoikoi.jpg")
betrayal = Image.open("./Images/principalkoikoi.jpg")
friends = Image.open("./Images/childrenvskoikoi.jpg")
faceoff = Image.open("./Images/bestfightscene.jpg")
boywin = Image.open("./Images/boywin.jpg")
koikoiwin = Image.open("./Images/koikoiwin.jpg")

moonlight.show()
# After read delay
afterReadDelay = 7
# After art delay
afterArtDelay = 5
# Round start delay
showRoundDelay = 3
# Print Game Intro ASCII Art then delay
print(art.gameIntro)
time.sleep(1)
# Print Game Intro
print(story.intro[0])
# Print School Front ASCII Art then delay
print(art.schoolFront1)
time.sleep(afterReadDelay)
# Print round ASCII Art then delay
print(art.round1)
time.sleep(showRoundDelay)
# Print round story then get user reply
choice1 = int(ipvr.get_input(story.round1[0]))
# Round 1
if choice1 == 2:
    # ASCII Art
    runfromkoikoi.show()
    os.system("cls")
    # Print previous round outcome then delay
    print(story.round1[1])
    time.sleep(afterReadDelay)
    # Print round ASCII Art then delay
    print(art.round2)
    time.sleep(showRoundDelay)
    # Print round story then get user reply
    choice1 = int(ipvr.get_input(story.round2[0]))
    if choice1 == 1:
        # ASCII Art
        os.system("cls")
        print(story.round2[1])
        print(art.round3)
        choice1 = int(ipvr.get_input(story.round3[0]))
        time.sleep(showRoundDelay)
        os.system("cls")


        if choice1 == 1:
            # ASCII Art
            print(story.round3[1])
            print(art.round4)
            choice1 = int(ipvr.get_input(story.round4[0]))
            time.sleep(showRoundDelay)
            os.system("cls")
            
            if choice1 == 1:
                # ASCII Art
                charm.show()
                print(story.round4[1])
                print(art.round5)
                choice1 = int(ipvr.get_input(story.round5[0]))
                time.sleep(showRoundDelay)
                os.system("cls")

                if choice1 == 1:
                    # ASCII Art
                    oneonone.show()
                    print(story.round5[1])
                    print(art.round6)
                    choice1 = int(ipvr.get_input(story.round6[0]))
                    time.sleep(showRoundDelay)
                    os.system("cls")


                    if choice1 == 1:
                        # ASCII Art
                        print(story.round6[1])
                        print(art.round7)
                        choice1 = int(ipvr.get_input(story.round7[0]))
                        time.sleep(showRoundDelay)
                        os.system("cls")

                        if choice1 == 1:
                            # ASCII Art
                            friends.show()
                            print(story.round7[1])
                            print(art.round8)
                            choice1 = int(ipvr.get_input(story.round8[0]))
                            time.sleep(showRoundDelay)
                            os.system("cls")

                            if choice1 == 1:
                                # ASCII Art
                                faceoff.show()
                                print(story.round8[1])
                                print(story.fight[0])
                                weaponChoice = w.pickWeapon()
                                # begin battle
                                a = True
                                yourPoints = 0
                                witchPoints = 0
                                for i in range(3):
                                    input("Press enter to roll a dice ")
                                    you = d.roll()
                                    print(art.die_faces[you - 1])
                                    koi = d.wroll()
                                    print(art.die_faces[koi - 1])
                                    if you > koi:
                                        yourPoints += story.fighting(weaponChoice)
                                        print(f"You have {yourPoints} points")
                                    if you < koi:
                                        witchPoints += story.beating()
                                        print(f"Mad Koi Koi has {witchPoints} points")
                                    if you == koi:
                                        yourPoints += story.fighting(weaponChoice)
                                        witchPoints += story.beating()
                                    time.sleep(10)

                                if yourPoints > witchPoints:
                                    print("Congratulations you won!")
                                    boywin.show()
                                else:
                                    print("Madam Koi Koi killed you. Sorry...\n Better luck next time")
                                    time.sleep(afterReadDelay)
                                    koikoiwin.show()
                            
                            else:
                                print(story.round8[2])
                                time.sleep(afterReadDelay)
                                koikoiwin.show()
                        else:
                            betrayal.show()
                            print(story.round7[2])
                            time.sleep(afterReadDelay)
                            koikoiwin.show()

                    else:
                        print(story.round6[2])
                        time.sleep(afterReadDelay)
                        koikoiwin.show()
                else:
                    betrayal.show()
                    print(story.round5[2])
                    time.sleep(afterReadDelay)
                    koikoiwin.show()
            else:
                print(story.round4[2])
                time.sleep(afterReadDelay)
                koikoiwin.show()
        else:
            print(story.round3[2])
            time.sleep(afterReadDelay)
            koikoiwin.show()
    else:
        print(story.round2[2])
        time.sleep(afterReadDelay)
        koikoiwin.show()
else:
    print(story.round1[2])
    time.sleep(afterReadDelay)
    koikoiwin.show()
