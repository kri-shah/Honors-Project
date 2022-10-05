import random
import time
from collections import OrderedDict

#copied list of names from random name generator
names = ['Stephanie Robinson', 'Brad Rodriguez', 'Ryan Ward', 'Katherine Morales', 'Brian Davis', 'Kendra Pope', 'April Carey', 'Brittany Chavez', 'Alexandra Johnson', 'Michael Bell', 'David Brown', 'Gregory Brewer', 'Alexandra Coleman', 'Steven Davis', 'Kristen Taylor', 'Kristine Woods', 'Jennifer Collins', 'Justin Cobb', 'Kelsey Rodriguez', 'Sara Russell', 'Stephanie Jones', 'Joseph Foster', 'Dr. James Murphy', 'Henry Davis', 'Kenneth Price', 'Tricia White', 'James Gates', 'Heather Moore', 'Lori Knox', 'Lauren Thompson', 'Amber Avila', 'Dalton Anthony', 'Jessica Simmons', 'Natalie Horn', 'Nicole Bryan', 'Dennis Williams', 'Shannon Carter', 'Connie Lee', 'Mark Everett', 'Robert Buck', 'Emily Clarke', 'Christopher Brown', 'Megan Turner', 'Elizabeth Price', 'April Edwards', 'Lonnie Woodward', 'Denise West', 'Frank Manning', 'John Powell', 'Timothy Gilmore']


#creating set with all people, uses set to avoid duplicates 
people = set()
while len(people) < 16:
    people.add(names[random.randint(0, 49)])

#creates list of names, creates answer dictionary 
temp = list(people) 
answer_key = {}
for x in range(0, 16, 2):
    answer_key.update({temp[x]: temp[x+1]})

#shuffles list to be "fair"- this will be the list that we pull random samples from 
start_list = random.sample(temp, 16) 

#initializes the correct pair dictionary, the incorrect pair dictionary and weeks
correct_pairs = {}
incorrect_pairs = {}
weeks = 0
total_correct = 0
#times the module
start = time.time()
while True:
    #picks two random names
    name1 = start_list[random.randint(0, 15)]
    name2 = start_list[random.randint(0, 15)]
    
    #checks that the names aren't the same
    while name1 == name2:
        name2 = start_list[random.randint(0, 15)]

    #checks that the names aren't incorrect, nor correct, as there is no point checking
    while incorrect_pairs.get(name1) == name2 or incorrect_pairs.get(name2) == name1 or correct_pairs.get(name1) == name2 or correct_pairs.get(name2) == name1:
        name1 = start_list[random.randint(0, 15)]
        name2 = start_list[random.randint(0, 15)] 

    #checks if name is in answer dictionary, if it is/isnt updates dictionary
    if answer_key.get(name1) == name2 or answer_key.get(name2) == name1:
        correct_pairs.update({name1: name2}) 
        total_correct += 1
    else:
        incorrect_pairs.update({name1: name2}) 

    #if all pairs have been found, break 
    if total_correct == 8:
        break 
    
    #incriment weeks by 1
    weeks +=1 

end = time.time()

print("_"*50)
print(f"Correct pair dictionary: {answer_key}")
print("_"*50)
print(f"My dictionary: {correct_pairs}") 
print("_"*50)
print(f"weeks {weeks}")
print("_"*50)
print(f"Time {end - start} seconds") 
