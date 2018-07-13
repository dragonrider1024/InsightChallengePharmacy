#! /usr/bin/python

class Drug:
  ''' drug class contains the drug name, number of prescribers, and total cost'''

  def __init__(self, drug_name, num_prescriber = 0, total_cost = 0):
    self.drug_name = drug_name
    self.num_pres = num_prescriber
    self.total_cost = total_cost


  def __str__(self):
    return self.drug_name + ',' + str(self.num_pres) + ',' + str(self.total_cost)


  def __hash__(self):
    return self.drug_name.__hash__()


  def  __lt__(self, other):
     if self.total_cost < other.total_cost:
       return True
     elif self.total_cost > other.total_cost:
       return False
     else:
       return self.drug_name > other.drug_name

  def __eq__(self, other):
     return (self.total_cost == other.total_cost) and (self.drug_name == other.drug_name)

  def __gt__(self, other):
     if self.total_cost > other.total_cost:
       return True
     elif self.total_cost < other.total_cost:
       return False
     else:
       return self.drug_name < other.drug_name

  def __le__(self, other):
     if self.__lt__(other) or self.__eq__(other):
       return True 
     else:
       return False

  def __ge__(self, other):
     if self.__gt__(other) or self.__eq__(other):
       return True
     else:
       return False

if __name__ == "__main__":
   drug1 = Drug("drug1", 2, 1000)
   drug2 = Drug("drug2", 1, 1500)
   drug3 = Drug("durg3", 4, 500)
   drug4 = Drug("drug4", 1, 1500)
   drug5 = Drug("drug5", 5, 1500)
   drugDict = {}
   drugDict[drug1] = 0
   drugDict[drug2] = 1
   print drug1 < drug2, drug1 > drug2, drug1 == drug2, drug1 < drug3, drug1 > drug3, drug1 == drug3
   print drug1
   print drug2
   print drug2 > drug4, drug2 < drug4, drug2 == drug4
   print drug2 > drug5, drug2 < drug5, drug2 == drug5
   for key in drugDict:
     print key, drugDict[key]
