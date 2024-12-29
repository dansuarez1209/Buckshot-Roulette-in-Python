import random
import time
items = ['magnifying_glass', 'handcuffs', 'beer', 'cigarettes', 'saw']
shot = ['blank', 'live']
player_lives = ["life", "life"]
dealer_lives = ["life", "life"]
print("Buckshot Roulette in Python, v1.0.0")
name = input("Please sign the waiver. ")
print("Round 1")
s1 = random.choice(shot)
s2 = random.choice(shot)
s3 = random.choice(shot)
s4 = random.choice(shot)
s5 = random.choice(shot)
s6 = random.choice(shot)
r1 = random.choice(items)
r2 = random.choice(items)
r3 = random.choice(items)
r4 = random.choice(items)
ro1 = random.choice(items)
ro2 = random.choice(items)
ro3 = random.choice(items)
ro4 = random.choice(items)
player_items = [r1, r2, r3, r4]
dealer_items = [ro1, ro2, ro3, ro4]
current_shot = "s1"
current_shot_state = s1
handcuffsv = "0"
turn = "player"
turn_number = "1"
cut = False
print("Dealer items: ", ro1, ro2, ro3, ro4)
print(name, " items: ", r1, r2, r3, r4)
def magnifying_glass():
    if current_shot == "s1":
        print("The shot is: ", s1)
        player_items.remove("magnifying_glass")
        time.sleep(2)
    if current_shot == "s2":
        print("The shot is: ", s2)
        player_items.remove("magnifying_glass")
        time.sleep(2)
    if current_shot == "s3":
        print("The shot is: ", s3)
        player_items.remove("magnifying_glass")
        time.sleep(2)
    if current_shot == "s4":
        print("The shot is: ", s4)
        player_items.remove("magnifying_glass")
        time.sleep(2)
def handcuffs():
        print("Dealer is now handcuffed")
        player_items.remove("handcuffs")
        global handcuffsv
        handcuffsv = "1"
def beer():
    if current_shot == "s1":
        print("You drink a beer")
        time.sleep(2)
        print("The shot was:", s1)
        player_items.remove("beer")
    if current_shot == "s2":
        print("You drink a beer")
        time.sleep(2)
        print("The shot was:", s2)
        player_items.remove("beer")
    if current_shot == "s3":
        print("You drink a beer")
        time.sleep(2)
        print("The shot was:", s3)
        player_items.remove("beer")
    if current_shot == "s4":
        print("You drink a beer")
        time.sleep(2)
        print("The shot was:", s4)
        player_items.remove("beer")
def cigarettes():
    if player_lives == ["life","life"]:
        print("You did not regenerate any lives.")
        player_items.remove("cigarettes")
    if player_lives == ["life"]:
        print(name + " regenerated one life")
        player_lives.append("life")
        player_items.remove("cigarettes")
def saw():
    global cut
    print("You cut the revolver")
    cut = True
    player_items.remove("saw")
