
def words_input():              # Defining the function to read the file and checking the length of the words
     c=0                        # Assaigning c to 0
     file=open("input.txt",'r') # opening the input text file
     lines = file.read()        # reading the text file  
     words = lines.split()      # using the split function words are splitted into list

     for i in words:            # iterating the list 
         if len(i)<5:           # Checking the length of the each word and if len is less than five or not
             print(i)           # printing the words which are less than 5
             file.close()       # Closing the file


words_input()      # Calling the function