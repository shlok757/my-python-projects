medical_cause = input("did you have an medical certificate Y or N")
atten = int(input("enter the attendance of the student"))
if medical_cause =='Y':  
  print("your allowed")
else:
  if atten>=75:
    print("allowed")
  else:
    print("not allowed")