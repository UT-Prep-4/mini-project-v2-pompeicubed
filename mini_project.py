import random

amount = 0
guess = 0
ans = random.randint(1,1000)
print("Guess a number between 1 and 1000")

while guess != ans:
  guess = int(input("Enter your guess: "))
  if guess < ans:
    print("Too low!")
  elif guess > ans:
    print("Too high!")
  amount = amount + 1
print("Correct! You took", amount, "guesses.")






