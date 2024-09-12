from Bio import Entrez
from Bio import SeqIO

Entrez.email = ""
handle = Entrez.efetch(db="nucleotide", id=["JX428803, JX308817, JQ342169, NM_204821, JX393321, BT149867, NM_001266228, JN573266, NM_001246828"], rettype="fasta")
records = list(SeqIO.parse(handle, "fasta"))
