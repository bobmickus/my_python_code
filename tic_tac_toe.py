
def print_board():
    global row1, row2, row3
    print row1
    print row2
    print row3, "\n"


def set_up_game():
    import random
    global player1, player2, first, second, turn
    print "\nWelcome to Sponge-Bob's Super-Duper Game of X's and O's!!!  Ready to have some fun? \n"
    player1 = raw_input('Hey, player one....what is your name? ')
    player2 = raw_input('Yo, player two....what is your name? ')
    instr = raw_input('Do you want to see the instructions on how to play the game? (y for yes, otherwise just hit enter) ')
    if instr == "y":
        print "Here is what the game board looks like: \n"
        print_board()

        print "When it is your turn, you will enter the code for which spot you want"
        print "to select. So for example, to select the spot shown above that corresponds"
        print "to (1,2) you will enter: 12.   Make sense? \n"

    print 'Alright, here we go! Let me flip a coin to see who goes first. \n'
    randnum = random.randrange(0,100)
    if randnum < 50:
        print player1, "you get to go first!  You will be the letter 'X' \n"
        first = player1
        second = player2
        turn = 1

    else:
        print player2, "you get to go first!  You will be the letter 'X' \n"
        first = player2
        second = player1
        turn = 1

def determine_winner(row1, row2, row3):
    global game_over
    if    row1[0] == row1[1] == row1[2]:
        game_over = 'y'
    elif  row2[0] == row2[1] == row2[2]:
        game_over = 'y'
    elif  row3[0] == row3[1] == row3[2]:
        game_over = 'y'
    elif  row1[0] == row2[0] == row3[0]:
        game_over = 'y'
    elif  row1[1] == row2[1] == row3[1]:
        game_over = 'y'
    elif  row1[2] == row2[2] == row3[2]:
        game_over = 'y'
    elif  row1[0] == row2[1] == row3[2]:
        game_over = 'y'
    elif  row1[2] == row2[1] == row3[0]:
        game_over = 'y'
    elif (row1[0] != (1,1) and row1[1] != (1,2) and row1[2] != (1,3)
          and row2[0] != (2,1) and row2[1] != (2,2) and row2[2] != (2,3)
          and row3[0] != (3,1) and row3[1] != (3,2) and row3[2] != (33)):
        game_over = 'tie'


def main():
    global row1, row2, row3, player1, player2, turn, first, second, game_over

    set_up_game()
    Empty_Grid = "True"
    game_over = "n"

    while game_over != 'y':
       if turn == 1:
           while Empty_Grid:
             boxstr = raw_input('{} where would you like to put your X: '.format(first))
             row = int(boxstr[0])
             column = int(boxstr[1])

             if row == 1:
                if row1[column-1] == 'X' or row1[column-1] == 'O':
                    print "Sorry, that space is already taken. Try again {}!".format(first)
                    Empty_Grid = "False"
                else:
                    row1[column-1] = 'X'
                    break
             elif row == 2:
                if row2[column-1] == 'X' or row2[column-1] == 'O':
                    print "Sorry, that space is already taken. Try again {}!".format(first)
                    Empty_Grid = "False"
                else:
                    row2[column-1] = 'X'
                    break
             elif row == 3:
                if row3[column-1] == 'X' or row3[column-1] == 'O':
                    print "Sorry, that space is already taken. Try again {}!".format(first)
                    Empty_Grid = "False"
                else:
                    row3[column-1] = 'X'
                    break

           print "\nHere is what the board looks like now:\n"
           print_board()

           determine_winner(row1, row2, row3)
           if game_over == 'y':
             print "\033[5;31;47m \033CONGRATULATIONS {}!!!  You are the winner, winner. Chicken dinner!".format(first)
             print "\nThanks for playing!  Please deposit another quarter to play again."
             break
           elif game_over == 'tie':
             print "Looks like it is a CATS game.....you know, a boring tie!"
             print "\nPlease deposit another quarter to play again."
             break
           else: turn = 2

       if turn == 2:
          while Empty_Grid:
            boxstr = raw_input('{} where would you like to put your O: '.format(second))
            row = int(boxstr[0])
            column = int(boxstr[1])

            if row == 1:
               if row1[column-1] == 'X' or row1[column-1] == 'O':
                   print "Sorry, that space is already taken. Try again {}!".format(second)
                   Empty_Grid = "False"
               else:
                   row1[column-1] = 'O'
                   break
            elif row == 2:
               if row2[column-1] == 'X' or row2[column-1] == 'O':
                   print "Sorry, that space is already taken. Try again {}!".format(second)
                   Empty_Grid = "False"
               else :
                   row2[column-1] = 'O'
                   break
            elif row == 3:
               if row3[column-1] == 'X' or row3[column-1] == 'O':
                   print "Sorry, that space is already taken. Try again {}!".format(second)
                   Empty_Grid = "False"
               else:
                   row3[column-1] = 'O'
                   break

          print "\nHere is what the board looks like now:\n"
          print_board()

          determine_winner(row1, row2, row3)
          if game_over == 'y':
            print "\033[5;31;47m \033CONGRATULATIONS {}!!!  You are the winner, winner. Chicken dinner!".format(second)
            print "\nThanks for playing!  Please deposit another quarter to play again."
            break
          elif game_over == 'tie':
            print "Looks like it is CATS game.....you know, a boring tie!"
            print "\nPlease deposit another quarter to play again."
            break
          else: turn = 1

#if __name__ == '__main__':


row1 = [(1,1), (1,2), (1,3)]
row2 = [(2,1), (2,2), (2,3)]
row3 = [(3,1), (3,2), (3,3)]
player1 = ''
player2 = ''
turn = 1
game_over = "False"

main()
