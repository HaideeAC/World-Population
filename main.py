import csv
from matplotlib import pyplot as plt


# Create an empty dict
population_per_continent = {}

filename = r'data.csv'

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for line in reader:
        continent = line['continent']
        year = int(line['year'])
        population = int(line['population'])
       # If the continent doesn't already exists- create this structure
        if continent not in population_per_continent:
            population_per_continent[continent] = {'population':[], 'years':[]}
        # Otherwise add this information to the dict
        else:
            population_per_continent[continent]['population'].append(population)
            population_per_continent[continent]['years'].append(year)
            
print(population_per_continent)
# Plot
for continent in population_per_continent:
    years = population_per_continent[continent]['years']
    population = population_per_continent[continent]['population']