"""
Smallest multiple
Problem 5

2520 is the smallest number that can be divided by each of the numbers 
from 1 to 10 without any remainder. What is the smallest positive number
that is evenly divisible by all of the numbers from 1 to 20?
"""
def run():
    """The Main Function"""
    num = 2520
    status = False
    while True:
        for i in range(20, 1, -1):
            if num % i != 0:
                status = False
                break
            else:
                status = True
        if status:
            break                
        num = num + 10

        
    print num
    
if __name__ == '__main__':
    run()
