# Welcome to Rock, Paper, Sissors agains the MACHINE!
import random

# variables to delare for user our rock paper sissors
# Ask user for choice
# way for computer to random choose rock paper sissors
# Check if they equal then tie
# Check if user wins
# Check if MACHINE wins

r = None
p = None
s = None

user = input('Please choose "r" for rock, "p" for paper, and "s" for sissors" \n').lower()


options = ['r', 'p', 's']
machine = random.choice(options)

if machine == user:
  print("It's a tie")
elif user == "r" and machine == "s" or user == "p" and machine == "r" or user == "s" and machine == "p":
  print("Yay! You've won")
else:
  print("Sorry, the MACHINE has defeated you")