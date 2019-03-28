#all the Python code to remember



'''




#1.fibonacci series: 0,1,1,2,3,5,8,13,21,34
def fibb(n):
    a = 0
    b = 1

    if n == 1:
        print (b)
    else :
        print(a)
        print (b)
        for i in range(2,n):
            c = a + b
            a = b
            b = c

            print (c)
fibb(12)

'''




'''

#2.Fizz Buzz: print ("fizz") for all numbers divisible by 3 , print ("buzz") for all numbers divisible by 5
# and finally print ("Fizz buzz") for numbers divisible by 3 and 5.

def fizzbuzz (n):
    for i in range (n):
        if i % 15 == 0:
            print ("Fizz Buzz")
        elif i % 5 == 0:
            print ("Buzz")
        elif i % 3 == 0:
            print ("Fizz")
        else :
            print (i)

fizzbuzz (100)
'''