import string           #using the modules string and random
import random     

class Password:
    def __init__(self) -> None:
        pass
    def generate(self,n):
        self.n=n
        joined=(random.sample(list(string.ascii_letters), self.n//2)        #concatenating list of uppercase, lowercase
            +   random.sample(list(string.digits), self.n//3)               #digits and punctuations depending on the size n
            +   random.sample(list(string.punctuation), self.n//4))     
        random.shuffle(joined)                                              #creating a shuffled sample
        x= ''.join(joined)                                                  #converting a list into a string
        return x    ,len(x)                                                 #returns a string

if __name__ == '__main__':
    #exception handling
    try:
        a = Password()
        a.generate(int(input()))
    except Exception as e:
        print("Invalid:", e)