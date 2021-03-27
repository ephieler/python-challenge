#import modules
import os
import csv

#find and read csv file
filename = 'election_data.csv'
csvpath = os.path.join('Resources', filename)

#open csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csv_reader)

    #set variables & lists
    total_votes = 0
    candidates = []
    candidates_votes = []

    #loop through all rows in csv
    for row in csv_reader:

        #add 1 to the total vote count
        total_votes += 1

        #see if the candidate has been added to the candidate list yet:
        #if not then add name to list and add a new counter to the votes list
        #if so then just add 1 to the coresponding vote counter
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes.append(1)
        else:
            index = candidates.index(row[2])
            candidates_votes[index] = candidates_votes[index] + 1

#set variables & lists
vote_percent = []
maxvotes = 0
winner = ""

#loop through the number of candidates in the candidates list
for i in range(len(candidates)):
    #take the candidates votes and divide by total votes *100 to get a percentage and add the percentage to a list
    percentage = round(candidates_votes[i]/total_votes*100, 2)
    vote_percent.append(percentage)
    #check and see if the candidates votes are more than the max votes if so set that as the max votes
    #if the candidates votes match the maxvotes then set them as the winner
    if candidates_votes[i] > maxvotes:
        maxvotes = candidates_votes[i]
    if candidates_votes[i] == maxvotes:
        winner = candidates[i]

#print results in the terminal
print()
print("Election Results")
print("----------------------")
print(f"Total Votes: {total_votes}")
print("----------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {vote_percent[i]}% ({candidates_votes[i]})")
print("----------------------")
print(f"Winner: {winner}")
print("----------------------")
print()

#set name and path for output file
output_filename = 'Poll Results.txt'
output_path = os.path.join('Analysis', output_filename)

#create text file, print analysis, and save
output = open(output_path, "x")

output.write("\n")
output.write("Election Results\n")
output.write("----------------------\n")
output.write(f"Total Votes: {total_votes}\n")
output.write("----------------------\n")
for i in range(len(candidates)):
    output.write(f"{candidates[i]}: {vote_percent[i]}% ({candidates_votes[i]})\n")
output.write("----------------------\n")
output.write(f"Winner: {winner}\n")
output.write("----------------------\n")
