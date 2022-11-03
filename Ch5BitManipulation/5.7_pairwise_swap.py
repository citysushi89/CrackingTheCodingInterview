"""
Write a program to swap odd and even bits in an integer with as few instructions as possible
(bit 0 and 1 are swapped, bits 2 and 3 are swapped, etc)
"""

num = 10
num_bits = bin(num).split('b')[1]

def flip_pairs(num_bits):
    num_bits_len = len(num_bits)
    if num_bits_len < 2:
        return 'ERROR: Cannot swap bits with fewer than two bits'

    output = ''
    num_bits_list = [bit for bit in num_bits]

    for i in range(0, num_bits_len, 2):
        # If last bit in an odd-numbered len
        if i == (num_bits_len - 1) and i % 2 == 0:
            num_bits_list[i] == num_bits_list[i] 
        else:
            temp_even = num_bits_list[i]
            temp_odd = num_bits_list[i + 1]
            num_bits_list[i] = temp_odd
            num_bits_list[i + 1] = temp_even

    for item in num_bits_list:
        output += item

    return output


print(flip_pairs(num_bits))
