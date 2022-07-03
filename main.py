#if condition:
  #if another condition:
    #do this
  #else:
    #do this
#else:
  #do this

#Elif ---- can add as many elif's as u like

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    print("Please pay £5")
  elif age <=18:
    print("Please pay £7")
  elif age ==23:
    print("Awesome age, you get to go for free.")
  else:
    print("Please pay £12")
else:
  print("Sorry, you have to grow taller before you can ride.")