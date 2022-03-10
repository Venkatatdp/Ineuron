def main(emails):
    l = []
    for i in emails:
        a = i.split('@')[0]
        b = i.split('@')[1]
        if '+' in a:
            c = a.split('+')[0]
            if '.' in c:
                d = c.replace('.','')
                l.append('@'.join([d,b]))
        elif '.' in a:
            c = a.replace('.','')
            l.append('@'.join([c,b]))
        else:
            l.append(i)
    return l

print(main(['abc.cej@gmail.com','abc.cehjsJ+djhkHDJj@gmail.com','abccej@gmail.com']))
