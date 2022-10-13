def countFunc (theStr: str) -> int :
    dict = {}
    for i in theStr :
        string = ''
        if i in string :
            continue
        else :
            count = theStr.count(i)
            dict[i]= count
            string += i 
            
    return dict 


text = input("Enter The Text : ")
for i in text :
    dict = countFunc(text)
    print(i , "==> ", dict[i])
    

