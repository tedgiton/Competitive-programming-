class Solution(object):
    def fizzBuzz(self, n):
        output=[]
        
        for i in range(1,n+1): 
            con = False
            if i%5==0 and i%3==0:
                output.append("FizzBuzz")
                con= True
                continue;
            if i%3==0:
                output.append("Fizz")
                con= True
                continue;
            if i%5==0:
                output.append("Buzz")
                con= True
                continue;
            if con == False:
                output.append(str(i))
                con= True
                continue;
        return output;
            
