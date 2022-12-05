import random
import time
from itertools import combinations
class gaming:
    def __init__(self):
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
        self.answer_key = set()
        for x in range(0, 16, 2):
            temp_list.append(temp[x])
            temp_list.append(temp[x+1])
            self.answer_key.add(frozenset(sorted(temp_list)))  
            temp_list = [] 
        
        #creates a start list, shuffles to be fair
        self.start_list = random.sample(temp, 16)
        
        #makes all possible combinations
        self.pairs = set(combinations(self.start_list, 2)) 
        
        #creates the start weeks and answer set
        self.weeks = 0
        self.my_ans = []

    def run(self, pos_solutions = None):
        #creates initial test case- just all pos solutions to begin with
        if pos_solutions is None:
            pos_solutions = self.pairs.copy()
        #base case- if answer key has 8 pairs (so 16 people), returns weeks taken
        if len(self.my_ans) == 8:            
            return self.weeks
        
        #copies pos solutions to avoid set modify error- iterates through possible combinations
        for x in pos_solutions.copy():            
            #if pos solution is correct, adds to answer key
            self.weeks += 1
            if set(x) in self.answer_key:
                self.my_ans.append(x)
                #scans through the pairs remaining and if either of the options are in a possible pair removes
                #removes as it cannot be a possible combination if it is known to be correct with another person
                for y in self.pairs.copy():
                    if x[0] in y or x[1] in y:
                        self.pairs.remove(y) 
                #recursively calls funtion with newer shortened list
                return self.run(self.pairs) 
            else:
                #can just 
                self.pairs.remove(x) 




n_trials = 1000
avg_weeks = 0
avg_time = 0
for x in range(n_trials):
    start = time.time() 
    
    test = gaming()
    avg_weeks += test.run()
    
    end = time.time() 
    avg_time += end - start



print(f"Avg weeks is {avg_weeks/n_trials}, for {n_trials} trials")
print(f"Avg time is {avg_time/n_trials}, for {n_trials} trials")
