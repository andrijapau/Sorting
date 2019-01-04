def partition(u, ini, fin):
        pivot = u[fin]
        pIndex = ini
        temp = 0
        for i in range(ini,fin):
                if u[i] <= pivot:
                        temp = u[i]
                        u[i] = u[pIndex]
                        u[pIndex] = temp
                        pIndex += 1
        temp=  u[fin]
        u[pIndex] = u[fin]
        u[fin] = temp
        return pIndex
