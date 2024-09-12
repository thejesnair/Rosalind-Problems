import re

infile= open('test data.txt')
sequence = ''

for line in infile:
    sequence+=line


motif = re.compile(r'(?=(N[^P][S|T][^P]))') #search for overlapping patterns
count = 0
positions = []
