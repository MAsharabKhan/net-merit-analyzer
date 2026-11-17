import math

ssc=float(input("What is your SSC/10th marks?\n"))
hssc=float(input("\nWhat is your HSSC/1st Year marks?\n"))
nscore=float(input("\nWhat is your NET Score?\n"))

aggregate=((ssc/1200)*10)+((hssc/550)*15)+((nscore/200)*75)
print(math.trunc(aggregate*100)/100)