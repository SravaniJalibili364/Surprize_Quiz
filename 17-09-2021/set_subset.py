'''Write a Python program to check if a set is a subset of another set.'''


# first taking input as sequence of numbers,converting str into int using map function
super_set = set(map(int,input().split(",")))
# now are sorting the set
[super_set].sort()
subset_input = set(map(int,input().split(",")))
[subset_input].sort()

#result = subset_input.issubset(super_set)

#print(result)
len_super = len(super_set)
len_sub   = len(subset_input)

print(subset_input)
super_set = list(super_set)
subset_input = list(subset_input)
print(subset_input)

c = 0
for i in super_set:
    # checking the condtion item in subset or not using index
    if i == subset_input[c]:
        #now incrementing index by 1
        c += 1
        # checking if index is equal to the length of the subset 
        if c == len_sub:
            break
# if index and subset_len is equal then it is superset
if c == len_sub:
    print("It is a Subset of Superset")
else:
    print("It is not a subset")
    

    

        
        
