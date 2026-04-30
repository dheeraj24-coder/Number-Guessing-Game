import random

comp_number = random.randint(1, 21)
guess_num=int(input("Enter a number between 1 to 20 : "))
c=1
while guess_num!=comp_number:
  if guess_num < comp_number:
    print("Bhai thoda bda soch: ")
    guess_num=int(input("Enter a number again: "))
    c+=1

  elif guess_num > comp_number:
    print("Bhai thoda chota soch: ")
    guess_num=int(input("Enter a number again: "))
    c+=1

  else:
    print("Coreect guess: ")
    print("Tune itane attempt liye: ", c)

print("Coreect guess")
print("Tune itane attempt liye: ", c)
