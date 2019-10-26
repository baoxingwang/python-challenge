import os

import csv

csvpath = os.path.join('..', 'PY homework', 'election_data.csv')

print("Election Results")
print("------------------------")

with open(csvpath)as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # for index, column_header in enumerate(header_row):
        # print(index,column_header)



    ID_vote = []
    candidates = []
    for row in reader:
        ID_n = str(row[0])
        ID_vote.append(ID_n)
        candidate = str(row[2])
        candidates.append(candidate)


  
    total_vote = (len(ID_vote))
    print(f"Total Vote: {total_vote} ")

    print("------------------------")
    

    d = {}
    
    for item in candidates:
        if item in d:
            d[item] = d.get(item)+1
        else:
            d[item] = 1

    for k,v in d.items():

        rate = '%.3f' % (v/total_vote*100)
        print(f"{k}: {rate}% ({v})")
        # print(f"\nname:{k}")
        # print(f"poll:{v}")
        # print(str(k)+':'+ str(v/total_vote*100)+'%')
    print("------------------------")
        
    print(f"winner: { max(d, key = d.get)} ")


    # print(d)    

    
        
    

    

    
    
