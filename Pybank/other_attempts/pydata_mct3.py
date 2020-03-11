import os
import csv
csvpath = os.path.join('..','Pybank_Resources', 'PyBank__data.csv')
month = []
profit_loss=[]
greatest_increase =0
greatest_descrease =0
monthly_change = []
prev_value = 0
new_value =0
greatest_value = 0
evenlist =[]

monthly_dict={}


with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    
    
    
    csv_header = next(csvreader)
 
    for row in csvreader:
       # print(row)
        month.append(row)
        length_month = len(month)

#list comprehension to convert string into int
      #  profit_loss = [int(i) for i in profit_loss]
        

        profit_loss.append(int(row[1]))
        current_value = int(row[1])
        new_value =  current_value - prev_value  
        prev_value = current_value
        monthly_change.append(new_value)
       
        monthly_dict[row[1]]=row[0]

    
        
       

        


   
# code includes the first value 867884, So had to omit that value and decrease length by 1 (85 instead of 86 months)
average_change = sum(monthly_change[1:])/((len(monthly_change)-1))

total_profit = sum(profit_loss)  
#print(str(max(monthly_change)))

#     total_profit = sum(profit_loss), need to create a new list, append new vvalues then get the average
print( "Financial Analysis")
print("--------------------------")
print(f'Total Months : {length_month}')
print(f'Total: ${total_profit}')
print(f'Average Change: {(str(round(average_change,2)))}')





