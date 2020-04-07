# Operating system and csv import
import os
import csv

# Path for cvs file
csvpath = os.path.join('Resources/election_data.csv')



# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")


#Candidate variables listed

    candidate1 = "Khan" 
    candidate2 = "Correy"
    candidate3 = "Li"
    candidate4 = "O'Tooley"


    #Starting number of votes set for each candidate
    initialvotes1 = 0
    initialvotes2 = 0
    initialvotes3 = 0
    initialvotes4 = 0



    # Total votes by candidate
    for row in csvreader:
        if row[2] == candidate1:
            initialvotes1 = initialvotes1 + 1
        elif row[2] == candidate2:
            initialvotes2 = initialvotes2 + 1
        elif row[2] == candidate3:
            initialvotes3 = initialvotes3 + 1
        elif row[2] == candidate4:
            initialvotes4 = initialvotes4 + 1


    #total votes is equal to the sum of initial votes 1,2,3,4

    totalvotes = initialvotes1 + initialvotes2 + initialvotes3 + initialvotes4

    #Calculate vote percentages to 3 digits rounding to the nearest tenth

    khanpercentage = round((initialvotes1/totalvotes)*100,3)
    correypercentage = round((initialvotes2/totalvotes)*100,3)
    lipercentage = round((initialvotes3/totalvotes)*100,3)
    otooleypercentage = round((initialvotes4/totalvotes)*100,3)
    
    #The Election Results are:
    print ("Election Results:")
    print("Total Votes:" + str(totalvotes))
    print("Khan:" + str(khanpercentage) + '%' + ' ' + '(' + str(initialvotes1) + ')')
    print("Correy:" + str(correypercentage) + '%' + ' ' + '(' + str(initialvotes2) + ')')
    print("Li:" + str(lipercentage) + '%' + ' ' + '(' + str(initialvotes3) + ')')
    print("Otooley:" + str(otooleypercentage) + '%' + ' ' + '(' + str(initialvotes4) + ')')

    if initialvotes1 > initialvotes2 and initialvotes1 > initialvotes2 and initialvotes1 > initialvotes4:
        print ("Winner: Khan")
    elif initialvotes2 > initialvotes1 and initialvotes2 > initialvotes3 and initialvotes2 > initialvotes4:
        print ("Winner: Correy")
    elif initialvotes3 > initialvotes1 and initialvotes3 > initialvotes2 and initialvotes3 > initialvotes4:
        print ("Winner: Li")
    elif initialvotes4 > initialvotes1 and initialvotes4 > initialvotes2 and initialvotes4 > initialvotes3:
        print ("Winner: O'Tooley")

# Produce txt file as result of election
exportpath = ("Results.txt")
with open(exportpath, "w") as textfile:
        textfile.write(f"Election Results:")
        textfile.write(f"Total Votes:" + str(totalvotes))
        textfile.write(f"Khan:" + str(khanpercentage) + '%' + ' ' + '(' + str(initialvotes1) + ')')
        textfile.write(f"Correy:" + str(correypercentage) + '%' + ' ' + '(' + str(initialvotes2) + ')')
        textfile.write(f"Li:" + str(lipercentage) + '%' + ' ' + '(' + str(initialvotes3) + ')')
        textfile.write(f"Otooley:" + str(otooleypercentage) + '%' + ' ' + '(' + str(initialvotes4) + ')')

