n={'a':20,'b':40,'c':2,'d':[2,3]}
n['e']=14
print(n)
print(n['b'],n['c'])
del n['d']
print(n.get(58,"not found"))
print(n.keys())
print(n.values())
print(n.items())
new={'f':5,'g':46}
n.update(new)
print(n)
print(n.pop("a"))
print(n.popitem())
ncp=n.copy()
print(ncp)
for key in ncp.keys():
    print(key)
for values in ncp.values():
    print(values)