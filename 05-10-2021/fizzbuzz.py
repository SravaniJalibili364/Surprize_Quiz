num  = 0 
while(num <100):
    if(num % 3 == 0):
        print(num," - fizz")
    elif(num % 5 == 0):
        print(num," - buzz")
    elif(num % 3 == 0 & num % 5 == 0):
        print(num," - fizzbuzz")
    
    num += 1