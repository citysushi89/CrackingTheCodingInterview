"""
You have an integer and you can flip exactly one bit from 0 to 1. 
Write code to find the length of the longest sequence of 1s you could create
"""

num = 1775
other_num = 177

def flip_bit(num):
    num_bit = bin(num).split('b')[1]
    max_ones_in_row = 0
    tracker = 0
    two_maxes = 0
    connected = False

    for i in range(0, len(num_bit)):
        if num_bit[i] == '1':
            tracker += 1
            if tracker > max_ones_in_row:
                max_ones_in_row = tracker 
                if connected:
                    if max_ones_in_row + tracker > two_maxes:
                        two_maxes = max_ones_in_row + tracker
                        connected = False
        else:
            tracker = 0
            if num_bit[i] == '0' and num_bit[i - 1] == '1' and num_bit[i + 1] == '1':
                connected = True

    if two_maxes > 0:
        return two_maxes
    else:
        return max_ones_in_row

# Should return 8
print(flip_bit(num))

# Should return 4
print(flip_bit(other_num))