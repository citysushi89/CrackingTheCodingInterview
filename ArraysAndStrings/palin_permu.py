# palin_permu.py checks if a given string is the same forward and backward

string_1 = 'Taco Cat'
string_2 = 'Not a palindrome nor a permutation'
not_string = 15

def check_palindrome_permutation(str_inp):
    # type check for edge cases
    if hasattr(str_inp, '__iter__'):
        pass
    else:
        return -1

    # ensure string uniformity in capilization and remove spaces
    str_inp = str_inp.lower()
    str_inp = str_inp.replace(' ', '')

    string_length = len(str_inp) - 1
    for i in range(string_length):
        if str_inp[i] == str_inp[-(i + 1)]:
            continue
        else:
            return False
    return True


print(check_palindrome_permutation(string_1))
print(check_palindrome_permutation(string_2))
print(check_palindrome_permutation(not_string))