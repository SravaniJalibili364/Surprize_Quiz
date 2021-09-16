first_input = input()           # Taking the first String
first_len = len(first_input)    # checking the length of the first string
if (first_len%2 != 0):          # if length of the first string is odd or not
    middle_one = round((first_len/2))   # if it is odd print the middle one
else:
    middle_one = round(first_len/2) + 1         # if it is even it takes first middle one


second_input = input()          # Taking the second String
sec_len = len(second_input)     # checking the length of the second string
if(sec_len % 2 != 0):           # if length of the second string is odd or not
    s_middle_one = round((sec_len/2))   #if it is odd print the middle one
else:
    s_middle_one = round(sec_len/2) + 1     # if it is even it takes first middle one


# Concatinating all the characters
output = str(first_input[0]) + str(second_input[0]) + str(first_input[middle_one-1])+ str(second_input[s_middle_one-1])+str(first_input[-1]) + str(second_input[-1])

print(output)       #print the output
