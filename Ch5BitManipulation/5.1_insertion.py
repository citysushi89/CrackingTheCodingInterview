"""
input n = 1
"""

n = 10000000000
m = 10011
i = 2 
j = 6

# OUTPUT: 100001001100

start = bin(j).split('b')[1]
print(start)
end = bin(i)
print()
print(end)
# bytes_j = j.to_bytes(2, 'big')

# print(bin(j))
# print(bin(i))