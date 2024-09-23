import csv
from matplotlib import pyplot as plt

def generate_population_dict_from_csv(filename):
    """Generate population dict from csv data
      Return a dict we can go through and export the data needed"""
# Create an empty dict
    output = {}


    with open(filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        for line in reader:
            continent = line['continent']
            year = int(line['year'])
            population = int(line['population'])
            # If the continent doesn't already exists- create this structure
            if continent not in output:
                output[continent] = {'population':[], 'years':[]}
            # Otherwise add this information to the dict
            else:
                output[continent]['population'].append(population)
                output[continent]['years'].append(year)
                
    return output

def generate_plot_from_dictionary(population_dict):
    """Generate the population plots frim a dictionary
      One plot per continent"""
    for continent in population_per_continent:
        years = population_per_continent[continent]['years']
        population = population_per_continent[continent]['population']
        plt.plot(years, population, label=continent, marker='o', alpha=0.5)

    plt.title("Internet population per continent")
    plt.ylabel("Year")
    plt.xlabel("Internet users")
    plt.legend()
    plt.grid(True)

    plt.show()

filename = r'data.csv'

# Display internet population in a plot
population_per_continent = generate_population_dict_from_csv(filename)
generate_plot_from_dictionary(population_per_continent)
