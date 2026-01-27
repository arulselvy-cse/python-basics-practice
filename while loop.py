n = int(input("Enter a number:"))
while n>0:
  print(n)
  n = n-1   #Countdown (backwards)

correct_password = "python123"
password = ""
while password!= correct_password:
  password = input("Enter ur password:")
  print("Access Granted")   #Password checker

secret_number = 7
guess = 0 
while guess != secret_number:
  guess = int(input("Guess the number:"))
  print("Correct! You guessed it.")   #Guessing game
