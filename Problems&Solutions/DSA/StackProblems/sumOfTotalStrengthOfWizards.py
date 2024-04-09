# 2281. Sum of Total Strength of Wizards

def totalStrength(strength):
    n = len(strength)
    prefixSum = [0]
    for i in range(1, n):
        prefixSum.append(prefixSum[i - 1] + strength[i])
    
    NGL = [n] * n
    PGL = [-1] * n

    

