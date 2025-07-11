def add(g,c):
    print(g+c)
    
def sub(g,c):
    print(g-c)
def div(g,c):
    print(g/c) 
def multi(g,c):
    print(g*c)
m=int(input("enter the first numero"))          
b=int(input("enter the second numero")) 
s= input("select a symbol -,+,/,*")
if s=="+":
    
    add(m,b)

elif s=="/":
    
    div(m,b)
elif s=="-":
    
    sub(m,b)
elif s=="*":
    
    multi(m,b)
    
    
    

