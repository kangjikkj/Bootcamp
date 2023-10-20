# 1. Modulo Operation: Odd or Even
number = int(input("Which number do you want to check? "))
if number / 2 != 0:
    print("This is an odd number.")
else:
    print("THis is an even number.")
print(number)

print("   --------------------   ")
# End

# 2. if elif else
height = float(input("How tall you are? "))
if height >= 120:
    print("your can ride")
    age = int(input("How old are you? "))
    if age < 12:
        print("your ticket is $5")
    elif age <= 18:
        print("your ticket is &7")
    elif age > 18:
        print("yout ticket is $12")
else:
    print("sorry, you can't ride")

print("   --------------------   ")
# End

# 3. BMI Calculator ver.2
height = float(input("Enter youot height in m: "))
weight = float(input("Enter your weight kg: "))
BMI = round(weight / height**2)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight")
elif BMI < 25:
    print(f"Your BMI is {BMI}, You are normal weight")
elif BMI < 30:
    print(f"Your BMI is {BMI}, You are overweight")
elif BMI < 35:
    print(f"Your BMI is {BMI}, You are obese")
else:
    print(f"Your BMI is {BMI}, You are clinically obese")
print("   --------------------   ")
# End

# 4. Leap Year
# have to make 0(no) remainder
year = int(input("which year do you want to check? "))
if year % 4 == 0:
    print(f"{year} is leap year.")
elif year % 100 == 0:
    print(f"{year} is not leap year.")
elif year % 400 == 0:
    print(f"{year} is leap year")
else:
    print(f"{year} is a not leap year")

year = int(input("which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year.")

print("   --------------------   ")
# End

# 5. Multiple if
height = float(input("How tall you are? "))
bill = 0
if height >= 120:
    print("your can ride")
    age = int(input("How old are you? "))
    if age < 12:
        bill = 5
        print("your ticket is $5")
    elif age <= 18:
        bill = 7
        print("your ticket is &7")
    elif age > 18:
        bill = 12
        print("yout ticket is $12")
    photo = input("Do you want photo, Y or N? ").lower()
    if photo == "Y".lower():
        bill += 3
    print(f"Your bill is {bill}")
else:
    print("sorry, you can't ride")

print("   --------------------   ")
# End

# 6. Pizza Order
print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S,M or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra chesse? Y or N ").lower()
if size == "S".lower():
    bill += 15
elif size == "M".lower():
    bill += 20
else:
    bill += 25
if add_pepperoni == "Y".lower():
    if size == "S".lower():
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y".lower():
    bill += 1
print(f"your final bill is: ${bill}")

print("   --------------------   ")
# End

# 7. Love Calculator Exercise
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is yout name? \n").lower()
name3 = name1 + name2
true = name3.count("t") + name3.count("r") + \
                   name3.count("u") + name3.count("e")
love = name3.count("l") + name3.count("o") + \
                   name3.count("v") + name3.count("e")
true_love = int(str(true) + str(love))
if true_love <= 10 or true_love >= 90:
    print(f"your score is {true_love}, you go together like coke and moentos.")
elif 40 <= true_love <= 50:
    print(f"yout score is {true_love}, you are alright together.")
else:
    print(f"your score is {true_love}")

# 8. Treasure Island
from day_03_1 import logo
print(logo)

print("Welcome to Treaure Island")
print("Your mission is to find the treasure.")
choice1=input('You\'re at a crossrad, where do you want to go? "Left" or "Right"? ').lower(
).upper()  # \' 사용시, ' 기입 가능
if choice1 == "left":
    choice2=input(
        'You\'ve come to a lake. Three is an island in the middle of lake. "Swim or Wait? ').lower().upper()
    if choice2 == "Wait":
        choice3=input("Which Door? Red, Yellow or Blue? ").lower().upper()
        if choice3 == "Yellow":
            print("YOU WIN")
        elif choice3 == "Blue":
            print("GAME OVER, You died.")
        else:
            print("GAME OVER")
    else:
        print("GAME OVER")
else:
    print("GAME OVER, You fell in to hole.")

print("   --------------------   ")
# End
