import random
print("------ WELCOME TO ROCK, PAPER & SCISSORS! ----- \n")
choice = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
win = {'Rock': 'Scissors', 'Paper': 'Rock', 'Scissors': 'Paper'}
select = random.randint(1,3)
compch = choice[select]
print("Computer chooses: ", select, "\n")
try:
  m = int(input("Enter your move: \n 1. Rock \n 2. Paper \n 3. Scissors \n"))
  if m < 1 or m > 3:
    print("Wrong input! Please enter a number between 1 and 3.")
  else:
    userch = choice[m]
    if compch==win[userch]:
      print("You win! \n You selected: ", userch, "\n Computer selected: ", compch)
    elif userch==win[compch]:
      print("Computer wins! \n You selected: ", userch, "\n Computer selected: ", compch)
    else:
      print("Tie!")
      

except ValueError:
    print("Invalid input! Please enter a number.")


