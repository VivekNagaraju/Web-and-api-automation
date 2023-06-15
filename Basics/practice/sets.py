a={1, 2, 3, 5} #homogeneous
print(type(a))

b={1, 2.0, "abc"} #sets can be heterogeneous
print(b)

c=set(range(1, 6)) #built-in func
print(c)

e={1, 1, 3, 4, 5} # sets can't store duplicates
print(e)

f= e.copy()
print(f)

e.add(6)
print(e)

g=e.difference(f)
print(g)





