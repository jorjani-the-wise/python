import random
import pygame
import math

ref = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
turn = 1
winner = False
play = True
ppl_C = []
p1C = []
aiC = []


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


def is_winner(pnc):
    win_cond = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [3, 6, 9], [1, 4, 7], [2, 5, 8]]
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


def ai_player_placeholder(aic, p1c):
    ppl_c = aic + p1c + [20]
    num = random.randint(1, 10)
    for i in ppl_c:
        if num == i:
            continue
        else:
            break
    return num


def ai_player():
    win_cond = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 5, 9], [3, 5, 7], [3, 6, 9], [1, 4, 7], [2, 5, 8]]
    # random.shuffle(win_cond)

    def ai_assist_remaining(p1c, aic):
        remaining = [[], [], [], [], [], [], [], []]
        for i in range(0, len(win_cond)):
            counter = 0
            for j in range(0, len(win_cond[i])):
                if win_cond[i][j] not in p1c and win_cond[i][j] not in aic:
                    remaining[i].append(win_cond[i][j])
        return remaining

    def ai_assist_def(p1c):
        p1c_chance = [[], [], [], [], [], [], [], []]
        for i in range(0, len(win_cond)):
            counter = 0
            for j in range(0, len(win_cond[i])):
                for num in p1c:
                    if win_cond[i][j] == num:
                        counter += 1
            p1c_chance[i] = counter
        return p1c_chance

    def num_win_rate():
        win_rate = []
        for i in range(1, 10):
            num = 0
            for j in ai_assist_def([i]):
                num += j
            win_rate.append((i, num))
        return win_rate

    def ai_assist(p1c, aic):
        ppl_c = aic + p1c + [20]
        num = random.randint(1, 10)
        for i in ppl_c:
            if num == i:
                continue
            else:
                break
        return num


def play_again():
    player_decision = "z"
    global winner, play, p1C, aiC, ppl_C, ref
    while player_decision.lower() != "y" and player_decision.lower() != "n":
        player_decision = input("Do You Want to Play Again ? Y/N : ")
        if player_decision.lower() == "y":
            # print("  PLAY Again !!!")
            # print(winner, play)
            winner = False
            play = True
            p1C, aiC, ppl_C, ref = [], [], [], ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
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
                    if len(p1C) > 2 and is_winner(p1C):
                        winner = 1
                    elif len(ppl_C) == 9:
                        winner = 0.5
                else:
                    print("the cell you chose was taken")
            else:
                print("inputted num was not in range")
        elif turn == 2:
            ai = ai_player_placeholder(aiC, p1C)
            if 1 <= ai <= 9:
                if ai not in ppl_C:
                    aiC.append(ai)
                    ppl_C.append(ai)
                    ref[ai - 1] = "═╬═"
                    turn = 1
                    printer(ref)
                    if len(aiC) > 2 and is_winner(aiC):
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
