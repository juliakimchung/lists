import random

random_numbers = random.sample(range(49), 22)
print(random_numbers)


squared_ints = [num**2 for num in random_numbers ]
	
print(squared_ints)	
