# Honors-Project

Control Algorithm:
Avg weeks is 271.68, for 1000 trials
Avg time is 0.0004553084373474121, for each trial

This algorithm has been the same since the beginning, it randomly sends 2 pairs to the truth booth, and if it is correct it adds it to an answer list, and if incorrect it adds it to an incorrect list to make sure that we aren't wasting a week by testing 2 pairs that have already been tested. 

Better Control algorithm:
Avg weeks is 106.698, for 1000 trials
Avg time is 0.0000253560543060302, for each trial

This was an unplanned algorithm. I was thinking and thought that instead of randomly sending 2 people to the truth booth, I could create every possible pair (so 120 different combinations) and then from this list, send pairs to the truth booth. This works much better than the control algorithm, effectively cutting the amount of weeks in 1/3. This makes sense, as in the worst case this algorithm can take 120 weeks (because in a list of 16 there are only 120 different combos of people (formula down below)). 

Better Better Control Algorithm:
Avg weeks is 46.063, for 1000 trials
Avg time is 0.000088866710662842, for each trial

This is quite similar to the previous algorithm, except an even better version (as shown by its name (: ). It does the same thing, except if a correct pair is sent to the truth booth, it goes through the remaining possible combinations, and removes it as an option if it has either of the people in the correct list. Ex. if (Mike, Bruce) are a pair, we can remove (Mike, Alana) as a potential pair as we know Mike is with Bruce. This cuts the number of weeks in roughly half. 
