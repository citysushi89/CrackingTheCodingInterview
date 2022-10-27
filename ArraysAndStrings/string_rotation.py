# string_rotation.py is_substring returns True if a string_2 can be created by a string_1 with just a single call 
# Works, not optimized

string1 = 'sampletext'
string2 = 'txetelpmas'

string3 = 'gibberish'
string4 = 'notinword'

string5 = 'sampletext'
string6 = 'ampletext'

def is_substring(base_string, potential_sub_string):
    is_sub = False
    string_length = len(base_string)
    already_tested_list = []

    def check_temp_string(temp_strings_list):
        for item in temp_strings_list:
            if item == potential_sub_string:
                return True

    for i in range(1, string_length):
        temp_strings_list = []
        temp_strings_list.append(base_string[i:])
        temp_strings_list.append(base_string[-i:])
        temp_strings_list.append(base_string[:i])
        temp_strings_list.append(base_string[:-i])
        temp_strings_list.append(base_string[i::])
        temp_strings_list.append(base_string[-i::])
        temp_strings_list.append(base_string[:i:])
        temp_strings_list.append(base_string[:-i:])
        temp_strings_list.append(base_string[::i])
        temp_strings_list.append(base_string[::-i])
        print(temp_strings_list)
        # print(temp_strings_list)
        is_sub = check_temp_string(temp_strings_list)
        # already_tested_list.append()
        if is_sub == True:
            return True
    return False


# Should be True
print(is_substring(string1, string2))
# Should be False
print(is_substring(string3, string4))
# Should be True
print(is_substring(string5, string6))   