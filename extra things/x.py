    for i in range(int(input())):
        a = [0 for i in range(26)]
        x = ord('a')
        for i in raw_input():
            a[ord(i) - x] += 1
        b = [0 for i in range(26)]
        for i in raw_input():
            b[ord(i) - x] += 1
        count  = 1
        for i in range(26):
            if a[i] != 0 and b[i] != 0 and a[i] >= b[i]:
                n = a[i]
                if b[i] > 1:
                    k = a[i] - b[i] + 1
                    n = k * (k + 1) / 2
                count *= n
                # print count
            elif a[i] < b[i]:
                return -1
        return count

