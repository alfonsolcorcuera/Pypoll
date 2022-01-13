# The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#import csv
#import os
#file_to_load = os.path.join("Resources","election_results.csv")
#with open(file_to_load) as election_data:
    #print(election_data)

import csv
# Assign a variable to load file from a path.
file_to_load = "C:/Users/acorcuera/Desktop/Data Science/02. Modules/04. Python/Resources/election_results.csv"
election_data = open(file_to_load,'r')
# Assign a variable to save the file to a path.
file_to_save = "C:/Users/acorcuera/Desktop/Data Science/02. Modules/04. Python/analysis/election_analysis.txt"
# Using the with statement open the file as a text file

# 1.  Initialize a total vote counter.
total_votes = 0

#Declare a Candidate Options list
candidate_options =[]

#Open the election results and read the file.
with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   
   #Read the header row.
   headers = next(file_reader)

   #Print each row in the CSV file.
   for row in file_reader:
       #2. Add to the total vote count.
       total_votes +=1      
        
        # Print the candidate
       candidate_name=row[2]
       
       # If the candidate does not match any existinf candidate..
       if candidate_name not in candidate_options:
       # Add the candidate name to the candidate list.
        candidate_options.append(candidate_name)

       print(candidate_options)

   

































    #Write three counties to the file.
    #txt_file.write("Counties in the election\n")
    #txt_file.write("--------------------------\n")
    #txt_file.write("Arapahoe\nDenver\nJefferson")
    




