
class Remove :
    def __init__(self, Str:str, Char: str) :

        self.Str = Str
        self.Char = Char 
        self.NewStr = ''

    def removeChar(self) :
        for i in self.Str :
            if self.Char == i :
                continue
            else :
                self.NewStr += i
        return self.NewStr

My_String = input("Enter The Str : ")
Char = input("Enter The Charactr : ")
NewStr = Remove(My_String, Char)

print(NewStr.removeChar())    
    