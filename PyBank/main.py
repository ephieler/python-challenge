#import modules
import os
import csv

#find and read csv file
filename = 'budget_data.csv'
csvpath = os.path.join('Resources', filename)

#open csv
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')

    #skip header
    next(csv_reader)

    #add variables
    total_months = 0
    net_profit_loss = 0
    priormonthprofitloss = 0
    maxprofit_value = 0
    maxprofit_month = ""
    minprofit_value = 0
    minprofit_month = ""
    monthlychanges = []
  
    #go through every line in csv
    for row in csv_reader:

        #add 1 to the month count
        total_months += 1
        #add to the net profit/loss count
        net_profit_loss += int(row[1])
        
        #add monthly profit change to monthly changes, (skip the first month because there is no previous month)
        if total_months == 1:
            pass
        elif total_months > 1: 
            monthlychanges.append(int(row[1]) - priormonthprofitloss)

        #check and track the highest gain and lowest loss
        if int(row[1]) - priormonthprofitloss > maxprofit_value:
                maxprofit_value = int(row[1]) - priormonthprofitloss
                maxprofit_month = f"{row[0]}"
        elif int(row[1]) - priormonthprofitloss < minprofit_value:
                minprofit_value = int(row[1]) - priormonthprofitloss
                minprofit_month = f"{row[0]}"
        else:
            pass
            
        #track the monthly change
        priormonthprofitloss = int(row[1])

    #calculate mean profit change for all months
    averagechange = round(sum(monthlychanges)/len(monthlychanges), 2)

#print analysis results in terminal
print()
print("Financial Analysis")
print("-------------------------------")
print(f"Total Months : {total_months}")
print(f"Total: ${net_profit_loss}")
print(f"Average Change: ${averagechange}") 
print(f"Greatest Increase in Profits: {maxprofit_month} $({maxprofit_value})")
print(f"Greatest Decrease in Profits: {minprofit_month} $({minprofit_value})")
print()

#set name and path for output file
output_filename = 'Financial Analysis.txt'
output_path = os.path.join('Analysis', output_filename)

#create text file, print analysis, and save
output = open(output_path, "x")

output.write("\n")
output.write("Financial Analysis\n")
output.write("-------------------------------\n")
output.write("\n")
output.write(f"Total Months : {total_months}\n")
output.write(f"Total: ${net_profit_loss}\n")
output.write(f"Average Change: ${averagechange}\n") 
output.write(f"Greatest Increase in Profits: {maxprofit_month} $({maxprofit_value})\n")
output.write(f"Greatest Decrease in Profits: {minprofit_month} $({minprofit_value})\n")
