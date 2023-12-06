# TODO: Implement a function that returns a list of numbers from 1 to n (already provided in original list)
def generate_numbers(n):
    return list(range(1,n+1))

# TODO: Implement a function that takes two lists as arguments, merges them into one list, and then sorts the merged list in ascending order
def merge_and_sort_lists(list1, list2):
    list1=list1+list2
    list1.sort()
    return list1

# TODO: Implement a function that removes all duplicate values in a list and returns a list with only the unique elements in the order they appeared
def remove_duplicates(my_list):
    list2=[]
    for i in my_list:
        if i not in list2:
            list2.append(i)
    return list2

# TODO: Implement a function that checks whether a list is a sublist of another list. A sublist is a sequence of consecutive elements that are part of another list
def is_sublist(list1, list2):
    if len(list1) > len(list2):
        return False
    for i in range(len(list2) - len(list1) + 1):
        if list2[i:i+len(list1)] == list1:
            return True
    return False

# TODO: Implement a function that rotates the elements of a list to the right by `k` places. `k` is non-negative
def rotate_list(my_list, k):
    if not my_list or k < 0:
        return my_list
    k=k%len(my_list)
    return my_list[-k:]+my_list[:-k]

