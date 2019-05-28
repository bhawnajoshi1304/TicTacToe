from os import system,name
from time import sleep
def clear():
     if name=='nt':
          _=system('cls')
     else:
          _=system('clear')

a=['1','2','3','4','5','6','7','8','9']
def show():
     print("     |     |     \n ",a[0]," | ",a[1]," | ",a[2]," \n_____|_____|_____\n     |     |     \n ",a[3]," | ",a[4]," | ",a[5]," \n_____|_____|_____\n     |     |     \n ",a[6]," | ",a[7]," | ",a[8]," \n     |     |     \n")
def check(pos):
      if a[pos-1]=='O' or a[pos-1]=='X':
            print("Move already made .\nINVALID MODE")
            return 0
      else: return 1
def win():
      if a[0]==a[1] and a[1]==a[2] and a[2]=='O':
            return 1
      elif a[0]==a[1] and a[1]==a[2] and a[2]=='X':
            return 2
      elif a[3]==a[4] and a[4]==a[5] and a[5]=='O':
            return 1
      elif a[3]==a[4] and a[4]==a[5] and a[5]=='X':
            return 2
      elif a[6]==a[7] and a[7]==a[8] and a[8]=='O':
            return 1
      elif a[6]==a[7] and a[7]==a[8] and a[8]=='X':
            return 2
      elif a[0]==a[3] and a[3]==a[6] and a[6]=='O':
            return 1
      elif a[0]==a[3] and a[3]==a[6] and a[6]=='X':
            return 2
      elif a[1]==a[4] and a[4]==a[7] and a[7]=='O':
            return 1
      elif a[1]==a[4] and a[4]==a[7] and a[7]=='X':
            return 2
      elif a[2]==a[5] and a[5]==a[8] and a[8]=='O':
            return 1
      elif a[2]==a[5] and a[5]==a[8] and a[8]=='X':
            return 2
      elif a[0]==a[4] and a[4]==a[8] and a[8]=='O':
            return 1
      elif a[0]==a[4] and a[4]==a[8] and a[8]=='X':
            return 2
      elif a[2]==a[4] and a[4]==a[6] and a[6]=='O':
            return 1
      elif a[2]==a[4] and a[4]==a[6] and a[6]=='X':
            return 2
      elif a[0]!=' ' and a[1]!=' ' and a[2]!=' ' and a[3]!=' ' and a[4]!=' ' and a[5]!=' ' and a[6]!=' ' and a[7]!=' ' and a[8]!=' ':
            return -1
      else:
            return 0
          
def move(player,player1,player2):
      print("Enter position for move...",player)
      pos=int(input())
      sleep(1)
      clear()
      if check(pos)==0:
            show()
            move(player,player1,player2)
      elif player==player1:
            a[pos-1]='O'
            player=player2
      else:
            a[pos-1]='X'
            player=player1
      if win()==1:
            show()
            print(player1,"WINS THE GAME")
      elif win()==2:
            show()
            print(player2,"WINS THE GAME")
      elif win()==-1:
            show()
            print("Its a TIE")
      else:
            show()
            move(player,player1,player2)
      sleep(2)
            
def start(a):
     print("\t\t\t\tWELCOME TO TIC TAC TOE\n\n\nThe game board design is as follows:")
     show()
     print("\nPlayers have to enter position number to make move .\nPlayer who makes a trio along any row , column or diagonal wins the game...")
     player1=input("Enter name of PLAYER 1 ( Player 1 gets O)")
     player2=input("Enter name of PLAYER 2 ( Player 2 gets X)")
     print(player1," gets the first chance...")
     player=player1
     a[0]=a[1]=a[2]=a[3]=a[4]=a[5]=a[6]=a[7]=a[8]=' '
     move(player,player1,player2)
start(a)

     


