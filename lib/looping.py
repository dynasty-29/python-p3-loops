#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    for e in range(10, 0, -1):
        print (e)
    print("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    return [b ** 2 for b in int_list]

def fizzbuzz():
    # code goes here!
    for t in range(1, 101):
        if t % 5 == 0 and t % 3 == 0:
            print("FizzBuzz")
        elif t % 3 == 0:
            print("Fizz")
        elif t % 5 == 0:
            print("Buzz")
        else:
            print(t)
