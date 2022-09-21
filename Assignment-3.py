# Teachnook Assignment - 3
from datetime import datetime as dt
from os import system
from time import sleep

import sys


def Print(s):
  for i in s:
    sys.stdout.write(i)
    sys.stdout.flush()
    sleep(0.3/10)

class Calc:
    """ Simple calculation functions"""
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def add(self):
        """ addition - returns num1 + num2 """
        return self.num1 + self.num2
    
    def sub(self):
        """ subtraction - returns num1 - num2 """
        return self.num1 - self.num2
    
    def div(self):
        """ division - returns num1 / num2 """
        return self.num1 / self.num2
    
    def mul(self):
        """ multiplication - returns num1 * num2 """
        return self.num1 * self.num2

def calculator():
    """ user input function """
    log = ""
    while True:
        timestamp = dt.now()
        timestamp = timestamp.strftime("%B %d, %Y @%-I:%M")
        output = 0
        try:
            num1 = input("Enter first num: ")
            if num1 in ["exit", "x"]:
                break
            elif num1 in ["log", "logs"]:
                try:
                    with open("calc.log", "r") as f:
                        data = f.read()
                        data = data if data else "No Logs Found!"
                        print(data)
                        continue
                except FileNotFoundError:
                    print("No Logs Found!")
                    continue
                
            num1 = int(num1)
            num2 = int(input("Enter second num: "))
        except ValueError:
            print("Value Error... Use Integers for calculation...")
            break
            
        op = """1. addition\n2. subtraction\n3. multiplication\n4. division\n5. log\n6. clear screen\n7. exit"""
        
        op = input(f"{op}\noperation: ")
        calc = Calc(num1, num2)
        add = ["1", "addition", "add"]
        sub = ["2", "subtraction", "sub"]
        mul = ["3", "multiplication", "mul"]
        div = ["4", "division", "div"]
        if op in add:
            output = calc.add()
            op = "+"
            print(f"{output:.2f}")
        
        elif op in sub:
            output = calc.sub()
            op = "-"
            print(f"{output:.2f}")
        
        elif op in mul:
            output = calc.mul()
            op = "*"
            print(f"{output:.2f}")
        
        elif op in div:
            output = calc.div()
            op = "/"
            print(f"{output:.2f}")
        
        elif op in ["5", "log"]:
            try:
                with open("calc.log", "r") as f:
                    data = f.read()
                    
                    # checks if value of data is None, if its none it prints "No Logs Found!"
                    data = data if data else "No Logs Found!"
                    print(data)
            except FileNotFoundError:
                print("No Logs Found!")
        
        elif op in ["6", "cls", "clear"]:
                system("clear")
                continue
                
        elif op in ["7", "exit", "x"]:
            break
        
        else:
            print("Enter valid input!!")
            continue
        
        if op not in [add + sub + mul + div][0]:
            data = f"{num1} {op} {num2} = {output}\t({timestamp})"
        else:
            data = None
        
        log += f"{data}\n"
    return log

def main():
    """ Executes calculator function and saves it to log file 
Functions:
- addition
- subtraction
- division
- multiplication
- save history
- view history
- clear screen"""
    Print("Simple Calculator".center(50))
    print()
    data = calculator()
    if data:   
        with open("calc.log", "a+") as f:
            f.write(data)

if __name__ == "__main__":
    main()
