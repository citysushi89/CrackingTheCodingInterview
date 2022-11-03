"""
Write a function to determine the number of bits you would need to flip to convert integer A to integer B
"""

input_a = 29
input_b = 10

input_a_binary = bin(input_a).split('b')[1]
input_b_binary = bin(input_b).split('b')[1]

# Make lists the same length with a placeholder
while True:
    if len(input_a_binary) > len(input_b_binary):
        input_b_binary += '_'
    elif len(input_a_binary) < len(input_b_binary):
        input_a_binary += '_'
    elif len(input_a_binary) == len(input_b_binary):
        break

counter = 0
digits_to_change = 0
for item in input_a_binary:
    if item != input_b_binary[counter]:
        digits_to_change += 1
    counter += 1

# Should equal 2
print(digits_to_change)
