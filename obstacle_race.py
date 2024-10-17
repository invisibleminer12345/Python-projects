import click
import random
import os
import threading
from time import sleep
from termcolor import colored
board =[[" ", " ", " ", " ", "O", "B", "S", "T", "A", "C", "L", "E", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", "R", "A", "C", "E", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", "Y", "O", "U", "-", ">", colored("0","red"), " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "],]
xMax = 15
yMax = 9
levelTicks =[0, 0, 0, 1, 1, 2, 1, 0, 0, 1, 3, 3, 1, 3, 1, 0] #how many spaces are between obstacles
obstacles = [2, 3, 4, 13, 14, 15, 13, 4, 5, 14, 15, 14, 15, 10, 14, 16] #How many obstacles are in one line
refreshRate=[0.8, 0.6, 0.4, 0.45, 0.6, 0.5, 0.4, 0.35, 0.4, 0.3, 0.5, 0.4, 0.4, 0.3, 0.4, 1] #Tempo
extra = [False, False, False, False,False,False,False,False,False,False, True, True, False, True, False] #Used for future levels
def scanForMoves():
    # Movement to move user controlled unit, will not move if there is obstacle to designated location
    def getCurrentPos():
        # Find user position, Used to fix bug where there were multiple user controlled units
        for i in range(yMax + 1):
            for a in range(xMax + 1):
                if board[i][a] == colored("0","red"): 
                    return a,i
    x, y = getCurrentPos()
    while scanForPlayer():     
        m = click.getchar()
        x, y = getCurrentPos()    
        if board[y][x] != colored("0","red"):
                y += 1 # To counter the constant movement down
        
        # Change the input values to the values of your computer's arrow key values
        if m == "\xe0H" or m == "w": #UP
            if y > 0:
                if board[y-1][x] != "X":
                    board[y-1][x] = colored("0","red")
                    board[y][x] = " "
                    y -= 1
        elif m == "\xe0P" or m == "s": #DOWN
            if y < yMax:
                if board[y+1][x] != "X":
                    board[y+1][x] = colored("0","red")
                    board[y][x] = " "
                    y += 1
        elif m == "\xe0K" or m == "a":#LEFT
            if x > 0:
                if board[y][x-1] != "X":
                    board[y][x-1] = colored("0","red")
                    board[y][x] = " "
                    x -= 1
        elif m == "\xe0M" or m == "d":#RIGHT
            if x < xMax:
                if board[y][x+1] != "X":
                    board[y][x+1] = colored("0","red")
                    board[y][x] = " "
                    x += 1
def generateObstacles(max, obs, tick, em):
    line = []
    empty = em
    if tick == levelTicks[level]: # inserts obstacles in increments
        empty = []
        for i in range(max+1):
            ran = random.randint(1, max+1)
            if ran <= obs:
                line.append("X")
                obs -= 1
                max -= 1
            else:
                line.append(" ")
                empty.append(-1-max)
                max -= 1
        tick = 0
    else:
        for i in range(max+1):
            line.append(" ")
        if extra[level]: # Adds another three obstacles above to make it more difficult
            if tick == 1 and levelUpTicks != 1:
                for i in empty:
                    if i == -16:
                        line[0] = "X"
                        line[1] = "X"
                    elif i == -1:
                        line[14] = "X"
                        line[15] = "X"
                    else:
                        line[i - 1] = "X"
                        line[i] = "X"
                        line[i + 1] = "X"
                possible = False
                for i in line:
                    if line == " ":
                        possible = True
                if not possible: # Ensure there is no dead end
                    line[random.randint(0,15)] = " "
        tick += 1
    return line, tick, empty
def scanForPlayer():
    # Checks to see if the game is over or not
    for i in range(yMax + 1):
        for a in range(xMax + 1):
            if board[i][a] == colored("0","red"):
                return True
    return False
def refreshTerminal():
    # Prints out board
    while True:
        bPrint = "" # Assign to variable then print variable to prevent bug
        bPrint = colored("-------------------------------------------------------------------\n", "green")
        for i in range(yMax + 1):
            bPrint = bPrint + colored(' | ', "green")
            for a in range(xMax + 1):
                bPrint = bPrint + board[i][a] + colored(' | ', "green")
            bPrint = bPrint + colored("\n-------------------------------------------------------------------\n", "green")
        print("\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A\033[A",end="")
        # Move back lines 
        print(bPrint)
        sleep(0.05)
        # Delay to prevent lag
def main():
    # Main program
    global level
    level = 0
    global levelUpTicks
    levelUpTicks = 0
    ticks = 0
    empty = []
    beatGame = False
    while scanForPlayer():
        for i in range(yMax):
            # Move downs every line
            board[yMax - i] = board[yMax - i - 1]
            
        line, ticks, empty = generateObstacles(xMax, obstacles[level], ticks, empty)
        board[0] = line
        if levelUpTicks >= 20:
            # Level Up
            if level == 9:
                # Triggers at level 10, landmark for final 5 levels
                sleep(2)
                board[0] = [" ", " ", " ", " ", "F", "E", "W", " ", "M", "O", "R", "E", " ", " ", " ", " "]
                board[1] = [" ", " ", " ", " ", " ", "R", "O", "U", "N", "D", "S", " ", " ", " ", " ", " "]
                board[2] = [" ", " ", " ", " ", " ", "Y", "O", "U", "-", ">", colored("0","red"), " ", " ", " ", " ", " "]
                board[3] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                board[4] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                board[5] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                board[6] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                board[7] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                board[8] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
                board[9] = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            levelUpTicks = 0
            level += 1
            ticks = 0
            
        else:
            # Keeps count of how many more ticks until next level
            levelUpTicks += 1
        sleep(refreshRate[level])
    if level == 15:
        print(colored("CONGRAGULATIONS! YOU BEAT SPACE RACE!", "blue"))
    else:
        print("You survived level:" + str(level+1))
    exit()
def start():
    # Create threads
    os.system("cls")
    tMove = threading.Thread(target=scanForMoves)
    tGame = threading.Thread(target=main)
    tPrint = threading.Thread(target=refreshTerminal)
    tPrint.start()
    tGame.start()
    tMove.start()
    tPrint.join()
    tMove.join()
    tGame.join()
start()
