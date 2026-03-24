import csv

def load_data(file):
    with open(file) as f:
        data=list(csv.reader(f))
    return data

data=load_data("employee_data.csv")

S=['0']*(len(data[0])-1)
G=[['?']*(len(data[0])-1)]

for row in data[1:]:
    
    if row[-1]=='Yes':
        for i in range(len(S)):
            if S[i]=='0':
                S[i]=row[i]
            elif S[i]!=row[i]:
                S[i]='?'
    
    else:
        new_G=[]
        for g in G:
            for i in range(len(S)):
                if g[i]=='?':
                    if row[i]!=S[i]:
                        new_h=g.copy()
                        new_h[i]=S[i]
                        new_G.append(new_h)
        G=new_G

print("Specific S:",S)
print("General G:")
for g in G:
    print(g)