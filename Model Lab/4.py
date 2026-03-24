import csv
import math

def encode(row):
    exp={'Low':1,'Medium':2,'High':3}
    sal={'Low':1,'Medium':2,'High':3}
    sat={'Poor':1,'Average':2,'Good':3}
    wlb={'Yes':1,'No':0}
    
    return [
        exp[row[0]],
        sal[row[1]],
        sat[row[2]],
        wlb[row[3]],
        1 if row[4]=='Yes' else 0
    ]

data=[]
with open("employee_data.csv") as f:
    reader=csv.reader(f)
    next(reader)
    for row in reader:
        data.append(encode(row))

w=[0,0,0,0]
b=0
lr=0.01

def sigmoid(z):
    return 1/(1+math.exp(-z))

for _ in range(1000):
    for row in data:
        x=row[:-1]
        y=row[-1]
        
        z=sum(w[i]*x[i] for i in range(4))+b
        y_pred=sigmoid(z)
        
        error=y-y_pred
        
        for i in range(4):
            w[i]+=lr*error*x[i]
        b+=lr*error

# Test
test=[1,2,2,1]  # Low, Medium, Average, Yes
z=sum(w[i]*test[i] for i in range(4))+b
print("Attrition Probability:",round(sigmoid(z),2))