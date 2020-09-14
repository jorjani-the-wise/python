ref = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
turn = 1
winner = False
play = True
ppl_C = []
p1C = []
p2C = []


def printer(r):
    print("""
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
███████████████████████████████
█         █         █         █
█   {}   █   {}   █   {}   █
█         █         █         █
███████████████████████████████
█         █         █         █
█   {}   █   {}   █   {}   █
█         █         █         █
███████████████████████████████
█         █         █         █
█   {}   █   {}   █   {}   █
█         █         █         █
███████████████████████████████
 """.format(r[6], r[7], r[8], r[3], r[4], r[5], r[0], r[1], r[2]))


def iswinner(pnc):
    win_cond = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [7, 5, 3], [3, 6, 9], [1, 4, 7], [2, 5, 8]]
    counter = 0
    while not counter == 3:
        for i in range(0, len(win_cond)):
            counter = 0
            for j in range(0, len(win_cond[i])):
                for num in pnc:
                    if win_cond[i][j] == num:
                        counter += 1

                        if counter == 3:
                            return True
                    else:
                        if i == 7 and j == 2:
                            return False


def play_again():
    player_decision = "z"
    global winner, play, p1C, p2C, ppl_C, ref
    while player_decision.lower() != "y" and player_decision.lower() != "n":
        player_decision = input("Do You Want to Play Again ? Y/N : ")
        if player_decision.lower() == "y":
            # print("  PLAY Again !!!")
            # print(winner, play)
            winner = False
            play = True
            p1C, p2C, ppl_C, ref = [], [], [], ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
        elif player_decision.lower() == "n":
            play = False


while play:

    while not winner:
        if turn == 1:
            p1 = int(input("player One please enter a cell num between 1 and 9 :\n"))
            if 1 <= p1 <= 9:
                if p1 not in ppl_C:
                    p1C.append(p1)
                    ppl_C.append(p1)
                    ref[p1 - 1] = "█═█"
                    turn = 2
                    printer(ref)
                    if len(p1C) > 2 and iswinner(p1C):
                        winner = 1
                    elif len(ppl_C) == 9:
                        winner = 0.5
                else:
                    print("the cell you chose was taken")
            else:
                print("inputted num was not in range")
        elif turn == 2:
            p2 = int(input("player Two please enter a cell num between 1 and 9 :\n"))
            if 1 <= p2 <= 9:
                if p2 not in ppl_C:
                    p2C.append(p2)
                    ppl_C.append(p2)
                    ref[p2 - 1] = "═╬═"
                    turn = 1
                    printer(ref)
                    if len(p2C) > 2 and iswinner(p2C):
                        winner = 2
                    elif len(ppl_C) == 9:
                        winner = 0.5
                    else:
                        continue
                else:
                    print("the cell you chose was taken")
            else:
                print("inputted num was not in range")

    if winner == 0.5:
        print("DRAW !!!")
        play_again()
        continue
    elif winner == 1:
        print(" PLAYER ONE WON THIS GAME")
        play_again()
        continue
    elif winner == 2:
        print(" PLAYER TWO WON THIS GAME")
        play_again()
        continue

if play is False:
    if winner == 0.5:
        print("\n"*50 + "May be Next Time . . .")
    if winner == 1:
        print("\n"*50 + "lucky you player ONE")
    if winner == 2:
        print("\n"*50 + "lucky you player TWO")
    print("         Good Luck")
