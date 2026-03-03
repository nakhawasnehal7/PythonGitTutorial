k = lambda x: x + 1
print(k(10))

l = lambda x, y: x + y
print(l(10, 8))

m = lambda x: x if x % 2 == 0 else 0

print(m(10))

print((lambda x: x * x)(5))

L1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
f=filter(lambda x: x%2 ==0, L1)
L2=list(f)
print(L2)
l3=list(map(lambda x:-x,L1))
print(l3)


k=lambda y: True if y*2 ==8 else False
print(k(4))

t=lambda a, b : a+b if a> b else a-b
print(t(3,6))