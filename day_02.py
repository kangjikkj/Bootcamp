# 1 type: integer, string, floating 변환 가능
print(int("70") + float("100.5"))
print(str(60) + str(100))
# 1-1 문자열과 정수를 합칠 수 없음
num_char = len(input("What's your name? "))
new_num_char = str(num_char)
print("Your name contains " + new_num_char + " characters")
# 연습
two_digit_numebr = input("type a two digit numebr: ")
print(two_digit_numebr[0] + two_digit_numebr[1])
print(int(two_digit_numebr[0]) + int(two_digit_numebr[1]))

print("   --------------------   ")
# End

# 2. 사칙연산
PEMDAS
() Parenthese
** Exponents
* / Multiplication, Division(파이썬 내에서 결과값은 소수(float))
+- Addition, Subtraction
# 2-1 변수와 사칙연산
score = score + 1 는 score += 1 과 같음, */+- 모두 사용 가능
# 2-2 나누기 소수점
print(round(8 / 3, 2))  # 소수점 2자리까지 출력 = 2.67
print(13 / 2)  # 나누기 = 6.5
print(13 // 2)  # 몫 구하기 = 6
print(13 % 2)  # 나머지 구하기 = 1

print("   --------------------   ")
# End

# 3. BMI calculator
height = input("enter your height: ")
weight = input("enter your weight: ")
BMI = float(weight) / float(height)**2
print(int(BMI))

print("   --------------------   ")
# End

# 4. f-string
score = 0
height = 1.8
isWinning = True
print(
    f"Your score is {score}, your height is {height}, you are winning is {isWinning}")

print("   --------------------   ")
# End

# 5. 연습: Your Life in Weeks
age = int(input("Waht is your current age? "))
left_age = 90 - age
day = left_age*365
week = left_age*52
month = left_age*12
message = f"You have {day} days, {week} and {month} months left."
print(message)

print("   --------------------   ")
# End

# 6. 연습: Bill Calcualtor
print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
split = float(input("How many peole to split the bill? "))
pay = (tip / 100 * bill + bill) / split
final = round(pay, 2)
# fianl = "{:.2f}".format(pay) # -> round를 사용하였을 경우, (예시) 3.60의 0은 표시되지 않음. 0까지 표시되게 하기 위해서 쓰는 함수
print(f"Each person should pay: ${final}")

print("   --------------------   ")
# End
