#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length == 0:
            print([])
    elif length == 1:
         print([0])
    elif length == 2:
         print([0,1])
    else:
        a,b = 0,1
        fib_list = [0,1]
        for x in range(length - 2):
            c = a + b
            a = b
            b = c
            fib_list.append(c)

        
        print(fib_list)
        return fib_list


print(print_fibonacci(10))

