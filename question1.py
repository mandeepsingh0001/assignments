for x in range (2000 , 3200):
    if (x % 7) == 0:
        y = x/5.0
        if (y % 5)!= 0 :
            print str(x) + ",",


# question number 2

num = raw_input("enter the number")
print (num)
factorial = 1

if num < 0:
    print("sorry factorial does not exist for negative numbers")
elif num == 0:
    print("the factorial of 0 is 1")
else:
    for i in range(1 , num + 1):
        factorial = factorial * i
        print ("the factorial of num is",factorial)


# question 3

def squares (n) :
    result = {}
    for i in range(1 , n+1):
        result[i] = i*i
        return result