def revolver():
    global cut
    global turn
    global op
    global opr
    global handcuffsv
    global player_lives
    global dealer_lives
    global current_shot
    opr = input("Select an aim (your name) or dealer: ")
    if current_shot == "s1":
        if opr == name:
            if s1 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                turn = "playerr"
            if s1 == "live" and cut == False:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s1 == "live" and cut == True:
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
                op = ""
                opr = ""
        if opr == "dealer":
            if s1 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s1 == "live" and cut == False:
                print("The shot was live")
                print("Dealer's lost a life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0" :
                    turn = "dealer"
            if s1 == "live" and cut == True:
                print("The shot was live")
                print("Dealer's lost two lives")
                dealer_lives.remove("life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
    if current_shot == "s2":
        if opr == name:
            if s2 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                turn = "playerr"
            if s2 == "live" and cut == False:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s2 == "live" and cut == True:
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
                op = ""
                opr = ""
        if opr == "dealer":
            if s2 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s2 == "live" and cut == False:
                print("The shot was live")
                print("Dealer's lost a life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0" :
                    turn = "dealer"
            if s2 == "live" and cut == True:
                print("The shot was live")
                print("Dealer's lost two lives")
                dealer_lives.remove("life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
    if current_shot == "s3":
        if opr == name:
            if s3 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                turn = "playerr"
            if s3 == "live" and cut == False:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s3 == "live" and cut == True:
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
                op = ""
                opr = ""
        if opr == "dealer":
            if s3 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                if handcuffsv == "1" :
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s3 == "live" and cut == False:
                print("The shot was live")
                print("Dealer's lost a life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s3 == "live" and cut == True and dealer_lives == ["life", "life"]:
                print("The shot was live")
                print("Dealer's lost two lives")
                dealer_lives.remove("life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
            if s3 == "live" and cut == True and dealer_lives == ["life"]:
                print("The shot was live")
                print("Dealer's lost a life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
    if current_shot == "s4":
        if opr == name:
            if s4 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                turn = "playerr"
            if s4 == "live" and cut == False:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s4 == "live" and cut == True:
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
                op = ""
                opr = ""
        if opr == "dealer":
            if s4 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s4 == "live" and cut == False:
                print("The shot was live")
                print("Dealer's lost a life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s4 == "live" and cut == True:
                print("The shot was live")
                print("Dealer's lost two lives")
                dealer_lives.remove("life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
    if current_shot == "s5":
        if opr == name:
            if s5 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                turn = "playerr"
            if s5 == "live" and cut == False:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s5 == "live" and cut == True:
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
                op = ""
                opr = ""
        if opr == "dealer":
            if s5 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                if handcuffsv == "1" :
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s5 == "live" and cut == False:
                print("The shot was live")
                print("Dealer's lost a life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s5 == "live" and cut == True:
                print("The shot was live")
                print("Dealer's lost two lives")
                dealer_lives.remove("life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
    if current_shot == "s6":
        if opr == name:
            if s6 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                turn = "playerr"
            if s6 == "live" and cut == False:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s6 == "live" and cut == True:
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
                op = ""
                opr = ""
        if opr == "dealer":
            if s6 == "blank":
                print("The shot was blank")
                op = ""
                opr = ""
                cut = False
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s6 == "live" and cut == False:
                print("The shot was live")
                print("Dealer's lost a life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
                if handcuffsv == "1":
                    turn = "playerr"
                if handcuffsv == "0":
                    turn = "dealer"
            if s6 == "live" and cut == True:
                print("The shot was live")
                print("Dealer's lost two lives")
                dealer_lives.remove("life")
                dealer_lives.remove("life")
                op = ""
                opr = ""
def nextshot():
    global current_shot
    global current_shot_state
    global turn
    if current_shot == "s6":
        print("The revolver has run out of shells!")
        turn = "empty"
    if current_shot == "s5":
        current_shot = "s6"
        current_shot_state = s6
    if current_shot == "s4":
        current_shot = "s5"
        current_shot_state = s5
    if current_shot == "s3":
        current_shot = "s4"
        current_shot_state = s4
    if current_shot == "s2":
        current_shot = "s3"
        current_shot_state = s3
    if current_shot == "s1":
        current_shot = "s2"
        current_shot_state = s2
if turn == "player":
    op = input("Select an option: ")
    if "magnifying_glass" in player_items:
        if op == "magnifying_glass":
            magnifying_glass()
            op = input("Select an option: ")
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                current_shot = "s3"
                                current_shot_state = s3
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()                                    
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                current_shot = "s2"
                                current_shot_state = s2
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2                                    
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()    
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                current_shot = "s2"
                                current_shot_state = s2
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s2"
                    current_shot_state = s2
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()                                    
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()                                    
                    if "beer" in player_items:
                        if op == "beer":
                           beer()
                           current_shot = "s3"
                           current_shot_state = s3
                           op = input("Select an option: ")
                           if "handcuffs" in player_items:
                            if op == "handcuffs":
                                handcuffs()
                                revolver()
                                nextshot()                                
                           if "beer" in player_items:
                            if op == "beer":
                                beer()
                                current_shot = "s4"
                                current_shot_state = s4
                                revolver()
                                nextshot()
                           if "cigarettes" in player_items:
                            if op == "cigarettes":
                                cigarettes()
                                revolver()
                                nextshot()
                           if "saw" in player_items:
                            if op == "saw":
                                saw()
                                revolver()
                                nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if op == "revolver":
                revolver()
                current_shot = "s2"
                current_shot_state = s2
    if "handcuffs" in player_items:
        if op == "handcuffs":
            handcuffs()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s2"
                    current_shot_state = s2
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if op == "revolver":
                revolver()
                current_shot = "s2"
                current_shot_state = s2
                if turn == "playerr":
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        handcuffsv = "0"
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
    if "beer" in player_items:
        if op == "beer":
            beer()
            current_shot = "s2"
            current_shot_state = s2
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s3"
                    current_shot_state = s3
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s4"
                            current_shot_state = s4
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s5"
                                    current_shot_state = s5
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s4"
                        current_shot_state = s4
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if op == "revolver":
                revolver()
                current_shot = "s3"
                current_shot_state = s3
    if "cigarettes" in player_items:
        if op == "cigarettes":
            cigarettes()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
                        op = input("Select an option: ")

            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
                        op = input("Select an option: ")

            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s2"
                    current_shot_state = s2
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                         if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if op == "revolver":
                revolver()
                current_shot = "s2"
                current_shot_state = s2
    if "saw" in player_items:
        if op == "saw":
            saw()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s2"
                    current_shot_state = s2
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s3"
                                    current_shot_state = s3
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s2"
                                    current_shot_state = s2
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        current_shot = "s2"
                        current_shot_state = s2
            if op == "revolver":
                revolver()
                current_shot = "s2"
                current_shot_state = s2
    if op == "revolver":
        revolver()
        current_shot = "s2"
        current_shot_state = s2
        if turn == "playerr":
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s3"
                    current_shot_state = s3
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s4"
                            current_shot_state = s4
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        current_shot = "s4"
                        current_shot_state = s4
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s3"
                            current_shot_state = s3
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        current_shot = "s3"
                        current_shot_state = s3
            if op == "revolver":
                revolver()
                current_shot = "s3"
                current_shot_state = s3
                if turn == "player":
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s4"
                            current_shot_state = s4
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                    if op == "revolver":
                        revolver()
                        current_shot = "s4"
                        current_shot_state = s4
if turn == "dealer" and dealer_lives != [] and turn_number == "1":
    time.sleep(5)
    if dealer_lives == ["life"] and "cigarettes" in dealer_items:
        print("Dealer regenerated one life")
        dealer_lives.append("life")
        dealer_items.remove("cigarettes")
    if "magnifying_glass" in dealer_items:
        print("The shot is...")
        time.sleep(2)
        print("Dealer: Very interesting...")
        dealer_items.remove("magnifying_glass")
        if current_shot_state == "blank":
            if "beer" in dealer_items:
                print("Dealer drinks a beer")
                time.sleep(2)
                print("The shot was", current_shot_state)
                dealer_items.remove("beer")
                nextshot()
                time.sleep(5)
                if "handcuffs" in dealer_items:
                    print(name, "is now handcuffed")
                    dealer_items.remove("handcuffs")
                    time.sleep(2)
                    print("Dealer points towards you")
                    time.sleep(2)
                    if current_shot_state == "live" and player_lives != []:
                        print("The shot was live")
                        print("You've lost a life")             
                        player_lives.remove("life")
                        nextshot()
                        time.sleep(5)
                        if player_lives != []:
                           print("Dealer points towards you")
                           time.sleep(2)
                           if current_shot_state == "live":
                               print("The shot was live")
                               print("You've lost a life")
                               player_lives.remove("life")
                           if current_shot_state == "blank":
                               print("The shot was blank")
                               turn = "playerr"
                           nextshot()
                        else:
                            turn = ""
                    if current_shot_state == "blank" and player_lives != []:
                        print("The shot was blank")
                        nextshot()
                        time.sleep(5)
                        print("Dealer points towards you")
                        time.sleep(2)
                        if current_shot_state == "live" and player_lives != []:
                            print("The shot was live")
                            print("You've lost a life")
                            player_lives.remove("life")
                            turn = "playerr"
                        if current_shot_state == "blank" and player_lives != []:
                            print("The shot was blank")
                            turn = "playerr"
                        nextshot()
                else:
                    print("Dealer points towards you")
                    time.sleep(2)
                    if current_shot_state == "live" and player_lives != []:
                        print("The shot was live")
                        print("You've lost a life")             
                        player_lives.remove("life")
                    if current_shot_state == "blank" and player_lives != []:
                        print("The shot was blank")
                        turn = "playerr"
                    nextshot()
            else:
                print("Dealer points the revolver towards himself")
                time.sleep(1)
                print("The shot was blank")
                if current_shot_state == "live":
                        print("Dealer points towards you")
                        print("The shot was live")
                        print("You've lost a life")
                        player_lives.remove("life")
                        turn = "playerr"
                if current_shot_state == "blank":
                        print("Dealer points towards you")
                        time.sleep(1)
                        print("The shot was blank")
                        turn = "playerr"
                nextshot()
        else:
            if "saw" in dealer_items and player_lives == ["life", "life"]:
                print("Dealer cuts the revolver")
                time.sleep(1)
                print("Dealer points towards you")
                time.sleep(2)
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
            else:
                print("Dealer points towards you")
                time.sleep(2)
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                turn = "playerr"
                nextshot()
    else:
        if "handcuffs" in dealer_items:
            print(name, "is now handcuffed")
            dealer_items.remove("handcuffs")
            time.sleep(2)
            print("Dealer points towards you")
            time.sleep(2)
            if current_shot_state == "live":
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                nextshot()
                time.sleep(5)
                if player_lives != []:
                    print("Dealer points towards you")
                    time.sleep(2)
                    if current_shot_state == "live" and player_lives != []:
                        print("The shot was live")
                        print("You've lost a life")
                        player_lives.remove("life")
                        turn = "playerr"
                    if current_shot_state == "blank" and player_lives != []:
                        print("The shot was blank")
                        turn = "playerr"
                        nextshot()
                else:
                    turn = ""
            if current_shot_state == "blank":
                print("The shot was blank")
                nextshot()
                time.sleep(5)
                print("Dealer points towards you")
                time.sleep(2)
                if current_shot_state == "live" and player_lives != []:
                    print("The shot was live")
                    print("You've lost a life")
                    player_lives.remove("life")
                    turn = "playerr"
                if current_shot_state == "blank" and player_lives != []:
                    print("The shot was blank")
                    turn = "playerr"
                nextshot()
        elif turn != "playerr":
            print("Dealer points towards you")
            time.sleep(2)
            if current_shot_state == "live" and player_lives != []:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                turn = "playerr"
            if current_shot_state == "blank" and player_lives != []:
                print("The shot was blank")
                turn = "playerr"
            nextshot() 
if turn == "playerr" and player_lives != [] and turn != "empty":
    turn_number = "2"
    op = input("Select an option: ")
    if "magnifying_glass" in player_items:
        if op == "magnifying_glass":
            magnifying_glass()
            op = input("Select an option: ")
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()                                    
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                nextshot()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()                                 
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()    
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()                                    
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()                                    
                    if "beer" in player_items:
                        if op == "beer":
                           beer()
                           nextshot()
                           op = input("Select an option: ")
                           if "handcuffs" in player_items:
                            if op == "handcuffs":
                                handcuffs()
                                revolver()
                                nextshot()                                
                           if "beer" in player_items:
                            if op == "beer":
                                beer()
                                nextshot()
                                revolver()
                                nextshot()
                           if "cigarettes" in player_items:
                            if op == "cigarettes":
                                cigarettes()
                                revolver()
                                nextshot()
                           if "saw" in player_items:
                            if op == "saw":
                                saw()
                                revolver()
                                nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if "handcuffs" in player_items:
        if op == "handcuffs":
            handcuffs()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s2"
                    current_shot_state = s2
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
                if turn == "playerr":
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        handcuffsv = "0"
                        revolver()
                        nextshot()
    if "beer" in player_items:
        if op == "beer":
            beer()
            nextshot()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if "cigarettes" in player_items:
        if op == "cigarettes":
            cigarettes()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
                        op = input("Select an option: ")

            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
                        op = input("Select an option: ")

            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                         if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if "saw" in player_items:
        if op == "saw":
            saw()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if op == "revolver":
        revolver()
        nextshot()
        if turn == "playerr":
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
                if turn == "player":
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                    if op == "revolver":
                        revolver()
                        nextshot()
if turn == "dealer" and dealer_lives != [] and turn_number == "2" and current_shot != "empty":
    time.sleep(5)
    if dealer_lives == ["life"] and "cigarettes" in dealer_items:
        print("Dealer regenerated one life")
        dealer_lives.append("life")
        dealer_items.remove("cigarettes")
    if "magnifying_glass" in dealer_items:
        print("The shot is...")
        time.sleep(2)
        print("Dealer: Very interesting...")
        dealer_items.remove("magnifying_glass")
        if current_shot_state == "blank":
            if "beer" in dealer_items:
                print("Dealer drinks a beer")
                time.sleep(2)
                print("The shot was", current_shot_state)
                dealer_items.remove("beer")
                nextshot()
                time.sleep(5)
                if "handcuffs" in dealer_items:
                    print(name, "is now handcuffed")
                    dealer_items.remove("handcuffs")
                    time.sleep(2)
                    print("Dealer points towards you")
                    time.sleep(2)
                    if current_shot_state == "live" and player_lives != []:
                        print("The shot was live")
                        print("You've lost a life")             
                        player_lives.remove("life")
                        nextshot()
                        time.sleep(5)
                        if player_lives != []:
                           print("Dealer points towards you")
                           time.sleep(2)
                           if current_shot_state == "live":
                               print("The shot was live")
                               print("You've lost a life")
                               player_lives.remove("life")
                           if current_shot_state == "blank":
                               print("The shot was blank")
                               turn = "playerr"
                           nextshot()
                        else:
                            turn = ""
                    if current_shot_state == "blank" and player_lives != []:
                        print("The shot was blank")
                        nextshot()
                        time.sleep(5)
                        print("Dealer points towards you")
                        time.sleep(2)
                        if current_shot_state == "live" and player_lives != []:
                            print("The shot was live")
                            print("You've lost a life")
                            player_lives.remove("life")
                            turn = "playerr"
                        if current_shot_state == "blank" and player_lives != []:
                            print("The shot was blank")
                            turn = "playerr"
                        nextshot()
                    else:
                        print("Dealer points towards you")
                        time.sleep(2)
                        if current_shot_state == "live" and player_lives != []:
                           print("The shot was live")
                           print("You've lost a life")             
                           player_lives.remove("life")
                        if current_shot_state == "blank" and player_lives != []:
                           print("The shot was blank")
                           turn = "playerr"
                        nextshot()
            else:
                print("Dealer points the revolver towards himself")
                time.sleep(1)
                print("The shot was blank")
                if current_shot_state == "live":
                        print("Dealer points towards you")
                        print("The shot was live")
                        print("You've lost a life")
                        player_lives.remove("life")
                        turn = "playerr"
                if current_shot_state == "blank":
                        print("Dealer points towards you")
                        time.sleep(1)
                        print("The shot was blank")
                        turn = "playerr"
                nextshot()
        else:
            if "saw" in dealer_items and player_lives == ["life", "life"]:
                print("Dealer cuts the revolver")
                time.sleep(1)
                print("Dealer points towards you")
                time.sleep(2)
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
            else:
                print("Dealer points towards you")
                time.sleep(2)
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                turn = "playerr"
                nextshot()
    else:
        if "handcuffs" in dealer_items:
            print(name, "is now handcuffed")
            dealer_items.remove("handcuffs")
            time.sleep(2)
            print("Dealer points towards you")
            time.sleep(2)
            if current_shot_state == "live":
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                nextshot()
                time.sleep(5)
                if player_lives != []:
                   print("Dealer points towards you")
                   time.sleep(2)
                   if current_shot_state == "live" and player_lives != []:
                       print("The shot was live")
                       print("You've lost a life")
                       player_lives.remove("life")
                       turn = "playerr"
                   if current_shot_state == "blank" and player_lives != []:
                       print("The shot was blank")
                       turn = "playerr"
                       nextshot()
                else:
                    turn = ""
            if current_shot_state == "blank":
                print("The shot was blank")
                nextshot()
                time.sleep(5)
                print("Dealer points towards you")
                time.sleep(2)
                if current_shot_state == "live" and player_lives != []:
                    print("The shot was live")
                    print("You've lost a life")
                    player_lives.remove("life")
                    turn = "playerr"
                if current_shot_state == "blank" and player_lives != []:
                    print("The shot was blank")
                    turn = "playerr"
                nextshot()
        elif turn != "playerr":
            print("Dealer points towards you")
            time.sleep(2)
            if current_shot_state == "live" and player_lives != []:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                turn = "playerr"
            if current_shot_state == "blank" and player_lives != []:
                print("The shot was blank")
                turn = "playerr"
            nextshot()
if turn == "playerr" and player_lives != [] and turn != "empty":
    turn_number = "3"
    op = input("Select an option: ")
    if "magnifying_glass" in player_items:
        if op == "magnifying_glass":
            magnifying_glass()
            op = input("Select an option: ")
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()                                    
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                nextshot()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()                                 
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()    
                                    revolver()
                                    nextshot()
                            if op == "revolver":
                                revolver()
                                nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()                                    
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()                                    
                    if "beer" in player_items:
                        if op == "beer":
                           beer()
                           nextshot()
                           op = input("Select an option: ")
                           if "handcuffs" in player_items:
                            if op == "handcuffs":
                                handcuffs()
                                revolver()
                                nextshot()                                
                           if "beer" in player_items:
                            if op == "beer":
                                beer()
                                nextshot()
                                revolver()
                                nextshot()
                           if "cigarettes" in player_items:
                            if op == "cigarettes":
                                cigarettes()
                                revolver()
                                nextshot()
                           if "saw" in player_items:
                            if op == "saw":
                                saw()
                                revolver()
                                nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if "handcuffs" in player_items:
        if op == "handcuffs":
            handcuffs()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    current_shot = "s2"
                    current_shot_state = s2
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
                if turn == "playerr":
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        handcuffsv = "0"
                        revolver()
                        nextshot()
    if "beer" in player_items:
        if op == "beer":
            beer()
            nextshot()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    current_shot = "s4"
                                    current_shot_state = s4
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if "cigarettes" in player_items:
        if op == "cigarettes":
            cigarettes()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
                        op = input("Select an option: ")

            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            current_shot = "s2"
                            current_shot_state = s2
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
                        op = input("Select an option: ")

            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                         if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                            if "saw" in player_items:
                                if op == "saw":
                                    saw()
                                    revolver()
                                    nextshot()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if "saw" in player_items:
        if op == "saw":
            saw()
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                            if "magnifying_glass" in player_items:
                                if op == "magnifying_glass":
                                    magnifying_glass()
                                    revolver()
                                    nextshot()
                            if "handcuffs" in player_items:
                                if op == "handcuffs":
                                    handcuffs()
                                    revolver()
                                    nextshot()
                            if "beer" in player_items:
                                if op == "beer":
                                    beer()
                                    nextshot()
                                    revolver()
                                    nextshot()
                            if "cigarettes" in player_items:
                                if op == "cigarettes":
                                    cigarettes()
                                    revolver()
                                    nextshot()
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
    if op == "revolver":
        revolver()
        nextshot()
        if turn == "playerr":
            op = input("Select an option: ")
            if "magnifying_glass" in player_items:
                if op == "magnifying_glass":
                    magnifying_glass()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "handcuffs" in player_items:
                if op == "handcuffs":
                    handcuffs()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "beer" in player_items:
                if op == "beer":
                    beer()
                    nextshot()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "cigarettes" in player_items:
                if op == "cigarettes":
                    cigarettes()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if "saw" in player_items:
                if op == "saw":
                    saw()
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                            op = input("Select an option: ")
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                            op = input("Select an option: ")
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                            op = input("Select an option: ")
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                            op = input("Select an option: ")
                    if op == "revolver":
                        revolver()
                        nextshot()
            if op == "revolver":
                revolver()
                nextshot()
                if turn == "player":
                    op = input("Select an option: ")
                    if "magnifying_glass" in player_items:
                        if op == "magnifying_glass":
                            magnifying_glass()
                    if "handcuffs" in player_items:
                        if op == "handcuffs":
                            handcuffs()
                    if "beer" in player_items:
                        if op == "beer":
                            beer()
                            nextshot()
                    if "cigarettes" in player_items:
                        if op == "cigarettes":
                            cigarettes()
                    if "saw" in player_items:
                        if op == "saw":
                            saw()
                    if op == "revolver":
                        revolver()
                        nextshot()
if turn == "dealer" and dealer_lives != [] and turn_number == "3" and current_shot != "empty":
    time.sleep(5)
    if dealer_lives == ["life"] and "cigarettes" in dealer_items:
        print("Dealer regenerated one life")
        dealer_lives.append("life")
        dealer_items.remove("cigarettes")
    if "magnifying_glass" in dealer_items:
        print("The shot is...")
        time.sleep(2)
        print("Dealer: Very interesting...")
        dealer_items.remove("magnifying_glass")
        if current_shot_state == "blank":
            if "beer" in dealer_items:
                print("Dealer drinks a beer")
                time.sleep(2)
                print("The shot was", current_shot_state)
                dealer_items.remove("beer")
                nextshot()
                time.sleep(5)
                if "handcuffs" in dealer_items:
                    print(name, "is now handcuffed")
                    dealer_items.remove("handcuffs")
                    time.sleep(2)
                    print("Dealer points towards you")
                    time.sleep(2)
                    if current_shot_state == "live" and player_lives != []:
                        print("The shot was live")
                        print("You've lost a life")             
                        player_lives.remove("life")
                        nextshot()
                        time.sleep(5)
                        if player_lives != []:
                           print("Dealer points towards you")
                           time.sleep(2)
                           if current_shot_state == "live":
                               print("The shot was live")
                               print("You've lost a life")
                               player_lives.remove("life")
                           if current_shot_state == "blank":
                               print("The shot was blank")
                               turn = "playerr"
                           nextshot()
                        else:
                            turn = ""
                    if current_shot_state == "blank" and player_lives != []:
                        print("The shot was blank")
                        nextshot()
                        time.sleep(5)
                        print("Dealer points towards you")
                        time.sleep(2)
                        if current_shot_state == "live" and player_lives != []:
                            print("The shot was live")
                            print("You've lost a life")
                            player_lives.remove("life")
                            turn = "playerr"
                        if current_shot_state == "blank" and player_lives != []:
                            print("The shot was blank")
                            turn = "playerr"
                        nextshot()
                    else:
                        print("Dealer points towards you")
                        time.sleep(2)
                        if current_shot_state == "live" and player_lives != []:
                            print("The shot was live")
                            print("You've lost a life")             
                            player_lives.remove("life")
                        if current_shot_state == "blank" and player_lives != []:
                            print("The shot was blank")
                            turn = "playerr"
                        nextshot()
            else:
                print("Dealer points the revolver towards himself")
                time.sleep(1)
                print("The shot was blank")
                if current_shot_state == "live":
                        print("Dealer points towards you")
                        print("The shot was live")
                        print("You've lost a life")
                        player_lives.remove("life")
                        turn = "playerr"
                if current_shot_state == "blank":
                        print("Dealer points towards you")
                        time.sleep(1)
                        print("The shot was blank")
                        turn = "playerr"
                nextshot()
        else:
            if "saw" in dealer_items and player_lives == ["life", "life"]:
                print("Dealer cuts the revolver")
                time.sleep(1)
                print("Dealer points towards you")
                time.sleep(2)
                print("The shot was live")
                print("You've lost two lives")
                player_lives.remove("life")
                player_lives.remove("life")
            else:
                print("Dealer points towards you")
                time.sleep(2)
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                turn = "playerr"
                nextshot()
    else:
        if "handcuffs" in dealer_items:
            print(name, "is now handcuffed")
            dealer_items.remove("handcuffs")
            time.sleep(2)
            print("Dealer points towards you")
            time.sleep(2)
            if current_shot_state == "live":
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                nextshot()
                time.sleep(5)
                if player_lives != []:
                    print("Dealer points towards you")
                    time.sleep(2)
                    if current_shot_state == "live" and player_lives != []:
                       print("The shot was live")
                       print("You've lost a life")
                       player_lives.remove("life")
                       turn = "playerr"
                    if current_shot_state == "blank" and player_lives != []:
                       print("The shot was blank")
                       turn = "playerr"
                       nextshot()
                else:
                    turn = ""
            if current_shot_state == "blank":
                print("The shot was blank")
                nextshot()
                time.sleep(5)
                print("Dealer points towards you")
                time.sleep(2)
                if current_shot_state == "live" and player_lives != []:
                    print("The shot was live")
                    print("You've lost a life")
                    player_lives.remove("life")
                    turn = "playerr"
                if current_shot_state == "blank" and player_lives != []:
                    print("The shot was blank")
                    turn = "playerr"
                nextshot()
        elif turn != "playerr":
            print("Dealer points towards you")
            time.sleep(2)
            if current_shot_state == "live" and player_lives != []:
                print("The shot was live")
                print("You've lost a life")
                player_lives.remove("life")
                turn = "playerr"
            if current_shot_state == "blank" and player_lives != []:
                print("The shot was blank")
                turn = "playerr"
            nextshot()
if player_lives == []:
    time.sleep(2)
    print("Dealer wins")
if dealer_lives == []:
    time.sleep(2)
    print(name, "wins")
print(s1, s2, s3, s4, s5, s6)