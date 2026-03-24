import csv

def load_data(file):
    with open(file) as f:
        data=list(csv.reader(f))
    return data[1:]

data=load_data("employee_data.csv")

hypothesis=['0']*(len(data[0])-1)

for row in data:
    if row[-1]=='Yes':
        for i in range(len(hypothesis)):
            if hypothesis[i]=='0':
                hypothesis[i]=row[i]
            elif hypothesis[i]!=row[i]:
                hypothesis[i]='?'

print("Final Hypothesis:",hypothesis)