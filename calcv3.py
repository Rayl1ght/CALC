import math


# Main calculator function
def calc(eq):
    try:
        eqSplit = eq.split()
        res = ""

        div = eqSplit.count("/")
        for amount in range(div):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "/":
                    mem = float(eqSplit[length - 1]) / float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " / " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        mul = eqSplit.count("*")
        for amount in range(mul):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "*":
                    mem = float(eqSplit[length - 1]) * float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " * " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        sub = eqSplit.count("-")
        for amount in range(sub):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "-":
                    mem = float(eqSplit[length - 1]) - float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " - " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        add = eqSplit.count("+")
        for amount in range(add):
            for length in range(len(eqSplit)):
                if eqSplit[length] == "+":
                    mem = float(eqSplit[length - 1]) + float(eqSplit[length + 1])
                    substr = eqSplit[length - 1] + " + " + eqSplit[length + 1]
                    res = eq.replace(substr, str(mem))
                    eq = res
            eqSplit = eq.split()

        return eq
    except IndexError:
        print("Error: Incorrect numin.")
    except ValueError:
        print("Error: Incorrect numbers.")

numin = input("> ")
subStr = ""

# Calculate parenthesises
parenthesis = numin.count("(")
for a in range(parenthesis):
    if not ((numin.rfind("(") - 1) < 0) and str(numin[numin.rfind("(") - 1]).isdigit():
        substr = numin[(numin.rfind("(") + 1):numin.find(")", numin.rfind("(") - 1)]
        numin = numin.replace("(" + substr + ")", " * " + str(calc(substr)))
    else:
        substr = numin[(numin.rfind("(") + 1):numin.find(")", numin.rfind("("))]
        numin = numin.replace("(" + substr + ")", str(calc(substr)))
numin = calc(numin)
print("Answer: " + str(numin))