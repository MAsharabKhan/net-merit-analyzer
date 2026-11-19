import csv
from datetime import date

def correct_input(upper_limit, sub_score, sub):
    value=int(0)
    while value==0:
        sub_score=int(input(f"{sub} Score (Out of {upper_limit}): "))
        if sub_score>=0 and sub_score<=upper_limit:
            value=1
        else:
            value=0
            print(f"\n(Enter a valid value between 0 and {upper_limit})")

value=0
math_score=0
phy_score=0
eng_score=0
Maths="Maths"
Physics="Physics"
English="English"
mock_date=date.today().isoformat()


correct_input(100, math_score, Maths)
correct_input(60, phy_score, Physics)
correct_input(40, eng_score, English)

while value==0:
    time_taken=int(input("\nTime Taken (in minutes): "))
    if time_taken>=1 and time_taken<=120:
        value=1
    else:
        value=0
        print("\nEnter a valid time between 1 and 120 minutes.")

with open("mocks.csv", mode="a", newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow([mock_date, math_score, phy_score, eng_score, time_taken])