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
