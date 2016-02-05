## Short script to explore some of the processes involved in defining, calling, and passing a function.
## The idea was to learn how to pass a function to another function, as well as learning how to obtain input
## from the keyboard/console.

## Low level function, representing some type of objective function one might wish to vary between calls.
def myFunc(x,y):
    return x*y

## High level function, doing something using the input function.
def NestedFunc(fun):
    x = float(input('Please define X: '))
    y = float(input('Please define Y: '))
    print('Function of (' + str(x) + ',' + str(y) + ') = ' + str(fun(x,y)))
    return

## Call the high level function and give it the handle of the low level function for it to call.
NestedFunc(myFunc)

