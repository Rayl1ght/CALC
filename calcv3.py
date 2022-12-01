import math


class calculator:

    def init(self):
        pass

    def start(self, inp_str):
        inp_str = self.cast_str(inp_str)
        print("Answer: " + str(self.start_calc(inp_str)))

    def start_calc(self, inp_str):
        split_str = inp_str.split()
        try:
            self.calc_mul(split_str)
            #print(split_str)
            self.calc_div(split_str)
            #print(split_str)
            self.calc_add(split_str)
            #print(split_str)
            self.calc_sub(split_str)
            #print(split_str)
            return str(split_str[0])

        except IndexError:
            print("Error: Incorrect numin.")
        except ValueError:
            print("Error: Incorrect numbers.")

    def cast_str(self, numin):
        parenthesis = numin.count("(")
        for i in range(parenthesis):
            if not ((numin.rfind("(") - 1) < 0) and str(numin[numin.rfind("(") - 1]).isdigit():
                substr = numin[(numin.rfind("(") + 1):numin.find(")", numin.rfind("(") - 1)]
                calculated_substr = str(self.start_calc(substr))
                numin = numin.replace("(" + substr + ")", " * " + calculated_substr)
            else:
                substr = numin[(numin.rfind("(") + 1):numin.find(")", numin.rfind("("))]
                calculated_substr = str(self.start_calc(substr))
                numin = numin.replace("(" + substr + ")", calculated_substr)
        return numin

    def calc_mul(self, split_str):
        i = 1
        while i < len(split_str):
            if split_str[i] == "*":
                res = float(split_str[i - 1]) * float(split_str[i + 1])
                split_str[i] = str(res)
                split_str.pop(i + 1)
                split_str.pop(i - 1)
                i -= 2
            i += 1

    def calc_div(self, split_str):
        i = 1
        while i < len(split_str):
            if split_str[i] == "/":
                res = float(split_str[i - 1]) / float(split_str[i + 1])
                split_str[i] = str(res)
                split_str.pop(i + 1)
                split_str.pop(i - 1)
                i -= 2
            i += 1

    def calc_add(self, split_str):
        i = 1
        while i < len(split_str):
            if split_str[i] == "+":
                res = float(split_str[i - 1]) + float(split_str[i + 1])
                split_str[i] = str(res)
                #print(split_str)
                split_str.pop(i + 1)
                #print(split_str)
                split_str.pop(i - 1)
                #print(split_str)
                i -= 2
            i += 1

    def calc_sub(self, split_str):
        i = 1
        while i < len(split_str):
            if split_str[i] == "-":
                res = float(split_str[i - 1]) - float(split_str[i + 1])
                split_str[i] = str(res)
                split_str.pop(i + 1)
                split_str.pop(i - 1)
                i -= 2
            i += 1

inp = input("> ")

new_calc = calculator()
new_calc.start(inp)