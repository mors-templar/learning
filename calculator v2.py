# calculator with validation checks using regex
import re

continue_equation = True
previous_run = 0


def calculation(equation):
    global continue_equation
    global previous_run
    simplify = re.sub('[A-Za-z.,;:]', " ", equation)
    previous_run = eval(simplify)
    continuerun(previous_run)


def continuerun(prev_run):
    global continue_equation
    while continue_equation == True:
        print(prev_run)
        equation = input()
        if equation != "x":
            calculation( str(prev_run) + equation )
        else:
            continue_equation = False

def calculator():
    global continue_equation
    global previous_run
    equation = input("please enter your equation:")
    print("x to terminate")
    calculation(equation)

    ######## main body #############

calculator()