new_file = open('newfile.txt','x')
new_file.close
import os
print("checking if my file exists or not...")
if os.path.exists("my_file.txt"):
os.remove("my_file.txt")
else:
   print("the file does not exist")
my_file = open("my_file.txt","w")
my_file.write("Hi! iam penguin i am one year old")
my_file.close
os.remove('codingal.txt')