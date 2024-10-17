# No functions included.
move_bking = 0
move_wking = 0
move_k = False
move_lr = False
move_rr = False
move_wlrook = 0
move_wrrook = 0
move_blrook = 0
move_brrook = 0
turn = 0
file = ["a","b","c","d","e","f","g","h"]
rank = ["1","2","3","4","5","6","7","8"]
square = [["a1","b1","c1","d1","e1","f1","g1","h1"],
          ["a2","b2","c2","d2","e2","f2","g2","h2"],
          ["a3","b3","c3","d3","e3","f3","g3","h3"],
          ["a4","b4","c4","d4","e4","f4","g4","h4"],
          ["a5","b5","c5","d5","e5","f5","g5","h5"],
          ["a6","b6","c6","d6","e6","f6","g6","h6"],
          ["a7","b7","c7","d7","e7","f7","g7","h7"],
          ["a8","b8","c8","d8","e8","f8","g8","h8"]]
piece = [["wr","wn","wb","wq","wk","wb","wn","wr"],
         ["wp","wp","wp","wp","wp","wp","wp","wp"],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["  ","  ","  ","  ","  ","  ","  ","  "],
         ["bp","bp","bp","bp","bp","bp","bp","bp"],
         ["br","bn","bb","bq","bk","bb","bn","br"]]
