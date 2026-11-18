import math

ssc=float(input("What is your SSC/10th marks?\n"))
hssc=float(input("\nWhat is your HSSC/1st Year marks?\n"))
nscore=float(input("\nWhat is your Mock NET Score?\n"))

aggregate=((ssc/1200)*10)+((hssc/550)*15)+((nscore/200)*75)
print(f"\nYou have achieved {math.trunc(aggregate*100)/100}% out of a toal of 25% in 10th & 1st Year.")

needed_net_score=int((79-((ssc/1200)*10)-((hssc/550)*15))/0.375)
print(f"\nYou need \033[5m{needed_net_score}\033[0m Marks/MCQs Correct in NET to match the aggregate cutoff for SEECS.")
print("\n")
