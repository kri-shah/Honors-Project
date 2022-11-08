import random
import time
from itertools import combinations
def run():
    #copied list of names from random name generator
    names = ['Stephanie Robinson', 'Brad Rodriguez', 'Ryan Ward', 'Katherine Morales', 'Brian Davis', 'Kendra Pope', 'April Carey', 'Brittany Chavez', 'Alexandra Johnson', 'Michael Bell', 'David Brown', 'Gregory Brewer', 'Alexandra Coleman', 'Steven Davis', 'Kristen Taylor', 'Kristine Woods', 'Jennifer Collins', 'Justin Cobb', 'Kelsey Rodriguez', 'Sara Russell', 'Stephanie Jones', 'Joseph Foster', 'Dr. James Murphy', 'Henry Davis', 'Kenneth Price', 'Tricia White', 'James Gates', 'Heather Moore', 'Lori Knox', 'Lauren Thompson', 'Amber Avila', 'Dalton Anthony', 'Jessica Simmons', 'Natalie Horn', 'Nicole Bryan', 'Dennis Williams', 'Shannon Carter', 'Connie Lee', 'Mark Everett', 'Robert Buck', 'Emily Clarke', 'Christopher Brown', 'Megan Turner', 'Elizabeth Price', 'April Edwards', 'Lonnie Woodward', 'Denise West', 'Frank Manning', 'John Powell', 'Timothy Gilmore']

    #creating set with all people, uses set to avoid duplicates 
    people = set()
    while len(people) < 16:
        people.add(names[random.randint(0, 49)])

    #creates list of names, creates answer set of frozen sets 
    temp = list(people) 
    temp_tuple = ()
    temp_list = []
    answer_key = set()
    for x in range(0, 16, 2):
        temp_list.append(temp[x])
        temp_list.append(temp[x+1])
        answer_key.add(frozenset(sorted(temp_list)))  
        temp_list = [] 

    #shuffles list to be "fair"- this will be the list that we pull random samples from 
    start_list = random.sample(temp, 16) 
    #timing the alg
    start = time.time() 

    #neat module to make ever single combination possible
    pairs = set(combinations(start_list, 2))  
    
    #creates answer list and weeks
    my_answer = []
    weeks = 0
    #basically goes through every possible option of pairs
    for pair in pairs:
        #by default, the combinations module results in a set of tuples, this converts the tuple to a frozen set to ignore the order
        if frozenset(pair) in answer_key:
            my_answer.append(pair)
            
        
        #if all 8 pairs have been found, no need to keep checking
        if len(my_answer) == 8:
            break 
        #increase amount of weeks by 1, every iteration, as checking if a pair is together is sending a couple to
        weeks += 1
    end = time.time() 
    return [weeks, end - start]
    '''
    print("-"*50)
    for ans in my_answer:
        print(ans)
    print("-"*50)
    for ans in answer_key:
        print(ans)
    print("-"*50)
    print(weeks)
    print("-"*50)
    print(end - start)  
    '''

n_trials = 1000
avg_weeks = 0
avg_time = 0
for x in range(n_trials):
    avg_weeks += run()[0]
    avg_time += run()[1]


print(f"Avg weeks is {avg_weeks/n_trials}, for {n_trials} trials")
print(f"Avg time is {avg_time/n_trials}, for {n_trials} trials")

