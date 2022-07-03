# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

calc1 = year % 4
calc2 = year % 100
calc3 = year % 400

# % == modulo operater... how many remaining numbers left E.G 11 % 5 = 1

#have to work backwards

if calc3 == 0:
    print("Leap year.")
elif calc2 == 0:
    print("Not leap year.")
elif calc1 == 0:
    print("Leap year.")
else:
    print("Not leap year.")