#def ASSIGNMENT(new_list, i, old_list, j): unnoetig
#    new_list[i] = old_list[j]


def mergeSort(list_to_sort_by_merge):
    '''if (
        len(list_to_sort_by_merge) > 1
        #and not len(list_to_sort_by_merge) < 1  unnoetig
        #and len(list_to_sort_by_merge) != 0
    ):'''
    if len(list_to_sort_by_merge) <= 1: # siehe return unten und nicht ganzer Code in if-Bedingung
        return list_to_sort_by_merge
    
    mid = len(list_to_sort_by_merge) // 2
    left = list_to_sort_by_merge[:mid]
    right = list_to_sort_by_merge[mid:]

    left = mergeSort(left) # bessere Verstaendlickeit
    right = mergeSort(right)

    merged = []
    left_index = 0 # bessere Verstaendlichkeit
    right_index = 0
    #i = 0 nicht mehr benoetigt

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            #ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=left, j=l)
            merged.append(left[left_index])
            left_index += 1
        else:
            #ASSIGNMENT(new_list=list_to_sort_by_merge, i=i, old_list=right, j=r)
            merged.append(right[right_index])
            right_index += 1
        #i += 1 nicht mehr benoetigt

    while left_index < len(left):
        merged.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        merged.append(right[right_index])
        right_index += 1

    return merged #Funktion mergeSort gibt die Liste als Rueckgabewert zurueck. Dies ermoeglicht eine verbesserte Lesbarkeit und Benutzerfreundlichkeit des Codes.


#neuer Plotting-Teil

import matplotlib.pyplot as plt

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
ax1.plot(x, my_list)
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_title('Vor dem Sortieren')

sorted_list = mergeSort(my_list)

x = range(len(my_list))
ax2.plot(x, sorted_list)
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_title('Nach dem Sortieren')

plt.subplots_adjust(wspace=0.3)

plt.show
