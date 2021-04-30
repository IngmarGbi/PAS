#QuickSort Annotation from GoogleVision

def compare(elem1,elem2,xVar,yVar) :
    ecartX = elem1.bounding_poly.vertices[0].x - elem2.bounding_poly.vertices[0].x
    ecartY = elem1.bounding_poly.vertices[0].y - elem2.bounding_poly.vertices[0].y
    #Comparaison par X puis Y avec tolérance de 10
    if ecartY < -yVar :
        return -1
    elif ecartY > yVar :
        return 1
    elif ecartX < -xVar :
        return -1
    elif ecartX > xVar:
        return 1
    else :
        return 0


def partition(array, start, end):
    pivot = array[start]
    low = start + 1
    high = end
    print(pivot.description)
    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot

        #Normal writing
        #while low <= high and array[high] >= pivot:
        while low <= high and compare(pivot,array[high]) < 0 :
            high = high - 1

        # Opposite process of the one above
        #Normal writing
        #while low <= high and array[low] <= pivot:
        while low <= high < 0 and compare(array[high],pivot) < 0 :
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        #Normal Writing
        #if low <= high:
        if low <= high :
            array[low], array[high] = array[high], array[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    array[start], array[high] = array[high], array[start]
    return high


def quick_sort(array, start, end):
    if start >= end:
        return

    p = partition(array, start, end)
    quick_sort(array, start, p-1)
    quick_sort(array, p+1, end)


def sort(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            #if x < pivot:
            if compare(x,pivot) < 0 :
                less.append(x)
            #elif x == pivot:
            elif compare(x,pivot) == 0 :
                equal.append(x)
            #elif x > pivot:
            elif compare(x,pivot) > 0 :
                greater.append(x)
        # Don't forget to return something!
        return sort(less)+equal+sort(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array


def bubbleSort(arr,xVar,yVar): 
    n = len(arr) 
  
    # Traverse through all array elements 
    for i in range(n): 
  
        # Last i elements are already in place 
        for j in range(0, n-i-1): 
  
            # traverse the array from 0 to n-i-1 
            # Swap if the element found is greater 
            # than the next element 
            #if arr[j] > arr[j+1] :
            if compare(arr[j],arr[j+1],xVar,yVar)>0 :
                arr[j], arr[j+1] = arr[j+1], arr[j] 
