# 2281. Sum of Total Strength of Wizards
# As the ruler of a kingdom, you have an army of wizards at your command.

# You are given a 0-indexed integer array strength, where strength[i] 
# denotes the strength of the ith wizard. For a contiguous group of wizards 
# (i.e. the wizards' strengths form a subarray of strength), the total strength 
#  is defined as the product of the following two values:

# The strength of the weakest wizard in the group.
# The total of all the individual strengths of the wizards in the group.
# Return the sum of the total strengths of all contiguous groups of wizards. 
# Since the answer may be very large, return it modulo 109 + 7.

# A subarray is a contiguous non-empty sequence of elements within an array.

def totalStrength(strength):
    n = len(strength)
    prefixSum = [0]
    for i in range(1, n):
        prefixSum.append(prefixSum[i - 1] + strength[i])
    
    NGL = [n] * n
    PGL = [-1] * n

    

