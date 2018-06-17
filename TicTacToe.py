import math
count=0
c=set()
s=[1,2,3,4,5,6,7,8,9]
def board(s):
    print("\t\t\t{}:::{}:::{}".format(s[0],s[1],s[2]))
    print("\t\t\t:::::::::")
    print("\t\t\t{}:::{}:::{}".format(s[3],s[4],s[5]))
    print("\t\t\t:::::::::")
    print("\t\t\t{}:::{}:::{}".format(s[6],s[7],s[8]))

def player_turn():
    global count
    print("Player {} , mention your position (1-9)".format(count%2+1))
    i=input()
    if i=='':
        player_turn()
        count=count-1
    else:
        if i not in c:
            if (count%2+1)==1:
                s[int(i)-1]='X'
            else:
                s[int(i)-1]='O'
        else:
            print("Already filled!  Player {} , try again (1-9)".format(count%2+1))
            count=count-1
    count=count + 1
    c.add(i)

def check_win():
    board=s
    return ((board[6] == board[7] and board[8] == board[7]) or # across the top
            (board[3] == board[4] and board[5] == board[4]) or # across the middle
            (board[0] == board[1] and board[2] == board[1]) or # across the bottom
            (board[6] == board[3] and board[0] == board[3]) or # down the middle
            (board[7] == board[4] and board[1] == board[4]) or # down the middle
            (board[8] == board[5] and board[2] == board[5]) or # down the right side
            (board[6] == board[4] and board[2] == board[4]) or # diagonal
            (board[8] == board[4] and board[0] == board[4])) # diagonal
        
if __name__=='__main__':
    while(1):
        while(1):
            board(s)
            player_turn()
            if check_win():
                count=count-1
                board(s)
                print("\t\tPlayer {} is the Winner!!!!".format(count%2+1))
                break
            else:
                if count==9:
                    board(s)
                    print("\t\tIt's a Tie!!!")
                    break
        print("Play again? (y/n)")
        i=input()
        if i.lower() == 'n':
            break
        else:
            count=0
            c=set()
            s=[1,2,3,4,5,6,7,8,9]
