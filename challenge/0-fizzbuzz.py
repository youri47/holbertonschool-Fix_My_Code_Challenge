#!/usr/bin/python3
"""Fizzbuzz"""
import sys


def fizzbuzz(n):
    """prints fizzbuzz"""
    for i in range(1, n + 1):
        if i % 15 == 0:
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            print("Fizz", end=" ")
        elif i % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(i), end=" ")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)
    fizzbuzz(int(sys.argv[1]))
    print("")
