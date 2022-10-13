
class PrimeNumber :
    def __init__(self , Range : int ) -> int :
        self.Range = Range 

    def is_Prime (self) :
        for num in range(1, self.Range +1) :
            if num > 1 :
                for i in range(2, num) :
                    if num % i == 0:
                        break
                else :
                    print(num , end=", ")

TheRange = int(input("Enter The Range : "))
The_Prime = PrimeNumber(TheRange)
The_Prime.is_Prime()

