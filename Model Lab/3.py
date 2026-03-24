import csv
from collections import Counter

data=[]
with open("employee_data.csv") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        data.append(row)

labels=[r[-1] for r in data]

prediction=Counter(labels).most_common(1)[0][0]

print("Predicted Attrition:",prediction)