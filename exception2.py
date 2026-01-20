try:
    num1,num2 = eval(input("enter 2 numbers seperated by a coma"))
    rusult = num1/num2
    print("result is ",rusult)
except ZeroDivisionError:
    print("Division by zero is error !!")
except SyntaxError:
    print("coma is missing. enter numbers like this 1,2")
except:
    print("wrong input")
else:
    print("no exception")