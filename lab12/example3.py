class Dna:
  def __init__(self,string):
    self.string = string
  def count_nucleotides(self):
    
    nukleotides = {"A":0,"T":0,"G":0,"C":0}
    for nukleon in self.string:
      nukleotides[nukleon] += 1
    return nukleotides
  def calculate_complement(self):
    revers = self.string[::-1]
    chain = {"A":"T","T":"A","G":"C","C":"G"}
    for nukleon in revers:
      nukleon = chain[nukleon]
    return revers
  def count_point_mutations(self,dna):
    count = 0
    for a in range(len(dna)):
      if dna[0] == self.string[a]:
        count+=1
      a+=1
    return count 
  def find_motif(self,dna):
    location = []
    for a in range(len(dna)-len(self.string)):
      if self.string == dna[a:len(self.string)+a]:
        location.append(a)
    return location 


dna = Dna("ATAT")
print(dna.find_motif("GATATATGCATATACTT"))