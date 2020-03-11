import os
import csv

csvpath = os.path.join('..','Pybank_Resources', 'PyBank__data.csv')

month=[]
prev_revenue = 0
month_of_change = []
revenue_change_list =[]
greatest_increase = ["",0]
greatest_decrease = ["",9999999999]
total_revenue = 0

with open(csvpath) as revenue_data:
    reader = csv.DictReader(revenue_data)

    for row in reader:

        month.append(row)
        length_month = len(month)
        total_revenue = total_revenue + int(row["Profit/Losses"])

        revenue_change = int(row['Profit/Losses'])- prev_revenue
        prev_revenue = int(row["Profit/Losses"])
        revenue_change_list = revenue_change_list + [revenue_change]
        month_of_change = month_of_change + [row["Date"]]

        if (revenue_change > greatest_increase[1]):
            greatest_increase[0] = row["Date"]
            greatest_increase[1] = revenue_change 

        if (revenue_change < greatest_decrease[1]):
            greatest_decrease[0] = row["Date"]
            greatest_decrease[1] = revenue_change     


average_change = (sum(revenue_change_list[1:])/ len(revenue_change_list[1:]))

average_change = round(average_change,2)

answer = (

f"\n Financial Analysis \n"
f"\n ---------------------------------\n"
f"\n Total Months: {length_month}\n"
f"\n Total : ${total_revenue}\n"
f"\n Average Change:$ {average_change}\n"
f"\n Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})\n" 
f"\n Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})\n" )

print(answer)

pybank_results = "pybank_results.txt"

with open(pybank_results,"w") as txt_file:
    txt_file.write(answer)
  