#calculator creation without any validation check

equation = input("please enter equation")
def calculator():
    print("output is",calculate(equation))
def calculate(equate):
    out = eval(equate)
    return out
calculator()
