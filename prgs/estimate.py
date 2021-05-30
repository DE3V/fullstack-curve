import math
import random

def wallis(n):
 result=1;
 a=1
 
 
 for i in range(1,n):
               a = 4*i**2/(4*i**2-1)
               result = result*a
             
 result = result*2 
                                                    
 return result
 
 
 
 
 
def monte_carlo(n):
 ins = 0
 result=1

 for i in range(0, n):
 
        x = random.random()**2
        y = random.random()**2
    
        if math.sqrt(x + y) < 1.0:
           ins += 1


 result *= (float(ins) / n) * 4
 
 return result


