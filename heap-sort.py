def heapify(u):
        if len(u) > 0:
                for j in range(0,len(u)):
                        k = j
                        while True:
                                if (k == 0):
                                        break
                                else:
                                        n = (k-1)/2
                                if (u[n] < u[k]):
                                        temp = u[n]
                                        u[n] = u[k]
                                        u[k] = temp
                                k = n
                return True
        else:
                return False
def reheapify(u,end):
        if len(u) > 0:
                i = 0
                while True:
                        if i > end:
                                break
                        left = i*2 + 1
                        right = i*2 +2
                        if left >= end:
                                break
                        if right >= end:
                                right = left
                        if u[right] >= u[left]:
                                n = right
                        else:
                                n = right
                        if u[right] > u[left]:
                                temp = u[i]
                                u[i] = u[n]
                                u[n] = temp
                        i = n
                return True
        else:
                return False
def heap_sort(u):
        if len(u) > 0:
                heapify(u)
                end = len(u)-1
                while (end >= 0):
                        temp = u[0]
                        u[0] = u[end]
                        u[end] = temp
                        reheapify(u, end)
                        end -= 1
                return True
        else:
                return False
