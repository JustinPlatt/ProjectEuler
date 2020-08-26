#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


###No function is needed to test for primes because only
###primes will divide evenly into cap
#def is_prime(x):
#    result = True
#    for a in range(2, x): #loop from 2 through x-1
#        if x % a == 0:
#            result = False
#    return result


def main():
    cap = int(input('Factor which number?:  '))  #put the number to factor here
    print('Printing factors of ' + str(cap))

    #we want to generate a list of primes.
    #If we hit a prime, divide the existing number until there's a remainder
    #then change the cap to be whatever's left after the division
    cur_num = 2
    while cur_num <= cap:
        while cap % cur_num == 0:
            print(cur_num)
            cap = cap / cur_num
        cur_num += 1

if __name__ == "__main__":
    main()
