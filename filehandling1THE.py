with open('css.txt','w') as file:
    file.write("Hi! I am penguin and I am 1 year old")
file.close
with open('css.txt','r') as file:
    data= file.readlines()  
    print("words in this file are...") 
    for line in data:
     word = line.split()
    print(word)
file.close    






