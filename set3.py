import array as arr
array_num = arr.array("i",[1,2,3,4,5,3,7,9,3])
print("original array:"+str(array_num))
print("number of occurrences of the number 3 in the said array:"+str(array_num.count(3)))
array_num.reverse()
print("Reverse the order of the given numbers:")
print(str(array_num))