king = True
startsquare_rank = 0
startsquare_file = 0
endsquare_rank = 0
endsquare_file = 0
temporary_holder = ""
temporary_holder2 = True
secondletter = ''
count = 0
while king == True:
    if turn == 0:
        input("it is now white's turn to play!")
        for i in range(8):
            print(" -----------------------------------------")
            print(rank[7-i]+"| ", end='')
            for a in range(8):
                print(piece[7-i][a] + " | ", end = '')
            print("\n", end = '')
        print("__________________________________________")
        print("   ",end='')
        for i in range(8):
            print(file[i]+"    ", end='')
        input("")
        while temporary_holder2 == True:
            temporary_holder = input("\nSelect a piece: ")
            for i in range(8):
                for a in range(8):
                    if square[i][a] == temporary_holder:
                        secondletter = piece[i][a][1]
                        if piece[i][a][0] == 'w':
                            if piece[i][a][1] == 'k':
                                move_wking = move_wking + 1
                                move_k = True
                            if square[i][a] == "a1":
                                if piece[i][a][1] == 'r':
                                    move_wlrook = move_wlrook + 1
                                    move_lr = True
                            elif square[i][a] == "h1":
                                if piece[i][a][1] == 'r':
                                    move_wrrook = move_wrrook + 1
                                    move_rr = True
                            startsquare_file = a
                            startsquare_rank = i
                            temporary_holder2 = False
                        else:
                            input("sorry, that is not a white piece. Please try again.")
        temporary_holder2 = True
        while temporary_holder2 == True:
            temporary_holder = input("now enter the square in which you would like to move to:")
            if temporary_holder == "r":
                if move_k == True:
                    move_k = False
                elif move_rr == True:
                    move_rr = False
                elif move_lr == True:
                    move_wlrook = move_wlrook - 1
                temporary_holder2 = False
                turn = turn - 1 
            for i in range(8):
                for a in range(8):
                    if square[i][a] == temporary_holder:
                        endsquare_file = a
                        endsquare_rank = i
                        if endsquare_file == startsquare_file and endsquare_rank == startsquare_rank:
                            input("Stop trying to prevent zugzwang or stop being lazy")
                        elif secondletter == 'p':
                            if piece[i][a] == "  ":
                                if startsquare_rank == 1:
                                    if endsquare_file - startsquare_file == 0 and ((endsquare_rank - 2) - startsquare_rank == 0 or (endsquare_rank - 1) - startsquare_rank == 0 ):
                                        temporary_holder2 = False
                                        piece[startsquare_rank][startsquare_file] = "  "
                                        piece[i][a] = "wp"
                                    else:
                                        input("Sorry, invalid move. Please try again.")
                                elif startsquare_rank != 1:
                                    if endsquare_file - startsquare_file == 0 and (endsquare_rank - 1) - startsquare_rank == 0:
                                        if endsquare_rank == 7:
                                            temporary_holder = input("Congrats! White has promoted a pawn. Please state the piece you want to promote to:")
                                            if temporary_holder == "b" or temporary_holder == "n" or temporary_holder == "r" or temporary_holder == "q":
                                                piece[i][a] = "w" + temporary_holder
                                                temporary_holder2 = False
                                                piece[startsquare_rank][startsquare_file] = "  "
                                            else:
                                                input("Sorry, that is not a promotable piece. Please try again.")
                                        else:
                                            temporary_holder2 = False
                                            piece[startsquare_rank][startsquare_file] = "  "
                                            piece[i][a] = "wp"  
                                    else: 
                                        input("Sorry, invalid move. Please try again. ")
                            elif piece[i][a][0] == 'b':
                                if endsquare_rank-startsquare_rank == 1 and abs(endsquare_file-startsquare_file) == 1:
                                    if endsquare_rank == 7:
                                        temporary_holder = input("Congrats! White has promoted a pawn. Please state the piece you want to promote to:")
                                        if temporary_holder == "b" or temporary_holder == "n" or temporary_holder == "r" or temporary_holder == "q":
                                            piece[i][a] = "w" + temporary_holder
                                            temporary_holder2 = False
                                            piece[startsquare_rank][startsquare_file] = "  "
                                    else:
                                        temporary_holder2 = False
                                        piece[startsquare_rank][startsquare_file] = "  "
                                        piece[i][a] = "wp"
                                else:
                                    input("Sorry, invalid move. Please try again.")
                            else:
                                input("Sorry, invalid move. Please try again.")
                        elif secondletter == 'r':
                            if endsquare_file == startsquare_file and endsquare_rank != startsquare_rank:
                                if endsquare_rank < startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                elif endsquare_rank > startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wr"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            elif endsquare_rank == startsquare_rank and endsquare_file != startsquare_file:
                                if endsquare_file < startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file + 1
                                elif endsquare_file > startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wr"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            else:
                                input("Rooks can only move in a straight line. Please try again. ")
                        elif secondletter == "b":
                            if abs(startsquare_rank - endsquare_rank) == abs(startsquare_file - endsquare_file):
                                if startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank > 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank < 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file - 1    
                                elif startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank < 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank > 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wb"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            else:
                                input("Bishops can only move diagonally. Please try again.")
                        elif secondletter == 'n':
                            if (abs(endsquare_file - startsquare_file) == 2 and abs(endsquare_rank - startsquare_rank) == 1) or (abs(endsquare_file - startsquare_file) == 1 and abs(endsquare_rank - startsquare_rank) == 2):
                                if piece[i][a][0] != 'w':
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wn"
                                elif piece[i][a][0] == 'w':
                                    input("You cannot take your own piece. Please try again. ")
                            else:
                                input("Knights can only move in a L shape. Please try again. ")
                        elif secondletter == 'q':
                            if endsquare_file == startsquare_file and endsquare_rank != startsquare_rank:
                                if endsquare_rank < startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                elif endsquare_rank > startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wq"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            elif endsquare_rank == startsquare_rank and endsquare_file != startsquare_file:
                                if endsquare_file < startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file + 1
                                elif endsquare_file > startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wq"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            elif abs(startsquare_rank - endsquare_rank) == abs(startsquare_file - endsquare_file):
                                if startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank > 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank < 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file - 1    
                                elif startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank < 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank > 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "w":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "w":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wq"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            else:
                                input("Queens can only move diagonally or in a straight line. Please try again.")
                        elif secondletter == 'k':
                            if abs(endsquare_file - startsquare_file) <= 1 and abs(endsquare_rank - startsquare_rank) <= 1:
                                if piece[i][a][0] != 'w':
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "wk"
                                elif piece[i][a][0] == 'w':
                                    input("You cannot take your own piece. Please try again.")
                            elif square[i][a] == "g1":
                                if move_wking == 1 and move_wrrook == 0:
                                    if piece[0][7] == "wr":
                                        if piece[0][6] + piece[0][5] == "    ":
                                            piece[0][4] = "  "
                                            piece[0][7] = "  "
                                            piece[0][6] = "wk"
                                            piece[0][5] = "wr"
                                            temporary_holder2 = False   
                                        else:
                                            input("There is a piece in the way. Please try again.")
                                    else:
                                        input("There is no rook on h1. Please try again.")
                                else:
                                    input("You've already moved your king or rook. Please try again.")
                            elif square[i][a] == "c1":
                                if move_wking == 1 and move_wlrook == 0:
                                    if piece[0][7] == "wr":
                                        if piece[0][1] + piece[0][2] + piece[0][3] == "      ":
                                            piece[0][4] = "  "
                                            piece[0][0] = "  "
                                            piece[0][2] = "wk"
                                            piece[0][3] = "wr"
                                            temporary_holder2 = False   
                                        else:
                                            input("There is a piece in the way. Please try again.")
                                    else:
                                        input("There is no rook on a1. Please try again.")
                                else:
                                    input("You've already moved your king or rook. Please try again.")
                            else:
                                input("A king cannot move more than one square at a time. Please try again.")
        for i in range(8):
            for a in range(8):
                if piece[i][a] == "bk":
                    count = count - 1
                elif piece[i][a] != "bk":
                    count = count + 1
        if count == 64:
            input("Black's king has been taken. White wins. Black is a skill issue.")
            king = False
        count = 0
        temporary_holder2 = True
        move_k = False
        move_rr = False
        move_lr = False
        turn = turn + 1
    elif turn == 1:
        input("it is now black's turn to play!")
        for i in range(8):
            print(" -----------------------------------------")
            print(rank[i]+"| ", end='')
            for a in range(8):
                print(piece[i][a] + " | ", end = '')
            print("\n", end = '')
        print("__________________________________________")
        print("   ",end='')
        for i in range(8):
            print(file[i]+"    ", end='')
        input("")
        while temporary_holder2 == True:
            temporary_holder = input("\nSelect a piece: ")
            for i in range(8):
                for a in range(8):
                    if square[i][a] == temporary_holder:
                        secondletter = piece[i][a][1]
                        if piece[i][a][0] == 'b':
                            if piece[i][a][1] == 'k':
                                move_bking = move_bking + 1
                                move_k = True
                            if square[i][a] == "a8":
                                if piece[i][a][1] == 'r':
                                    move_blrook = move_blrook + 1
                                    move_lr = True
                            elif square[i][a] == "h8":
                                if piece[i][a][1] == 'r':
                                    move_brrook = move_brrook + 1
                                    move_rr = True
                            startsquare_file = a
                            startsquare_rank = i
                            temporary_holder2 = False
                        else:
                            input("sorry, that is not a black piece. Please try again.")
        temporary_holder2 = True
        while temporary_holder2 == True:
            temporary_holder = input("now enter the square in which you would like to move to:")
            if temporary_holder == "r":
                if move_k == True:
                    move_k = False
                elif move_rr == True:
                    move_rr = False
                elif move_lr == True:
                    move_lr = False
                temporary_holder2 = False
                turn = turn + 1 
            for i in range(8):
                for a in range(8):
                    if square[i][a] == temporary_holder:
                        endsquare_file = a
                        endsquare_rank = i
                        if endsquare_file == startsquare_file and endsquare_rank == startsquare_rank:
                            input("Stop trying to prevent zugzwang or stop being lazy")
                        elif secondletter == 'p':
                            if piece[i][a] == "  ":
                                if startsquare_rank == 6:
                                    if endsquare_file - startsquare_file == 0 and ((endsquare_rank + 2) - startsquare_rank == 0 or (endsquare_rank + 1) - startsquare_rank == 0 ):
                                        temporary_holder2 = False
                                        piece[startsquare_rank][startsquare_file] = "  "
                                        piece[i][a] = "bp"
                                    else:
                                        input("Sorry, invalid move. Please try again.")
                                elif startsquare_rank != 6:
                                    if endsquare_file - startsquare_file == 0 and (endsquare_rank + 1) - startsquare_rank == 0:
                                        if endsquare_rank == 0:
                                            temporary_holder = input("Congrats! Black has promoted a pawn. Please state the piece you want to promote to:")
                                            if temporary_holder == "b" or temporary_holder == "n" or temporary_holder == "r" or temporary_holder == "q":
                                                piece[i][a] = "b" + temporary_holder
                                                temporary_holder2 = False
                                                piece[startsquare_rank][startsquare_file] = "  "
                                            else:
                                                input("Sorry, that is not a promotable piece. Please try again.")
                                        else:
                                            temporary_holder2 = False
                                            piece[startsquare_rank][startsquare_file] = "  "
                                            piece[i][a] = "bp"  
                                    else: 
                                        input("Sorry, invalid move. Please try again. ")
                            elif piece[i][a][0] == 'w':
                                if endsquare_rank-startsquare_rank == -1 and abs(endsquare_file-startsquare_file) == 1:
                                    if endsquare_rank == 7:
                                        temporary_holder = input("Congrats! Black has promoted a pawn. Please state the piece you want to promote to:")
                                        if temporary_holder == "b" or temporary_holder == "n" or temporary_holder == "r" or temporary_holder == "q":
                                            piece[i][a] = "b" + temporary_holder
                                            temporary_holder2 = False
                                            piece[startsquare_rank][startsquare_file] = "  "
                                        else:
                                            input("Sorry, that is not a promotable piece. Please try again.")
                                    else:
                                        temporary_holder2 = False
                                        piece[startsquare_rank][startsquare_file] = "  "
                                        piece[i][a] = "bp"
                                else:
                                    input("Sorry, invalid move. Please try again.")
                            else:
                                input("Sorry, invalid move. Please try again.")
                        elif secondletter == 'r':
                            if endsquare_file == startsquare_file and endsquare_rank != startsquare_rank:
                                if endsquare_rank < startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                elif endsquare_rank > startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "br"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            elif endsquare_rank == startsquare_rank and endsquare_file != startsquare_file:
                                if endsquare_file < startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file + 1
                                elif endsquare_file > startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "br"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            else:
                                input("Rooks can only move in a straight line. Please try again. ")
                        elif secondletter == "b":
                            if abs(startsquare_rank - endsquare_rank) == abs(startsquare_file - endsquare_file):
                                if startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank > 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank < 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file - 1    
                                elif startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank < 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank > 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "bb"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            else:
                                input("Bishops can only move diagonally. Please try again.")
                        elif secondletter == 'n':
                            if (abs(endsquare_file - startsquare_file) == 2 and abs(endsquare_rank - startsquare_rank) == 1) or (abs(endsquare_file - startsquare_file) == 1 and abs(endsquare_rank - startsquare_rank) == 2):
                                if piece[i][a][0] != 'b':
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "bn"
                                elif piece[i][a][0] == 'b':
                                    input("You cannot take your own piece. Please try again. ")
                            else:
                                input("Knights can only move in a L shape. Please try again. ")
                        elif secondletter == 'q':
                            if endsquare_file == startsquare_file and endsquare_rank != startsquare_rank:
                                if endsquare_rank < startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                elif endsquare_rank > startsquare_rank:
                                    while endsquare_rank != startsquare_rank:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "bq"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            elif endsquare_rank == startsquare_rank and endsquare_file != startsquare_file:
                                if endsquare_file < startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file + 1
                                elif endsquare_file > startsquare_file:
                                    while endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            else:
                                                count = count + 100
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "bq"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            elif abs(startsquare_rank - endsquare_rank) == abs(startsquare_file - endsquare_file):
                                if startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank > 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank < 0:
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file - 1    
                                elif startsquare_file - endsquare_file > 0 and startsquare_rank - endsquare_rank < 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank - 1
                                        endsquare_file = endsquare_file + 1
                                elif startsquare_file - endsquare_file < 0 and startsquare_rank - endsquare_rank > 0:     
                                    while endsquare_rank != startsquare_rank and endsquare_file != startsquare_file:
                                        if piece[endsquare_rank][endsquare_file] != "  ":
                                            if piece[endsquare_rank][endsquare_file][0] != "b":
                                                count = count + 1
                                            elif piece[endsquare_rank][endsquare_file][0] == "b":
                                                count = count + 100
                                        endsquare_rank = endsquare_rank + 1
                                        endsquare_file = endsquare_file - 1
                                if count <= 1:
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "bq"
                                elif count >= 2 and count != 100:
                                    input("You are passing over a piece. Please try again.")
                                elif count == 100:
                                    input("You cannot take your own piece. Please try again.")
                                count = 0
                            else:
                                input("Queens can only move diagonally or in a straight line. Please try again.")
                        elif secondletter == 'k':
                            if abs(endsquare_file - startsquare_file) <= 1 and abs(endsquare_rank - startsquare_rank) <= 1:
                                if piece[i][a][0] != 'b':
                                    temporary_holder2 = False
                                    piece[startsquare_rank][startsquare_file] = "  "
                                    piece[i][a] = "bk"
                                elif piece[i][a][0] == 'b':
                                    input("You cannot take your own piece. Please try again.")
                            elif square[i][a] == "g8":
                                if move_bking == 1 and move_brrook == 0:
                                    if piece[7][7] == "br":
                                        if piece[7][6] + piece[7][5] == "    ":
                                            piece[7][4] = "  "
                                            piece[7][7] = "  "
                                            piece[7][6] = "bk"
                                            piece[7][5] = "br"
                                            temporary_holder2 = False   
                                        else:
                                            input("There is a piece in the way. Please try again.")
                                    else:
                                        input("There is no rook on h8. Please try again.")
                                else:
                                    input("You've already moved your king or rook. Please try again.")
                            elif square[i][a] == "c8":
                                if move_bking == 1 and move_blrook == 0:
                                    if piece[7][7] == "br":
                                        if piece[7][1] + piece[7][2] + piece[7][3] == "      ":
                                            piece[7][4] = "  "
                                            piece[7][0] = "  "
                                            piece[7][2] = "bk"
                                            piece[7][3] = "br"
                                            temporary_holder2 = False   
                                        else:
                                            input("There is a piece in the way. Please try again.")
                                    else:
                                        input("There is no rook on a8. Please try again.")
                                else:
                                    input("You've already moved your king or rook. Please try again.")
                            else:
                                input("A king cannot move more than one square at a time. Please try again.")
        for i in range(8):
            for a in range(8):
                if piece[i][a] == "wk":
                    count = count - 1
                elif piece[i][a] != "wk":
                    count = count + 1
        if count == 64:
            input("White's king has been taken. Black wins. White is a skill issue.")
            king = False
        count = 0
        temporary_holder2 = True
        move_k = False
        move_rr = False
        move_lr = False
        turn = turn - 1
