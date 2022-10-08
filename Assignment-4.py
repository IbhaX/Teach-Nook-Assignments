from random import choice
from time import sleep
from string import Template

female = ["attractive", "beautiful", "dazzling", "elegant", "fancy", "gorgeous", "magnificent", "shapely"]

male = ["handsome", "muscular", "fit", "glamorous", "stocky", "chubby",]

points = {
        "1": ["1.2", "little to no exercise"],
        "2": ["1.37", "slightly active person 1-3 days of exercise a week"],
        "3": ["1.55", "moderately active person 3-5 days of exercise a week"],
        "4": ["1.725", "very active person 6-7 days of exercise a week"],
        "5": ["1.9", "extra active person"]
    }

def Decimals(func):
    def wrapper(*args, **kwargs):
        out, status = func(*args, **kwargs)
        return float(str(f"{out:.2f}")), status
    return wrapper

def Print(string, speed=3):
    for i in string:
        print(i, flush=True, end="")
        sleep(speed/100)
        
def Typewrite(speed=5):
    def wrapper(func):
        def inner(*args, **kwargs):
            for i in func(*args, **kwargs):
                print(i, flush=True, end="")
                sleep(speed/100)
        return inner
    return wrapper

class Check:
    def __init__(self, weight, height, age, point=1):
        self.weight = weight
        self.height = height
        self.age = age
        self.point = point
     
    @Decimals
    def BMR(self, sex):
        if sex == "male":
            burned_cal = int(66 + (6.2 * self.weight) + (12.7 * self.height) - (6.76 * self.age)) * self.point
            
        elif sex == "female":
            burned_cal = int(655.1 + (4.35 * self.weight) + (4.7 * self.height) - (4.7 * self.age)) * self.point
        else:
            burned_cal = 0
        return float(burned_cal), None
    
    @Decimals
    def BMI(self):
        bmi = float(self.weight / (self.height/100)**2)
        status = None
        
        if bmi < 18.5:
            status = "underweight"
        elif bmi >= 18.5 and bmi <= 24.9:
            status = "normal"
        elif bmi >= 25 and bmi <= 29.9:
            status = "overweight"
        elif bmi >= 30:
            status = "obese"
            
        return bmi, status

@Typewrite(3)
def main():
    
    Print("Hello there...\n")
    Print("Please enter your name: ")
    name = input()
    Print("Please enter your age: ")
    age = int(input())
    Print("Enter your height in cm: ")
    height = int(input())
    Print("Enter your weight in kg: ")
    weight = int(input())
    Print("Enter your gender (male or female): ")
    sex = input()
    Print("Enter your activity scale: ")
    for key, value in points.items():
        Print(f"\n{key}. {value[1].capitalize()}")
    print() 
    Print("Enter Scale: ")
    point = int(input())
    point = float(str(points[f"{point}"][0]))
    check = Check(weight, height, age, point=point)
    
    bmi, status = check.BMI()
    bmr = check.BMR(sex)
    gender = male if sex == "male" else "female"
    temp = Template("Hello there $adj $name. Your BMI status is $status , score is $bmi and $bmr is your average BMR score...")
    data = temp.substitute(adj = choice(gender), name=name, status=status, bmi=bmi, bmr=bmr[0])
    print()
    return data

if __name__ == "__main__":
    main()



