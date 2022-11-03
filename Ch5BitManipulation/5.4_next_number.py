"""
given a positive integer, print the next smallest and the next largest number 
that hav ethe same number of 1 bits in their binary representation
"""

input_num = 77

def make_bit(num):
    return bin(num).split('b')[1]

def get_ones(bit_num):
    number_of_ones = 0
    for item in bit_num:
        if item == '1':
            number_of_ones += 1
    return number_of_ones

input_bit = make_bit(input_num)
input_num_ones = get_ones(input_bit)

# Find the larger number with same number of ones
larger_num = input_num + 1
while True:
    current = make_bit(larger_num)
    current_ones = get_ones(current)
    if current_ones == input_num_ones:
        output_num_large = larger_num
        break
    larger_num += 1

# Find the smaller number with same number of ones
smaller_num = input_num - 1
while True:
    current = make_bit(smaller_num)
    current_ones = get_ones(current)
    if current_ones == input_num_ones:
        output_num_small = smaller_num
        break
    smaller_num -= 1

print(f"The input number is {input_num}. The larger number with the"
    f"same number of ones in its binary representation is "
    f"{output_num_large} and the smaller is {output_num_small}.")
