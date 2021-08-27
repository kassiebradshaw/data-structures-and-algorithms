def merge(left, right, list): # define a function to merge the sides back together
    i = 0 # variable for iteration of left side's index
    j = 0 # variable for iteration of right side's index
    k = 0 # variable for iteration of list 

    while i < len(left) and j < len(right):
        if left[i] <= right[j]: # if left side's value is less/equal to value in right side's list,
            
            list[k] = left[i] # assign the value to the list and
            i = i + 1 # increment the iteration of the left side

        else: # if left side's value is NOT less/equal to value in right side's list,
            list[k] = right[j] # assign the right side's value to the list
            j = j + 1 # increment the iteration of the right side
        
        k = k + 1 # increment the iteration of the list
    
    while i < len(left):
        list[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        list[k] = right[j]
        j += 1
        k += 1
    
    return list

def merge_sort(list):
    n = len(list) # n is length of list
    if n <= 1:
        return "List must not be empty. List must have more than 1 item."
    else:
        if n > 1: # if the list is greater than 1:
            mid = n // 2 # determine the middle by dividing the list in 2
            left = list[:mid] # left side is list of items from start to middle of list
            right = list[mid:] # right side is list of items from middle to end of list

            merge_sort(left) # call function on left side
            merge_sort(right) # call function on right side
            merge(left, right, list) # merge the sorted sides together
    
    return list
        