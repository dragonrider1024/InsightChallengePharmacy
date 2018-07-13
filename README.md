# A drug object contains the total cost for that drug, drug's name, and number of prescribers
# Traverse through the row of input file. If we find a new drug, we create a drug object, with total cost as the row's total cost entry, number of prescriber as 1. We then add the drug object to a drugList. We also keep a dictionary with drugname as key, and drug object's index in the list as value.
# If the drug is already been found, we check whether the prescriber for this drug is already found. If not, we increase the number of prescribers for that drug object. We also need to increase the drug object's total cost
# If yes, we only increase the drug object's total cost. While the number of prescribers is not changed.
# The drug object implements comparators, such as <, >, ==, <=, and >=.
# We sort the drugList in reverse order.
# We output the drugList item by item.
