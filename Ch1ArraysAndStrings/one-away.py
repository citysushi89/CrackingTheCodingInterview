# one_away.py contains a function that checks if a string is the same or one edit away from a second string

string_1 = 'pale'
string_2 = 'ple'

string_3 = 'pale'
string_4 = 'bake'

string_5 = "cake"
string_6 = "bake the cake"

string_7 = 'pale'
string_8 = 'pael'


def check_one_away(str_inp_1, str_inp_2):
    # type check for edge cases
    if isinstance(str_inp_1, str) and isinstance(str_inp_2, str):
        pass
    else:
        return -1

    edits_away = 0
    string_1_length = len(str_inp_1) - 1
    string_2_length = len(str_inp_2) - 1

    # if strings have lengths that vary by more than 1, they cannot be one edit away
    if abs(string_1_length - string_2_length) > 1:
        return False

    str_inp_1 = str_inp_1.lower()
    str_inp_2 = str_inp_2.lower()
     
    for letter in str_inp_1: 
        if str_inp_1.count(letter) == str_inp_2.count(letter):
            if abs(str_inp_1.index(letter) - str_inp_2.index(letter)) == 0:
                pass

            # Only one item can be at a different index between the strings
            # so if two are at different indices edits_away will be above 1, ending the loop
            elif abs(str_inp_1.index(letter) - str_inp_2.index(letter)) >= 1:
                edits_away += .9

        # removes the letter from str_inp_1 if not in str_inp_2 
        # this allows for the index checking to work (see difference between Strings 1&2 and 7&8)
        elif letter not in str_inp_2:
            str_inp_1 = str_inp_1.replace(letter, '')
        else:
            edits_away += 1
        
        # end the loop if more than one edit is discovered
        if edits_away > 1:
            return False

    return True


# should be true
print(check_one_away(string_1, string_2))
# should be false
print(check_one_away(string_3, string_4))
# should be false
print(check_one_away(string_5, string_6))
# should be false
print(check_one_away(string_7, string_8))