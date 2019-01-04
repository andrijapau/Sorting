def merge_sort(u):
        if len(u) > 1:
                length = len(u)/2
                ulow = u[:length]
                uhigh = u[length:]

                merge_sort(ulow)
                merge_sort(uhigh)

                i = 0
                j = 0
                k = 0
                while i < len(ulow) and j < len(uhigh):
                        if ulow[i] < uhigh[j]:
                                u[k] = ulow[i]
                                i = i+ 1
                        else:
                                u[k] = uhigh[j]
                                j = j+ 1
                        k += 1
                while i < len(ulow):
                        u[k] = ulow[i]
                        i = i +1
                        k = k+ 1
                while j < len(uhigh):
                        u[k] = uhigh[j]
                        j = j+ 1
                        k=k+ 1

        return True
