def range_of_numbers(number):
  if -100 <= number <= 100:
    print("Your number is within the range of -100 to 100")
  else:
    print("Your number is not within -100 and 100")

def even_options(number):
  five_division = int(number % 5)
  three_division = int(number % 3)
  print("Your number is even.")
  range_of_numbers(number)
  if five_division > 0:
    print("Your number is not divisible by 5.")
  else:
    print("Your number is divisible by 5.")
  if three_division > 0:
    print("Your number is not divisible by 3.")
  else:
    print("Your number is divisible by 3.")

def odd_options(number):
  print("Your number is odd")
  range_of_numbers(number)
  if number >= 0:
    print("Your number is positive")
  else:
    print("Your number is negative")


number = float(input("What is your number? "))
number_after = number % 2 
if number_after == 0:
  even_options(number)
else:
  odd_options(number)
