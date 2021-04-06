# BINGO! 2 player game
import random


# numbers

# make the playing board

def board():
  # Board for player 1
  num1_list = list(range (1,26))
  random.shuffle(num1_list)
  num1_list = list(map(str,num1_list))
  x1= 0
  print("Player 1 board: \n")
  for i in range (5):
    for j in range(5):
        print(num1_list[x1], end ="\t")
        x1+=1
    print("\n")
  # Board for player 2
  print("\nPlayer 2 board:\n ")
  num2_list = list(range(1,26))
  random.shuffle(num2_list)
  num2_list = list(map(str, num2_list))
  x2 = 0
  for i in range (5):
    for j in range(5):
      print(num2_list[x2],end='\t')
      x2+=1
    print("\n")
  r = 1

  while True:
    try:
      print("\nRound",r)
      strike = int(input("\nTo end the game input any word.\nPlayer 1 enter your number: "))
      x1 = 0
      #striking a numerber for player 1's board
      print("\nPlayer 1's board: \n")
      for i in range(5):
        for j in range(5):
          if str(strike) == num1_list [x1]:
            print(num1_list[x1],end ="❌\t")
            num1_list[x1] = num1_list[x1]+'❌'
            x1+=1
          else:
            print(num1_list[x1],end = "\t")
            x1+=1
        print("\n")

      # Striking board for player 2's board
      print('\n')
      x2 =0 
      print("\nPlayer 2's board: \n")
      for i in range(5):
        for j in range(5):
          if str(strike) == num2_list [x2]:
            num2_list[x2] = num2_list[x2]+'❌'
            print(num2_list[x2],end ="\t")
            
            x2+=1
          else:
            print(num2_list[x2],end = "\t")
            x2+=1
        print("\n")

      print("\nRound",r)
      strike = int(input("\nTo end the game input any word.\nPlayer 2 enter your number: "))

     #striking a numerber for player 1's board
      x1 =0
      print("\nPlayer 1's board: \n")
      for i in range(5):
        for j in range(5):
          if str(strike) == num1_list [x1]:
            print(num1_list[x1], end ="❌\t")
            num1_list[x1] = num1_list[x1]+'❌'
            x1+=1
          else:
            print(num1_list[x1],end = "\t")
            x1+=1
        print("\n")
      x2=0
      # Striking a number for player 2's board
      print("\nPlayer 2's board: \n")
      for i in range(5):
        for j in range(5):
          if str(strike) == num2_list [x2]:
            print(num2_list[x2],end ="❌\t")
            num2_list[x2] = num2_list[x2]+'❌'
            x2+=1
          else:
            print(num2_list[x2],end = "\t")
            x2+=1
        print("\n")
      r+=1

     

    except ValueError:
      print("Thank you for playing BINGO. ")
      break
      
board()

