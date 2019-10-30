# Strings, Lists, Functions!

# Create a function that adds all the elements of a list together.
# Hint: Use a for loop
def sum_list (nums):
    return None

#Create a function that finds the largest number in a list
#return None if the list is empty
def largest_element (nums):
    return None

# Create a function that multiplies all the elements of a list together.
# Hint: Use a for loop
def multiply_array (nums):
    return None

# Create a function that returns the length of a string
# Do not use the in-built length() function for this
def string_length (string):
    return None

# Create a function that multiplies all the odd numbers in a list together, adds all the even numbers together, then returns those two numbers added together. Assume there are no negative elements
#  hint: use the modulus operator
def multiply_odd_add_even (nums):
    return None

# Create a function that adds "ing" to the end of a string
# e.g 'abc' -> 'abcing'
def add_ing (string):
    return None

# Create a function that takes a list of integers, and returns two new arrays: the first has all the even numbers, the second has all the odd numbers. the order of these lists is not changed.

def odd_even (nums):
    return None

#Create a function that shouts each word (separated by a space) in a string
#eg. 'giraffes' -> 'giraffes!'
#'do not want' -> 'do! not! want!'
#'python, programming.' -> 'python,! programing.!'
#'' -> '!'
def shout_it (string):
    return None

#Create a function that multiplies each element of a list with the index of that element. e.g [2,2,2,2] -> [0, 2, 4, 6]

def times_by_index (nums):
    return None

#Create a function that return True if a string *contains* at least one instance of the word "monkey" (lower case) as a substring.
#eg 'mere ape' -> False
#'bb_monkey_xx' -> True
#'Are we monkeys or men?' -> True
#'i am a MONKEY' -> False
def contains_monkey (string):
    return None

#Create a function that returns the nth fibonacci number. For example 6->8

def fibonacci (n):
    return None

#Create a function that takes a string of alternating 1-digit numbers and letters (for example '3a2b5q9z'), and then creates a new string which repeats each character by the preceding number of times.
#For example: '2a4q3n' -> 'aaqqqqnnn'
#Hint: You may find String.repeat(), String.split(), and Array.join() useful.

def build_string (string):
    return None

#write a function that returns the highest product of *consecutive* numbers in a list of at least 2 elements
#For example, [5,2,10,9,11,3] -> 99, because 9*11 is the highest product of consecutive numbers. Some numbers might be negative!

def highest_pair (nums):
    return None


#create a function that returns True if a positive integer is prime, and False if it is not prime.
def is_prime (n):
    return None


#a palindrome is a string that reads the same way forward as it does backwards.
#e.g abcd -> False, abcdcba -> True
#create a function that returns True if the string is a palindrome

def is_palindrome (string):
    return None


#create a function that returns true if the string *contains* a palindrome
#e.g abc -> False, abcba -> True, aaaabob0 -> True, because bob is a palindrome

def contains_palindrome (string):
    return None

#A sub-list is a part of a list that can be made without any gaps. For example [7,2,3] is a sub-list of [4,7,2,3,1]. But [7,3] is not a sub-list because it skips 2. And [3,2,1] is not a sub-list because it is in the incorrect order. A sub-list can have one element.

#Write a function that takes a list of numbers (positive, negative, and zero) and returns the highest *sum* that can be made from a sub-list.

#This is a tricky one! Make sure you think of *all* the different kinds of input your function could get.

def highest_sub_sum (nums):
    return None
