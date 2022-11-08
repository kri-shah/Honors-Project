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
        
        
        self.start_list = random.sample(temp, 16)
        self.pairs = set(combinations(self.start_list, 2))
        self.weeks = 0
        self.my_ans = []
        

    def run(self, pos_solutions = None):
        if pos_solutions is None:
            pos_solutions = self.pairs
        #print(f"{pos_solutions} \n\n")
        if len(self.my_ans) == 8:
            return self.weeks 
        
        for pos in pos_solutions.copy():
            self.weeks += 1
            if frozenset(pos) in self.answer_key:
                self.my_ans.append(pos)
                t1 = pos[0]
                t2 = pos[1]
                for p in self.pairs.copy():
                    if t1 in p:
                        self.pairs.remove(p) 
                    elif t2 in p:
                        self.pairs.remove(p) 
                if len(self.my_ans) < 5:
                    self.run(self.pairs) 
                else:
                    print(f"my ans:{(self.my_ans)}   corr: {self.answer_key}")
                    return self.weeks 



n_trials = 1
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

