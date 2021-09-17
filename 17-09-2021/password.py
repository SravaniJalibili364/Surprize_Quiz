''''Write a Python program to check the validity of password input by users. 
Validation criteria: Must contain
At least 1 letter between [a-z] and 1 letter between [A-Z].
At least 1 number between [0-9]
At least 1 character from [$#@]
Minimum length 6 characters
Maximum length 16 characters


'''

#Taking the password from the user to check it is valid or not
password_input = input()
length_of_password = len(password_input)

# Now it is checking the length of the password is in valid length or not
if (length_of_password >= 6 or length_of_password <= 16):
    upper_case_count = 0
    lower_case_count = 0
    num_count = 0
    special_char  = 0
    # Using the for loop checking lowercase_count,uppercase_count,num_count,special_char_count
    for char in password_input:
        if char.isupper():
            upper_case_count += 1
        elif char.islower():
            lower_case_count += 1
        elif char.isnumeric():
            num_count += 1 
        elif(char == "$" or char == "#" or char == "@"):
            special_char += 1

    # Now checking the all conditions whether it is satisfying with given condition or not   
    if(upper_case_count >= 1 and  lower_case_count >= 1  and num_count >= 1 and special_char >= 1):
        print("It is Valid Password")
    else:
        print("It is not a Valid Password") 
else:
    print("It is not a valid Password")