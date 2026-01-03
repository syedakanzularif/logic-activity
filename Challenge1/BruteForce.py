#BRUTE FORCE CHALLENGE1.PY 
contribution=[10,20,30]
impact=[]
for i in range(len(contribution)):
    product=1
    for j in range(len(contribution)):
        if i!=j:
            product*=contribution[j]
    impact.append(product)
print(impact)
