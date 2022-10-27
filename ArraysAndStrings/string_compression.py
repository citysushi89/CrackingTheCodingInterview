# string_compression.py returns a string with counts of consecutive letters
import unittest 

string_1 = 'aabcccccaaa'
string_2 = 'abca'


def compress_string(inp_str):
    # TODO type check
    # type check for edge cases
    if isinstance(inp_str, str):
        pass
    else:
        return -1

    string_length = len(inp_str) 
    count = 0
    answer =''

    for i in range(string_length):
        try:
            if inp_str[i] == inp_str[i + 1]:
                count += 1
            else:
                count += 1
                if count > 0:
                    answer += (inp_str[i] + str(count))
                else:
                    answer += (inp_str[i])
                count = 0

        # catches last letter in the string 
        except IndexError:
            count += 1
            if count > 0:
                answer += (inp_str[i] + str(count))
            else:
                    answer += (inp_str[i])
            count = 0

    return answer

# should return 'a2b1c5a3'
print(compress_string(string_1))
# should return 'a1b1c1a1'
print(compress_string(string_2))
