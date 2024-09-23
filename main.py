import csv
from matplotlib import pyplot as plt


filename = r'data.csv'

with open(filename, 'r') as csvfile:
    reader = csv.DictReader(csvfile)