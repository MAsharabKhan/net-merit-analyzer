import csv
from datetime import date

#defiine a function to validate the input for subject scores
def correct_input(upper_limit, sub_score, sub):
    while True:
        sub_score=input(f"\n{sub} Score (Out of {upper_limit}): ")
        try:
            sub_score=int(sub_score)
        except ValueError:
            print("\nPlease enter a valid number.")
            continue
        if sub_score>=0 and sub_score<=upper_limit:
            return sub_score
        else:
            print(f"\n(Enter a valid value between 0 and {upper_limit})")

#define variables to store the scores for each subject and the date of the mock test
math_score=0
phy_score=0
eng_score=0
Maths_string="Maths"
Physics_string="Physics"
English_string="English"
mock_date=date.today().isoformat()

#call the correct_input function for each subject to get the scores from the user
correct_input(100, math_score, Maths_string)
correct_input(60, phy_score, Physics_string)
correct_input(40, eng_score, English_string)

#take input for the time taken to complete the mock test and validate it
while True:
    time_taken=int(input("\nTime Taken (in minutes): "))
    try:
        time_taken=int(time_taken)
    except ValueError:
        print("\nPlease enter a valid time between 1 and 120 minutes")
        continue
    if time_taken>=1 and time_taken<=120:
        break
    else:
        print("\nEnter a valid time between 1 and 120 minutes.")

#write the scores and time taken to a CSV file named "mocks.csv"
with open("mocks.csv", mode="a", newline="", encoding="utf-8") as file:
    writer=csv.writer(file)
    writer.writerow([mock_date, math_score, phy_score, eng_score, time_taken])
