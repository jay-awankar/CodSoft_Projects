import random

print("\t Rock Paper Scissor Game\n")
print("Choose: \n 1 for Rock \n 2 for Paper \n 3 for Scissor :")
user_score = 0
comp_score = 0
i=0
while i<10:
  user_choice = int(input("Enter your choice: "))
  if user_choice == 1:
    print("You choose Rock")
  elif user_choice == 2:
    print("You choose Paper")
  elif user_choice == 3:
    print("You choose Scissor")
  else:
    print("Invalid choice")
  comp_choice = random.randint(1, 3)
  if comp_choice == 1:
    print("Computer choose Rock")
  elif comp_choice == 2:
    print("Computer choose Paper")
  elif comp_choice == 3:
    print("Computer choose Scissor")
  
  if user_choice == comp_choice:
    print("Draw")
    print(f"Your score:{user_score}\tComputer score: {comp_score}")
    continue 
  elif user_choice == 2 and comp_choice == 1:
    user_score += 1
    print("You won")
    print(f"Your score:{user_score}\tComputer score: {comp_score}")
  elif user_choice == 3 and comp_choice == 1:
    comp_score += 1
    print("Computer won")
    print(f"Your score:{user_score}\tComputer score: {comp_score}")
  elif user_choice == 1 and comp_choice == 2:
    print("Computer won")
    comp_score += 1
    print("Computer won")
    print(f"Your score:{user_score}\tComputer score: {comp_score}")
  elif user_choice == 3 and comp_choice == 2:
    user_score += 1
    print("You won")
    print(f"Your score:{user_score}\tComputer score: {comp_score}")
  elif user_choice == 1 and comp_choice == 3:
    user_score += 1
    print("You won")
    print(f"Your score:{user_score}\tComputer score: {comp_score}")
  elif user_choice == 2 and comp_choice == 3:
    comp_score += 1
    print("Computer won")
    print(f"Your score:{user_score}\tComputer score: {comp_score}")
  i+=1

print("Game Over")
if user_score > comp_score:
  print("You won the game")
elif user_score < comp_score:
  print("Computer won the game")
else:
  print("Tie")