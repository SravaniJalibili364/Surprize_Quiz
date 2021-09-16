
def words_input():
     c=0 
     file=open("input.txt",'r') 
     lines = file.read() 
     words = lines.split() 
     print(words)
     for i in words: 
         if len(i)<5: 
             print(i) 
             file.close()


words_input()