# This program prints numbers from 1 to 100 on a new line
# For each multiple of 3, the program says "Fizz" instead
# For each multiple of 5, the program says "Buzz" instead
# For each multiple of 15, the program says "Fizz-Buzz"

for i in range (1,101):     # listing numbers from 1 to 100 (excluding 101)
    if (i%15 == 0):      # factors of 15, numbers when divided by 15 give 0
        print('fizz-buzz')
    elif (i%5 == 0):    # factors of 5, numbers when divided by 5 give 0
        print('buzz')
    elif (i%3 == 0):    # factors of 3, numbers when divided by 3 give 0
        print ('fizz')
    else:
        print (i)   # print the remaining nmbers
