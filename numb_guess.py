import random
import time
print ("Hello World! Welcome to the game!")
time.sleep(3)
n = random.randint(1, 10)
print("Number has been generated!!\nYou have 4 chances to guess the number!")

count = 4

while count != 0:
    a = int(input("Guess the number: "))

    if a == n:
        print("Correct! You got the number right!")
        break
    elif a > n:
        print("lower ", a)
    else:
        print("Greater ", a)
    count =- 1
