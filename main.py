import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_icon=[rock,paper,scissors]
#Write your code below this line 👇
print("Welcome to Roc,paper,scissor game.To start playing with computer choose your option\n")
user_choice=int(input("For Rock press 0,for  paper press 1,for scissor press 2\n"))
if user_choice<0 or user_choice>3:
  print("You type invalid number,You Lose")
else:
  print(game_icon[user_choice])
  computer_choice=random.randint(0,2)
  print(game_icon[computer_choice])
  # print(computer_choice)
  
  if(user_choice==0 and computer_choice==2):
    print("You win")
  elif(computer_choice==0 and user_choice==2):
    print("You lose")
  elif computer_choice>user_choice:
    print("You Lose")
  elif computer_choice<user_choice:
    print("You win")
  elif computer_choice== user_choice:
    print("Its a draw")
  
  
  
