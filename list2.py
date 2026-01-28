def match_word(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word) 
            print("list of wrods with first and last chracter same", list)
            return str
count = match_word(["abc","cfc","xyz","aba",1221])
print("number of words having first and last and last chracter same:", count)

