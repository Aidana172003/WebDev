def xor(x, y):
    if (x==1 and y==1):
        return 0
    elif (x==1 or y==1):
        return 1
x=int(input())
y=int(input())
print(xor(x,y))