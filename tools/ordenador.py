def partition(array, low, high, reverse=False):
    # elegimos el primer elemento
    pivot = array[low][4]
    izq = low+1
    der = high
    while True:
        if reverse:
            while izq <= der and array[izq][4] >= pivot:
                izq+=1
            while izq <= der and array[der][4] <= pivot:
                der-=1
        else:
            while izq <= der and array[izq][4] <= pivot:
                izq+=1
            while izq <= der and array[der][4] >= pivot:
                der-=1
        if der < izq:
            break
        else:
            array[izq], array[der] = array[der], array[izq]
    array[low], array[der] = array[der], array[low]
    return der

# function to perform quicksort
def quicksort(array, low, high, reverse=False):
    if low < high:
        pi = partition(array, low, high,reverse)
        quicksort(array, low, pi - 1,reverse)
        quicksort(array, pi + 1, high,reverse)