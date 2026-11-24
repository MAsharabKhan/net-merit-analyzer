import math

#define a function to validate the input for subject scores
def correct_input(upper_limit, level, grade):
    while True:
        ssc_marks=input(f"What is your {level}/{grade} marks?\n")
        try:
            ssc_marks=int(ssc_marks)
        except ValueError:
            print(f"\n(Please enter a valid number between 0 and {upper_limit})")
            continue
        if ssc_marks>=0 and ssc_marks<=upper_limit:
            return ssc_marks
        else:
            print(f"\n(Enter a valid number between 0 and {upper_limit})")

#define variables to store the scores for each subject and the date of the mock test
ssc_marks=correct_input(1200, "SSC", "10th")
hssc_marks=correct_input(550, "HSSC", "1st Year")
net_score=correct_input(200, "Mock NET", "Score")

#calculate the net aggregate, level aggregate, and needed net score to match the aggregate cutoff for SEECS
calc_net_aggregate=((ssc_marks/1200)*10)+((hssc_marks/550)*15)+((net_score/200)*75)
calc_level_aggregate=((ssc_marks/1200)*10)+((hssc_marks/550)*15)
calc_needed_net=int((79-((ssc_marks/1200)*10)-((hssc_marks/550)*15))/0.375)

#display the results to the user
print(f"\nYou have achieved {math.trunc(calc_level_aggregate*100)/100}% out of a total of 25% in 10th & 1st Year.\n\nYou need \033[5m{calc_needed_net}\033[0m Marks/MCQs Correct in NET to match the aggregate cutoff for SEECS.\n\nYou have achieved {math.trunc(calc_net_aggregate*100)/100}% out of a total of 100% in 10th, 1st Year & Mock NET.\n")
