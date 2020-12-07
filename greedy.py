import math
import time


def gEdit_d(target, source):
    "shifting strings to find maximum character overlap"
    flip = False
    if len(target) > len(source):
        temp = target
        target = source
        source = temp
        flip = True

        align_string1 = ""
        align_string2 = ""
        edit_distance = math.inf
        for shift_index in range(int(len(target) / 2), -1, -1):
            string2 = shift_index * "-" + source
            string1 = target + (len(string2) - len(target)) * "-"
            count = 0
            for x, y in zip(string1, string2):
                if x != y:
                    count += 1

        if count < edit_distance:
            align_string1 = string1
            align_string2 = string2
            edit_distance = count

        for shift_index in range(1, int(len(source) - len(target)/2) + 1):
            string1 = shift_index * "-" + target
            max_length = max(len(string1), len(source))
            string2 = source + "-" * (max_length - len(source))
            string1 = string1 + "-" * (max_length - len(string1))
            count = 0

            for x, y in zip(string1, string2):
                if x != y:
                    count += 1
            if count < edit_distance:
                align_string1 = string1
                align_string2 = string2
                edit_distance = count

        if flip:
            return (align_string2, align_string1), edit_distance
        else:
            return (align_string1, align_string2), edit_distance


if __name__ == '__main__':

    randomstringlength = 8

    firststring = "ROYGBIVERTT"
    secondstring = "BERTTRUEIDI"

    print("{:<20}".format("First String  :"), firststring)
    print("{:<20}".format("Second String :"), secondstring)

    print("XXXXXXXXXXXXXXXXXXX")
    print("Greedy Approach")
