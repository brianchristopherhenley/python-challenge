# Import operating system and csv file
import os
import csv
#Create a path to import the csv from its parent folder Resources
csvpath = os.path.join("Resources/budget_data.csv")
# Opening up CSV path as a reader of the file
with open (csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader, None)

#Open path to reader and cvs file:
#    lines = csv_reader.read()


# The number of months
# 1. lists made to store months and profit
    months = []
    profit = []

    for row in csv_reader:
        months.append(row[1])
        profit.append(int(row[1]))

    total_months = len(months)
    print (f"Total Months: {total_months}")

# Calculate profit and loss for each and every month
# to get revenues
    revenues = 0
    i = 1
    for i in range(total_months):
        revenues = revenues + int(profit[i])
    print (f"Total: ${revenues}")

# Retrieve Average month's donation
# 1. find change per month in profit/loss
    change = []
    j = 0
    k = 0

    for j in range (1, total_months):
        if j == 0:
            change.append(0)
        else:
            change.append(int(profit[j])-int(profit[k]))
            k += 1
    #print (change)
# sum the monthly changes and divide by total_months
    average_month = ((sum(change))/(len(change)))
    print (f"Average Change: ${round((average_month),2)}")
   
# greatest increase: profits
    max_change = max(change)
    print (f"Greatest Increase in Revenues: ${max_change}")
# greatest decrease: profits
    min_change = min(change)
    print (f"Greasest Decrease in Revenues:  ${min_change}") 
# Text produced
exportpath = ("Results.txt")
with open(exportpath, "w") as textfile:
        textfile.write(f"Total Months: {total_months}")
        textfile.write(f"Total: ${revenues}")
        textfile.write(f"Average Change: ${round((average_month),2)}")
        textfile.write(f"Greatest Increase in Revenues: ${max_change}")
        textfile.write(f"Greasest Decrease in Revenues:  ${min_change}")