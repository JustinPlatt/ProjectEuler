

#If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.

total = 0
for n in range(999): #go from 1 to 999
    if (n+1) % 3 == 0 or (n+1) % 5 == 0:
        total+= n+1

print('Total = ' + str(total))
