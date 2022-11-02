# check_permutation.py writes a method to decide if string_1 one is a permutation of string_2

# case should success
string_1 = 'abcde'
string_2 = 'edcba'

# case should fail
string_3 = 'abcde'
string_4 = 'aaaaaa'

# case should return -1
string_5 = 'abcde'
string_6 = 10

def is_permutation(str_inp_1, str_inp_2):
    # Check if input is a string
    if isinstance(str_inp_1, str) and isinstance(str_inp_2, str):
        pass
    else:
        return -1

    for item in str_inp_1:
        if item in str_inp_2:
            pass
        else:
            return False
    return True

print(is_permutation(string_1, string_2))
print(is_permutation(string_3, string_4))
print(is_permutation(string_5, string_6))

