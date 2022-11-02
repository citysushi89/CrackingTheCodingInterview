# is_unique.py Implements an Algorithm to determine if a string has all unique characters.
# Also Try to use an additional data structure?

string_1 = 'abcdefg'
string_2 = 'aabbccdd'
# edge case
string_3 = 15
string_4 = ''

def determine_if_unique(str_inp):
    # Check if input is a string
    if isinstance(str_inp, str):
        pass
    else:
        return -1
    
    for item in str_inp:
        if str_inp.count(item) > 1:
            return False
    return True


print(determine_if_unique(string_1))
print(determine_if_unique(string_2))
print(determine_if_unique(string_3))
print(determine_if_unique(string_4))
