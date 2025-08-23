file = open('css.txt','r')
print(file.read())
file.close()
#2
file = open('css.txt','r')
print("\n Read in parts \n")
print(file.read(5))
file.close()