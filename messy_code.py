def f(a,b,c):
    x=a+b
    y=x*c
    if y>100:
        return "big"
    else:
        if y>50:
            return "medium"
        else:
            return "small"

l=[1,2,3,4,5]
t=0
for i in range(0,len(l)):
    t=t+l[i]
print(t)
print(f(10,20,3))
print(f(5,5,2))
