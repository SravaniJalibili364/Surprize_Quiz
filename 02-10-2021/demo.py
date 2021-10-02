def words_input(words): 
    word_set = {}
                      
    for i in words:
        if i not in word_set:
            word_set[i] = 1
        else:
            word_set[i] += 1


    aa = sorted(word_set.values(),reverse=True)
    for word in word_set:
        print(word,word_set(aa))

                     

file =open("input_file.txt",'r') 
lines = file.read()          
words = lines.split()             
words_input(words) 
