def quicksort(u, ini, fin):
        if ini < fin:
                pIndex = partition(u, ini, fin)
                quicksort(u, ini, pIndex-1)
                quicksort(u, pIndex+1, fin)
        else:
                return -1
