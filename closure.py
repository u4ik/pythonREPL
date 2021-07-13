import time
import random
# ----------------------------------------------------------
# ? 0 ffWrap------------------------------------------------
# ffWrap should accept another function cb as an argument, call it with no arguments, and return the result of this call. (A perfectly useless wrapper function.)
# TODO - [✔]


def ffWrap(cb):
    return cb


y = ffWrap(lambda: "I'm being returned inside of a nested function!")
print('ffWrap:', y())

# ? 1 ffMap-------------------------------------------------
# ffMap should take two arguments, an array and another function, and return a new array resulting from applying the given function to each element of the given array in order. (Essentially, write your own implementation of the .map array method. Actually, I fully endorse trying to rewrite all the common array methods in your own terms as an exercise in and of itself.)
# TODO - [✔]


def ffMap(arr, func):
    tempArr = []
    for i in arr:
        tempArr.append(func(i))
    return tempArr


print('ffMap:', ffMap([1, 2, 3], lambda x: x + 1))

# ? 2 ffCompose---------------------------------------------
# ffCompose should take two unary functions f and g ("unary" meaning taking exactly one argument), and return a new unary function that has the effect of applying f first, applying g to the result of that, and returning the final result.
# TODO - Hardcoded :( --Not dynamic

# ! Stuck on returning a multiline lambda, hard to find an alternative

# Holding onto each of functions that were passed as arguments


def ffCompose(*args):
    arr = args[::]    
    for arg in arr:
        return
        

print('-ffCompose:', ffCompose(
    lambda x: x * 2,
    lambda y: y + 1
)(2))

# ? 3 ffDoubleShuffleMaker----------------------------------
# ffDoubleShuffleMaker should take two arrays, one of functions and one of numbers. It should return a new function doubleShuffler that, when called, picks one of the functions uniformly at random (meaning each function has the same chance of being chosen) and one of the numbers, also uniformly, returning the result of applying the chosen function to the chosen number.
# TODO - [✔]


def ffDoubleShuffleMaker(funcs, nums):
    return lambda: funcs[random.randint(0, len(funcs) - 1)](nums[random.randint(0, len(nums)-1)])


print('ffDoubleShuffler:', ffDoubleShuffleMaker(
    [
        lambda x: x + 1,
        lambda y: y + 2,
        lambda z: z + 3
    ]
    , [1, 2, 3, 4, 5, 6])()
)

# ? 4 ffArgMin----------------------------------------------
# ffArgMin should take a function f and an array of numbers and return the element of the array which has the lowest output after applying f.
# TODO Pretty sure this is not the right approach...lol


def ffArgMin(f, arr):
    newArr = []
    arr.sort()
    for i in arr:
        newArr.append(f(i))
        newArr.sort()
        smallest = min(arr)
        for n in newArr:
            if n >= smallest:
                return smallest
        return smallest


print('-ffArgMin:', ffArgMin(lambda x: x*500, [-3, 5, -8, 2]))

# ? 5 ffMakeFlipper-----------------------------------------
# ffMakeFlipper should take two arguments a and b. It should return a function that alternates returning a and b when it is called repeatedly on zero arguments.
# TODO - [✔]


def ffMakeFlipper(a, b):
    hold = True

    def check():
        nonlocal hold
        if hold:
            hold = not hold
            return a
        else:
            hold = not hold
            return b
    return check


flipper = ffMakeFlipper('Amit', 'Justin')
print('ffMakeFlipper:', flipper(), flipper(), flipper(), flipper())

# ? 6 ffPhoenixTimeout--------------------------------------
# ffPhoenixTimeout should take one argument, ms, which is a number representing milliseconds. It should do two things: first, print "rising from the ashes" to the console, and second, set up a timeout that will do these two steps again after the given number of milliseconds. If you do it right, the phoenix will rise over and over until you Ctrl-C out of the console. (When you set up the timeout think carefully: what two steps do you need to execute after ms milliseconds, and might you already have a function lying around that does exactly those two steps?)
# TODO - [✔]


def ffPhoenixTimeout(ms):
    def x(ms):
        print('rising from the ashes')
        time.sleep(ms)
        x(ms)
    return (x)(ms)


print('ffPhoenixTimeout: Commented Out')
# ffPhoenixTimeout(1)

# ? 7 ffMemo-----------------------------------
# ffMemoize should take a function f and return a function fMemo that can look up and see, given an input, if it has seen that input before and what its respective output was. If it is not a new input, it should return the previously computed value without having to invoke f. If it is a new input, it should run f on that and returns the result (though make sure to store this new input-output pair!). When might a function like this be useful?
# TODO - [✔]


def ffMemoize(f):
    cache = {}

    def fMemo(*args):
        num1 = args[0]
        num2 = args[1]
        op = f(num1, num2)
        if op in cache:
            return cache[op], 'Lookup Found'
        else:
            cache[f(num1, num2)] = f(num1, num2)
            return f(num1, num2), 'Initial Add'
    return fMemo


memoAdd = ffMemoize(lambda x, y: x+y)

print('ffMemoize:', memoAdd(2, 3), memoAdd(2, 3))

# ? 8 ffCurry----------------------------------
# ffCurry should take a binary function f (a function which takes two arguments) and return a new function fCurr such that f(a, b) produces the same output as fCurr(a)(b). This is tricky so I will try to clarify. Our higher-order function ffCurry needs to take a function f on two arguments and give back a new function fCurr that essentially does the same thing, except that with fCurr, we give it only the first of the two arguments that f was expecting. Then fCurr returns a function that is now only looking for the second argument for f because it has been "fixed" on the first argument. OK here's an example. Suppose I have a function add that takes two numbers and returns their sum. If I apply add to ffCurry, I will get back a function addCurr that is looking for one argument. Say I give addCurr an 8. addCurr(8) returns a function that will take any number and add 8 to it. Let's write this out explicitly:
# TODO - Not getting the output that I need :( "ffCurry.<locals>.<lambda>.<locals>.<lambda>.<locals>.<lambda>"

# JS EXAMPLE:
# const add = (x, y) => x + y
# const addCurr = ffCurry(add)
# const add8 = addCurr(8)
# const finalSum = add8(15)  // add8(15) is also addCurr(8)(15)
# console.log(finalSum)  // prints out 23


def add(x, y): return x+y


def ffCurry(f):
    # def x(f):
    #     def y(a):
    #         def z(b):
    #                 return f(a,b)
    #         return z
    #     return y
    # return x
    return lambda f: lambda a: lambda b: f(a, b)


print('-ffCurry:',ffCurry(add)(1)(2))
