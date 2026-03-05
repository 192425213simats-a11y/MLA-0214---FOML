import csv
import copy

def load_data(filename):
    with open(filename, 'r') as file:
        data = list(csv.reader(file))
    return data

def candidate_elimination(data):
    attributes = len(data[0]) - 1
    
    S = ['0'] * attributes
    G = [['?'] * attributes]
    
    for row in data[1:]:
        if row[-1] == 'Yes':  # Positive example
            for i in range(attributes):
                if S[i] == '0':
                    S[i] = row[i]
                elif S[i] != row[i]:
                    S[i] = '?'
            
            G = [g for g in G if all(g[i] == '?' or g[i] == S[i] for i in range(attributes))]
        
        else:  # Negative example
            new_G = []
            for g in G:
                for i in range(attributes):
                    if g[i] == '?':
                        if row[i] != S[i]:
                            new_h = g.copy()
                            new_h[i] = S[i]
                            new_G.append(new_h)
            G = new_G
    
    return S, G


data = load_data("training_data.csv")
S, G = candidate_elimination(data)

print("Final Specific Hypothesis S:")
print(S)

print("\nFinal General Hypothesis G:")
for g in G:
    print(g)