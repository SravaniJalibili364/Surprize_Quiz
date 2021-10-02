def words_input(words): 
    words_dict = {}
                      
    for word in words:
        if word not in words_dict:
            words_dict[word] = 1
        else:
            words_dict[word] += 1

    word_list = []
    for word,count in sorted(words_dict.items()):
        word_list.append((count,word))

    word_list = sorted(word_list,reverse=True)

    for word in word_list:
        print("%s : %s" %(word[1],word[0]))

                     

file =open("input_file.txt",'r') 
lines = file.read()          
words = lines.split()             
words_input(words) 
