# url_ify.py replaces every space in a string with '%20'

# standard cases
string_1 = 'Sample String'
string_2 = ' Other Test '
string_3 = 'noPercents'

# edge cases
string_4 = 15
string_5 = []



def make_url(str_inp):
    # check if input is a string
    if isinstance(str_inp, str):
        pass
    else:
        return -1

    # what to replace the space with 
    replacement = '%20'
    # string to return 
    str_output = ''
    for item in str_inp:
        if item == ' ':
            str_output = str_inp.replace(item, replacement)
        else:
            str_output += item
    return str_output


print(make_url(string_1))
print(make_url(string_2))
print(make_url(string_3))
print(make_url(string_4))
print(make_url(string_5))