import numpy as np 
import chili_object

Numofchili = int(input("\nEnter the amount of chili's in contest: "))

chilis = list()
for i in range(Numofchili):
    chilis.append(chili_object.chili(i+1,0,0,0,0,0))

fin = False
loop_count = 0
while fin == False: 
    for i in range(len(chilis)):
        print("\nChili", chilis[i].name)
        look_score = int(input("Enter Look Score: "))
        taste_score = int(input("Enter Taste Score: "))
        flavor_score = int(input("Enter Flavor Score: "))
        aroma_score = int(input("Enter Aroma Score: "))
        heat_score = int(input("Enter Heat Score: "))
        chilis[i].look += look_score
        chilis[i].taste += taste_score
        chilis[i].flavor += flavor_score
        chilis[i].aroma += aroma_score
        chilis[i].heat += heat_score
    
    loop_count += 1

    endloop = input("\nAre you done entering in scores? (Y/n) ")

    if endloop == 'Y':
        fin = True
    else:
        continue

totals = list()
for i in range(len(chilis)):
    totals.append(chilis[i].total())

max_value = max(totals)
max_index = totals.index(max_value)
print("\nChili with highest overall score is chili", chilis[max_index].name)