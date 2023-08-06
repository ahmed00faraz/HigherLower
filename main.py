from art import *
from game_data import data
import random
from replit import clear 
#Format the account data in prinatble format
def format_data(acc):
  account_name=acc["name"]
  account_desc=acc["description"]
  account_country=acc["country"]
  return f"{account_name} , a {account_desc}, from {account_country}"
def check_answer(guess,a_followers,b_followers):
  '''takes the account data and return it in printable format'''
  if a_followers == b_followers :
    return True
  elif a_followers >b_followers:
    return guess == "A"
  else:
    return guess == "B"
  
#Display the art
print(logo)

score = 0
game_should_continue = True


# make game repeatable  
account_b=random.choice(data)

while game_should_continue:
  
  #Generate random acc from game data
  account_a=account_b
  account_b=random.choice(data)
  while account_a==account_b:
    account_b=random.choice(data)
  
  print(f"Compare A {format_data(account_a)}.")
  print(vs)
  print(f"Against B {format_data(account_b)}.")
  
  # ask User for a guess
  guess=input("Who has more followers? Type 'A' or 'B':").upper()
  
  #check if user is correct
    #get follower count of each user 
    #use if statement to check
  a_follower_count=account_a['follower_count']
  b_follower_count=account_b['follower_count']
  clear()
  print(logo)
  is_correct = check_answer(guess,a_follower_count,b_follower_count)
  #give user feedback for their answer
  if is_correct :
    score+=1
    
    print(f"You're Right! Current Score : {score}")
  else:
    game_should_continue = False
    print(f"Sorry ! , You're Wrong   Final Score : {score}")
#score keeping


# change position of account B to move to position of Account A

