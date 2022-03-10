def func(a,b):
    l = []
    if set(a).intersection(set(b)) == set():
        return [-1]
    else:
        for i in range(len(a)):
            if a[i] in b:
                l.append(a[i])
                b.remove(a[i])
        return l
