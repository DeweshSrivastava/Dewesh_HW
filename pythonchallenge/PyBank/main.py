import csv
import os 

#The path to the CSV file
filePath = "Resources/budget_data.csv"
# Read in the CSV file
with open(filePath, newline='') as file:
   
   months =[]
   monPrftRLs = []
   csvReader = csv.reader(file, delimiter=',')
   # Read the header row first 
   csv_header = next(csvReader)
   #Iterate through the file and save the values into a list for easier manipulation
   for row in csvReader:
      months.append(row[0])
      monPrftRLs.append(int(row[1]))
total_profits_Iosses = 0
monthlyChange = list()
for i in range(len(monPrftRLs)):
   total_profits_Iosses = total_profits_Iosses + monPrftRLs[i]
   if i != 0: 
      monthlyChange.append( monPrftRLs[i] - monPrftRLs[i-1])

print(f"Total profits/losses is {total_profits_Iosses}")
averageChange = sum(monthlyChange)/len(monthlyChange) 
print(f"Average change is {averageChange}")

maxIncreaseMonth = months[monthlyChange.index(max(monthlyChange))+1]
print(f"The greatest increase is {maxIncreaseMonth}  {max(monthlyChange)}")
maxDecreaseMonth = months[monthlyChange.index(min(monthlyChange))+1]
print(f"The greatest decrease is {maxDecreaseMonth}  {min(monthlyChange)}")
#Writing to the file
outputFile = open("PyBankOutput.txt", "w")
outputFile.write(f"Total profits/losses is {total_profits_Iosses}\n")
outputFile.write(f"Average change is {averageChange}\n")
outputFile.write(f"The greatest increase is {maxIncreaseMonth}  {max(monthlyChange)}\n")
outputFile.write(f"The greatest decrease is {maxDecreaseMonth}  {min(monthlyChange)}\n")