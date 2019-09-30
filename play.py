from main import *
from best import *
import random
numlist = [1,2,3,4,5,6,7,8,9,10]
symbollist = ["+","-","*","/"]

print("Welcome to Equation Check")
show_best()
name = input("What your name?\n> ")
login(name)
lv = input("Choose your level\nlevel 1 have 2 number 1 symbol\nlevel 2 have 3 number 2 symbol\n> ")
print("\nIf equation is True you should input T else input F\n")
score = 0

while True:
    num1 = random.choice(numlist)
    num2 = random.choice(numlist)
    num3 = random.choice(numlist)
    symbol1 = random.choice(symbollist)
    symbol2 = random.choice(symbollist)
    Equation = EquationCreate(num1,num2,num3,symbol1,symbol2,lv)
    answer_show = answer(num1,num2,num3,symbol1,symbol2,lv,Equation)
    answer_input = input(">")
    while answer_input not in ["T","F"]:
        answer_input = input("Plase input T or F\n> ")
    if answer_check(Equation,answer_show,answer_input) == True:
        score +=1
        print("Nice! You score is: %s"%score)
    elif answer_check(Equation,answer_show,answer_input) == False:
        print("Game Over!!!")
        print("You score is: %s"%score)
        best(name,score)
        break