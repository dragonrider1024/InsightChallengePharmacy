#! /usr/bin/python
from drug import Drug
import sys
from csv import reader,writer

class Solution:
  
  def readInput(self, fileInput):
    '''read input line by line'''
    columnNames = {"id":0, "prescriber_last":1, "prescriber_first":2, "drug_name":3, "drug_cost":4}
    try:
      columnValueString = next(fileInput)
    except StopIteration:
      return None
    entryid = columnValueString[columnNames["id"]]
    last = columnValueString[columnNames["prescriber_last"]]
    first = columnValueString[columnNames["prescriber_first"]]
    drug_name = columnValueString[columnNames["drug_name"]]
    drug_cost = columnValueString[columnNames["drug_cost"]]
    return (entryid, last, first, drug_name, drug_cost)


  def worker(self):
    '''worker function to store a list of drug, and sort them'''
    fileInput = reader(open(sys.argv[1], "r"), delimiter=',')
    fileOutput = writer(open(sys.argv[2], "w+"), delimiter=',')
    rowItem = self.readInput(fileInput) # skip the header
    rowItem = self.readInput(fileInput)
    drugList = []
    drugDict = {}
    drugPrescriberDict = {}
    while rowItem != None:
       entry_id, last, first, drug_name, drug_cost = rowItem
       drug_cost = int(float(drug_cost))
       if drug_name not in drugDict:
         drug = Drug(drug_name, 1, drug_cost)
	 drugList.append(drug)
         drugDict[drug_name] = len(drugList) - 1 
         drugPrescriberDict[(drug_name, last, first)] = len(drugList) - 1
       else:
         if (drug_name, last, first) not in drugPrescriberDict:
           drugindex = drugDict[drug_name]
           drug = drugList[drugindex]
           drug.num_pres += 1
           drug.total_cost += drug_cost
           drugPrescriberDict[(drug_name, last, first)] = drugindex
         else:
           drugindex = drugDict[drug_name]
           drug = drugList[drugindex]
	   drug.total_cost += drug_cost
       rowItem = self.readInput(fileInput)

    drugList.sort(reverse = True)
    self.saveOutput(drugList, fileOutput)

  def saveOutput(self, drugList, fileOutput):
    header = ["drug_name","num_prescriber","total_cost"]
    fileOutput.writerow(header)
    for i in range(len(drugList)):
       item = drugList[i]
       fileOutput.writerow([item.drug_name, item.num_pres, item.total_cost])

if __name__ == "__main__":
  sol = Solution()
  sol.worker()
