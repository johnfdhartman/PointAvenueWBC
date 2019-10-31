#Dictionary exercises:


#write a function that adds a key value pair to a dictionary
#e.g add_key_val({'a':10, 'b':20}, {'c':50}) -> {'a':10, 'b':20, 'c':50}
def add_key_val (dict, key_val):
    return None

#write a function that takes two lists of the same length and creates
#a dictionary out of them. the first list will be the keys, the second
#list is the values. map them according to their indices, that is,
#key_list = ['a','b','c'], val_list = [1,2,3] -> {'a':1, 'b':2, 'c':3}
def lists_to_dict (key_list, val_list):
     return None

#write a function that merges two dictionaries together
#assume that dict_1 and dict_2 have no key values in common
#e.g if a = {'p':1, 'q':2} and b = {'x':10, 'y':20} then
#merge_dicts(a, b) = {'p':1, 'q':2, 'y':20}
def merge_dicts (dict_1, dict_2):
    return None

#Basic algorithms
#By now you should know the basics of loops and data structures.
#As we start getting into Algorithms, the functions you have to make will
#become trickier. Remember to think before you code!


#Bubble sort is a well known algorithm for sorting a list.
#It works by looping over the list and comparing adjacent elements
#If two elements are out of order, it swaps them
#It keeps looping over the list, doing this until all of the elements are sorted

#Write a bubble sort function that sorts a list of number in increasing order.

def bubble_sort (unsorted):
    return None

#Bubble sort is famous for being really inefficient and slow.
#Can you think of another way of sorting a list of numbers that might be faster?

def my_sort (unsorted):
    return None

#A nested list is a list that contains lists.
#E.g the list [ [1,2,3],[4,5,6],[7,8,9] ] has 3 elements, each of which
#is also a list.
#lists can also be deeply nested - which means that lists can contain
#lists which can contain lists, and so on and so forth.

#Write a function that 'flattens' a list.
#That is, it takes a deeply nested list and returns a new list with all
#the non-list elements *in the correct order*.
#for example: [ [[1],2], [[3]], [4], 5] -> [1,2,3,4,5]

def flatten_list (deep_nested):
    return None


#Write a function that takes a deeply nested list and a target, and
#returns True if the list contains the target. (and false if it doesn't)
#For example [1,2, [3,4], [[[5]]]], 3 -> True
def search_nested_list (deep_nested, target):
    return None


#let the 'depth' of a list be its maximum level of listing. that is,
#[1,2,3] has depth 1, [1,[2,3]] has depth 2, [[1],[2,[3]]] has depth 3.
#write a function that finds the depth of a deeply nested list.

def list_depth (in_list):
    return None
