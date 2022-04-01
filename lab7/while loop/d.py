n=int(input())
k=1
while k!=n:
    if k>n:
        print("NO")
        break
    k*=2
else:
    print("YES")