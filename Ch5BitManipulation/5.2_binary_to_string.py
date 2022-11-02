"""
Given a num between 0 and 1, print the binary representations.
If the number cannot be represented accurately in binary with at most 32 characters print 'ERROR'
"""

num = .72

def get_binary(num):
    num_converted = int(num * 100)
    binary = '.' + bin(num_converted).split('b')[1]
    if len(binary) > 32:
        return 'ERROR'
    return binary

print(get_binary(num))