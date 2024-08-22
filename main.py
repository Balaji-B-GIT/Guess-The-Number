from random import randint
from art import logo,won,lose

print(logo)
print("Welcome to The Number Guessing Game!")
print("I'm thinking of a number between 1 to 100")
difficulty = input("Choose a difficuly.Type 'easy' or 'hard': ")

#to choose a value within the range
comp_guess = randint(1,100)
   
def easy():
  attempts = 10
  while attempts > 0:
    print(f"You have {attempts} attempts to guess the number")
    my_guess = int(input("Make A Guess: "))
    if(my_guess < comp_guess):
      attempts -= 1
      print("Too Low!")
    elif (my_guess > comp_guess):
      attempts -= 1
      print("Too High!")
    else:
      print(won)
      print(f"You Found!! The answer is {comp_guess}")
      break
    if (attempts == 0):
      print(lose)
      print("You've run out of guesses, You Lose!")

def hard():
  attempts = 5
  while attempts > 0:
    print(f"You have {attempts} attempts to guess the number")
    my_guess = int(input("Make A Guess: "))
    if(my_guess < comp_guess):
      attempts -= 1
      print("Too Low!")
    elif (my_guess > comp_guess):
      attempts -= 1
      print("Too High!")
    else:
      print(won)
      print(f"You Found!! The answer is {comp_guess}")
      break
    if (attempts == 0):
      print(lose)
      print("You've run out of guesses, You Lose!")

if difficulty == "easy":
  easy()
elif difficulty == "hard":
  hard()
else:
  print("Invalid Input!!!")
  
    
    
