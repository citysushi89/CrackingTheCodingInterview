"""
Explain what the following code does ((n & (n-1)) == 0)
"""

n = 1
print(((n & (n-1)) == 0))

print(n & 10)

# Subtracts 1 from n
# (n & (n)) --> returns 1 if both bits are one, else returns 0
# if above returns 0, == 0 returns true, else false