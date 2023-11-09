#Module Imports
import itertools

import time



aaa = input('Enter a Username: ')

#Used later to check if string contains letters from only a - h
Invalid = set('ijklmnopqrstuvwxyz')
#Checks to see if there are digits in the string
def digits(string):
  for char in string:
    if char.isdigit():
      return True
  return False

#Stores password in a variable.
password = input('Enter a password that is 8 characters long, contains only lowercase letters and contains characters a - h: ')



while len(password) != 8 or Invalid.intersection(password) or password.lower() == False or digits(password) == True: #Checks to see if it meets the conditions for the codes, if not it reloops
  print()
  print('The password you have entered is either not 8 characters, contains letters other than lowercase letters, or contains letters outside of a-h, please try again.')
  print()
  password = input('Enter a password that is 8 characters long, contains only lowercase letters and contains characters a - h:')


start = time.time() #Begins timer
characters = 'abcdegh' #Makes characters have all lowercase letters and numbers
for password_length in range(1,9): 
  for guess in itertools.product(characters, repeat=password_length): #Repeats until password is found
    guess = ''.join(guess)
    if guess == password:
      seconds = time.time() - start #Finds how long it took to run the program
      #Prints the data gained from the earlier code
      print()
      print('Account Cracked.')
      print('Username:',aaa)
      print()
      print('Password was cracked in: ', seconds)
      print('Password: ', guess)
