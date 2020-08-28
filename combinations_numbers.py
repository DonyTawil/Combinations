# Used this to turn the file into exe https://dev.to/eshleron/how-to-convert-py-to-exe-step-by-step-guide-3cfi

from itertools import combinations
import pprint


numbers = []
nbr = 0
while nbr < 6:
    print("Please give a number between 1 and 19, so far you have given us %d numbers"%nbr)
    num = input(">:")
    try:
        num = int(num)
        if num < 1 or num > 19:
            print("what you gave is not a number between 1 and 19")
        
        else:
            numbers.append(num)
            nbr += 1    
    except:
        print("What you gave us is not a number, please try again")

        
        
the_combinations = combinations(numbers, 4)
the_combinations = list(the_combinations)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(the_combinations)
