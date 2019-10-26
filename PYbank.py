import os

import csv

csvpath = os.path.join('..', 'PY homework', 'budget_data.csv')

print("Financial Analysis")
print("------------------------")


with open(csvpath)as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
    #     print(index,column_header)

    time = []
    amount = []
    for row in reader:
        month = str(row[0])
        time.append(month)
        benifit = int(row[1])
        amount.append(benifit)
    

    # print(time)
    print(f"Total Month: {len(time)} ")
    # print(amount)


    net_total = 0
    for i in amount:
        net_total= net_total+(i)
    print(f"Total : {net_total}")
    

    changes = []
    for i in range(len(amount)-1):
        change = (amount[i+1]) - (amount[i])
        changes.append(change)
    # print(changes)
    # print(len(changes))

    changes_total = 0
    for i in changes:
        changes_total= changes_total + i
        average_change = '%.2f' %(changes_total/(len(changes)))
    print(f"Average Change: {average_change} ")


    index_inc = changes.index(max(changes))
    # print(index_inc)
    max_num = max(changes)
    inc_date = time[index_inc+1]
    print(f"Greatest Increase in Profits: {inc_date} ({max_num})")


    index_dec = changes.index(min(changes))
    # print(index_dec)
    min_num = min(changes)
    dec_date = time[index_dec+1]
    print(f"Greatest Decrease in Profits: {dec_date} ({min_num})")



     
