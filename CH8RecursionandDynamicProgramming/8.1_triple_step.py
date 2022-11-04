"""
A child is runnning up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time, 
implement a method to count how amny possible ways the child can run up the stairs
Problem does not require recursion, maybe that's faster than a while loop but it works
"""


num_steps = 5


def get_combos(num_steps):
    counter = 0

    while True:
        if num_steps > 3:
            counter += 3
        elif num_steps > 2:
            counter += 2
        elif num_steps > 1:
            counter += 2
        elif num_steps == 1:
            counter += 1
            break
        num_steps -= 1

    return counter


print(get_combos(num_steps))
