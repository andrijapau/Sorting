def selection_sort(u):
        if len(u) > 0:
                for i in range(0, len(u)):
                        min_ = min(u[i:])
                        mini = u[i:].index(min_)
                        u[i+mini] = u[i]
                        u[i] = min_
                return True
        else:
                return False
