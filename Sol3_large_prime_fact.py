"""
Largest prime factor
--------------------
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
"""

def run():
    """Main Function"""
    main_num = 600851475143
    start_num = 2
    while start_num * start_num < main_num:
        while main_num % start_num == 0:
            main_num = main_num / start_num
        start_num += 1
    print start_num
    
if __name__ == '__main__':
    run()
