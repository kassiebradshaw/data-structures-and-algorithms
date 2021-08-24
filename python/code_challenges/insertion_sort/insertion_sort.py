def InsertionSort(list):
    if len(list) <2:
        return 'List must not be empty. List must have more than 1 value to sort.'
    
    for i in range(1, len(list)):
        j = i - 1
        temp = list[i]

        while j >= 0 and temp < list[j]:
            list[j + 1] = list[j]
            j = j - 1
        
        list[j + 1] = temp
    
    return list

