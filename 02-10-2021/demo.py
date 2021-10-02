def words_input(words): 
    words_dict = {}
                      
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1


    for word,count in sorted(words_dict.items()):
        print(word,count)

                     

file =open("input_file.txt",'r') 
lines = file.read()          
words = lines.split()             
words_input(words) 
