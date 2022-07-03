print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill += 5
    print("Child tickets are £5")
  elif age <=18:
    bill += 7
    print("Youth tickets are £7")
  elif age >= 45 and age <= 55:
    print("Tickets for customers aged between 45 and 55 are free of charge.")
  else:
    bill += 12
    print("Adult tickets are £12")

  wants_photo = input("Want Photos for £3? y or n ")
  if wants_photo == "y":
    bill += 3
  print(f"Your total bill is £{bill}")
  
else:
  print("Sorry, you have to grow taller before you can ride.")