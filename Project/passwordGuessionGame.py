import random

easy_word = ["cat", "dog", "sun", "book", "tree"]
medium_word = ["python", "guitar", "flower", "mountain", "computer"]
hard_word = ["elephant", "astronomy", "philosophy", "architecture", "psychology"]

print("Welcome to the Password Guessing Game!")
print("Choose a difficulty level: easy, medium, hard")

level = input("Enter your choice: ").lower()
if level == "easy":
  secret = random.choice(easy_word)
elif level == "medium":
  secret = random.choice(medium_word)
elif level == "hard":
  secret = random.choice(hard_word)
else:
  print("Invalid choice. Defaulting to easy level.")
  secret = random.choice(easy_word)
attempts = 0
print("\nguess the secret password: ")

while True:
  guess = input("Enter your guess: ")
  attempts += 1
  if guess == secret:
    print(f"Congratulations! You've guessed in it {attempts} attempts!")
    break

  hint = ""

  for i in range(len(secret)):
    if i < len(guess) and guess[i] == secret[i]:
      hint += guess[i]
    else:
      hint += "_"

  print(f"Hint: {hint}")
print("Thanks for playing the Password Guessing Game!")

# time = 1:23