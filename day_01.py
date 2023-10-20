# 1. print 함수
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

print("   --------------------   ")
# End

# 2. 줄 바꾸기
print("Hello world!\nHello world!\nHello World!")

print("   --------------------   ")
# End

# 3. 단어 띄어쓰기
print("Hello" + " " + "Angela"), print("Hello " +
                                       "Angela"), print("Hello" + " Angela")

print("   --------------------   ")
# End

# 4. 디버깅
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

print("   --------------------   ")
# End

# 5. input은 입력함수로 input 내 prompt를 통해 입력된 데이터가 출력. 하단의 경우 "Hello NAME"이 출력 됨 / Hello가 먼저 출력되지 않음.
print("Hello" + " " + input("What is your name? "))

print("   --------------------   ")
# End

# 6. 하단 두개의 print의 결과는 같음
name = input("What is your name? ")
print(len(name))
print(len(input("What is your name? ")))

print("   --------------------   ")
# End

# 7. a와 b의 값이 같아지게 하는 법
a = input("a: ")
b = input("b: ")

c = a
a = b
b = c

print("a = " + a)
print("b = " + b)

print("   --------------------   ")
# End

# 8. 종합
print("Welcome to the Band Name Generater.")
city = input("What's name of the city you grew up in?\n")
pet_name = input("What's your pet's name?\n")
print("Your badn name could be", city, pet_name)
# End
