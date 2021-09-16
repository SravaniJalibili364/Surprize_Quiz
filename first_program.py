first_input = input()
first_len = len(first_input)
if (first_len%2 != 0):
    middle_one = round((first_len/2))
else:
    middle_one = round(first_len/2) + 1


second_input = input()
sec_len = len(second_input)
if(sec_len % 2 != 0):
    s_middle_one = round((sec_len/2))
else:
    s_middle_one = round(sec_len/2) + 1

output = str(first_input[0]) + str(second_input[0]) + str(first_input[middle_one-1])+ str(second_input[s_middle_one-1])+str(first_input[-1]) + str(second_input[-1])
print(output)
