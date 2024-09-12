from Bio import Entrez
Entrez.email = ''
handle = Entrez.esearch(db='nucleotide', \
                        term='"Chlamyphorus"[Organism] AND "2006/09/28"[Publication Date] : "2010/05/05"[Publication Date]')
record = Entrez.read(handle)
record['Count']

print(record)
