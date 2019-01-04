def hanoi(n, start, temp, final):
        if n > 0:
                hanoi(n-1, start,final,temp)
                final.append(start.pop())
                hanoi(n-1, temp, start,final)
                print(start,temp,final)
                return True
        else:
                return True

